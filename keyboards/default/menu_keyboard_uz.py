from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu_uz = ReplyKeyboardMarkup(
    keyboard=[
        [
           KeyboardButton(text = "🏠 Ko'chmas mulk"),
           KeyboardButton(text = "🚘 Avto servis"),
            
        ],
        [
           KeyboardButton(text = "ℹ️ Biz haqimizda"),
           KeyboardButton(text = "📞 Kontakt"),
            
        ],
        [
           KeyboardButton(text = "📞 Biz bilan bog'lanish"), 
        ],
    ],
    resize_keyboard=True
)

menu_ru = ReplyKeyboardMarkup(
    keyboard=[
        [
           KeyboardButton(text = "🏠 Недвижимость"),
           KeyboardButton(text = "🚘 Авто сервис"),
            
        ],
        [
           KeyboardButton(text = "ℹ️ О нас"),
           KeyboardButton(text = "📞 Контакт"),
            
        ],
        [
           KeyboardButton(text = "📞 Связать"), 
        ],
    ],
    resize_keyboard=True
)