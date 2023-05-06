from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

b1 = KeyboardButton("Информатика")
b2 = KeyboardButton("Математика")
b3 = KeyboardButton("Технология")
b4 = KeyboardButton("Черчение")
b5 = KeyboardButton("Робототехника")
b6 = KeyboardButton("Физика")

technical_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

technical_kb.row(b1, b2).row(b3, b4).row(b5, b6)