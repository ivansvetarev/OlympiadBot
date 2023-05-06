from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

social_sci_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

b1 = KeyboardButton("История")
b2 = KeyboardButton("Обществознание")
b3 = KeyboardButton("Предпринимательство")
b4 = KeyboardButton("Право")
b5 = KeyboardButton("Экономика")
b6 = KeyboardButton("ОБЖ")

social_sci_kb.row(b1, b2).row(b3, b4).row(b5, b6)