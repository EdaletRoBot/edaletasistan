from Plugins.komekci.edaletconfig import edalet
from telethon import events, Button
from telethon.tl.types import ChannelParticipantsAdmins
import random




@edalet.on(events.NewMessage(pattern="^/start$"))
async def start(event):
  if event.is_private:
    async for usr in edalet.iter_participants(event.chat_id):
     ad = f"[{usr.first_name}](tg://user?id={usr.id}) "
     await edalet.send_message(-1001890451886, f"📮 **Start Veren Istifadəçi -** {ad}")
     return await event.reply(f"**👋🏻 Salam mən @edalet_22 tərəfindən hazırlanan bir botam\nMənə start verdiyin hakkında məlumatı Sahibimə dedim 📨\nKömək üçün /help yazn**")


  if event.is_group:
    return await edalet.send_message(event.chat_id, f"**Məni qrupunuza daxil etdiyiniz üçün təşəkkür edirəm ✨**")

                              
                                                        
                              
@edalet.on(events.NewMessage(pattern="/help"))
async def handler(event):
    await event.reply(f"📮 @EdaletRoBot əmirləri bunlardır 📮\n\n\n/ship - Qrup içərisində iki random istifadəçini shipləyir\n/id - İstifadəçi id sini göstərir\n/banda - qrupda olan silinmiş hesabları qrupdan atar\n/bots - qrupda olan botları göstərir\n/admins - qrupdakı adminleri göstərir\n/song - YouTube dən mahnı yükləyir\n/video - YouTube dən video yükləyir\n\nSahibim bekar olduqca yeni funksiyalar əlave edəcək")
    
 

@edalet.on(events.ChatAction)
async def handler(event):
    if event.user_joined:
        await event.reply(random.choice(userjoin))
        
        
        
        
@edalet.on(events.NewMessage(pattern='@edalet_22'))
@edalet.on(events.NewMessage(pattern='edalet_22'))
@edalet.on(events.NewMessage(pattern='ədoş'))
@edalet.on(events.NewMessage(pattern='edalet'))
async def handler(event):
    await event.reply(random.choice(edalet))



@edalet.on(events.ChatAction)
async def handler(event):
    if event.user_left:
        await event.reply("Əla Birdə gəlmə")


userjoin = (

    "Salam qrupumuza xoş gəldin",
    "Harahdir, Burda imişki",
    "Həmişə sən gələsən",
    "Bıyyyy kimləri görürəm",
    "Gözümüz yolda qalmışdı gəl çıxda",
    "Yenə gəldidə bu",
)


edalet = (
    "Az tağ elə sahibimi",
    "Buyur mənə de",
    "Ə di nolub Ədalət Ədalət",
    "Buyur sözünü mənə de",
    "/ban az tağ ele",
    "Ay xanım yer ged o yana istirahət edirem",
    "Yatre o yapon rejimi ilədi her an yata biler",
    "az bəsdidəəəəəəə",
    "Get çay gətir,Cəld ol",
    "manatdan 1 nefer qaldı",
    "Kiməm mən"
)



