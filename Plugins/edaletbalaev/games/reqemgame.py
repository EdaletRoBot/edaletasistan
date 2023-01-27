import asyncio
import random
from telethon import events
from Plugins.komekci.edaletconfig import edalet


@edalet.on(events.NewMessage(pattern="/start"))
async def start(event):
    await event.respond('Salam, /game yazaraq oyunu başlaya bilərsiniz.')

# Rastgele bir sayı seçin
number_to_guess = random.randint(1, 500)

# /game komutunu dinleyin
@edalet.on(events.NewMessage(pattern='/game'))
async def game_handler(event):
    await event.respond('Oyun başladı! 🎊 1 ile 500 arasında bir rəaqəm təxmin edin:')
    edalet.add_event_handler(guess_number)

# Kullanıcının tahmini alın
async def guess_number(event):
    # Kullanıcının tahmini sayıyı alın
    guess = int(event.message.message)
    if guess == number_to_guess:
        await edalet.send_message(event.message.to_id, 'Təbriklər düz cavabı tapdınız 👍\n/game yazaraq yenidən oynayın.')
        edalet.remove_event_handler(guess_number)
    elif guess < number_to_guess:
        await edalet.send_message(event.message.to_id, 'Qalx biraz.❌')
    else:
        await edalet.send_message(event.message.to_id, 'Çox oldu birazda düş.❌')
    event = await edalet.wait_for_event(events.NewMessage(incoming=True))
    await guess_number(event)


@edalet.on(events.NewMessage(pattern='/goster'))
async def show_number(event):
    await edalet.send_message(event.chat_id, 'Rəqəm: {}'.format(number_to_guess))
