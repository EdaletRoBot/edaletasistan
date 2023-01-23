from Plugins.komekci.eventsimport register
from Plugins.komekci.edaletconfig import edalet
from telethon.tl.functions.users import GetFullUserRequest
from time import time
from requests import get, post
from os import remove
from telegraph import upload_file


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



@edalet.on(events.NewMessage(pattern="^/phub$"))
async def tweet(event):
    if not event.is_reply:
        return await event.edit('**Lütfen bir mesaja yanıt verin!**')
    
    if not event.text:
        return await event.edit('**Lütfen bir mesaja yanıt verin!**')

    await event.edit("`Dıtdıtdun (PornHub Intro)...`")
    reply = await event.get_reply_message()
    foto = await event.client.download_profile_photo(reply.from_id)
    if foto == None:
        return await event.edit("`Bu kişinin profil fotoğrafı yüklemek için yardıma ihtiyacı var!`")
    kullanici = await event.client(
        GetFullUserRequest(
            reply.from_id
        )
    )
    url = post(f'https://uguu.se/upload.php', files={'files[]': (f'{time()}.jpg', open(foto, 'rb'))}).json()
    print(url)
    if kullanici.user.username:
        json = get(f"https://nekobot.xyz/api/imagegen?type=phcomment&image={url['files'][0]['url']}&text={reply.message}&username={kullanici.user.username}").json()
    else:
        json = get(f"https://nekobot.xyz/api/imagegen?type=phcomment&image={url['files'][0]['url']}&text={reply.message}&username={kullanici.user.first_name}").json()

    await event.client.send_file(event.chat_id, json["message"], caption="[🔥](https://t.me/AsenaUserBot)", reply_to=reply)
    await event.delete()
    remove(foto)

    
Print("Hahahahaahah phub")


    
    
   
