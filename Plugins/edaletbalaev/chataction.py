from Plugins.komekci.edaletconfig import edalet
from telethon import events, Button
from telethon.tl.types import ChannelParticipantsAdmins
import random
#
from requests import get, post
from os import remove
from telethon.tl.functions.users import GetFullUserRequest
from time import time

 

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



