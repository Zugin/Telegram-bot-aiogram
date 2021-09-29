#!venv/bin/python
import logging
import os
from aiogram import Bot, Dispatcher, executor, types
from sys import exit

from config import BOT_TOKEN
import keyboards
import function

"""
Бот по обработке фотографий для торговых представителей и мерчендайзеров.

Структурирует по заданным папкам, создает итоговый архив
"""

# Объект бота
bot_token = BOT_TOKEN
if not bot_token:
    exit("Error: no token provided")

bot = Bot(token=bot_token, parse_mode=types.ParseMode.HTML)

# Диспетчер для бота
dp = Dispatcher(bot)
# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)

#  Создание экземпляра FunctionBot
function = function.FunctionBot()

@dp.message_handler(commands=['start'])
async def process_command_1(message: types.Message):
    #  Проверка создания каталога пользователя
    try:
        os.mkdir(str(message.from_user.id))
    except FileExistsError:
        pass
    #  Добавление клавиатуры
    function.delete_func()
    function.flag_start = True
    function.folders(message.from_user.id)
    inline_bn = keyboards.kb(function.bn_list, function.comand_bn)
    await message.reply("Начало работы с ботом", reply_markup=inline_bn)

@dp.callback_query_handler()
async def main_func(message: types.CallbackQuery):
    #  Выполнение служебных команд: Назад, Создать, Удалить, перемещение по папкам
    data = message.data
    #  Вызов функции для реакции на нажатие кнопок Создание клавиатур, запись текста сообщения
    text = function.bn_reaction(data)
    #  Создание клавиатуры
    inline_bn = keyboards.kb(function.bn_list, function.comand_bn)

    #  await bot.send_message(message.from_user.id, 'В папке есть файлы', reply_markup=inline_bn)
    await bot.answer_callback_query(message.id)
    await message.message.edit_text(f'{text}', reply_markup=inline_bn)

@dp.message_handler()
async def any_text_message(message: types.Message):
    print(message.text)
    if function.flag_create_foldier:
        try:
            new_folder = os.path.join(function.path_fold, str(message.text))
            os.mkdir(new_folder)
        except FileExistsError:
            await bot.send_message(message.from_user.id, 'Папка с таким именем уже есть')
    function.flag_create_foldier = False

if __name__ == "__main__":
    # Запуск бота
    executor.start_polling(dp, skip_updates=True)