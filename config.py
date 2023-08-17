import logging
from aiogram import Dispatcher, Bot, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import openai
storage = MemoryStorage()

BOT_TOKEN = '6146009037:AAGqU1swh9utMUrOaTVvLlfWb3_1d6Ypb84'
bot = Bot(token=BOT_TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot, storage=storage)
logging.basicConfig(level=logging.INFO)
openai.api_key = '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'