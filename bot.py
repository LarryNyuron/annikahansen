import time


from trash import BOT_TOKEN
from aiogram import Bot, Dispatcher, executor, types
from db.create_db import get_cursor
from inline_keyboard.inline_keyboard import create_inline_bloc, \
                                            create_inline_callback_button, \
                                            alphabet_keyboard, \
                                            create_inline_bloc_with_region, \
                                            create_inline_bloc_square, \
                                            create_inline_bloc_price,\
                                            create_inline_bloc_list
from inline_keyboard.inline_keyboard import REGION


annika = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot=annika)


@dp.message_handler(commands=['start'])
async def gazprom_handler(message: types.Message):
    await message.answer(
        text='Выбери, что интересует:',
        reply_markup=create_inline_bloc(
            create_inline_callback_button('Земельные участки', 'land'),
            create_inline_callback_button('Что-то еще', 'back')
        )
    )


async def what_alphabet_region(callback: types.CallbackQuery):
    await callback.message.edit_text(text='Выберите букву области/субъекта',
                                     reply_markup=alphabet_keyboard())


async def what_region(callback: types.CallbackQuery):
    await callback.message.edit_text(text='Выберите область/субъект',
                reply_markup=create_inline_bloc_with_region(callback.data))


async def square(callback: types.CallbackQuery):
    await callback.message.edit_text(text='Какая площадь интересует',
                reply_markup=create_inline_bloc_square())


async def price(callback: types.CallbackQuery):
    await callback.message.edit_text(text='Стоимсть объекта',
                reply_markup=create_inline_bloc_price())


async def plug(callback: types.CallbackQuery):
    await callback.message.edit_text(text='Пока это заглушка, пиши /start')


async def list_of_land(callback: types.CallbackQuery):
    await callback.message.edit_text(text='Пример\n1.Some /someurl,\n2.Some\
/someurl,\n3.Some /someurl,\netc.',  reply_markup=create_inline_bloc_list())



async def object_card(callback: types.CallbackQuery):
    await callback.message.edit_text(text='Населенный пункт: {}\nПлощадь {}\n\
Кадастровый номер {}\nПраво собственности {}\nЦена {}\n'.format('Rostov',    \
'150', '1488', 'Uncle Frank', '100500$'),
        reply_markup=create_inline_bloc(create_inline_callback_button('Назад', \
                                                              'back')))



dp.register_callback_query_handler(what_alphabet_region,
                                   text='land')
dp.register_callback_query_handler(what_region,
                                   text=REGION.keys())
dp.register_callback_query_handler(plug,
                                   text='back')
dp.register_callback_query_handler(square,
                                   text='some region')
dp.register_callback_query_handler(price,
                                   text='some price')
dp.register_callback_query_handler(list_of_land,
                                   text='list')
dp.register_callback_query_handler(object_card,
                                   text='card')


if __name__ == '__main__':
    executor.start_polling(dp)
