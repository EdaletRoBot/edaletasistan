from telethon import TelegramClient
from pyrogram import Client
# Config məlumatları

# Telegram Client (Telethon)
API_ID = 28054551
API_HASH = "64a0620c2644ceff0c1058a4ffc861ad"
bot_token = "5883816340:AAFJpGNHNPNvogeKaLH0duNJjpchsmQ1UOg"

edalet = TelegramClient('edalet', API_ID, API_HASH).start(bot_token=bot_token)

app = Client("edalet", bot_token=bot_token, api_hash=API_HASH, api_id=API_ID)




