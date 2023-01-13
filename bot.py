import time


from trash import BOT_TOKEN
from aiogram import Bot, Dispatcher, executor, types
from db.create_db import get_cursor
from inline_keyboard.inline_keyboard import create_inline_bloc, \
                                            create_inline_callback_button, \
                                            alphabet_keyboard, \
                                            create_inline_bloc_with_region
from inline_keyboard.inline_keyboard import REGION


annika = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot=annika)


@dp.message_handler(commands=['start'])
async def gazprom_handler(message: types.Message):
    await message.answer(
        text='Выбери, что интересует:',
        reply_markup=create_inline_bloc(
            create_inline_callback_button('Земельные участки', 'land'),
            create_inline_callback_button('Что-то еще', 'something')
        )
    )


async def what_alphabet_region(callback: types.CallbackQuery):
    await callback.message.edit_text(text='Выберите букву области/субъекта',
                                     reply_markup=alphabet_keyboard())


async def what_region(callback: types.CallbackQuery):
    await callback.message.edit_text(text='Выберите область/субъект',
                reply_markup=create_inline_bloc_with_region(callback.data))


async def callback_back(callback: types.CallbackQuery):
    await callback.message.edit_text(text='Пока это заглушка, пиши /start')

    '''time.sleep(3)
    await callback.message.edit_text(text='Введите примерную цену')
    time.sleep(3
    await callback.message.edit_text(text='Введите ценовой диапазон')
'''
dp.register_callback_query_handler(what_alphabet_region,
                                   text='land')
dp.register_callback_query_handler(what_region,
                                   text=REGION.keys())
dp.register_callback_query_handler(callback_back,
                                   text='back')


if __name__ == '__main__':
    executor.start_polling(dp)
