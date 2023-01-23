import os
import logging
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from Config import Config 

logging.basicConfig(
    level=logging.INFO,
    format='%(name)s - [%(levelname)s] - %(message)s'
)
LOGGER = logging.getLogger(__name__)

api_id = Config.API_ID
api_hash = Config.API_HASH
bot_token = Config.BOT_TOKEN
bot_username = Config.BOT_USERNAME
bot_name = Config.BOT_NAME


#-#-#-# Pyrogram Başlanğıc #-#-#-#
app = Client(":memory:", api_id, api_hash, bot_token=bot_token)




@app.on_message(filters.private & filters.command("info"))
async def info(app, update):
    
    text = f"""--**Information**--
**🙋🏻‍♂️ Adın :** {update.from_user.first_name}
**🧑🏻‍🎓 Username :** {update.from_user.username}
**🆔  Telegram ID :** {update.from_user.id}
**🔗 Profil linkin  :** {update.from_user.mention}"""
    
    await update.reply_text(        
        text=text,
        disable_web_page_preview=True,
    )


@app.on_message(filters.private & filters.command("id"))
async def id(app, update):
    await update.reply_text(        
        text=f"**Telegram ID :** {update.from_user.id}",
        disable_web_page_preview=True,
    )


print("İnfo modulu pis deyil")
app.run()
