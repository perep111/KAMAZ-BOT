import re
from pydub import AudioSegment
import aiosqlite
import io
from config import *
from aiogram import Bot, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, Voice


kb_read_zn = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
button_1 = KeyboardButton(text='За сегодня')
button_2 = KeyboardButton(text='За вчера')
button_3 = KeyboardButton(text='За выбранную дату')
button_cansel = KeyboardButton(text='отмена')
kb_read_zn.add(button_1,button_2,button_3)
kb_read_zn.row(button_cansel)

kb_cansel = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb_cansel.add(button_cansel)

kb_main = ReplyKeyboardMarkup(resize_keyboard=True)
button_see = KeyboardButton(text='Просмотр з/н')
button_to = KeyboardButton(text='Просмотр ТО')
kb_main.add(button_to, button_see)

kb_to = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
bt_kamaz = KeyboardButton(text='KAMAZ')
bt_china = KeyboardButton(text='китайцы')
kb_to.add(bt_kamaz, bt_china)

kb_china = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
howo = KeyboardButton(text='HOWO')
sitrak = KeyboardButton(text='SITRAK')
faw_DM = KeyboardButton(text='FAW big DM')
faw_DL = KeyboardButton(text='FAW little DL')
kb_china.row(sitrak,howo)
kb_china.add(faw_DM,faw_DL)


kb_kamaz = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
orig_740 = KeyboardButton(text='740 ДВС')
old_740 = KeyboardButton(text='740 старые')
cummins = KeyboardButton(text='cummins')
dvs_5490 = KeyboardButton(text='5490')
dvs_54901 = KeyboardButton(text='54901')
hubs = KeyboardButton(text='Ступицы')
kompas = KeyboardButton(text='КОМПАС')
gbc = KeyboardButton(text='ГБЦ')
kb_kamaz.add(orig_740,old_740,cummins)
kb_kamaz.row(dvs_54901, dvs_5490, kompas)
kb_kamaz.row(hubs, gbc)


kb_hubs = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
hubs_43118 = KeyboardButton(text='43118')
hubs_6520 = KeyboardButton(text='6520')
kb_hubs.add(hubs_43118,hubs_6520)


def gbc_kb():
    gbc_kamaz = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    bt_740 = KeyboardButton(text='ГБЦ 740')
    bt_901 = KeyboardButton(text='ГБЦ 901')
    gbc_kamaz.add(bt_740, bt_901)
    return gbc_kamaz


async def set_default_commands(dip):
    await dip.bot.set_my_commands([
        types.BotCommand("start", "старт бот"),
    ])


def user_input_format(user_input):
    a = [',', '.', '-']
    b = [' ']

    if user_input[2] in a:
        cleaned_text = re.sub(r'(\d+)[^\w\s]*(\d+)', r'\1\2', user_input)
        return cleaned_text
    elif user_input[2] in b:
        cleaned_text = re.sub(r'(\d+)\s+(\d+)', r'\1\2', user_input)

        return cleaned_text
    else:
        return user_input


async def audio_to_text(file_path: str) -> str:
    """Принимает путь к аудио файлу, возвращает текст файла."""
    with open(file_path, "rb") as audio_file:
        transcript = await openai.Audio.atranscribe(
            "whisper-1", audio_file
        )
    return transcript["text"]


async def save_voice_as_mp3(bot: Bot, voice: Voice) -> str:
    """Скачивает голосовое сообщение и сохраняет в формате mp3."""
    voice_file_info = await bot.get_file(voice.file_id)
    voice_ogg = io.BytesIO()
    await bot.download_file(voice_file_info.file_path, voice_ogg)
    voice_mp3_path = f"voice_files/voice-{voice.file_unique_id}.mp3"
    AudioSegment.from_file(voice_ogg, format="ogg").export(
        voice_mp3_path, format="mp3"
    )
    return voice_mp3_path


async def create_table_users():
    conn = await aiosqlite.connect('kamaz.db')
    cursor = await conn.cursor()

    await cursor.executescript('''
        CREATE TABLE IF NOT EXISTS users(
            user_id INTEGER PRIMARY KEY,
            user_name TEXT
        )
    ''')
    await conn.commit()
    await conn.close()


async def write_to_db_user(user_id, user_name):
    conn = await aiosqlite.connect('kamaz.db')
    cursor = await conn.cursor()
    select_user_id = await cursor.execute(
        "SELECT user_id FROM users WHERE user_id = ?", (user_id,)
    )
    user_id1 = await select_user_id.fetchone()
    if not user_id1:
        await cursor.execute(
            'INSERT INTO users (user_id, user_name) VALUES (?, ?)',
            (user_id, user_name),)
    await conn.commit()
    await conn.close()


async def read_to_db_user_id():
    conn = await aiosqlite.connect('kamaz.db')
    cursor = await conn.cursor()
    select_user_id = await cursor.execute(
        "SELECT * FROM users "
    )
    select_order = await select_user_id.fetchall()
    users_dict = []
    for i in select_order:
        users_dict.append(i[0])

    await conn.commit()
    await conn.close()
    return users_dict


async def send_to_all_users(text):
    users = await read_to_db_user_id()
    for user_id in users:

        await bot.send_message(chat_id=user_id, text=text)


async def create_table():
    conn = await aiosqlite.connect('kamaz.db')
    cursor = await conn.cursor()

    await cursor.executescript('''
        CREATE TABLE IF NOT EXISTS kamaz(
            id INTEGER PRIMARY KEY,
            order_outfit INTEGER,
            product TEXT,
            send_date DATE
        )
    ''')
    await conn.commit()
    await conn.close()


async def write_to_db(order_outfit, product2, join_date):
    conn = await aiosqlite.connect('kamaz.db')
    cursor = await conn.cursor()
    order_outfit1 = await cursor.execute(
        "SELECT order_outfit FROM kamaz WHERE order_outfit = ?", (str(order_outfit),)
    )
    order_outfit1 = await order_outfit1.fetchone()
    if order_outfit1:
        select_product = await cursor.execute(
            "SELECT product FROM kamaz WHERE order_outfit = ?", (str(order_outfit),)
        )
        select_product = await select_product.fetchone()
        await cursor.execute(
            'UPDATE kamaz SET product = ? || ? WHERE order_outfit = ?',
            (product2,
             ' '.join(select_product),
             order_outfit
             ),
        )
    else:
        await cursor.execute(
            'INSERT INTO kamaz (order_outfit, product, send_date) VALUES (?, ?, ?)',
            (int(order_outfit), product2, join_date),)
    await conn.commit()
    await conn.close()


async def read_to_db(order_outfit):
    conn = await aiosqlite.connect('kamaz.db')
    cursor = await conn.cursor()
    select_order = await cursor.execute(
        "SELECT product FROM kamaz WHERE order_outfit = ?", (str(order_outfit),)
    )
    select_order = await select_order.fetchone()
    if select_order:
        for row in select_order:
            return row
    await conn.commit()
    await conn.close()


async def read_to_db_today(date):
    conn = await aiosqlite.connect('kamaz.db')
    cursor = await conn.cursor()
    select_order = await cursor.execute(
        "SELECT * FROM kamaz WHERE send_date = ?", (date,)
    )
    select_order = await select_order.fetchall()
    await conn.commit()
    await conn.close()
    return select_order














