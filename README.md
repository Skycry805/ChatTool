# Chat Support - Distributed Systems - Chat

![Chat Support](https://github.com/Skycry805/ChatTool/blob/master/misc/chat_support_logo.png?raw=true)

Innovative Chat Tool with AI integration.

The goal for the chat system was to make chats much more accessible and to break curtain barriers. The primary obstacle faced by the majority of individuals is the language barrier. Therefore, the chat system is equipped with an integrated translator that translates every message into the user's native language. Another significant barrier for many people is to determine if a message is meant positively or negatively. That is why, the chat system has an integrated sentiment analysis to indicate how a message was intended. It also includes a helpful AI-driven Chat Bot, that can be activated on demand.

## Installation

### Debian/Ubuntu
Install git, docker and docker-compose.

```
sudo apt-get update
sudo apt-get install git docker.io docker-compose
```

You can also install the latest version of docker by unsing the official documentation.

Add your user to the docker group:

```
sudo usermod -a -G docker john
```
"john" is an example. To use docker commands, it is sometimes nessasary to reload your shell.

Clone the repository
```
git clone https://github.com/Skycry805/ChatTool.git
```

## Configure
Copy configuration file.
```
cp backend/config_template.py backend/configy.py
```

Put your API-Key in backend/config.py

Example:
```
"auth_key": "INSERT_API_KEY_HERE",
```

Change API Backend name in frontend/src/utils.js
Port for internal API is 5000 by default.
```
let serverUrl = 'https://your-server.com:5000';
```

### SSL Certificate for frontend and backend
Put your certificate and the private key into docker/cert forlder

Naming:
```
fullchain.pem
privkey.pem
```

## Build and run

### Build
```
cd ./docker
docker-compose build
docker-compose up -d
```

### Run
```
docker-compose up -d
```

## Test

### Backend
Run coverage 
```
python3 ./backend/unitttest.py
```

Keep in mind, the backend/apy.py will not be fully covert in unittests, because the routes are called by a HTTP-Request!

### Run with coverage WebUI
If you want to run the coverage test, make sure that the backend adress is correct in backend/unittest.py

```
class UnittestApi(unittest.TestCase):
    ...
    base_url = "https://your-server.com:5000"
```

Run the test

```
python3 backend/unittest.py
```

Run the coverage compose file for the coverage WebUI:

```
docker-compose --file ./docker-compose.coverage.yml up -d 
```
WebUI will be available on http[s]://[HOST]:5000/coverage