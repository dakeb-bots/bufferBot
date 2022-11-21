from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from config import TOKEN
import asyncio

loop = asyncio.get_event_loop()

bot = Bot(TOKEN, parse_mode=types.ParseMode.MARKDOWN)
dp = Dispatcher(bot, loop=loop)
