from aiogram import F , Router , types
from aiogram.types import  Message
from aiogram.filters import Command , CommandStart
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
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

router = Router() 


class REG_KANAWU(StatesGroup): # prem_podpiska , name , kategorii, ssulka , dlitelnost_podpiski , opisanie , fotoshka
    name = State()
    kategorii =  State()
    ssulka =  State()
    opisanie = State()
    fotoshka = State()


class PREM_NA_KANAL(StatesGroup):
    vvidite = State()
    poshli =  State()



@router.message(Command("regist_kanala")) 
async def regitka(message: Message, state: FSMContext ):
    print(1 , message.from_user.id)

    id_pol = polushit_id_polz(message.from_user.id)

    if id_pol :
        await message.answer(f"{id_pol[1] }  вы авторезированы введите имя канавы")
        await state.set_state(REG_KANAWU.name)
        
    else:
        await message.answer(f"{id_pol[1] } вы не авторезированы зарегестрируйтесь или авторизируйтесь ")


@router.message(REG_KANAWU.name)
async def regkawu(message: Message, state: FSMContext): 
    await message.answer(f"введите категорию")

    await state.update_data(name = message.text)
    await state.set_state(REG_KANAWU.kategorii)


@router.message(REG_KANAWU.kategorii)
async def regkawu(message: Message, state: FSMContext): 
    await message.answer(f"введите ссылку")

    await state.update_data(kategorii = message.text)
    await state.set_state(REG_KANAWU.ssulka)


@router.message(REG_KANAWU.ssulka)
async def regkawu(message: Message, state: FSMContext): 
    await message.answer(f"ввидите описание")
    
    await state.update_data(ssulka = message.text)
    await state.set_state(REG_KANAWU.opisanie)


@router.message(REG_KANAWU.opisanie )
async def regkawu(message: Message, state: FSMContext): 
    await message.answer(f"выставте фото канала ")
    
    await state.update_data(opisanie  = message.text)
    await state.set_state(REG_KANAWU.fotoshka )


@router.message(REG_KANAWU.fotoshka )
async def regkawu(message: Message, state: FSMContext): 
    await message.answer(f"начинаем запись")
    
    photo_id = message.photo[-1].file_id
    data = await state.get_data()

    user_id = message.from_user.id
    polzuwatel = polushit_id_polz(user_id )

    print(polzuwatel )
    list_kort = list(polzuwatel) 
    list_kort[5] -= 1000
    list_kort = tuple(list_kort)
    polzuwatel = list_kort
    #print(polzuwatel[0][5])


    zapisuwat_kanal(False , data["name"] , data["kategorii"] , data["ssulka"] , 0 , data["opisanie"],photo_id  ) # prem_podpiska , name , kategorii, ssulka , dlitelnost_podpiski , opisanie , fotoshka 
    await message.answer(f"офрмите подписку,  при первом оформлении скидка 99 %" , reply_markup = kb.oplata_podpiski)
    return



