from telethon.events import NewMessage
from telethon.tl.custom import Message
from dotenv import load_dotenv
from os import getenv
from match.find_match import find_match
from match.get_match_values import get_match_values
from utils.get_values import get_values
from telegram.connect import client
import asyncio

load_dotenv()

parsed_chat_id = getenv("parsed_chat_id")
message_client = getenv("message_client")

if not parsed_chat_id or not message_client:
    print("Нет значения parsed_chat_id в переменных окружения")
    raise SystemExit

parsed_chat_id = int(parsed_chat_id)

client.start()


@client.on(NewMessage(chats=parsed_chat_id))
async def get_messages(event: Message):
    message = event.text
    is_retry_message = event.is_reply

    if is_retry_message:
        return

    if message is None:
        print("Warning: Не удалось прочитать сообщение из telegram")
        return

    message_values = get_values(message)

    if message_values is None:
        print("Warning: Не удалось обработать сообщение")
        return

    match_id = await find_match(message_values.teams)

    if match_id is None:
        await client.send_message(
            message_client,
            "Message from bot!\n" + f"{message}\n" + f"Матч не найден!\n",
        )
        return

    while True:
        match_values = await get_match_values(match_id)

        if match_values.time / 60 >= 60:
            break

        await asyncio.sleep(60)

    is_first_team_equal = message_values.score[0] == match_values.players[0].goal_count
    is_second_team_equal = message_values.score[1] == match_values.players[1].goal_count

    if not (is_first_team_equal and is_second_team_equal):
        print("Warning: счет из сообщения и счет из матча не равны")
        return

    await client.send_message(
        message_client,
        "Message from bot!\n"
        + f"{message}\n"
        + f"Текущее время матча: {match_values.time // 60}:{match_values.time % 60}",
    )


client.run_until_disconnected()