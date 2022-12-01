import time
import logging
import asyncio

from trash import BOT_TOKEN, MSG
from aiogram import Bot, Dispatcher, executor, types


annika = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot=annika)


@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    id_user = message.from_user.id
    name_user = message.from_user.first_name
    surname_user = message.from_user.full_name
    logging.info(f'{id_user} {surname_user} {time.asctime()}')
    await message.reply(f'Hello, {surname_user}! Where Commander?')

    for i in range(7):
        await asyncio.sleep(86400)
        await annika.send_message(id_user, MSG.format(name_user))

if __name__ == '__main__':
    executor.start_polling(dp)