import os
import sqlite3

from aiogram import types



def create_true_REGION():
    con = sqlite3.connect(os.getcwd() + '\\db\\' + 'gazprom.db')
    cursor = con.cursor()
    reg = cursor.execute('''SELECT DISTINCT Region FROM land''')
    region = {}
    for i in reg:
        if i[0][0] not in region.keys():
            region[i[0][0]] = [i[0]]
        else:
            region[i[0][0]].append(i[0])
    return region


REGION = create_true_REGION()
SQUARE = ['<500', '500-1000', '1000-10000', '10000>']
PRICE = ['<250', '250-1', '1-5', '5>']
all_region = [ j for i in REGION.keys() for j in REGION[i] ]


def create_inline_callback_button(text: str, callback: str):
    button = types.InlineKeyboardButton(
        text=text,
        callback_data=callback
    )
    return button


def create_inline_bloc(*args):
    keyboard = types.InlineKeyboardMarkup()
    for button in args:
        keyboard.add(button)
    return keyboard


def alphabet_keyboard():
    keyboard = types.InlineKeyboardMarkup(row_width=4)
    for button in REGION.keys():
        keyboard.insert(create_inline_callback_button(button, button))
    keyboard.insert(create_inline_callback_button('Назад', 'back'))
    return keyboard


def create_inline_bloc_with_region(letter):
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    print(REGION[letter])
    for button in REGION[letter]:
        keyboard.insert(create_inline_callback_button(button, button))
    keyboard.insert(create_inline_callback_button('Назад', 'back'))
    return keyboard


def create_inline_bloc_square(square=SQUARE, values=SQUARE):
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    for button in SQUARE:
        keyboard.insert(create_inline_callback_button(button, 'some price'))
    keyboard.insert(create_inline_callback_button('Назад', 'back'))
    return keyboard


def create_inline_bloc_price(price=PRICE, values=PRICE):
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    for button in PRICE:
        keyboard.insert(create_inline_callback_button(button, 'list'))
    keyboard.insert(create_inline_callback_button('Назад', 'back'))
    return keyboard


def create_inline_bloc_list():
    keyboard = types.InlineKeyboardMarkup(row_width=5)
    for button in ['<', '1', '2', '3', '>']:
        keyboard.insert(create_inline_callback_button(button, 'card'))
    keyboard.insert(create_inline_callback_button('Назад', 'back'))
    return keyboard
