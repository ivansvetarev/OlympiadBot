from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()

bot = Bot(token = '5814407465:AAGaH2bVwtkrvh9MvXNSQIskIcgQS6nsmNc')

dp = Dispatcher(bot, storage = storage)