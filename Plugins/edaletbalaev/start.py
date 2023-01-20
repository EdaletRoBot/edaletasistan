from Plugins import edalet
from telethon import events, Button
from telethon.tl.types import ChannelParticipantsAdmins




@edalet.on(events.NewMessage(pattern="^/start$"))
async def start(event):
  if event.is_private:
    async for usr in edalet.iter_participants(event.chat_id):
     ad = f"[{usr.first_name}](tg://user?id={usr.id}) "
     await edalet.send_message(-1001890451886, f"ℹ️ **Start Veren Istifadəçi -** {ad}")
     return await event.reply(f"**👋🏻 Salam mən @edalet_22 tərəfindən hazırlanan bir botam\nMənə start verdiyin hakkında məlumatı Sahibimə dedim 📨\nNəyi bacara bildiklərimi görmək üçün /help yazn**"


  if event.is_group:
    return await Maho.send_message(event.chat_id, f"**Məni qrupunuza daxil etdiyiniz üçün təşəkkür edirəm ✨**")

                              
                                                        
                              
@edalet.on(events.NewMessage(pattern="/help"))
async def handler(event):
    app.send_message(message.chat.id, "/ship - Bu kommanda vasitəsi ilə qrupunuzda random 2 istiafdəçini shipləyir\nHələki bu qədərdi gözləmədə qal")

