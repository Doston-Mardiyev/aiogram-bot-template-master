
from aiogram.types import Message
from keyboards.inline.avto_key import avto_menu_uz, avto_menu_ru
from keyboards.inline.kochmas_mulk import uy_menu_ru, uy_menu_uz

from loader import dp


@dp.message_handler(text_contains = "🚘 Avto servis")
async def select_category(message: Message):
    await message.answer("🚘 Avto servis",reply_markup = avto_menu_uz)

@dp.message_handler(text_contains = "🚘 Авто сервис")
async def select_category(message: Message):
    await message.answer("🚘 Авто сервис",reply_markup = avto_menu_ru)

@dp.message_handler(text_contains = "🏠 Ko'chmas mulk")
async def select_category(message: Message):
    await message.answer("🏠 Ko'chmas mulk",reply_markup = uy_menu_uz)

@dp.message_handler(text_contains = "🏠 Недвижимость")
async def select_category(message: Message):
    await message.answer("🏠 Недвижимость",reply_markup = uy_menu_ru)

@dp.message_handler(text_contains = "ℹ️ О нас")
async def select_category(message: Message):
    await message.answer("citihabitat")

@dp.message_handler(text_contains = "ℹ️ Biz haqimizda")
async def select_category(message: Message):
    await message.answer("citihabitat")

@dp.message_handler(text_contains = "📞 Kontakt")
async def select_category(message: Message):
    await message.answer("📨 azizbek.lukmanov@gmail.com\n🌎 http://citihabitat.uz/ \n🚀 @citihabitat\n📞 +998 97 461 61 99\n📞 +998 95 199 91 97")

@dp.message_handler(text_contains = "📞 Контакт")
async def select_category(message: Message):
    await message.answer("📨 azizbek.lukmanov@gmail.com\n🌎 http://citihabitat.uz/ \n🚀 @citihabitat\n📞 +998 97 461 61 99\n📞 +998 95 199 91 97")