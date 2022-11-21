from aiogram import types
from aiogram.dispatcher import Dispatcher
from create_bot import dp, bot
from datetime import datetime, timedelta
from config import PAYMENT_TOKEN

async def start(message: types.Message):
    await bot.send_message(message.chat.id, 'Чтобы купить подписку на наш канал /buy')

# Обработка оплаты
@dp.pre_checkout_query_handler(lambda query: True)
async def process_pre_checkout_query(pre_checkout_query: types.PreCheckoutQuery):
    await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)

# Успешная оплата
@dp.message_handler(content_types=types.ContentType.SUCCESSFUL_PAYMENT)
async def successful_payment(message: types.Message):
    expire_data = datetime.now() + timedelta(days=1)
    link = await bot.create_chat_invite_link('@superiden', expire_date=expire_data, member_limit=1)
    await bot.send_message(message.chat.id, 'Добро пожаловать в наш канал!')
    await bot.send_message(message.chat.id, link.invite_link)

async def buy(message: types.Message):
    PRICE = types.LabeledPrice(label='Подписка на канал', amount=500*100)
    if PAYMENT_TOKEN.split(':')[1] == 'Test':
        await bot.send_message(message.chat.id, 'Платеж осуществляется в тестовом режиме!')
    await bot.send_invoice(message.chat.id,
                           title='Подписка на канал',
                           description='Подписка на канал сроком в один месяц',
                           provider_token=PAYMENT_TOKEN,
                           currency='rub',
                           is_flexible=False,
                           prices=[PRICE],
                           start_parameter='subscribe-to-channel',
                           payload='invoice-pay-subscribe')

def register_client_handlers(dp: Dispatcher):
    dp.register_message_handler(start, commands='start')
    dp.register_message_handler(buy, commands='buy')
