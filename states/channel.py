from aiogram.dispatcher.filters.state import StatesGroup, State

class NewPost(StatesGroup):
      PhoneNumber = State()
      NewMessage = State()
      PhoneNumber_ru = State()
      NewMessage_ru = State()
      