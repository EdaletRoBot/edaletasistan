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
**🙋🏻‍♂️ First Name :** {update.from_user.first_name}
**🧖‍♂️ Your Second Name :** {update.from_user.last_name if update.from_user.last_name else 'None'}
**🧑🏻‍🎓 Your Username :** {update.from_user.username}
**🆔 Your Telegram ID :** {update.from_user.id}
**🔗 Your Profile Link :** {update.from_user.mention}"""
    
    await update.reply_text(        
        text=text,
        disable_web_page_preview=True,
    )


@app.on_message(filters.private & filters.command("id"))
async def id(app, update):
    await update.reply_text(        
        text=f"**Your Telegram ID :** {update.from_user.id}",
        disable_web_page_preview=True,
    )


print("İnfo modulu pis deyil")
Bot.run()
