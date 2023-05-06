from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

b1 = KeyboardButton("Русский язык")
b2 = KeyboardButton("Литература")
b3 = KeyboardButton("Английский язык")
b4 = KeyboardButton("Китайский язык")
b5 = KeyboardButton("Испанский язык")
b6 = KeyboardButton("Немецкий язык")
b7 = KeyboardButton("Французский язык")
b8 = KeyboardButton("Латинский язык")
b9 = KeyboardButton("Японский язык")

humanitarian_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

humanitarian_kb.add(b1, b2, b3, b4, b5, b6 ,b7, b8, b9)