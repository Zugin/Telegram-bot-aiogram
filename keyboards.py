from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton


# Инлайн клавиатура
def kb(bn_list, bn_comand):
    inline_bn = InlineKeyboardMarkup(row_width=2)
    for i in bn_comand:
        inline_bn.insert(InlineKeyboardButton(i, callback_data=i))

    for i in bn_list:
        inline_bn.insert(InlineKeyboardButton(f'{i} 📁', callback_data=i))

    return inline_bn

inline_bn_create_foldier = InlineKeyboardMarkup
inline_bn_create_foldier.add(InlineKeyboardButton('Создать папку', callback_data='create_foldier'))