import new_message_handler  # noqa: F401
from telegram.connect import client

client.start()
client.run_until_disconnected()
