from telethon.sync import TelegramClient
from dotenv import load_dotenv
from os import getenv

load_dotenv()


def create_client():
    api_id = getenv("API_ID")
    api_hash = getenv("API_HASH")
    phone = getenv("PHONE")

    if api_id is None or api_hash is None or phone is None:
        raise ImportError("Нет API_ID, API_HASH или PHONE в переменных окружения")

    api_id = int(api_id)
    client = TelegramClient(phone, api_id, api_hash)

    return client


client = create_client()
