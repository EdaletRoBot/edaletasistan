# **🐺 EdaletRoBot** <img title="PP" height="40" src="https://avatars.githubusercontent.com/u/99437747?v=4">

## **🌐 Əsasən özüm ve bəzi kodları aykhan_s köməyi ilə yazmışam**
</br>

- İçində sadə funksiyalar var.

- Özünü multi bot kimi aparır.
</br>

## Örnek Plugin
```python
from userbot.events import register
from userbot.cmdhelp import CmdHelp # <-- Bunu ekleyin.

@register(outgoing=True, pattern="^.deneme")
async def deneme(event):
    await event.edit('Gerçekten deneme!')

Help = CmdHelp('deneme') # Bilgi ekleyeceğiz diyoruz.
Help.add_command('deneme', # Komut
    None, # Komut parametresi varsa yazın yoksa None yazın
    'Gerçekten deneme yapıyor!', # Komut açıklaması
    'deneme' # Örnek kullanım.
    )
Help.add_info('@Fusuf tarafından yapılmıştır.') # Bilgi ekleyebilirsiniz.
# Ya da uyarı --> Help.add_warning('KULLANMA!')
Help.add() # Ve Ekleyelim.
```

### **🕹 Qurulum:**

<p><a href="https://heroku.com/deploy?template=https://github.com/Fakebody31/edaletasistan"><img alt="Heroku" width="52px" src="https://www.nicepng.com/png/full/223-2233246_heroku-logo-salesforce-heroku.png"></p>

### **📨 Əlaqə :**

[![Github](https://img.shields.io/badge/Github-525252?style=for-the-badge&logo=github)](https://github.com/EdaletRoBot) [![Opensource](https://img.shields.io/badge/Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white)](https://t.me/edalet_22)

</br>
