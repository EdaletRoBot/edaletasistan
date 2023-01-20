from telethon import TelegramClient
import logging
from Configs import *

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.INFO)

bot = TelegramClient('edalet', api_id=Configs.APP_ID, api_hash=Configs.API_HASH)
edalet = bot.start(bot_token=Configs.TOKEN)
