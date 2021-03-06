import sqlite3
import asyncpg
from functools import cache
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, ReplyKeyboardRemove
from keyboards.default.language_keyboard import menu
from keyboards.default.menu_keyboard_uz import menu_uz, menu_ru
from keyboards.default.contact import contact, contact_ru
from data.config import CHANNELS

from loader import dp, db, bot
from states.channel import NewPost 


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    
    try:
        user = await db.add_user(telegram_id=message.from_user.id,
                                 full_name=message.from_user.full_name,
                                 #phone_number='1234567',#message.from_user.contact, 
                                # ariza='text',#message.from_user.answer,
                                 username=message.from_user.username)
    except asyncpg.exceptions.UniqueViolationError:
        user = await db.select_user(telegram_id=message.from_user.id)


    await message.answer(f"Assalom alekum, {message.from_user.full_name}!\n Bizning xizmatlarimizga xush kelibsiz, bizda ta'mirlash va ko'chmas mulk xizmatlari mavjud", reply_markup = menu)
    # Adminga xabar beramiz
    # count = await db.count_users()
    # msg = f"{user[1]} bazaga qo'shildi.\nBazada {count} ta foydalanuvchi bor."
    # await bot.send_message(chat_id=CHANNELS[0], text=msg)



@dp.message_handler(text = "πΊπΏ O'zbekcha")
async def show_menu(message: Message):
    await message.answer("Asosiy menyu", reply_markup = menu_uz)
    #info =  await db.get_categories(menu_language="UZB", category_name="Avto servis", service_name="Polirovka")
    #message.reply_photo(info) #caption=Description
    #await message.answer_photo(info)

@dp.message_handler(text = "π Biz bilan bog'lanish")
async def show_menu(message: Message, state: FSMContext):
    await message.answer("Iltimis raqamingizni yuboring ...", reply_markup = contact)
    await NewPost.PhoneNumber.set ()

@dp.message_handler(text = "Ortga qaytish", state=NewPost.PhoneNumber)
async def show_menu(message: Message, state: FSMContext):
   await message.answer( reply_markup = menu_uz)  #replay_markup=ReplayKeyboardRemove()
   await state.finish()

#========================Rus tili===============================

@dp.message_handler(text = "π·πΊ Π ΡΡΡΠΊΠΈΠΉ")
async def show_menu(message: Message):
    await message.answer("ΠΠ»Π°Π²Π½ΠΎΠ΅ ΠΌΠ΅Π½Ρ", reply_markup = menu_ru)


@dp.message_handler(text = "π Π‘Π²ΡΠ·Π°ΡΡ")
async def show_menu(message: Message, state: FSMContext):
    await message.answer("ΠΠΎΠΆΠ°Π»ΡΠΉΡΡΠ°, ΠΎΡΠΏΡΠ°Π²ΡΡΠ΅ ΠΊΠΎΠ½ΡΠ°ΠΊΡ ...", reply_markup = contact_ru)
    await NewPost.PhoneNumber_ru.set ()

@dp.message_handler(text = "ΠΠ΅ΡΠ½ΠΈΡΠ΅ΡΡ Π½Π°Π·Π°Π΄", state=NewPost.PhoneNumber_ru)
async def show_menu(message: Message, state: FSMContext):
    await message.answer("ΠΠ»Π°Π²Π½ΠΎΠ΅ ΠΌΠ΅Π½Ρ", reply_markup = menu_ru)  #replay_markup=ReplayKeyboardRemove()
    await state.finish()


