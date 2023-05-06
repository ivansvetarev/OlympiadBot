from aiogram import types, Dispatcher
from aiogram.types import ReplyKeyboardMarkup
from aiogram.dispatcher.filters import Text
import sys
sys.path.append("..")
from database import *
from keyboards import action_kb, categories_kb, humanitarian_kb, natural_sci_kb, technical_kb, social_sci_kb, get_add_olympiad_kb, get_remove_olympiad_kb
from create_bot import bot



#@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await bot.send_message(message.from_user.id, """Вас приветсивует OlympiadBot!\nЯ могу предоставить информацию о школьных перечневых олимпиадах""", reply_markup=action_kb)

async def get_my_olympiads(message: types.Message):
    user_id = message.from_user.id
    messages = get_my_olympiads_message(user_id)
    c = 0
    if len(messages) == 0:
        await bot.send_message(user_id, "У Вас пока что нет олимпиад")
    else:
        ids = get_olympiad_ids(user_id)
        print(ids)
        for mess in messages:
            await bot.send_message(user_id, mess, reply_markup=get_remove_olympiad_kb(ids[c]))
            c += 1
    #await bot.send_message(message.from_user.id, """""", reply_markup=action_kb)

#@dp.message_handler(commands=['Поиск олимпиад'])
async def choose_category(message: types.Message):
    await bot.send_message(message.from_user.id, "Выберите направление", reply_markup=categories_kb)

#@dp.message_handler(commands=['Технические',
#'Естественно-научные','Общественно-научные', 'Гуманитарные', 'Искусство'])
async def choose_subject(message: types.Message):
    keyboard = ReplyKeyboardMarkup()
    match message.text:
        case 'Гуманитарное':
            keyboard = humanitarian_kb
        case 'Естественно-научное':
            keyboard = natural_sci_kb
        case 'Техническое':
            keyboard = technical_kb
        case 'Общественно-научное':
            keyboard = social_sci_kb
    await bot.send_message(message.from_user.id, "Выберите предмет", reply_markup=keyboard)

class_ids = ()
subject_ids = ()
async def get_subject_classes(message: types.Message):
    #if message.text in [ "Биология", "География", "ИЗО", "Информатика", "Искусство","История","Лингвистика","Литература","Математика","ОБЖ","Обществознание","Предпринимательство","Право","Психология","Русский язык","Технология","Физика","Физкультура","Химия","Черчение","Экология","Экономика", "Английский язык", "Китайский язык", "Немецкий язык", "Русский язык","Литература", "Испанский язык", "Французский язык", "Японский язык", "Латинский язык"]:
    global class_ids
    global subject_ids
    if any(char.isdigit() for char in message.text):
        class_ids = select_by_class(message.text)
        ids = class_ids&subject_ids
        class_ids = ()
        subject_ids = ()
        await post_info(message.from_user.id, ids)
    else:
        subject_ids = select_by_subject(message.text)
        await bot.send_message(message.from_user.id, "Введите класс")

async def post_info(user_id, ids):
    c = 0   
    for id in ids:
        message = get_olympid_by_id(id)
        if message != "":
            await bot.send_message(user_id, message, reply_markup=get_add_olympiad_kb(id))
            c += 1
    if c == 0:
        await bot.send_message(user_id, "К сожалению, олимпиады по вашему запросу не найдены", reply_markup=action_kb)
    else: 
        await bot.send_message(user_id, "Благодарим Вас за то, что воспользовались OlympiadBot", reply_markup=action_kb)

async def process_add_olympiad(callback_query: types.CallbackQuery):
    add_olympiad(callback_query.from_user.id, callback_query.data[1::])
    await callback_query.answer("Олимпиада добавлена")

async def process_remove_olympiad(callback_query: types.CallbackQuery):
    remove_olympiad(callback_query.from_user.id, callback_query.data[1::])
    await callback_query.answer("Олимпиада удалена")


async def glory_to_ukr(message: types.Message):
    await bot.send_message(message.from_user.id, "Героям слава!\nСмерть врагам!")

def register_handlers_info(dp: Dispatcher):
    dp.register_message_handler(start_command, commands=['start'])
    dp.register_message_handler(choose_category, Text('Поиск олимпиад'))
    dp.register_message_handler(choose_subject, Text(['Техническое',
'Естественно-научное','Общественно-научное', 'Гуманитарное']))
    dp.register_message_handler(get_subject_classes, Text(["1","2","3","4","5","6","7","8","9","10","11", "Биология", "География", "ИЗО", "Информатика", "Искусство","История","Лингвистика","Литература","Математика","ОБЖ","Обществознание","Предпринимательство","Право","Психология","Русский язык","Технология","Физика","Физкультура","Химия","Черчение","Экология","Экономика", "Английский язык", "Китайский язык", "Немецкий язык", "Русский язык","Литература", "Испанский язык", "Французский язык", "Японский язык", "Латинский язык"]))
    dp.register_callback_query_handler(process_add_olympiad, Text(startswith="a"))
    dp.register_callback_query_handler(process_remove_olympiad, Text(startswith="r"))
    dp.register_message_handler(get_my_olympiads, Text("Мои олимпиады"))
    dp.register_message_handler(glory_to_ukr, Text("Слава Украине"))
