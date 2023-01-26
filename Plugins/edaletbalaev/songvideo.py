#sahibim #Ruslan

#əməyə xatir kanala qoşulun @DvBotlar
import os, youtube_dl, requests, aiohttp, wget, time
from Config import Config
from youtube_search import YoutubeSearch
from pyrogram.handlers import MessageHandler
from yt_dlp import YoutubeDL
from io import BytesIO
from aiohttp import ClientSession
from pyrogram import Client, filters, idle
import yt_dlp
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Message
)

bot = Client(
    'MusicAzBot',
    bot_token = Config.BOT_TOKEN,
    api_id = Config.API_ID,
    api_hash = Config.API_HASH
)

OWNER_ID = [5324143657]


#musiqi əmri#

@bot.on_message(filters.command("song") & ~filters.edited)
def song(_, message):
    query = " ".join(message.command[1:])
    m = message.reply("<b>Musiqi Axtarılır ... 🔍</b>")
    ydl_ops = {"format": "bestaudio[ext=m4a]"}
    try:
        results = YoutubeSearch(query, max_results=1).to_dict()
        link = f"https://youtube.com{results[0]['url_suffix']}"
        title = results[0]["title"][:40]
        thumbnail = results[0]["thumbnails"][0]
        thumb_name = f"{title}.jpg"
        thumb = requests.get(thumbnail, allow_redirects=True)
        open(thumb_name, "wb").write(thumb.content)
        duration = results[0]["duration"]

    except Exception as e:
        m.edit("İstədiyiniz musiqi tapılmadı 😔")
        print(str(e))
        return
    m.edit("`📥 Musiqini tapdım və yükləyirəm.`")
    try:
        with yt_dlp.YoutubeDL(ydl_ops) as ydl:
            info_dict = ydl.extract_info(link, download=False)
            audio_file = ydl.prepare_filename(info_dict)
            ydl.process_info(info_dict)
        rep = f'📜 **Başlıq**: [{title[:35]}]({link})\n⏳ **Müddət**: `{duration}`\n'f"🎵 Yüklədi [EdaletRoBot](https://t.me/EdaletRoBot)\n'f"[🎧 Play List](https://t.me/EdaletRoBotPlayList)"
        secmul, dur, dur_arr = 1, 0, duration.split(":")
        for i in range(len(dur_arr) - 1, -1, -1):
            dur += int(float(dur_arr[i])) * secmul
            secmul *= 60
        m.edit("📤 Yüklənir..")
        message.reply_audio(audio_file, caption=rep, parse_mode='md',quote=False, title=title, duration=dur, thumb=thumb_name, performer=f"{Config.PLAYLIST_NAME}")
        m.delete()
        bot.send_audio(chat_id=Config.PLAYLIST_ID, audio=audio_file, caption=rep, performer=f"EdaletRoBot", parse_mode='md', title=title, duration=dur, thumb=thumb_name)
    except Exception as e:
        m.edit('**⚠️ Gözlənilməyən xəta yarandı.**\n**Xahiş edirəm xətanı sahibimə xəbərdar et!**')
        print(e)

    try:
        os.remove(audio_file)
        os.remove(thumb_name)
    except Exception as e:
        print(e)


@bot.on_message(filters.command("video") & ~filters.edited)
async def vsong(client, message):
    ydl_opts = {
        "format": "best",
        "keepvideo": True,
        "prefer_ffmpeg": False,
        "geo_bypass": True,
        "outtmpl": "%(title)s.%(ext)s",
        "quite": True,
    }
    query = " ".join(message.command[1:])
    try:
        results = YoutubeSearch(query, max_results=1).to_dict()
        link = f"https://youtube.com{results[0]['url_suffix']}"
        title = results[0]["title"][:40]
        thumbnail = results[0]["thumbnails"][0]
        thumb_name = f"{title}.jpg"
        thumb = requests.get(thumbnail, allow_redirects=True)
        open(thumb_name, "wb").write(thumb.content)
        results[0]["duration"]
        results[0]["url_suffix"]
        results[0]["views"]
        message.from_user.mention
    except Exception as e:
        print(e)
    try:
        msg = await message.reply("📥 **Video Axtarılır...**")
        with YoutubeDL(ydl_opts) as ytdl:
            ytdl_data = ytdl.extract_info(link, download=True)
            file_name = ytdl.prepare_filename(ytdl_data)
    except Exception as e:
        return await msg.edit(f"🚫 **Xəta:** {e}")
    preview = wget.download(thumbnail)
    await msg.edit("📤 **Videonu tapdım və endirirəm ...**")
    await message.reply_video(
        file_name,
        duration=int(ytdl_data["duration"]),
        thumb=preview,
        caption=ytdl_data["title"],
    )
    try:
        os.remove(file_name)
        await msg.delete()
    except Exception as e:
        print(e)



print("song ve video molulu işləyir")
bot.run()
