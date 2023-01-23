import os


class Config():
    # Bu dəyərləri my.telegram.org saytından əldə edin
    #>>> https://my.telegram.org
    API_ID = int(os.environ.get("API_ID","28054551"))
    API_HASH = os.environ.get("API_HASH","64a0620c2644ceff0c1058a4ffc861ad")
    BOT_TOKEN = "5883816340:AAFJpGNHNPNvogeKaLH0duNJjpchsmQ1UOg"
    BOT_USERNAME = os.environ.get("BOT_USERNAME","Ədalət")
    BOT_NAME = os.environ.get("BOT_NAME","EdaletRoBot")
