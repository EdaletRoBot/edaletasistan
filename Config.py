import os


class Config():
    # Bu dəyərləri my.telegram.org saytından əldə edin
    #>>> https://my.telegram.org
    API_ID = int(os.environ.get("API_ID","28054551"))
    API_HASH = os.environ.get("API_HASH","64a0620c2644ceff0c1058a4ffc861ad")
    BOT_TOKEN = "5628406386:AAGE4oMxDksUKHl6Urr8IeIpDHVoH8tV8PI"
    BOT_USERNAME = os.environ.get("BOT_USERNAME","Ədalət")
    BOT_NAME = os.environ.get("BOT_NAME","EdaletRoBot")
