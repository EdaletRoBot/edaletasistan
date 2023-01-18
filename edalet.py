from komekci.edalet import Edalet
from telethon import events, Button
import random    


@Edalet.on(events.NewMessage(pattern='(?i)/start+'))
async def yeni_mesaj(event: events.NewMessage.Event):
    await event.reply(f"👋🏻 Salam mən @edalet_22 nin asistaniyam\nMənə start verdiyin hakkında məlumatı Sahibimə dedim 📨")
 


@Edalet.on(events.ChatAction)
async def handler(event):
    if event.user_joined:
        await event.reply(f"Salam qrupa xoş gəldin")
 
    
    

print(">> Edalet qoz kimi işləyir  <<")
Edalet.run_until_disconnected()
