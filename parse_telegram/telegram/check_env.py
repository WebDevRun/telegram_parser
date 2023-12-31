from os import getenv
from typing import NamedTuple

from dotenv import load_dotenv

from .print_dialogs import print_dialogs

load_dotenv()


class TargetChats(NamedTuple):
    parsed_chat_id: int
    client_chat: str


async def check_env() -> TargetChats:
    parsed_chat_id = getenv("PARSED_CHAT_ID")
    client_chat = getenv("MESSAGE_CLIENT")

    if parsed_chat_id is None or client_chat is None:
        await print_dialogs()
        raise ImportError(
            "Нет PARSED_CHAT_ID или MESSAGE_CLIENT в переменных окружения"
        )

    chat_id = int(parsed_chat_id)

    return TargetChats(parsed_chat_id=chat_id, client_chat=client_chat)
