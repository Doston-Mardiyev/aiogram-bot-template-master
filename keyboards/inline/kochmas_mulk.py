from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

uy_menu_uz = InlineKeyboardMarkup(
    inline_keyboard=[
        [
           InlineKeyboardButton(text = "Sotish", callback_data='Sotish'),
           InlineKeyboardButton(text = "Olish", callback_data='Olish'),
            
        ],
        [
           InlineKeyboardButton(text = "Arendaga berish", callback_data='Arendaga berish'),
           InlineKeyboardButton(text = "Arendaga olish", callback_data='Arendaga olish'),
            
        ],
        [
           InlineKeyboardButton(text = "Tez uy olish", callback_data='Tez uy olish'),
           InlineKeyboardButton(text = "Ishonchli boshqaruv", callback_data='Ishonchli boshqaruv'),
            
        ],
         [
           InlineKeyboardButton(text = "Auksion tashkilotchisi", callback_data='Auksion tashkilotchisi'),
           InlineKeyboardButton(text = "Meros hujjatlarni tayyorlash", callback_data='Meros hujjatlarni tayyorlash'),
            
        ],

        [
           InlineKeyboardButton(text = "Turar hujjatlarni tayyorlash", callback_data='Turar hujjatlarni tayyorlash'),
            
        ],
    ],
   
)

uy_menu_ru = InlineKeyboardMarkup(
    inline_keyboard=[
        [
           InlineKeyboardButton(text = "Продать", callback_data='Продать'),
           InlineKeyboardButton(text = "Купить", callback_data='Купить'),
            
        ],
        [
           InlineKeyboardButton(text = "Снять", callback_data='Снять'),
           InlineKeyboardButton(text = "Сдать", callback_data='Сдать'),
            
        ],
        [
           InlineKeyboardButton(text = "Быстрый выкуп недвижимости", callback_data='Быстрый'),
           InlineKeyboardButton(text = "Доверительное управление", callback_data='Доверительное'),
            
        ],
         [
           InlineKeyboardButton(text = "Организатор торгов", callback_data='Организатор'),
           InlineKeyboardButton(text = "Meros olish hujjatlari", callback_data='Meros'),
            
        ],

        [
           InlineKeyboardButton(text = "Turar joydan noturar joygacha yoki aksincha xujjatlarni tayyorlash", callback_data='tayyorlash'),
            
        ],
    ],
   
)