from aiogram import Bot, Dispatcher
#from aiogram.contrib.fsm_storage.memory import MemoryStorage
import os


'''
# создание экземпляра бота и диспетчера с использованием машины состояний и хранилицем
STORAGE = MemoryStorage()
BOT = Bot(token = os.getenv('TOKEN'))
DP = Dispatcher(BOT, storage=STORAGE)
'''

# создание экземпляра бота и диспетчера 
BOT = Bot(token = os.getenv('TOKEN'))
DP = Dispatcher(BOT)