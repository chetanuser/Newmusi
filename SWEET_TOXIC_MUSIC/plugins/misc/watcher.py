from pyrogram import filters
from pyrogram.types import Message

from SWEET_TOXIC_MUSIC import app
from SWEET_TOXIC_MUSIC.core.call import WEREWOLF_DEMON

welcome = 20
close = 30


@app.on_message(filters.video_chat_started, group=welcome)
@app.on_message(filters.video_chat_ended, group=close)
async def welcome(_, message: Message):
    await WEREWOLF_DEMON.stop_stream_force(message.chat.id)
