# Bu repo edalet_22 tərəfindən 18.01.2023 tarixində yığılıb
# Bu repodan icazəsiz hər hansı kodu sətri məlumatı kopyalıyıb
# Öz adına çıxaran peysərdi
# Bu yazıları silmədən işlədin

# t.me/RoBotlarimTg | t.me/edaletsup
# t.me/edalet_22


from komekçi.edalet import Edalet
from telethon import events, Button
import random


#---------------------------------------------------------------Qrupa yeni istifadəçi qoşulanda---------------------------------------------------------------------------------#

@Edalet.on(events.ChatAction)
async def handler(event):
    if event.user_joined:
        await event.reply(f"Salam qrupa xoş gəldin")
        
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

@Edalet.on(events.NewMessage(pattern='(?i)/start+'))
async def yeni_mesaj(event: events.NewMessage.Event):
    await event.reply(f"👋🏻 Salam "[{usr.first_name}](tg://user?id={usr.id})" mən @edalet_22 -nin asistaniyam\nMənə start verdiyin hakkında məlumatı Sahibimə dedim 📨")
f"[{usr.first_name}](tg://user?id={usr.id}) "
                      
                      
                      
                      
                      
      
print(">> Edalet qoz kimi işləyir  <<")
Edalet.run_until_disconnected()
