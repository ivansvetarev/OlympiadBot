from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

b1 = KeyboardButton("Техническое")
b2 = KeyboardButton("Естественно-научное")
b3 = KeyboardButton("Общественно-научное")
b4 = KeyboardButton("Гуманитарное")

categories_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
categories_kb.row(b1, b2).row(b4, b3)