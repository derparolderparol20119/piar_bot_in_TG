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
from komandu.regist_kanawu import *


router = Router()

class REGIST(StatesGroup):
    name = State()
    users_name = State()
    parol =  State()

class AWTORIZ(StatesGroup):
    name2 = State()
    parol2 =  State()



@router.message(Command("registred"))
async def hi(message: Message, state: FSMContext):
    await message.answer("ввидите имя")
    await state.set_state(REGIST.name)
    await message.answer(f"ваш id {message.from_user.id}")


@router.message(REGIST.name)
async def name1(message: Message, state: FSMContext): 

    nety = False

    for i in message.text:
        if i in "1234567890":
            nety = True
            break
        if i in '@()':
            nety = True
            break

    if nety:
        await message.answer("имя введено не правильно содержыт цыфры или символы ")  
        nety = False   
    else:
        await state.update_data(name = message.text)
        await message.answer("ввидите user_name")
        await state.set_state(REGIST.users_name)



@router.message(REGIST.users_name)
async def name2(message: Message, state: FSMContext):

    user_name = polushit_user_name(message.text)

    uses1 = False
    uses2 = False
    uses3 = False

    for i in message.text:
        if i in "123456789":
            uses1 = True
        if i in "@()[]":
            uses2 = True

      
    if user_name:
        uses3 = True
        
    if uses1:
        await message.answer("имя введено не правильно содержыт цыфры ")
    elif uses2:
        await message.answer("имя введено не правильно содержыт знаки")
    elif uses3:
        await message.answer("такое имя уже есть")
    else:
        await state.update_data(name_user = message.text)
        await message.answer("ввидите пароль 8 символов Большая буква и знак")
        await state.set_state(REGIST.parol)




@router.message(REGIST.parol)
async def name4(message: Message, state: FSMContext):    
    nety1 = False
    nety2 = False
    nety3 = False


    for i in message.text:
        if i in "ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮQWERTYUIOPASDFGHJKLZXCVBNM":
            print(2)
            nety1 = True

        if i in "!@#$%^&*()!№;%:?**()//":
            print(1)
            nety2 = True
    
    if len(message.text) > 8:
        print(6)
        nety3 = True

        
    if nety3 and nety2 and nety1 :
        await message.answer("хорошо")
        await state.update_data(password = message.text)

        data = await state.get_data()
        zapisuwat_polzuwatela(data["name"] , data["name_user"]  , data["password"] , None , 1000 , message.from_user.id)

        await state.clear()

    else:
        await message.answer("не правильно ")


############################################################################################################################################

@router.message(Command("avtor")) # имя usrer name  пароль номер телефона сохронять в json 
async def name(message: Message, state: FSMContext):
    await message.answer("ввидите user имя")
    await state.set_state(AWTORIZ.name2) 


@router.message(AWTORIZ.name2)
async def name1(message: Message, state: FSMContext): 

    uses3 = False
    user_name = polushit_user_name(message.text)
      
    
    if user_name:
        uses3 = True
        
    if uses3:
        await state.update_data(name_user = message.text)
        await message.answer("ввидите пароль")
        await state.update_data(name2 = message.text)   
        await state.set_state(AWTORIZ.parol2)
    else:
        await message.answer("не правельно")


@router.message(AWTORIZ.parol2)
async def name1(message: Message, state: FSMContext):

    data = await state.get_data()

    parol = polushit_user_name_parol(data["name2"])   # ('pass123',)

    if parol is None:
        await message.answer("Ошибка пользователь не найден")
        return

    bd_parol = parol[0]  

    if bd_parol == message.text:
        await message.answer("хорошо")
        zaregan = True
        await state.clear()
    else:
        await message.answer("не правельно")


