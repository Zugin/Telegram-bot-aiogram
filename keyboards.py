from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton


# Инлайн клавиатура
"""
inline_kb_full = InlineKeyboardMarkup(row_width=2)
inline_btn_1 = InlineKeyboardButton('Первая', callback_data='button1')
inline_btn_2 = InlineKeyboardButton('Вторая', callback_data='button2')
inline_kb_full.add(inline_btn_1, inline_btn_2)
inline_btn_3 = InlineKeyboardButton('Третья', callback_data='button3')
inline_kb_full.row(inline_btn_3)
inline_kb_full.insert(InlineKeyboardButton("query='qwerty'", switch_inline_query='qwerty'))
inline_kb_full.insert(InlineKeyboardButton("Inline в этом же чате", switch_inline_query_current_chat='wasd'))
"""

def kb(num):
    inline_bn = InlineKeyboardMarkup()
    for i in range(num):
        inline_bn.insert(InlineKeyboardButton(f'Кнопка {i}', callback_data=f'button{i}'))

    return inline_bn

inline_bn_create_foldier = InlineKeyboardMarkup
inline_bn_create_foldier.add(InlineKeyboardButton('Создать папку', callback_data='create_foldier'))