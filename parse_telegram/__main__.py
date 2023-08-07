from telethon.events import NewMessage
from telethon.tl.custom import Message
import asyncio

from match.find_match import find_match
from match.get_match_values import get_match_values
from utils.get_values import get_values
from telegram.connect import client
from telegram.check_env import check_env

client.start()

loop = asyncio.get_event_loop()
parsed_chat_id, client_chat = loop.run_until_complete(check_env())


@client.on(NewMessage(chats=parsed_chat_id))
async def get_messages(event: Message) -> None:
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
            client_chat,
            "Message from bot!\n" + f"{message}\n" + f"Матч не найден!\n",
        )
        return

    while True:
        match_values = await get_match_values(match_id)
        print(match_values)

        if match_values.time.minutes >= 60:
            break

        await asyncio.sleep(60)

    is_first_team_equal = message_values.score[0] == match_values.players[1].goal_count
    is_second_team_equal = message_values.score[1] == match_values.players[0].goal_count

    if not (is_first_team_equal and is_second_team_equal):
        print("Warning: счет из сообщения и счет из матча не равны")
        return

    await client.send_message(
        client_chat,
        "Message from bot!\n"
        + f"{message}\n"
        + f"Текущее время матча: {match_values.time.minutes}:{match_values.time.seconds}",
    )


client.run_until_disconnected()
