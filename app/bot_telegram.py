from create_bot import bot, dp
from aiogram import executor
from handlers import olympiad_info_handlers

olympiad_info_handlers.register_handlers_info(dp)

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

async def on_startup(_):
    print("Bot is online")

if __name__ == '__main__':
    print("Bot is online")
    executor.start_polling(dp, skip_updates=True)
