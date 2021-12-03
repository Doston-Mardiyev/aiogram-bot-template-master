import asyncio
from os import mkdir

from aiogram.types.message import ContentType, ContentTypes
from aiogram.types.video import Video
from states.category import SaveData
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import Message, CallbackQuery
from aiogram.types import Message, ReplyKeyboardRemove
from keyboards.default.menu_keyboard_uz import menu_uz, menu_ru
from keyboards.default.admin_keyboard import menu_admin_ru, menu_admin_uz, avto_admin_uz, avto_admin_ru, uy_admin_uz, uy_admin_ru, language

from data.config import CHANNELS, ADMINS
from loader import dp, db, bot
from pathlib import Path

# download_path = Path().joinpath("download")
# download_path.mkdir(parents = True, exist_ok=True)

@dp.message_handler(text="/user", user_id=ADMINS)
async def get_all_users(message: types.Message):
    users = await db.select_all_users()
    #print(users[0][0])
    await message.answer(users)

#==========================reklama===========================
# @dp.message_handler(text="/reklama", user_id=ADMINS, state=None)
# async def send_ad_to_all(message: types.Message):
#     await message.answer("Rasm yuboring:")
#     await SaveData.Photo.set() 
    
 
# @dp.message_handler(state=SaveData.Photo, content_types=types.ContentType.ANY)
# async def get_photo(message: Message, state: FSMContext):
#     Reklama_rasm = message.photo[-1].file_id
#     await state.update_data(Reklama_rasm=Reklama_rasm)
#     await message.answer("Izox yuboring:")
#     await SaveData.next()

# @dp.message_handler(state=SaveData.Description)
# async def create_post(message: Message, state: FSMContext):
#     Izox = message.text
#     await state.update_data(Izox=Izox)
#     await message.answer("Ma'lumotlar bazaga saqlandi")
#     async with state.proxy() as data: 
#         Reklama_rasm = data.get("Reklama_rasm")
#         Izox = data.get("Izox")
#         await db.add_product(photo=Reklama_rasm, description=Izox)

#     ad = await db.get_categories()
#     users = await db.select_all_users()
#     for adv in ad:
#         ad_photo = adv[2]
#         ad_description = adv[1]
#         for user in users:
#             user_id = user[5]
#             advertise = await message.answer_photo(ad_photo, caption=ad_description)
#             await bot.send_message(chat_id=user_id, text=advertise)
#             await asyncio.sleep(0.05)
    
#===================================================================

@dp.message_handler(text="/clean", user_id=ADMINS)
async def get_all_users(message: types.Message):
    await db.drop_products()
    await message.answer("Baza tozalandi!")


@dp.message_handler(text="/admin", user_id=ADMINS, state=None)
async def get_all_users(message: types.Message):
    await message.answer("Tilni tanlang:", reply_markup = language)
    await SaveData.Language.set()

@dp.message_handler(content_types=["text"], state=SaveData.Language)
async def choosing_language(message: Message, state: FSMContext):
    if message.text == "UZB":
            Language = message.text
            await state.update_data(Language=Language)
            await message.answer("Katigoriyani tanlang:", reply_markup = menu_admin_uz)
            await SaveData.next()

            @dp.message_handler(content_types=["text"], state=SaveData.Catigory)
            async def catigory_uz(message: Message, state: FSMContext):
                if message.text == "Kochmas mulk":
                        Catigory = message.text
                        await state.update_data(Catigory=Catigory)
                        await message.answer("Servisni tanlang:", reply_markup =  uy_admin_uz)
                        await SaveData.next()
                else:
                        Catigory = message.text
                        await state.update_data(Catigory=Catigory)
                        await message.answer("Servisni tanlang:", reply_markup = avto_admin_uz)
                        await SaveData.next()

    else:
            Language = message.text
            await state.update_data(Language=Language)
            await message.answer("Katigoriyani tanlang:", reply_markup = menu_admin_ru)
            await SaveData.next()


            @dp.message_handler(content_types=["text"], state=SaveData.Catigory)
            async def catigory_ru(message: Message, state: FSMContext):
                if message.text == "Недвижимость":
                        Catigory = message.text
                        await state.update_data(Catigory=Catigory)
                        await message.answer("Servisni tanlang:", reply_markup =  uy_admin_ru)
                        await SaveData.next()
                else:
                        Catigory = message.text
                        await state.update_data(Catigory=Catigory)
                        await message.answer("Servisni tanlang:", reply_markup = avto_admin_ru)
                        await SaveData.next()




@dp.message_handler(state=SaveData.Service)
async def create_post(message: Message, state: FSMContext):
    Service = message.text
    await state.update_data(Service=Service)
    await message.answer("Rasim yuboring:", reply_markup = ReplyKeyboardRemove())
    await SaveData.next()

@dp.message_handler(state=SaveData.Photo, content_types=ContentType.ANY)  
async def get_photo(message: Message, state: FSMContext):
    try:
    # Photo = message.video.download
        Photo = message.photo[-1].file_id
    #await message.reply(message.video.file_id)
        await state.update_data(Photo=Photo)
        await message.answer("Izox yuboring:")
        await SaveData.next()
    except: 
         Photo = message.video.file_id
         await state.update_data(Photo=Photo)
         await message.answer("Izox yuboring:")
         await SaveData.next()

@dp.message_handler(state=SaveData.Description)
async def create_post(message: Message, state: FSMContext):
    Description = message.text
    await state.update_data(Description=Description)
    await message.answer("Ma'lumotlar bazaga saqlandi")
    async with state.proxy() as data: 
        Language = data.get("Language")
        Catigory = data.get("Catigory")
        Service = data.get("Service")
        Photo = data.get("Photo")
        Description = data.get("Description")
        await db.add_product(menu_language=Language, category_name=Catigory, service_name=Service, photo=Photo, description=Description)
        await message.answer(f"Til: {Language}\nBo'lim: {Catigory}\nXizmat: {Service}")
        #await message.answer_photo(Photo, caption=Description)
        try:
             await message.answer_video(Photo, caption=Description, reply_markup = menu_uz)
        except:
            await message.answer_photo(Photo, caption=Description, reply_markup = menu_uz)

        

    await state.finish()



#  @dp.message_handler(state=SaveData.Catigory)
#         async def create_post(message: Message, state: FSMContext):
#             Catigory = message.text
#             await state.update_data(Catigory=Catigory)
#             await message.answer("Service yozing:", reply_markup =  uy_admin_uz)
#             await SaveData.next()