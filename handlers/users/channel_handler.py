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
async def enter_message(message: Message, state: FSMContext):
    NewMessage = message.text
    await state.update_data(text=NewMessage)
    await message.answer(f"Arizangiz qabul qilindi, operatorlarimiz tez orada siz bilan bog'lanishadi.")
    await message.answer("Asosiy menu",reply_markup = menu_uz)
    async with state.proxy() as data: 
        phone_number = data.get("phone_number")
        text = data.get("text")
        await state.finish()
    await bot.send_message(CHANNELS[0], f"Fullname {message.from_user.full_name}\nUsername @{message.from_user.username}\nPhone Number {phone_number}\nAriza {text}")
    #db.update_phone_number(phone_number=phone_number, telegram_id=call.from_user.id)
    #db.update_ariza(ariza=text, telegram_id=call.from_user.id)

    await state.finish()



@dp.message_handler(state=NewPost.PhoneNumber_ru, content_types= types.ContentTypes.CONTACT)
async def create_post(message: Message, state: FSMContext):
    P_number_ru = message.contact.phone_number
    await state.update_data(phone_number=P_number_ru)
    await message.answer("Ваш номер принят. Отправьте заявку ...")
    await NewPost.next()


@dp.message_handler(state=NewPost.NewMessage_ru)
async def enter_message(message: Message, state: FSMContext):
    NewMessage = message.text
    await state.update_data(text=NewMessage)
    await message.answer(f"Ваша заявка принята, наши операторы свяжутся с вами в ближайшее время.")
    await message.answer("Главное меню",reply_markup = menu_ru)
    async with state.proxy() as data: 
        phone_number = data.get("phone_number")
        text = data.get("text")
        await state.finish()
    await bot.send_message(CHANNELS[0], f"Fullname {message.from_user.full_name}\nUsername @{message.from_user.username}\nPhone Number {phone_number}\nAriza {text}")
    #db.update_phone_number(phone_number=phone_number, telegram_id=call.from_user.id)
    #db.update_ariza(ariza=text, telegram_id=call.from_user.id)

    await state.finish()





