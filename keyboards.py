from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton


# Инлайн клавиатура
def kb(num):
    inline_bn = InlineKeyboardMarkup()
    for i in range(num):
        inline_bn.insert(InlineKeyboardButton(f'Кнопка {i}', callback_data=f'button{i}'))

    return inline_bn

inline_bn_create_foldier = InlineKeyboardMarkup
inline_bn_create_foldier.add(InlineKeyboardButton('Создать папку', callback_data='create_foldier'))