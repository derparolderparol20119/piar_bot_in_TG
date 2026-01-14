from aiogram import F , Router , types
from aiogram.types import  Message
from aiogram.filters import Command , CommandStart
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery
from aiogram import Bot , Dispatcher
import json
import random 
import re
import math
from datetime import *
from aiogram.types import FSInputFile
import os
from database.database import *
from config import * 
import komandu.inline_knopki as kb
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton , InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


router = Router()


class WUWUD_KANALOW(StatesGroup):
    page = State()
    channel_messages = State()

@router.message(Command("wuw_kanalow")) 
async def ww_kanal(message: Message, state: FSMContext ):
    await message.answer(f"нажмите на один из номеров" , reply_markup = kb.wubor_kategori )


@router.callback_query(F.data == "4")
async def open_channels(callback: CallbackQuery, state: FSMContext):
    await state.set_state(WUWUD_KANALOW.page)
    await state.update_data(page=0, channel_messages=[])

    await callback.message.edit_text(
        "Каналы:\n\n",
        reply_markup=kb.pagination
    )

    await show_channels(callback, state)



async def show_channels(callback: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    page = data.get("page", 0)
    old_messages = data.get("channel_messages", [])

    for msg_id in old_messages:
        try:
            await callback.bot.delete_message(
                callback.message.chat.id,
                msg_id
            )

        except:
            pass

    channels = poluShet_kanal()
    per_page = 5

    start = page * per_page
    end = start + per_page
    current = channels[start:end]

    if not current:
        await callback.answer("Больше каналов нет")
        return

    new_messages = []

    for ch in current:
        msg = await callback.message.answer(
            f"{ch[2]}",
            reply_markup=kb.obzor_kanal(ch[0])  # ID канала
        )
        new_messages.append(msg.message_id)

    await state.update_data(channel_messages=new_messages)


@router.callback_query(F.data == "page_next")
async def next_page(callback: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    page = data.get("page", 0)

    channels = poluShet_kanal()
    max_page = (len(channels) - 1) // 5

    if page >= max_page:
        await callback.answer("Это последняя страница")
        return

    await state.update_data(page=page + 1)
    await show_channels(callback, state)


@router.callback_query(F.data == "page_back")
async def prev_page(callback: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    page = data.get("page", 0)

    if page <= 0:
        await callback.answer("Это первая страница")
        return

    await state.update_data(page=page - 1)
    await show_channels(callback, state)
    await show_channels(callback, state)


@router.callback_query(F.data.startswith("view_"))
async def view_channel(callback: CallbackQuery):
    channel_id = callback.data.split("_")[1]
    await callback.message.answer(f"Информация о канале {channel_id}")
    channels = poluShet_kanal()

    for i in channels:
        
        if i[0] == int(channel_id) :
            await callback.message.answer(f"Имя ({i[2]}) \n Котегория ({i[3]}) \n Ссылка ({i[4]}) \n Описание ({i[6]})")
            await callback.message.answer_photo(photo= i[7])

    user_id = callback.from_user.id
    polzuwatel = polushit_id_polz(user_id )


    list_kort = list(polzuwatel[0]) 
    list_kort[5] += 100
    list_kort = tuple(list_kort)
    polzuwatel[0] = list_kort
    print(polzuwatel[0][5])


@router.callback_query(F.data == "3")
async def open_channels(callback: CallbackQuery, state: FSMContext):
    await state.set_state(WUWUD_KANALOW.page)
    await state.update_data(page=0)

    user_id = callback.from_user.id
    polzuwatel = polushit_id_polz(user_id)

    if not polzuwatel or not polzuwatel[4]:
        await callback.message.edit_text(
            "❗ Вы пока не подписаны ни на один канал"
        )
        return

    await show_channels(callback, state, polzuwatel)


@router.callback_query(F.data.startswith("sub_"))
async def sub_channel(callback: CallbackQuery):
    user_id = callback.from_user.id
    channel_id = int(callback.data.split("_")[1])

    polzuwatel = polushit_id_polz(user_id)
    if not polzuwatel:
        await callback.message.answer("Пользователь не найден")
        return

    channels = poluShet_kanal_wan(channel_id)
    if not channels:
        await callback.message.answer("Канал не найден")
        return

    subs = polzuwatel[4].split(",") if polzuwatel[4] else []
    if str(channel_id) in subs:
        await callback.message.answer(" Вы уже получили бонус за этот канал")
        return

    subs.append(str(channel_id))
    new_subs = ",".join(subs)
    new_coins = polzuwatel[5] + 100

    zapisuwat_polzuwatela2(
        polzuwatel[1], polzuwatel[2], polzuwatel[3],
        new_subs, new_coins, polzuwatel[6]
    )

    channel_username = channels[0][4].replace("https://t.me/", "").replace("@", "")
    channel_url = f"https://t.me/{channel_username}"

    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[[InlineKeyboardButton(text="Перейти и подписаться", url=channel_url)]]
    )

    await callback.message.answer(
        f"Вы получили +100 коинов! \nНажмите на кнопку ниже, чтобы перейти на канал:",
        reply_markup=keyboard
    )