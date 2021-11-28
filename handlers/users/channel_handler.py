from functools import update_wrapper
import logging

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.types import Message, CallbackQuery
from states.channel import NewPost 
from keyboards.default.menu_keyboard_uz import menu_uz, menu_ru


from data.config import CHANNELS
from loader import dp, db, bot



@dp.message_handler(state=NewPost.PhoneNumber, content_types= types.ContentTypes.CONTACT)
async def create_post(message: Message, state: FSMContext):
    P_number = message.contact.phone_number
    await state.update_data(phone_number=P_number)
    await message.answer("Raqamingiz qabul qilindi iltimos arizangizni yuboring...")
    await NewPost.next()


@dp.message_handler(state=NewPost.NewMessage)
async def enter_message(call: CallbackQuery, state: FSMContext):
    NewMessage = call.text
    await state.update_data(text=NewMessage)
    await call.answer(f"Arizangiz qabul qilindi")
    await call.answer( reply_markup = menu_uz)
    async with state.proxy() as data: 
        phone_number = data.get("phone_number")
        text = data.get("text")
        await state.finish()
    await bot.send_message(CHANNELS[0], f"Fullname {call.from_user.full_name}\nUsername @{call.from_user.username}\nPhone Number {phone_number}\n Ariza {text}")
    #db.update_phone_number(phone_number=phone_number, telegram_id=call.from_user.id)
    #db.update_ariza(ariza=text, telegram_id=call.from_user.id)

    await state.finish()





