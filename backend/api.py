import sys

from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import copy

from flasgger import Swagger
from werkzeug.middleware.proxy_fix import ProxyFix
from werkzeug.exceptions import HTTPException

import external
from history import History

chat = Flask(__name__)

# Swagger base config
swagger_config = {
    "spec": {
        "openapi": "3.0.3", 
        "info": {
            "title": "Chat Support - 1.0",
            "description": "Chat Support API 1.0",
            "version": "1.0.0",
        },
    },
    "components": {
        "securitySchemes": {
            "bearerAuth": {
                "type": "http",
                "scheme": "bearer",
                "bearerFormat": "JWT",
            }
        }
    },
}
chat.config["SWAGGER"] = swagger_config
chat.config["SWAGGER"]['openapi'] = '3.0.3'

# Load yaml
swagger = Swagger(chat, template_file='swagger/swagger.yaml')
CORS(chat)

# Fix for Proxy
chat.wsgi_app = ProxyFix(
    chat.wsgi_app, x_for=1, x_proto=1, x_host=1, x_prefix=1
)


# History data class
chat_history = History()

# Default ok for 200
default_ok = {"status": "ok"}

# Clear histroy data
def clear_history():
    chat_history.reset()


#builds a message that can be send to the user
def build_message(receive_message):

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
def ask_bot(message: str, lang: str) -> str:
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
def send_message(): # pragma: no cover # exclude from unittest. Test calls via web request
   
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
        # Concat name msg
        msg = json_data.get('sender') + ": " + json_data.get('message')
        answer = ask_bot(msg, json_data.get('language'))
        build_message (answer)
 
    received_message[chat_history.message_id] = json_data

    return jsonify(default_ok)


@chat.route('/update_message/<int:msg_id>', methods=['POST'])
def update_message(msg_id): # pragma: no cover # exclude from unittest. Test calls via web request
    # catch exception
    if msg_id < 1:
        msg_id = 1

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
    return jsonify(response)


@chat.route('/get_message_id', methods=['POST'])
def get_message_id(): # pragma: no cover # exclude from unittest. Test calls via web request
     #get message from database
    send_data = {'message_id': chat_history.message_id}

    print(f"Sending message: {send_data}")

    #build json for export
    response = json.loads(json.dumps(send_data, ensure_ascii=False))
    print (response)
    
    #return json
    return jsonify(response)


# Gerneric errror handler
@chat.errorhandler(HTTPException)
def handle_exception(e): # pragma: no cover # exclude from unittest. Test calls via web request
    response = e.get_response()
    response.data = json.dumps({
        "code": e.code,
        "name": e.name,
        "description": e.description,
    })
    response.content_type = "application/json"
    return response


if __name__ == '__main__': # pragma: no cover
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