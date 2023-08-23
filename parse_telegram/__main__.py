from telegram.connect import client
import new_message_handler

client.start()
client.run_until_disconnected()
