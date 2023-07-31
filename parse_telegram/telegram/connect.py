from telethon.sync import TelegramClient
from dotenv import load_dotenv
from os import getenv

load_dotenv()

api_id = getenv("api_id")
api_hash = getenv("api_hash")
phone = getenv("phone")

client: TelegramClient

if api_id and api_hash and phone:
    api_id = int(api_id)
    client = TelegramClient(phone, api_id, api_hash)
