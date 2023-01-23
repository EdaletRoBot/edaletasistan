from Plugins.komekci.edaletconfig import edalet
from telethon import TelegramClient
from telethon import events

#-Yeni komandalar
@edalet.on(events.NewMessage(pattern="^/bots$"))
async def bots(event):
    if event.fwd_from:
        return
    mentions = "**Qrupdakı botlar:**\n"
    async for user in event.edalet.iter_participants(event.chat_id, filter=ChannelParticipantsBots):
        if not user.deleted:
            mentions += f"\n[{user.first_name}](tg://user?id={user.id}) `{user.id}`"
        else:
            mentions += f"\nSilinən hesab `{user.id}`"
    await event.reply(mentions)
