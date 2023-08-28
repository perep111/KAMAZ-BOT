from aiogram import executor
import logging
from config import dp
import asyncio
from func import set_default_commands, create_table, create_table_users
import handler_to
import handler_zn
logging.basicConfig(level=logging.INFO)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.create_task(create_table())
    loop.create_task(create_table_users())
    executor.start_polling(dp, on_startup=set_default_commands, skip_updates=True)
