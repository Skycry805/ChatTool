import sys

from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import copy

from flasgger import Swagger
from werkzeug.middleware.proxy_fix import ProxyFix

import external

chat = Flask(__name__)
swagger = Swagger(chat)
CORS(chat)

# Fix for Proxy
# https://flask.palletsprojects.com/en/3.0.x/deploying/proxy_fix/
chat.wsgi_app = ProxyFix(
    chat.wsgi_app, x_for=1, x_proto=1, x_host=1, x_prefix=1
)

messages_to_send = {}
language_list = ['en'] 
message_id = 0   #### Var namen

@chat.route('/send_message', methods=['POST'])
def send_message():

    global message_id
    
    print ("Message ID:", message_id)
    local_m_id = message_id + 1
    received_message = {}

    json_data = request.get_json()
    build_message (json_data, local_m_id)


    print(json_data)
    #Debug Output for test
    message = json_data.get('message')
    sender = json_data.get('name')
    language = json_data.get('language')
    print(f"Received message: {message}, Sender: {sender}, Language: {language}")

    if json_data.get('bot'):
        answer = ask_bot(json_data.get('message'),json_data.get('language'))
        local_m_id = local_m_id + 1
        build_message (answer, local_m_id)

    
    #print(f"Received message: {json_data['message']}, Sender: {json_data['name']}, Language: {json_data['language']}")
    message_id = message_id + 1 
    received_message[message_id] = json_data

    response = {"status": "Message received successfully"}
    return jsonify(response), 200

#builds a message that can be send to the user
def build_message (receive_message, m_ID: int):
    global messages_to_send

    message = receive_message.get('message')
    sender = receive_message.get('name')
    source_lang = receive_message.get('language')

    add_new_language(source_lang)

    translated_messages = {}
    translated_messages[source_lang] = message

    for target_lang in language_list:
        translation = translate_message(source_lang, target_lang, message)
        print ("Empfangene Übersetzung", translation)
        translated_messages[target_lang]=translation
        print ("Gespeicherte Übersetzung", translated_messages)


    sentiment = external.sentiment(translated_messages['en'])

    builed_message = {'message':translated_messages, 'sender':sender, 'sentiment':sentiment}
    print("Builded Messages:", builed_message)
    messages_to_send[m_ID] = builed_message
    print("Added Messages:", messages_to_send)

#Sending message to ChatBot and returns the answer
def ask_bot (message: str, lang: str) -> str:
    answer = external.llm(message)
    output = {'Sender': 'Bob der Bot', 'Message': answer, 'Language': lang}
    return output
    

#Add new User Language
def add_new_language(language: str):
    global language_list
    if language not in language_list:
        language_list.append(language)

def translate_message(source_lang: str, target_lang: str, message: str) -> str:
    translated_message = external.translate(source_lang, target_lang, message)
    print("Übersetzte Nachricht:", translated_message)
    return translated_message



@chat.route('/update_message/<int:msg_id>', methods=['POST'])
def update_message(msg_id):

    global messages_to_send, message_id
    print("Messages:", messages_to_send)
    print("ID vom CLient", msg_id)

    local_all_messages = copy.deepcopy(messages_to_send)
    print("Messages:", local_all_messages)

    print("Test der Ausgabe:", local_all_messages[msg_id]) 
    local_message_id = message_id
    send_data = {}

    while msg_id <= local_message_id:
        send_data[msg_id] = local_all_messages[msg_id]
        msg_id +=1

    print("Sending message:", send_data)
    #build json for export
    response = json.loads(json.dumps(send_data, ensure_ascii=False))
    print (response)  
    #return json
    return jsonify(response), 200


@chat.route('/get_message_id', methods=['POST'])
def get_message_id():

    global message_id
    #get message from database
    send_data = {'message_id': message_id}


    print(f"Sending message: {send_data}")

    #build json for export
    response = json.loads(json.dumps(send_data, ensure_ascii=False))
    print (response)
    
    #return json
    return jsonify(response), 200


if __name__ == '__main__':
    # Disable debug, when deployed in a container, for production use
    debug = True #######################################################################################################
    if len( sys.argv ) > 1:
        first_arg = str(sys.argv[1])
        if first_arg.lower() == "debug":
            debug=True
            print("Debug enabled!")

    chat.run(host='0.0.0.0', port=5001, debug=debug) ################################################## PORRT!!!