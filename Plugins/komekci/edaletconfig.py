from telethon import TelegramClient
# Config məlumatları

# Telegram Client (Telethon)
API_ID = 28054551
API_HASH = "64a0620c2644ceff0c1058a4ffc861ad"
bot_token = "5628406386:AAF_P7o95g0j3L-h0JefWyHGPFsgXma0Nug"

edalet = TelegramClient('edalet', API_ID, API_HASH).start(bot_token=bot_token)
