#aykhan_s - terefinden yazılıb bu 
import asyncio
import os
from time import sleep
from urllib.parse import quote_plus
from urllib.error import HTTPError
# Selenium
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from telethon import events
from Plugins.komekci.edaletconfig import edalet


CHROME_DRIVER = "/app/.chromedriver/bin/chromedriver"
GOOGLE_CHROME_BIN = "/app/.apt/usr/bin/google-chrome"
CARBONLANG = "auto"


@aykhan.on(events.NewMessage(pattern="^/carbon ?(.*)"))
async def carbon_api(e):
    mesaj = await e.reply("🔄 __İşlənir...__")
    await e.delete()
    CARBON = 'https://carbon.now.sh/?l={lang}&code={code}'
    global CARBONLANG
    textx = await e.get_reply_message()
    pcode = e.text
    if pcode[8:]:
        pcode = str(pcode[8:])
    elif textx:
        pcode = str(textx.message)
    code = quote_plus(pcode)
    await mesaj.edit("🔄 İşlənir...\nTamamlanma Faizi: **25%**")
    if os.path.isfile("./carbon.png"):
        os.remove("./carbon.png")
    url = CARBON.format(code=code, lang=CARBONLANG)
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.binary_location = GOOGLE_CHROME_BIN
    chrome_options.add_argument("--window-size=1920x1080")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-gpu")
    prefs = {'download.default_directory': './'}
    chrome_options.add_experimental_option('prefs', prefs)
    driver = webdriver.Chrome(executable_path=CHROME_DRIVER,
                              options=chrome_options)
    driver.get(url)
    await mesaj.edit("🔄 İşlənir...\nTamamlanma Faizi: **50%**")
    download_path = './'
    driver.command_executor._commands["send_command"] = (
        "POST", '/session/$sessionId/chromium/send_command')
    params = {
        'cmd': 'Page.setDownloadBehavior',
        'params': {
            'behavior': 'allow',
            'downloadPath': download_path
        }
    }
    command_result = driver.execute("send_command", params)
    driver.find_element(by=By.XPATH, value="//button[contains(text(),'Export')]").click()
    driver.find_element(by=By.ID, value="export-menu").click()
    # driver.find_element(by=By.XPATH, value="//button[contains(text(),'4x')]").click()
    # driver.find_element(by=By.XPATH, value="//button[contains(text(),'PNG')]").click()
    await e.edit("`İşlənir...\nTamamlanma Faizi: 75%`")
    # TGUSERBOT
    while not os.path.isfile("./carbon.png"):
        await asyncio.sleep(0.5)
    await mesaj.edit("🔄 İşlənir...\nTamamlanma Faizi: **100%**")
    file = './carbon.png'
    await mesaj.edit("✅ __Carbon hazırdı göndərirəm...__")
    await e.client.send_file(
        e.chat_id,
        file,
        caption=f"Bu şəkil @EdaletRoBot vasitəsilə Carbona çevrildi",
        force_document=True,
        reply_to=e.message.reply_to_msg_id,
    )

    os.remove('./carbon.png')
    driver.quit()
    await mesaj.delete()



print("Carbon modulu yükləndi")
