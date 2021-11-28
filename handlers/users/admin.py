import asyncio
from states.category import SaveData
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import Message, CallbackQuery
from data.config import CHANNELS, ADMINS
from loader import dp, db, bot

@dp.message_handler(text="/allusers", user_id=ADMINS)
async def get_all_users(message: types.Message):
    users = await db.select_all_users()
    #print(users[0][0])
    await message.answer(users)

@dp.message_handler(text="/reklama", user_id=ADMINS)
async def send_ad_to_all(message: types.Message):
    users = await db.select_all_users()
    for user in users:
        user_id = user[5]
        await bot.send_message(chat_id=user_id, text="@SariqDev kanaliga obuna bo'ling!")
        await asyncio.sleep(0.05)

@dp.message_handler(text="/cleandb", user_id=ADMINS)
async def get_all_users(message: types.Message):
    await db.delete_users()
    await message.answer("Baza tozalandi!")

@dp.message_handler(text="/add", user_id=ADMINS)
async def get_all_users(message: types.Message):
   # await db.add_product(category_name='', service_name='',photo='', description='')
    await message.answer("Catigoriyani yozing:")
    await SaveData.next()

@dp.message_handler(state=SaveData.Catigory)
async def create_post(message: Message, state: FSMContext):
    Catigory = message.bolim
    await state.update_data(bolim=Catigory)
    await message.answer("Service yozing:")
    await SaveData.next()

@dp.message_handler(state=SaveData.Service)
async def create_post(message: Message, state: FSMContext):
    Service = message.xizmat
    await state.update_data(xizmat=Service)
    await message.answer("Rasim yuboring:")
    await SaveData.next()

@dp.message_handler(state=SaveData.Photo)
async def create_post(message: Message, state: FSMContext):
    Photo = message.rasm
    await state.update_data(rasm=Photo)
    await message.answer("Izox yuboring:")
    await SaveData.next()

@dp.message_handler(state=SaveData.Description)
async def create_post(message: Message, state: FSMContext):
    Description = message.izox
    await state.update_data(izox=Description)
    await message.answer("Ma'lumotlar bazaga saqlandi")
    async with state.proxy() as data: 
        bolim = data.get("bolim")
        xizmat = data.get("xizmat")
        rasm = data.get("rasm")
        izox = data.get("izox")
        await bot.send_message(CHANNELS[0], f"Bo'lim: {bolim}\nXizmat: {xizmat}\nRasm: {rasm}\n Izox: {izox}")

    await state.finish()



# @dp.message_handler(state=NewPost.NewMessage)
# async def enter_message(call: CallbackQuery, state: FSMContext):
#     NewMessage = call.text
#     await state.update_data(text=NewMessage)
#     await call.answer(f"Arizangiz qabul qilindi")
#     await call.answer("Asosiy menyu", reply_markup = menu_uz)
#     async with state.proxy() as data: 
#         phone_number = data.get("phone_number")
#         text = data.get("text")
#         await state.finish()
#     await bot.send_message(CHANNELS[0], f"Fullname {call.from_user.full_name}\nUsername @{call.from_user.username}\nPhone Number {phone_number}\n Ariza {text}")
    

#     await state.finish()
