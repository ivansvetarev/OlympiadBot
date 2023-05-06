from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


natural_sci_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

b1 = KeyboardButton("Биология")
b2 = KeyboardButton("Химия")
b3 = KeyboardButton("Физика")
b4 = KeyboardButton("География")
b5 = KeyboardButton("Астрономия")
b6 = KeyboardButton("Экология")

natural_sci_kb.row(b1, b2).row(b3, b4).row(b5, b6)