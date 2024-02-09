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
chat.wsgi_app = ProxyFix(
    chat.wsgi_app, x_for=1, x_proto=1, x_host=1, x_prefix=1
)

# Class for chat history
class history:
    def __init__(self):
        self.messages_to_send = {}
        self.language_list = ['en'] 
        self.message_id = 0

# History data class
chat_history = history()

# Clear histroy data
def clear_history():
    # sadly flask is not good in a class...
    global chat_history
    chat_history = history()

#builds a message that can be send to the user
def build_message (receive_message):

    message = receive_message.get('message')
    sender = receive_message.get('sender')
    source_lang = receive_message.get('language')

    add_new_language(source_lang)

    translated_messages = {}
    translated_messages[source_lang] = message

    for target_lang in chat_history.language_list:
        translation = translate_message(source_lang, target_lang, message)
        translated_messages[target_lang]=translation


    sentiment = external.sentiment(translated_messages['en'])

    builed_message = {'message':translated_messages, 'sender':sender, 'sentiment':sentiment}
    chat_history.message_id = chat_history.message_id + 1
    chat_history.messages_to_send[chat_history.message_id] = builed_message


#Sending message to ChatBot and returns the answer
def ask_bot (message: str, lang: str) -> str:
    answer = external.llm(message)
    sender = "Bob der Bot"
    output = {'sender': sender, 'message': answer, 'language': lang}
    return output
    

#Add new User Language
def add_new_language(language: str):
    #global language_list
    if language not in chat_history.language_list:
        chat_history.language_list.append(language)

def translate_message(source_lang: str, target_lang: str, message: str) -> str:
    translated_message = external.translate(source_lang, target_lang, message)
    return translated_message


### Routes
@chat.route('/send_message', methods=['POST'])
def send_message():
    
    received_message = {}

    json_data = request.get_json()
    build_message(json_data)


    print(json_data)
    #Debug Output for test
    message = json_data.get('message')
    sender = json_data.get('sender')
    language = json_data.get('language')
    print(f"Received message: {message}, Sender: {sender}, Language: {language}")
   

    if json_data.get('bob'):
        answer = ask_bot(json_data.get('message'),json_data.get('language'))
        build_message (answer)
 
    received_message[chat_history.message_id] = json_data

    response = {"status": "Message received successfully"}
    return jsonify(response), 200


@chat.route('/update_message/<int:msg_id>', methods=['POST'])
def update_message(msg_id):

    local_all_messages = copy.deepcopy(chat_history.messages_to_send)

    local_message_id = chat_history.message_id
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

    #get message from database
    send_data = {'message_id': chat_history.message_id}


    print(f"Sending message: {send_data}")

    #build json for export
    response = json.loads(json.dumps(send_data, ensure_ascii=False))
    print (response)
    
    #return json
    return jsonify(response), 200


if __name__ == '__main__':
    # Disable debug, when deployed in a container, for production use
    debug = False
    if len( sys.argv ) > 1:
        first_arg = str(sys.argv[1])
        if first_arg.lower() == "debug":
            debug=True
            print("Debug enabled!")
    
    # Logging
    sys.stdout = open('logs/flask_output.log', 'w')
    sys.stderr = open('logs/flask_error.log', 'w')

    # Run
    chat.run(host='0.0.0.0', port=5000, debug=debug)