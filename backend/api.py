
from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import sys
from flasgger import Swagger

chat = Flask(__name__)
swagger = Swagger(chat)
CORS(chat)

@chat.route('/send_message_to_server', methods=['POST'])
def receive_message():
    """
    Test mit viel SWAG, Tööörnup
    ---
    parameters:
      - name: name
        in: path
        type: json
        required: true
        description: TEEST 123.
    responses:
        200:
           description: TEST undso....
    """

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
    # Disable debug, when deployed in a container, for production use
    debug = False
    if len( sys.argv ) > 1:
        first_arg = str(sys.argv[1])
        if first_arg.lower() == "debug":
            debug=True
            print("Debug enabled!")

    chat.run(host='0.0.0.0', port=5000,debug=debug)