# Telegram strainer service

This service received telegram messages from telegram groups, strain them and resend to another channel

### How to deploy

```shell
cd src
cp docker/prod.env.example docker/prod.env
vim docker/prod.env

docker-compose up --build -d
```

### How to run locally

```shell
cd src/bot
cp .env.example .env
vim .env

docker-compose up --build -d
```
