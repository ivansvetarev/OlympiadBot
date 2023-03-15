from create_bot import bot, dp
from aiogram import types
from aiogram import executor
from fetch_db_data import *



"""
b.             8     ,o888888o.    8 8888        8    d888888o.   8 8888        8 
888o.          8    8888     `88.  8 8888        8  .`8888:' `88. 8 8888        8 
Y88888o.       8 ,8 8888       `8. 8 8888        8  8.`8888.   Y8 8 8888        8 
.`Y888888o.    8 88 8888           8 8888        8  `8.`8888.     8 8888        8 
8o. `Y888888o. 8 88 8888           8 8888        8   `8.`8888.    8 8888        8 
8`Y8o. `Y88888o8 88 8888           8 8888        8    `8.`8888.   8 8888        8 
8   `Y8o. `Y8888 88 8888           8 8888888888888     `8.`8888.  8 8888888888888 
8      `Y8o. `Y8 `8 8888       .8' 8 8888        8 8b   `8.`8888. 8 8888        8 
8         `Y8o.`    8888     ,88'  8 8888        8 `8b.  ;8.`8888 8 8888        8 
8            `Yo     `8888888P'    8 8888        8  `Y8888P ,88P' 8 8888        8                                                                                                                           
"""

@dp.message_handler(commands=['com'])
async def func(message: types.Message):
    await message.reply("d")

































@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Вас приветствует OlympidBot\n")


@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply("Напиши мне что-нибудь, и я отпрпавлю этот текст тебе в ответ!")

# @dp.message_handler(commands=['olympiads'])
# async def list_of_olympiads(message: types.Message):
#     rep = ""
#     for olympiad in range(15):
#        rep = olympiads[olympiad].subject_name +  "\n" + olympiads[olympiad].subject_name + "\n" + olympiads[olympiad].classes + "\n" + olympiads[olympiad].level
#     await bot.send_message(message.from_user.id, 
#             olympiad.name 
#                 )

@dp.message_handler()
async def test(msg: types.Message):
    print(msg)
    await bot.send_message(msg.from_user.id, select_by_attr(msg.text, "История"))

# @dp.message_handler()
# async def echo_message(msg: types.Message):
#     await bot.send_message(msg.from_user.id, msg.text)


if __name__ == '__main__':
    print("started")
    executor.start_polling(dp, skip_updates=True)
