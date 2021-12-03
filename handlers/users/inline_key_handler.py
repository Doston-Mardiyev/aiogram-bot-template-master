import logging

from aiogram.types import Message, CallbackQuery, message
from keyboards.inline.avto_key import avto_menu_ru, avto_menu_uz
from keyboards.inline.kochmas_mulk import uy_menu_uz, uy_menu_ru
from loader import dp, db, bot

@dp.callback_query_handler(text="Polirovka")
async def cancel_buying(call: CallbackQuery):
    #users = await db.select_all_users()
    info =  await db.get_categories(menu_language = "UZB", category_name= "Avto servis", service_name = "Polirovka")
    for photo in info:
        photo_id = photo[4]
        description = photo[5]
        try:
            await call.message.answer_video(photo_id, caption=description)
        except:
            await call.message.answer_photo(photo_id, caption=description)
    await call.answer(cache_time=60)
    
@dp.callback_query_handler(text="Keramika")
async def cancel_buying(call: CallbackQuery):
    info =  await db.get_categories(menu_language = "UZB", category_name= "Avto servis", service_name = "Keramika")
    for photo in info:
        photo_id = photo[4]
        description = photo[5]
        try:
            await call.message.answer_video(photo_id, caption=description)
        except:
            await call.message.answer_photo(photo_id, caption=description)
    await call.answer(cache_time=60)
    
@dp.callback_query_handler(text="Ximchistka")
async def cancel_buying(call: CallbackQuery):
    info =  await db.get_categories(menu_language = "UZB", category_name= "Avto servis", service_name = "Ximchistka")
    for photo in info:
        photo_id = photo[4]
        description = photo[5]
        try:
            await call.message.answer_video(photo_id, caption=description)
        except:
            await call.message.answer_photo(photo_id, caption=description)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text="Shumoizolyatsiya")
async def cancel_buying(call: CallbackQuery):
    info =  await db.get_categories(menu_language = "UZB", category_name= "Avto servis", service_name = "Shumoizolyatsiya")
    for photo in info:
        photo_id = photo[4]
        description = photo[5]
        try:
            await call.message.answer_video(photo_id, caption=description)
        except:
            await call.message.answer_photo(photo_id, caption=description)
    await call.answer(cache_time=60)
    
@dp.callback_query_handler(text="Tonirovka")
async def cancel_buying(call: CallbackQuery):
    info =  await db.get_categories(menu_language = "UZB", category_name= "Avto servis", service_name = "Tonirovka")
    for photo in info:
        photo_id = photo[4]
        description = photo[5]
        try:
            await call.message.answer_video(photo_id, caption=description)
        except:
            await call.message.answer_photo(photo_id, caption=description)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text="Avtosignallizatsiya")
async def cancel_buying(call: CallbackQuery):
    info =  await db.get_categories(menu_language = "UZB", category_name= "Avto servis", service_name = "Avtosignallizatsiya")
    for photo in info:
        photo_id = photo[4]
        description = photo[5]
        try:
            await call.message.answer_video(photo_id, caption=description)
        except:
            await call.message.answer_photo(photo_id, caption=description)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text="Laminatsiya")
async def cancel_buying(call: CallbackQuery):
    info =  await db.get_categories(menu_language = "UZB", category_name= "Avto servis", service_name = "Laminatsiya")
    for photo in info:
        photo_id = photo[4]
        description = photo[5]
        try:
            await call.message.answer_video(photo_id, caption=description)
        except:
            await call.message.answer_photo(photo_id, caption=description)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text="Chexol")
async def cancel_buying(call: CallbackQuery):
    info =  await db.get_categories(menu_language = "UZB", category_name= "Avto servis", service_name = "Chexol")
    for photo in info:
        photo_id = photo[4]
        description = photo[5]
        try:
            await call.message.answer_video(photo_id, caption=description)
        except:
            await call.message.answer_photo(photo_id, caption=description)
    await call.answer(cache_time=60)


#====================avto ru===================================

@dp.callback_query_handler(text="Полировка")
async def cancel_buying(call: CallbackQuery):
    #users = await db.select_all_users()
    info =  await db.get_categories(menu_language = "RU", category_name= "Авто сервис", service_name = "Полировка")
    for photo in info:
        photo_id = photo[4]
        description = photo[5]
        try:
            await call.message.answer_video(photo_id, caption=description)
        except:
            await call.message.answer_photo(photo_id, caption=description)
        # await call.message.video.file_id
    await call.answer(cache_time=60)
    
@dp.callback_query_handler(text="Керамика")
async def cancel_buying(call: CallbackQuery):
    info =  await db.get_categories(menu_language = "RU", category_name= "Авто сервис", service_name = "Керамика")
    for photo in info:
        photo_id = photo[4]
        description = photo[5]
        try:
            await call.message.answer_video(photo_id, caption=description)
        except:
            await call.message.answer_photo(photo_id, caption=description)
    await call.answer(cache_time=60)
    
@dp.callback_query_handler(text="Химчистка")
async def cancel_buying(call: CallbackQuery):
    info =  await db.get_categories(menu_language = "RU", category_name= "Авто сервис", service_name = "Химчистка")
    for photo in info:
        photo_id = photo[4]
        description = photo[5]
        try:
            await call.message.answer_video(photo_id, caption=description)
        except:
            await call.message.answer_photo(photo_id, caption=description)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text="Шумоизоляция")
async def cancel_buying(call: CallbackQuery):
    info =  await db.get_categories(menu_language = "RU", category_name= "Авто сервис", service_name = "Шумоизоляция")
    for photo in info:
        photo_id = photo[4]
        description = photo[5]
        try:
            await call.message.answer_video(photo_id, caption=description)
        except:
            await call.message.answer_photo(photo_id, caption=description)
    await call.answer(cache_time=60)
    
@dp.callback_query_handler(text="Тонировка")
async def cancel_buying(call: CallbackQuery):
    info =  await db.get_categories(menu_language = "RU", category_name= "Авто сервис", service_name = "Тонировка")
    for photo in info:
        photo_id = photo[4]
        description = photo[5]
        try:
            await call.message.answer_video(photo_id, caption=description)
        except:
            await call.message.answer_photo(photo_id, caption=description)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text="Автосигнализация")
async def cancel_buying(call: CallbackQuery):
    info =  await db.get_categories(menu_language = "RU", category_name= "Авто сервис", service_name = "Автосигнализация")
    for photo in info:
        photo_id = photo[4]
        description = photo[5]
        try:
            await call.message.answer_video(photo_id, caption=description)
        except:
            await call.message.answer_photo(photo_id, caption=description)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text="Ламинирование")
async def cancel_buying(call: CallbackQuery):
    info =  await db.get_categories(menu_language = "RU", category_name= "Авто сервис", service_name = "Ламинирование")
    for photo in info:
        photo_id = photo[4]
        description = photo[5]
        try:
            await call.message.answer_video(photo_id, caption=description)
        except:
            await call.message.answer_photo(photo_id, caption=description)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text="чехол")
async def cancel_buying(call: CallbackQuery):
    info =  await db.get_categories(menu_language = "RU", category_name= "Авто сервис", service_name = "чехол")
    for photo in info:
        photo_id = photo[4]
        description = photo[5]
        try:
            await call.message.answer_video(photo_id, caption=description)
        except:
            await call.message.answer_photo(photo_id, caption=description)
    await call.answer(cache_time=60)




#====================Ko'chmas mulk================================

@dp.callback_query_handler(text="Sotish")
async def cancel_buying(call: CallbackQuery):
    #users = await db.select_all_users()
    info =  await db.get_categories(menu_language = "UZB", category_name= "Kochmas mulk", service_name = "Sotish")
    for photo in info:
        photo_id = photo[4]
        description = photo[5]
        try:
            await call.message.answer_video(photo_id, caption=description)
        except:
            await call.message.answer_photo(photo_id, caption=description)

    await call.answer(cache_time=60)
    
@dp.callback_query_handler(text="Olish")
async def cancel_buying(call: CallbackQuery):
    info =  await db.get_categories(menu_language = "UZB", category_name= "Kochmas mulk", service_name = "Olish")
    for photo in info:
        photo_id = photo[4]
        description = photo[5]
        try:
            await call.message.answer_video(photo_id, caption=description)
        except:
            await call.message.answer_photo(photo_id, caption=description)
    await call.answer(cache_time=60)
    
@dp.callback_query_handler(text="Arendaga berish")
async def cancel_buying(call: CallbackQuery):
    info =  await db.get_categories(menu_language = "UZB", category_name= "Kochmas mulk", service_name = "Arendaga berish")
    for photo in info:
        photo_id = photo[4]
        description = photo[5]
        try:
            await call.message.answer_video(photo_id, caption=description)
        except:
            await call.message.answer_photo(photo_id, caption=description)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text="Arendaga olish")
async def cancel_buying(call: CallbackQuery):
    info =  await db.get_categories(menu_language = "UZB", category_name= "Kochmas mulk", service_name = "Arendaga olish")
    for photo in info:
        photo_id = photo[4]
        description = photo[5]
        try:
            await call.message.answer_video(photo_id, caption=description)
        except:
            await call.message.answer_photo(photo_id, caption=description)
    await call.answer(cache_time=60)
    
@dp.callback_query_handler(text="Tez uy olish")
async def cancel_buying(call: CallbackQuery):
    info =  await db.get_categories(menu_language = "UZB", category_name= "Kochmas mulk", service_name = "Tez uy olish")
    for photo in info:
        photo_id = photo[4]
        description = photo[5]
        try:
            await call.message.answer_video(photo_id, caption=description)
        except:
            await call.message.answer_photo(photo_id, caption=description)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text="Ishonchli boshqaruv")
async def cancel_buying(call: CallbackQuery):
    info =  await db.get_categories(menu_language = "UZB", category_name= "Kochmas mulk", service_name = "Ishonchli boshqaruv")
    for photo in info:
        photo_id = photo[4]
        description = photo[5]
        try:
            await call.message.answer_video(photo_id, caption=description)
        except:
            await call.message.answer_photo(photo_id, caption=description)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text="Savdo organizatsiyasi")
async def cancel_buying(call: CallbackQuery):
    info =  await db.get_categories(menu_language = "UZB", category_name= "Kochmas mulk", service_name = "Savdo organizatsiyasi")
    for photo in info:
        photo_id = photo[4]
        description = photo[5]
        try:
            await call.message.answer_video(photo_id, caption=description)
        except:
            await call.message.answer_photo(photo_id, caption=description)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text="Meros olish hujjatlari")
async def cancel_buying(call: CallbackQuery):
    info =  await db.get_categories(menu_language = "UZB", category_name= "Kochmas mulk", service_name = "Meros olish hujjatlari")
    for photo in info:
        photo_id = photo[4]
        description = photo[5]
        try:
            await call.message.answer_video(photo_id, caption=description)
        except:
            await call.message.answer_photo(photo_id, caption=description)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text="Turar hujjatlarni tayyorlash")
async def cancel_buying(call: CallbackQuery):
    info =  await db.get_categories(menu_language = "UZB", category_name= "Kochmas mulk", service_name = "Turar hujjatlarni tayyorlash")
    for photo in info:
        photo_id = photo[4]
        description = photo[5]
        try:
            await call.message.answer_video(photo_id, caption=description)
        except:
            await call.message.answer_photo(photo_id, caption=description)
    await call.answer(cache_time=60)

    #===================ko'chmas mulk ru====================

@dp.callback_query_handler(text="Продать")
async def cancel_buying(call: CallbackQuery):
    #users = await db.select_all_users()
    info =  await db.get_categories(menu_language = "RU", category_name= "Недвижимость", service_name = "Продать")
    for photo in info:
        photo_id = photo[4]
        description = photo[5]
        try:
            await call.message.answer_video(photo_id, caption=description)
        except:
            await call.message.answer_photo(photo_id, caption=description)
        # await call.message.video.file_id
    await call.answer(cache_time=60)
    
@dp.callback_query_handler(text="Купить")
async def cancel_buying(call: CallbackQuery):
    info =  await db.get_categories(menu_language = "RU", category_name= "Недвижимость", service_name = "Купить")
    for photo in info:
        photo_id = photo[4]
        description = photo[5]
        try:
            await call.message.answer_video(photo_id, caption=description)
        except:
            await call.message.answer_photo(photo_id, caption=description)
    await call.answer(cache_time=60)
    
@dp.callback_query_handler(text="Снять")
async def cancel_buying(call: CallbackQuery):
    info =  await db.get_categories(menu_language = "RU", category_name= "Недвижимость", service_name = "Снять")
    for photo in info:
        photo_id = photo[4]
        description = photo[5]
        try:
            await call.message.answer_video(photo_id, caption=description)
        except:
            await call.message.answer_photo(photo_id, caption=description)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text="Сдать")
async def cancel_buying(call: CallbackQuery):
    info =  await db.get_categories(menu_language = "RU", category_name= "Недвижимость", service_name = "Сдать")
    for photo in info:
        photo_id = photo[4]
        description = photo[5]
        try:
            await call.message.answer_video(photo_id, caption=description)
        except:
            await call.message.answer_photo(photo_id, caption=description)
    await call.answer(cache_time=60)
    
@dp.callback_query_handler(text="Быстрый")
async def cancel_buying(call: CallbackQuery):
    info =  await db.get_categories(menu_language = "RU", category_name= "Недвижимость", service_name = "Быстрый")
    for photo in info:
        photo_id = photo[4]
        description = photo[5]
        try:
            await call.message.answer_video(photo_id, caption=description)
        except:
            await call.message.answer_photo(photo_id, caption=description)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text="Доверительное")
async def cancel_buying(call: CallbackQuery):
    info =  await db.get_categories(menu_language = "RU", category_name= "Недвижимость", service_name = "Доверительное")
    for photo in info:
        photo_id = photo[4]
        description = photo[5]
        try:
            await call.message.answer_video(photo_id, caption=description)
        except:
            await call.message.answer_photo(photo_id, caption=description)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text="Организатор")
async def cancel_buying(call: CallbackQuery):
    info =  await db.get_categories(menu_language = "RU", category_name= "Недвижимость", service_name = "Организатор")
    for photo in info:
        photo_id = photo[4]
        description = photo[5]
        try:
            await call.message.answer_video(photo_id, caption=description)
        except:
            await call.message.answer_photo(photo_id, caption=description)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text="Meros")
async def cancel_buying(call: CallbackQuery):
    info =  await db.get_categories(menu_language = "RU", category_name= "Недвижимость", service_name = "Meros")
    for photo in info:
        photo_id = photo[4]
        description = photo[5]
        try:
            await call.message.answer_video(photo_id, caption=description)
        except:
            await call.message.answer_photo(photo_id, caption=description)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text="tayyorlash")
async def cancel_buying(call: CallbackQuery):
    info =  await db.get_categories(menu_language = "RU", category_name= "Недвижимость", service_name = "tayyorlash")
    for photo in info:
        photo_id = photo[4]
        description = photo[5]
        try:
            await call.message.answer_video(photo_id, caption=description)
        except:
            await call.message.answer_photo(photo_id, caption=description)
        #await call.message.answer_photo(photo_id, caption=description)
    await call.answer(cache_time=60)
        