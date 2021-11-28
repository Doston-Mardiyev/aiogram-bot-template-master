from aiogram.dispatcher.filters.state import StatesGroup, State

class NewPost(StatesGroup):
      PhoneNumber = State()
      NewMessage = State()
      