from telethon import TelegramClient
# Config məlumatları

# Telegram Client (Telethon)
API_ID = 28054551
API_HASH = "64a0620c2644ceff0c1058a4ffc861ad"
bot_token = "5628406386:AAGE4oMxDksUKHl6Urr8IeIpDHVoH8tV8PI"

edalet = TelegramClient('edalet', API_ID, API_HASH).start(bot_token=bot_token)
