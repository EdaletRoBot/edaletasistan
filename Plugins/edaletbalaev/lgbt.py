from requests import get
from os import remove
from telegraph import upload_file
from Plugins.komekci.eventsimport register
from Plugins.komekci.edaletconfig import edalet



@edalet.on(events.NewMessage(pattern="^/lgbt$"))
async def lgbt(event):
    if not event.is_reply:
        return await event.edit('**Lütfen bir mesaja yanıt verin!**')

    await event.edit("`🏳️‍🌈`")
    reply = await event.get_reply_message()
    foto = await event.client.download_profile_photo(reply.from_id)
    if foto == None:
        return await event.edit("`Bu kişinin profil fotoğrafı yüklemek için yardıma ihtiyacı var!`")
    
    avatar = upload_file(foto)
    
    r = get(f"https://some-random-api.ml/canvas/gay?avatar=https://telegra.ph{avatar[0]}", allow_redirects=True)
    open('EdaletRoBot.png', 'wb').write(r.content)
    await event.client.send_file(event.chat_id, "EdaletRoBot.png", caption="[🏳️‍🌈](https://t.me/EdaletRoBot)", reply_to=reply)
    await event.delete()
    remove(foto)
    remove("EdaletRoBot.png")
    
    
    Print("Lgbt dide hemiseki kimi")
