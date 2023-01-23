import os
import logging
import requests
import aiohttp
import youtube_dl
from pyrogram import filters, Client, idle
from youtube_search import YoutubeSearch
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from Config import API_ID, API_HASH, BOT_TOKEN


# logging
bot = Client(
   "Song Downloader",
   api_id=API_ID,
   api_hash=API_HASH,
   bot_token=BOT_TOKEN,
)

@bot.on_message(filters.command("song") & ~filters.edited)
async def song(_, message):
    if len(message.command) < 2:
       return await message.reply("**Usage:**\n - `Eg:- /song Saybu Asta dur`")
    query = message.text.split(None, 1)[1]
    shed = await message.reply("🔎 Sorğu axtarılır...")
    ydl_opts = {
       "format": "bestaudio[ext=m4a]",
       "geo-bypass": True,
       "nocheckcertificate": True,
       "outtmpl": "downloads/%(id)s.%(ext)s",
       }
    try:
        results = YoutubeSearch(query, max_results=1).to_dict()
        link = f"https://youtube.com{results[0]['url_suffix']}"
        #print(results)
        title = results[0]["title"][:40]       
        thumbnail = results[0]["thumbnails"][0]
        thumb_name = f'thumb{title}.jpg'
        thumb = requests.get(thumbnail, allow_redirects=True)
        open(thumb_name, 'wb').write(thumb.content)

        duration = results[0]["duration"]
        url_suffix = results[0]["url_suffix"]
        views = results[0]["views"]
        channel = results[0]["channel"]
    except Exception as e:
        await shed.edit(
            "❌ Found Nothing.\n\nTry another keywork or maybe spell it properly."
        )
        print(str(e))
        return
    await shed.edit("📥 Yüklənir...")
    try:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(link, download=False)
            audio_file = ydl.prepare_filename(info_dict)
            ydl.process_info(info_dict)
        rep = "🎵 Musiqi Kanalım -  @AudioWaveMusic"
        secmul, dur, dur_arr = 1, 0, duration.split(':')
        for i in range(len(dur_arr)-1, -1, -1):
            dur += (int(dur_arr[i]) * secmul)
            secmul *= 3
        await shed.edit("📤 Göndərilir...")
        s = await message.reply_audio(audio_file, caption=rep, thumb=thumb_name, parse_mode='md', title=title, duration=dur, performer=channel)
        await shed.delete()
    except Exception as e:
        await shed.edit("❌ Xəta.!")
        print(e)

    try:
        os.remove(audio_file)
        os.remove(thumb_name)
    except Exception as e:
        print(e)

bot.start()
idle()
