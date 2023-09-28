import asyncio

from match.find_match import find_match
from match.get_match_values import get_match_values
from telegram.check_env import check_env
from telegram.connect import client
from telethon.events import NewMessage
from telethon.tl.types import Message
from utils.check_scores import check_scores
from utils.get_values import get_values

LAST_TICK_MINUTE = 60

client.start()
loop = asyncio.get_event_loop()
(parsed_chat_id, client_chat) = loop.run_until_complete(check_env())
client.run_until_disconnected()


@client.on(NewMessage(chats=parsed_chat_id))
async def get_messages(event: NewMessage.Event) -> None:
    if event.reply_to is not None:
        return

    if type(event.message) is not Message:
        print("Warning: Не удалось прочитать сообщение из telegram")
        return

    message = event.message.message
    message_values = get_values(message)

    if message_values is None:
        print("Warning: Не удалось обработать сообщение")
        return

    match_id = await find_match(message_values.teams)

    if match_id is None:
        await client.send_message(
            client_chat,
            "Message from bot!\n" + f"{message}\n" + "Матч не найден!\n",
        )
        return

    while True:
        match_values = await get_match_values(match_id)
        is_equal_scores = check_scores(
            message_values.score,
            (match_values.players[0].goal_count, match_values.players[1].goal_count),
        )

        if not is_equal_scores:
            print("Warning: счет из сообщения и счет из матча не равны")
            return

        if match_values.time.minutes >= LAST_TICK_MINUTE - 1:
            break

        await asyncio.sleep(60)

    await client.send_message(
        client_chat,
        "Message from bot!\n"
        + f"{message}\n"
        + f"Текущее время матча: \
            {match_values.time.minutes}:{match_values.time.seconds}",
    )
