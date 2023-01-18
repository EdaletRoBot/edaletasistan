from komekci.edalet import Edalet
     


@Edalet.on(events.NewMessage(pattern='(?i)/start+'))
async def yeni_mesaj(event: events.NewMessage.Event):
    await event.reply(f"👋🏻 Salam mən @edalet_22 nin asistaniyam\nMənə start verdiyin hakkında məlumatı Sahibimə dedim 📨")
    
    

print(">> Edalet qoz kimi işləyir  <<")
Edalet.run_until_disconnected()
