from typing import Union
from aiogram import Bot

async def check(channel: Union[str, int]):
    bot = Bot.get_current()
    #member = 
    await bot.get_chat_member(chat_id=channel)
    #return member.is_chat_member()