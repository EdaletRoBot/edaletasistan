#1-Qrupda random istifadəçiləri ship eder
from telethon import TelegramClient as tg
from telethon import events
import random
import time



urekler = ("❤️", "💘", "💝", "💖", "💗", "💓", "💞", "💕", "❤️‍🔥", "❤️‍🩹", "❤️", "🧡", "💛", "💚", "💙", "💜", "🤎", "🖤", "🤍")

@edalet.on(events.NewMessage(pattern="/ship"))
async def handler(event):
    if event.is_private:
        return await event.respond("**Bu əmr qruplar üçün etibarlıdır!**")
    # Get the chat from the event
    chat = await event.get_chat()
    # Get the users in the chatç
    users = await bot.get_participants(chat)
    # Get two random users
    user1, user2 = random.sample(users, 2)
    # Send a message tagging the two random users
    await event.respond(f'[{user1.first_name}](tg://user?id={user1.id}) {random.choice(urekler)} [{user2.first_name}](tg://user?id={user2.id})')
    
    
def main():
    edalet.run_until_disconnected()
    
    
#________________________________________________@edalet_22 Tərəfinfən yazılıb icazəsiz götürən ata desin mene_________________________________________________________#
