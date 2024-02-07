
from flask import Flask, request, jsonify
from flask_cors import CORS
import json

chat = Flask(__name__)
CORS(chat)


@chat.route('/send_message_to_server', methods=['POST'])
def receive_message():

    json_data = request.get_json()



    message = json_data.get('message')
    name = json_data.get('name')
    language = json_data.get('language')

    print(f"Received message: {message}, Sender: {name}, Language: {language}")

    #message_add(message: {message}, Sender: {sender}, Language: {language}



    response = {"status": "Message received successfully"}
    return jsonify(response), 200



@chat.route('/hello')
def hello():
    return "Hallo von der API"


 

@chat.route('/update_message', methods=['POST'])
def send_message():

    message = 'Mir gehts gut'
    sender = 'Server'
    language = 'de'
    sentiment = 'happy'



    #get message from database
    send_data = {'message': message,
                'sender': sender,
                'language': language,
                'sentiment': sentiment}


    print(f"Sending message: {send_data}")

    #build json for export
    response = json.loads(json.dumps(send_data, ensure_ascii=False))
    print (response)
    
    #return json
    return jsonify(response), 200

if __name__ == '__main__':
    chat.run(host='0.0.0.0', port=5000,debug=True)