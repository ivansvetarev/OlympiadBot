from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def get_remove_olympiad_kb(id):
    remove_olympiad_kb = InlineKeyboardMarkup()
    remove_olympiad = InlineKeyboardButton("Удалить олимпиаду", callback_data=f'r{id}')

    remove_olympiad_kb.add(remove_olympiad)

    return remove_olympiad_kb