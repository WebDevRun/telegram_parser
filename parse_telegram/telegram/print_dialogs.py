from .connect import client


async def print_dialogs():
    print("Список чатов с id")

    async for dialog in client.iter_dialogs():
        print(f"{dialog.message.peer_id} - {dialog.name}")
