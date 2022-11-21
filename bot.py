from aiogram import executor
from create_bot import dp

from handlers import client

client.register_client_handlers(dp)

async def on_startup(_):
    print('Bot is online!')

if __name__ == '__main__':
    executor.start_polling(dp,
                           on_startup=on_startup,
                           skip_updates=False
                           )
