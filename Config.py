import os


class Config():
    # Bu dəyərləri my.telegram.org saytından əldə edin
    #>>> https://my.telegram.org
    API_ID = int(os.environ.get("API_ID","28054551"))
    API_HASH = os.environ.get("API_HASH","64a0620c2644ceff0c1058a4ffc861ad")
    BOT_TOKEN = "5628406386:AAF_P7o95g0j3L-h0JefWyHGPFsgXma0Nug"
    BOT_USERNAME = os.environ.get("BOT_USERNAME","Ədalət")
    BOT_NAME = os.environ.get("BOT_NAME","EdaletRoBot")
    PLAYLIST_ID = int(os.environ.get("PLAYLIST_ID ","-1001834511938"))
    PLAYLIST_NAME = os.environ.get("PLAYLIST_NAME","EdaletRoBot PlayList")
