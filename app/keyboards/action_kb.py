from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

b1 = KeyboardButton("Мои олимпиады")
b2 = KeyboardButton("Поиск олимпиад")

action_kb = ReplyKeyboardMarkup(resize_keyboard=True)

action_kb.row(b1, b2)