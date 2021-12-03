from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

avto_menu_uz = InlineKeyboardMarkup(
    inline_keyboard=[
        [
           InlineKeyboardButton(text = "💫Polirovka", callback_data='Polirovka'),
           InlineKeyboardButton(text = "💎Keramika", callback_data='Keramika'),
            
        ],
        [
           InlineKeyboardButton(text = "🧤Ximchistka", callback_data='Ximchistka'),
           InlineKeyboardButton(text = "🗣Shumoizolyatsiya", callback_data='Shumoizolyatsiya'),
            
        ],
        [
           InlineKeyboardButton(text = "🕶Tonirovka", callback_data='Tonirovka'),
           InlineKeyboardButton(text = "🔊Avtosignallizatsiya", callback_data='Avtosignallizatsiya'),
            
        ],
         [
           InlineKeyboardButton(text = "💈Laminatsiya", callback_data='Laminatsiya'),
           InlineKeyboardButton(text = "🏮Chexol", callback_data='Chexol'),
            
        ],
    ],
   
)

avto_menu_ru = InlineKeyboardMarkup(
    inline_keyboard=[
        [
           InlineKeyboardButton(text = "💫Полировка", callback_data='Полировка'),
           InlineKeyboardButton(text = "💎Керамика", callback_data='Керамика'),
            
        ],
        [
           InlineKeyboardButton(text = "🧤Химчистка", callback_data='Химчистка'),
           InlineKeyboardButton(text = "🗣Шумоизоляция", callback_data='Шумоизоляция'),
            
        ],
        [
           InlineKeyboardButton(text = "🕶Тонировка", callback_data='Тонировка'),
           InlineKeyboardButton(text = "🔊Автосигнализация", callback_data='Автосигнализация'),
            
        ],
         [
           InlineKeyboardButton(text = "💈Ламинирование", callback_data='Ламинирование'),
           InlineKeyboardButton(text = "🏮чехол", callback_data='чехол'),
            
        ],
    ],
   
)