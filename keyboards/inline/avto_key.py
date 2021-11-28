from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

avto_menu_uz = InlineKeyboardMarkup(
    inline_keyboard=[
        [
           InlineKeyboardButton(text = "Polirovka!", callback_data='service'),
           InlineKeyboardButton(text = "Keramika", callback_data='service1'),
            
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

avto_menu_ru = InlineKeyboardMarkup(
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