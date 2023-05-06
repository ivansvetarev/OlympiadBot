from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def get_add_olympiad_kb(id):
    add_olympiad_kb = InlineKeyboardMarkup()
    add_olympiad = InlineKeyboardButton("Добавить олимпиаду", callback_data=f'a{id}')

    add_olympiad_kb.add(add_olympiad)

    return add_olympiad_kb