# Distributed Systems - Chat
Chat tool with AI integration.

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
usermod -a -G docker john
```
"john" is an example. To use docker commands, it is sometimes nessasary to reload your shell.

Clone the repository
```
git clone https://github.com/Skycry805/ChatTool.git
```

### Configure external API-Key
Put your API-Key in backend/config.py

Example:
```
"auth_key": "INSERT_API_KEY_HERE",
```

### SSL
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