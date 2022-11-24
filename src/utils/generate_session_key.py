from telethon.sessions import StringSession
from telethon.sync import TelegramClient


api_id = 123
api_hash = "123"

with TelegramClient(StringSession(), api_id, api_hash) as client:
    print(client.session.save())
