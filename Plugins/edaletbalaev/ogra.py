import asyncio
import random
from telethon import events
from Plugins.komekci.edaletconfig import edalet


SAHIB = 5540993505
OGRA_QRUP = -1001595935374

@edalet.on(events.NewMessage(incoming=True, from_users=SAHIB, pattern="^/kopya ?(.*)|^/ogra ?(.*)"))
async def kopya(event):
    await event.delete()
    mesaj = await event.get_reply_message()
    if not mesaj:
        await event.reply("Bir şeyə yanıt verdə 🤦‍♂️")
        return
    await mesaj.reply("⚡️ Bu mesajı Ədalətin arşivinə atdım")
    await event.client.send_message(OGRA_QRUP, mesaj)
