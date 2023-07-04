import asyncio
import datetime
import json
import logging
import sys
from aiogram import Dispatcher, executor
from handlers import dp
import database

logging.basicConfig(level=logging.INFO)
logFormatter = logging.Formatter(
    "%(asctime)s [%(threadName)-12.12s] [%(levelname)-5.5s]  %(message)s"
)
rootLogger = logging.getLogger()

fileHandler = logging.FileHandler("logs.log")
fileHandler.setFormatter(logFormatter)
rootLogger.addHandler(fileHandler)

consoleHandler = logging.StreamHandler()
consoleHandler.setFormatter(logFormatter)
rootLogger.addHandler(consoleHandler)

async def on_startup(dp: Dispatcher):
    await database.initialize()
    
async def on_shutdown(dp: Dispatcher):
    await dp.storage.close()
    await dp.storage.wait_closed()
    
if __name__ == "__main__":
    executor.start_polling(
        dp, on_startup=on_startup, on_shutdown=on_shutdown, skip_updates=True
    )