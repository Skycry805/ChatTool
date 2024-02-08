# Distributed Systems - Chat
Chat tool with AI integration.

## Installation

### Debian/Ubuntu
Install docker and docker-compose.

```
sudo apt-get update
sudo apt-get install docker.io docker-compose
```

You can also install the latest version of docker by unsing the official documentation.

Add your user to the docker group:

```
usermod -a -G docker john
```
"john" is an example. To use docker commands, it is sometimes nessasary to reload your shell.

### Configure external API-Key


### Build and run

```
cd ./docker
docker-compose build
docker-compose up -d
```