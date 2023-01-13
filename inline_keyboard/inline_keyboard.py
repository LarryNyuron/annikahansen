from aiogram import types


REGION = {
    'А':['Республика Адыгея', 'Республика Алтай', 'Алтайский край',
          'Амурская область', 'Архангельская область', 'Астраханская область'],
    'Б':['Республика Башкортостан','Республика Бурятия', 'Белгородская область',
         'Брянская область'],
    'В':['Владимирская область', 'Волгоградская область', 'Вологодская область',
         'Воронежская область'],
    'Д':['Республика Дагестан'],
    'Е':['Еврейская автономная область'],
    'З':['Забайкальский край', 'Запорожская область'],
    'И':['Республика Ингушетия', 'Ивановская область', 'Иркутская область'],
    'К':['Кабардино-Балкарская Республика', 'Республика Калмыкия',
         'Карачаево-Черкесская Республика', 'Республика Карелия',
         'Республика Коми', 'Республика Крым', 'Камчатский край',
         'Краснодарский край', 'Красноярский край', 'Калининградская область',
         'Калужская область', 'Кемеровская область', 'Кировская область',
         'Костромская область', 'Курганская область', 'Курская область'],
    'Л':['Ленинградская область', 'Липецкая область'],
    'М':['Республика Марий Эл', 'Республика Мордовия', 'Магаданская область',
         'Московская область', 'Мурманская область', 'Москва'],
    'Н':['Нижегородская область', 'Новгородская область',
         'Новосибирская область','Ненецкий автономный округ'],
    'О':['Омская область', 'Оренбургская область', 'Орловская область'],
    'П':['Пермский край', 'Приморский край', 'Пензенская область',
         'Псковская область'],
    'Р':['Ростовская область', 'Рязанская область'],
    'С':['Республика Саха (Якутия)', 'Республика Северная Осетия — Алания',
         'Ставропольский край', 'Самарская область', 'Саратовская область',
         'Сахалинская область', 'Свердловская область', 'Смоленская область',
         'Санкт-Петербург', 'Севастополь'],
    'Т':['Республика Татарстан', 'Республика Тыва', 'Тамбовская область',
         'Тверская область', 'Томская область', 'Тульская область',
         'Тюменская область'],
    'У':['Удмуртская Республика', 'Ульяновская область'],
    'Х':['Республика Хакасия', 'Хабаровский край',
         'Ханты-Мансийский автономный округ — Югра'],
    'Ч':['Чеченская Республика', 'Чувашская Республика', 'Челябинская область',
         'Чукотский автономный округ'],
    'Я':['Ярославская область', 'Ямало-Ненецкий автономный округ']
}


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
    for button in REGION[letter]:
        keyboard.insert(create_inline_callback_button(button, button))
    keyboard.insert(create_inline_callback_button('Назад', 'back'))
    return keyboard