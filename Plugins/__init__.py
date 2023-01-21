from telethon import TelegramClient 
import logging
from Config import *

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.INFO)


edalet = TelegramClient('edalet', API_ID, API_HASH).start(bot_token=bot_token)
