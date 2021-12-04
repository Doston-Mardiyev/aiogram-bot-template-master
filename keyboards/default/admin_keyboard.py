from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

language = ReplyKeyboardMarkup(
    keyboard=[
        [
           KeyboardButton(text = "UZB"),
           KeyboardButton(text = "RU"),
            
        ],
    ],
    resize_keyboard=True
)



menu_admin_uz = ReplyKeyboardMarkup(
    keyboard=[
        [
           KeyboardButton(text = "Kochmas mulk"),
           KeyboardButton(text = "Avto servis"),
            
        ],
    ],
    resize_keyboard=True
)

menu_admin_ru = ReplyKeyboardMarkup(
    keyboard=[
        [
           KeyboardButton(text = "Недвижимость"),
           KeyboardButton(text = "Авто сервис"),
            
        ]
        
    ],
    resize_keyboard=True
)

avto_admin_uz = ReplyKeyboardMarkup(
    keyboard=[
        [
           KeyboardButton(text = "Polirovka"),
           KeyboardButton(text = "Keramika"),
            
        ],
        [
           KeyboardButton(text = "Ximchistka"),
           KeyboardButton(text = "Shumoizolyatsiya"),
            
        ],
        [
           KeyboardButton(text = "Tonirovka"),
           KeyboardButton(text = "Avtosignallizatsiya"),
            
        ],
         [
           KeyboardButton(text = "Laminatsiya"),
           KeyboardButton(text = "Chexol"),
            
        ],
    ],
        resize_keyboard=True
   
)



avto_admin_ru = ReplyKeyboardMarkup(
    keyboard=[
        [
           KeyboardButton(text = "Полировка"),
           KeyboardButton(text = "Керамика"),
            
        ],
        [
           KeyboardButton(text = "Химчистка"),
           KeyboardButton(text = "Шумоизоляция"),
            
        ],
        [
           KeyboardButton(text = "Тонировка"),
           KeyboardButton(text = "Автосигнализация"),
            
        ],
         [
           KeyboardButton(text = "Ламинирование"),
           KeyboardButton(text = "чехол"),
            
        ],
    ],
    resize_keyboard=True
   
)

uy_admin_uz = ReplyKeyboardMarkup(
        keyboard=[
        [
           KeyboardButton(text = "Sotish"),
           KeyboardButton(text = "Olish"),
            
        ],
        [
           KeyboardButton(text = "Arendaga berish"),
           KeyboardButton(text = "Arendaga olish"),
            
        ],
        [
           KeyboardButton(text = "Tez uy olish"),
           KeyboardButton(text = "Ishonchli boshqaruv"),
            
        ],
         [
           KeyboardButton(text = "Savdo organizatsiyasi"),
           KeyboardButton(text = "Meros olish hujjatlari"),
            
        ],

        [
           KeyboardButton(text = "Turar hujjatlarni tayyorlash"),
            
        ],
    ],
    resize_keyboard=True

)

uy_admin_ru = ReplyKeyboardMarkup(
        keyboard=[
        [
           KeyboardButton(text = "Продать"),
           KeyboardButton(text = "Купить"),
            
        ],
        [
           KeyboardButton(text = "Снять"),
           KeyboardButton(text = "Сдать"),
            
        ],
        [
           KeyboardButton(text = "Быстрый выкуп недвижимости"),
           KeyboardButton(text = "Доверительное Управление!"),
            
        ],
         [
           KeyboardButton(text = "Организатор торгов!"),
           KeyboardButton(text = "Подготовка документов для получения наследство!"),
            
        ],

        [
           KeyboardButton(text = "Подготовка документов с жилого на нежилое или наоборот!"),
            
        ],
    ],
    resize_keyboard=True

)