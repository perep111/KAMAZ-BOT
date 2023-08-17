from aiogram import executor
import logging
from config import dp
from func import set_default_commands
import handler_to
import handler_zn
logging.basicConfig(level=logging.INFO)


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=set_default_commands, skip_updates=True)
