from datetime import datetime
import asyncio
from datetime import timedelta
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ChatActions
from func import *
from config import dp, bot
storage = MemoryStorage()

admin = [1348491834]


class UserState(StatesGroup):
    DATE_INT = State()
    PROCESS = State()


@dp.message_handler(commands=['start'])
async def get_menu(message: types.Message):
    await create_table()
    await create_table_users()
    await write_to_db_user(message.from_user.id, message.from_user.username)

    username = message.from_user.first_name
    if username:

        await bot.send_chat_action(message.chat.id, "typing")
        await message.answer(f'Добро пожаловать {username}\n\n'
                             'это KAMAZ детка\n\n'
                             'Во имя коленвала', reply_markup=kb_main)

    else:
        username = message.from_user.username
        await bot.send_chat_action(message.chat.id, "typing")
        await message.answer(f'Добро пожаловать {username}\n\n'
                             'это KAMAZ детка', reply_markup=kb_main)


@dp.message_handler(commands=['read'])
async def all_users(message: types.Message):
    if message.from_user.id in admin:
        text = message.get_args()
        await send_to_all_users(text)
    else:
        await message.reply("У вас нет прав для выполнения этой команды.")


@dp.message_handler(text="Просмотр з/н")
async def read_z_n(message: types.Message):
    await write_to_db_user(message.from_user.id, message.from_user.username)
    await message.answer('за какой период смотрим?', reply_markup=kb_read_zn)
    await UserState.DATE_INT.set()


@dp.message_handler(text="отмена", state='*')
async def read_z_n(message: types.Message, state: FSMContext):
    await message.answer('отменено', reply_markup=kb_main)
    await state.finish()


@dp.message_handler(text="За сегодня", state=UserState.DATE_INT)
async def read_z_n(message: types.Message, state: FSMContext):
    date = datetime.now().strftime('%d-%m-%Y')
    order = await read_to_db_today(date)
    # await message.answer(f'дата {date}')
    if order:
        await message.answer('Все че было за сегодня')
        for item in order:
            mess = f"{item[1]}\n{item[2]}"
            await message.answer(f'з/н {mess}', reply_markup=kb_main)
    else:
        await message.answer('нихера сегодня не перемещали', reply_markup=kb_main)
    await state.finish()


@dp.message_handler(text="За вчера", state=UserState.DATE_INT)
async def read_z_n(message: types.Message, state: FSMContext):
    date_now = datetime.now()
    date = date_now - timedelta(days=1)
    date = date.strftime('%d-%m-%Y')
    order = await read_to_db_today(date)
    # await message.answer(f'дата {date}')
    if order:
        await message.answer('Все че было за вчера')
        for item in order:
            mess = f"{item[1]}\n{item[2]}"
            await message.answer(f'з/н {mess}', reply_markup=kb_main)
            await state.finish()
    else:
        await message.answer('нихера вчера не перемещали)', reply_markup=kb_main)
        await state.finish()


@dp.message_handler(text="За выбранную дату", state=UserState.DATE_INT)
async def read_z_n(message: types.Message):
    await message.answer("Введи дату в формате\n"
                         "ДД-ММ-ГГГГ\n"
                         "тире обязательно", reply_markup=kb_cansel)
    await UserState.PROCESS.set()


@dp.message_handler(state=UserState.PROCESS)
async def process_date(message: types.Message, state: FSMContext):
    date = message.text
    order = await read_to_db_today(date)
    # await message.answer(f'дата {date}')
    if order:
        await message.answer(f'Все че было за {date}')
        for item in order:
            mess = f"{item[1]}\n{item[2]}"
            await message.answer(f'з/н {mess}', reply_markup=kb_main)
            await state.finish()
    else:
        await message.answer('не верно введена дата,\n'
                             'либо нет перемещений за это число', reply_markup=kb_cansel)


@dp.message_handler(content_types=types.ContentType.VOICE)
async def process_message(message: types.Message):
    """Принимает все голосовые сообщения и отвечает эхо."""
    voice_path = await save_voice_as_mp3(bot, message.voice)
    transcripted_voice_text = await audio_to_text(voice_path)
    # print(transcripted_voice_text)
    if transcripted_voice_text:
        for file in os.scandir('voice_files'):
            os.remove(file.path)

    else:
        await bot.send_chat_action(message.chat.id, ChatActions.TYPING)
        await asyncio.sleep(3)
        await message.reply('не распознали твой сраный голос\n'
                            'попробуй еще раз...')
    if transcripted_voice_text.lower().startswith("добавь"):
        try:
            user_input = ' '.join(transcripted_voice_text.split()[1:])
            input1 = user_input_format(user_input)
            user_input1 = input1.split()
            user_imput2 = user_input1[0].replace(",", "").replace(" ", "").replace(".", "").replace("-", "")
            user_comand = ' '.join([user_imput2] + user_input1[1:])
            order_outfit = ''.join(user_comand[:4])
            product2 = ''.join(user_comand[5:])
            join_date = datetime.now().strftime('%d-%m-%Y')
            # print(order_outfit,product2,join_date)
            await write_to_db(order_outfit, product2, join_date)
            await bot.send_chat_action(message.chat.id, ChatActions.TYPING)
            await asyncio.sleep(3)
            await message.answer(f'занес в базу:\n'
                                 f'з/н: {order_outfit}\n'
                                 f'товар: {product2}', reply_markup=kb_main)
        except:
            await bot.send_chat_action(message.chat.id, ChatActions.TYPING)
            await asyncio.sleep(2)
            await message.answer('Что ты там промямлил?\n'
                                 'Нормально сформулируй запрос\n'
                                 'Пример: ДОБАВЬ 1234 фильтр ГУР', reply_markup=kb_main)

    elif transcripted_voice_text.lower().startswith("покажи"):
        try:

            user_input = ' '.join(transcripted_voice_text.split()[1:])
            user_input = user_input_format(user_input)
            user_input = user_input.split()
            user_imput = user_input[0].replace(",", "").replace(" ", "").replace(".", "").replace("-", "")
            product = await read_to_db(str(user_imput))
            if product:
                await bot.send_chat_action(message.chat.id, ChatActions.TYPING)
                await asyncio.sleep(3)
                await message.answer(f'в з/н {str(user_imput)}\n'
                                     f'добавлен товар: {product}', reply_markup=kb_main)
            else:
                await bot.send_chat_action(message.chat.id, ChatActions.TYPING)
                await asyncio.sleep(2)
                await message.answer(f'в з/н {str(user_imput)} ниче не перемещали', reply_markup=kb_main)
        except:
            await bot.send_chat_action(message.chat.id, ChatActions.TYPING)
            await asyncio.sleep(2)
            await message.answer('Что ты там промямлил?\n'
                                 'Нормально сформулируй запрос\n'
                                 'Пример: ДОБАВЬ 1234 фильтр ГУР', reply_markup=kb_main)

    else:
        await bot.send_chat_action(message.chat.id, ChatActions.TYPING)
        await asyncio.sleep(2)
        await message.answer('Что ты там промямлил?\n'
                             'Нормально сформулируй запрос\n'
                             'Пример: ДОБАВЬ 1234 фильтр ГУР', reply_markup=kb_main)


@dp.message_handler(content_types=types.ContentType.TEXT)
async def process_message(message: types.Message):
    await write_to_db_user(message.from_user.id, message.from_user.username)
    if message.text.lower()[0:6] == 'покажи':
        product = await read_to_db(str(message.text[7:]))
        if product:
            await bot.send_chat_action(message.chat.id, ChatActions.TYPING)
            await asyncio.sleep(3)
            await message.answer(f'в з/н {str(message.text[7:])}\n'
                                 f'добавлен товар: {product}', reply_markup=kb_main)
        else:
            await bot.send_chat_action(message.chat.id, ChatActions.TYPING)
            await asyncio.sleep(3)
            await message.answer('в такой з/н ниче не перемещали', reply_markup=kb_main)

    else:
        await message.answer('Корявками своими не тыкай.\n'
                             'я принимаю голосовые сообщения\n'
                             'Пример: ДОБАВЬ 1234 фильтр ГУР\n'
                             'Пример: ПОКАЖИ 1234', reply_markup=kb_main)
