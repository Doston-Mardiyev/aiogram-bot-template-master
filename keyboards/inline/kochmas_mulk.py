from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

uy_menu_uz = InlineKeyboardMarkup(
    inline_keyboard=[
        [
           InlineKeyboardButton(text = "Sotish", callback_data='service'),
           InlineKeyboardButton(text = "Olish", callback_data='service1'),
            
        ],
        [
           InlineKeyboardButton(text = "Arendaga berish", callback_data='service2'),
           InlineKeyboardButton(text = "Arendaga olish", callback_data='service3'),
            
        ],
        [
           InlineKeyboardButton(text = "Tez uy olish", callback_data='service4'),
           InlineKeyboardButton(text = "Ishonchli boshqaruv", callback_data='service5'),
            
        ],
         [
           InlineKeyboardButton(text = "Savdo organizatsiyasi", callback_data='service4'),
           InlineKeyboardButton(text = "Meros olish hujjatlari", callback_data='service5'),
            
        ],

        [
           InlineKeyboardButton(text = "Turar joydan noturar joygacha yoki aksincha xujjatlarni tayyorlash", callback_data='service6'),
            
        ],
    ],
   
)

uy_menu_ru = InlineKeyboardMarkup(
    inline_keyboard=[
        [
           InlineKeyboardButton(text = "Polirovka_ru", callback_data='service'),
           InlineKeyboardButton(text = "Keramika_ru", callback_data='service1'),
            
        ],
        [
           InlineKeyboardButton(text = "Ximchistka!", callback_data='service2'),
           InlineKeyboardButton(text = "Shumoizolyatsiya!", callback_data='service3'),
            
        ],
        [
           InlineKeyboardButton(text = "Tonirovka!", callback_data='service4'),
           InlineKeyboardButton(text = "Avtosignallizatsiya!", callback_data='service5'),
            
        ],
         [
           InlineKeyboardButton(text = "Laminatsiya!", callback_data='service4'),
           InlineKeyboardButton(text = "Chexol!", callback_data='service5'),
            
        ],
    ],
   
)