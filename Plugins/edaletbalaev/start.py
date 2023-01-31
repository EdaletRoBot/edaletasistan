from Plugins.komekci.edaletconfig import edalet
from telethon import events, Button
from telethon.tl.types import ChannelParticipantsAdmins
import random
#
from requests import get, post
from os import remove
from telethon.tl.functions.users import GetFullUserRequest
from time import time



@edalet.on(events.NewMessage(pattern="^/start$"))
async def start(event):
  if event.is_private:
    async for usr in event.chat.iter_participants():
     ad = f"[{usr.first_name}](tg://user?id={usr.id}) "
     await event.reply(f"Salam {ad},Mən [Ədalət](t.me/edalet_22) tərəfindən yazılmış bir çox funksiyaya malik botam", buttons=(
        [Button.inline("📖 Əmrlər", data="help")],
        [Button.url("🔊 PlayList", url="https://t.me/EdaletRoBotPlayList"),
        Button.url("📣 Kanal", url="https://t.me/RoBotlarimTg"),
        Button.url("👤 Sahib", url="https://t.me/edalet_22")],
        [Button.url('➕ Məni Qrupa əlavə et ➕','http://t.me/EdaletRoBot?startgroup=a')],
    ), 
    link_preview=False)

  if event.is_group:
    return await client.send_message(event.chat_id, f"** Məni qrupunuza dəvət etdiyiniz üçün sagolun 🥰**", buttons=(
                     [Button.url('📖 Əmrlər','data="help"')],
               [Button.url('👤 Sahib', 'https://t.me/edalet_22'),
          Button.url('📣 Kanal', 'https://t.me/RoBotlarimTg')],
                    ),
                    link_preview=False)




@edalet.on(events.callbackquery.CallbackQuery(data="start"))
async def handler(event):
    async for usr in edalet.iter_participants(event.chat_id):
     ad = f"[{usr.first_name}](tg://user?id={usr.id}) "
     await event.edit(f"Salam {ad},Mən [Ədalət](t.me/edalet_22) tərəfindən yazılmış bir çox funksiyaya malik botam", buttons=(
        [Button.inline("📖 Əmrlər", data="help")],
        [Button.url("🔊 PlayList", url="https://t.me/EdaletRoBotPlayList"),
        Button.url("📣 Kanal", url="https://t.me/RoBotlarimTg"),
        Button.url("👤 Sahib", url="https://t.me/edalet_22")],
        [Button.url('➕ Məni Qrupa əlavə et ➕','http://t.me/EdaletRoBot?startgroup=a')],
    ), 
                    link_preview=False)


@edalet.on(events.callbackquery.CallbackQuery(data="help"))
async def handler(event):   
    await event.edit(f"📮 @EdaletRoBot əmirləri bunlardır 📮\n\n\n/ship - Qrup içərisində iki random istifadəçini shipləyir\n/telegraph - yanıt verdiyiniz şəkli telegraph linkinə çevirər\n/id - İstifadəçi id sini göstərir\n/banda - qrupda olan silinmiş hesabları qrupdan atar\n/bots - qrupda olan botları göstərir\n/admins - qrupdakı adminleri göstərir\n/song - YouTube dən mahnı yükləyir\n/video - YouTube dən video yükləyir\n\nSahibim bekar olduqca yeni funksiyalar əlave edəcək", buttons=(
                 [Button.url('📣 Kanal', 'https://t.me/RoBotlarimTg'),
                      Button.url('👤 Sahib', 'https://t.me/edalet_22')],
                 [Button.inline(f"🔙 Geri", data="start")]
                    ),
                    link_preview=False)
 

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
    "/ban {ad} az tağ ele",
    "Ay xanım yer ged o yana istirahət edirem",
    "Yatre o yapon rejimi ilədi her an yata biler",
    "az bəsdidəəəəəəə",
    "Get çay gətir,Cəld ol",
)



