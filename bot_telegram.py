from create_bot import bot, dp
from aiogram import types
from aiogram.utils import executor
from parsing import olympiads


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Вас приветствует OlympidBot\n")


@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply("Напиши мне что-нибудь, и я отпрпавлю этот текст тебе в ответ!")

@dp.message_handler(commands=['olympiads'])
async def list_of_olympiads(message: types.Message):
    
    rep = ""

    for olympiad in range(15):
       rep = olympiads[olympiad].subject_name +  "\n" + olympiads[olympiad].subject_name + "\n" + olympiads[olympiad].classes + "\n" + olympiads[olympiad].level

    await bot.send_message(message.from_user.id, 
            olympiad.name 
                )

# @dp.message_handler()
# async def echo_message(msg: types.Message):
#     await bot.send_message(msg.from_user.id, msg.text)


if __name__ == '__main__':
    print("started")
    executor.start_polling(dp, skip_updates=True)
