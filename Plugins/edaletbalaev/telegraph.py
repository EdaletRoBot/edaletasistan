import asyncio
import random
from telethon import events
from Plugins.komekci.edaletconfig import edalet



@edalet.on(events.NewMessage(pattern="^/telegraph$"))
async def telegraph(event):
        if event.reply_to_msg_id:
            reply_message = await event.get_reply_message()
            if reply_message.media:
                downloaded_file_name = await edalet.download_media(reply_message)
                response = post("https://telegra.ph/upload", files={"file": ("file.png", open(downloaded_file_name, "rb"))})
                remove(downloaded_file_name)
                await edalet.send_message(event.chat_id, f"**Link:** https://telegra.ph{response.json()[0]['src']}", reply_to=event.reply_to_msg_id)
            else:
                await edalet.send_message(event.chat_id, "Bir şəkilə cavab verin", reply_to=event.reply_to_msg_id)
        else:
            await edalet.send_message(event.chat_id, "Bir şəkilə cavab verin", reply_to=event.reply_to_msg_id)
            
            
            
            
print('telegraph işləyirdeee')
