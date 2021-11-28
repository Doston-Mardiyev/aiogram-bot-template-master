from functools import cache
from aiogram.types import Message, CallbackQuery
from keyboards.inline.avto_key import avto_menu_uz

from loader import dp

#========inline keybord handler===============
@dp.callback_query_handler(text = "service")
async def select_category(call: CallbackQuery):
    await call.message.answer_photo("menuylar bo'limi")
    #bot.send_photo(chat_id=chat_id, photo=open('tests/test.png', 'rb'))
    #await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text = "service1")
async def select_category(call: CallbackQuery):
    await call.message.answer("menuylar bo'limi 1")
    await call.answer(cache_time=60)

@dp.callback_query_handler(text = "service2")
async def select_category(call: CallbackQuery):
    await call.message.answer("menuylar bo'limi 2")
    await call.answer(cache_time=60)