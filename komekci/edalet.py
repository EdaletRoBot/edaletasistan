from telethon import TelegramClient

# Config məlumatları

# Telegram Client (Telethon)

API_ID = 28054551
API_HASH = "64a0620c2644ceff0c1058a4ffc861ad"
bot_token = "5883816340:AAFJpGNHNPNvogeKaLH0duNJjpchsmQ1UOg"

# Edalet
Edalet = TelegramClient('Edalet', API_ID, API_HASH).start(bot_token=bot_token)
