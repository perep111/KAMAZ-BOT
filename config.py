import logging
from aiogram import Dispatcher, Bot, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import openai
import os
from dotenv import load_dotenv

load_dotenv()
storage = MemoryStorage()

BOT_TOKEN = os.getenv('BOT_TOKEN')
bot = Bot(token=BOT_TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot, storage=storage)
logging.basicConfig(level=logging.INFO)
openai.api_key = os.getenv('OPENAI_API_KEY')
