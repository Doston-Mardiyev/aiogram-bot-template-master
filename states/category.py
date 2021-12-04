from aiogram.dispatcher.filters.state import StatesGroup, State

class SaveData(StatesGroup):
      Language = State()
      Catigory = State()
      Service = State()
      Photo = State()
      Description = State()
      
