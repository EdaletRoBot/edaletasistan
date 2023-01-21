from telethon import TelegramClient as tg
import logging
from Config import *

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.INFO)


bot = tg('edalet', api_id=Config.APP_ID, api_hash=Config.API_HASH)

edalet = bot.start(bot_token=Config.TOKEN)
