from telethon import TelegramClient as tg
import logging
from Configs import *

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.INFO)


edalet = tg('edalet',API_ID, API_HASH).start(bot_token=BOT_TOKEN)



