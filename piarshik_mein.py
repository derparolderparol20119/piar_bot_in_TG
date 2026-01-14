from aiogram import Bot , Dispatcher
import asyncio
from config import * 
from komandu import comand , regist_kanawu , wuwod_wsex_kanal
bot = Bot(TOKEN) 

dp = Dispatcher()

async def main():
    dp.include_router(comand.router)
    dp.include_router(regist_kanawu.router)
    dp.include_router(wuwod_wsex_kanal.router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("выкл")