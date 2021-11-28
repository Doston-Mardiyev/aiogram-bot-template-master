from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from states.channel import NewPost 




contact = ReplyKeyboardMarkup(
    keyboard=[
        [
           KeyboardButton(text = "Raqam yuborish", request_contact=True),  
           #NewPost.PhoneNumber.set ()  
        ],
   
        [
           KeyboardButton(text = "Ortga qaytish"),   
        ],
    ],
    resize_keyboard=True
    
)

contact_ru = ReplyKeyboardMarkup(
    keyboard=[
        [
           KeyboardButton(text = "Отправить номер", request_contact=True),    
        ],
    
        [
           KeyboardButton(text = "Вернитесь назад"),   
        ],
    ],
    resize_keyboard=True
)