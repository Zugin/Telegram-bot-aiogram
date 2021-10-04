from aiogram import Bot, Dispatcher, executor, types
import os
import keyboards


class FunctionBot():
    def __init__(self):
        self.dir_list = []
        self.bn_comand = []
        self.path_fold = ""
        self.bn_create = ['Создать', 'Отмена']
        self.flag_start = False
        self.flag_step_back = False
        self.flag_create_foldier = False
        self.bn_list = []
        self.bn_dict = {}


    def create_bn_dict(self,user_id):
        #  Создание словаря при вызове команды старт
        self.bn_dict[user_id] = {
                'bn_comand' : [],
                'dir_list' : [],
                'path_fold' : '',
                'flag_start' : True,
                'flag_step_back' : False,
                'flag_create_foldier' : False
            }
        print(self.bn_dict)

    def bn_dict_args(self, user_id):
        bn_comand = self.bn_dict[user_id]['bn_comand']




    def folders(self, path_fold=''):
        #  Формирование списка состоящего из папок и добавление кнопки списка "Назад" и "Создать папку"
        self.bn_comand = ['Создать папку']
        if not self.flag_start:
            self.bn_comand += ['Удалить папку', 'Назад']
        else:
            try:
                self.bn_comand.remove('Назад')
            except ValueError:
                pass
        if not self.flag_step_back or not path_fold == '':
            self.path_fold = os.path.join(self.path_fold, str(path_fold))
        self.dir_list = os.listdir(self.path_fold)
        for dir in self.dir_list.copy():
            dir_path = os.path.join(str(self.path_fold), dir)
            if not os.path.isdir(dir_path):
                self.dir_list.remove(dir)
        self.bn_list = self.dir_list

    def step_back(self):
        #  Нажатие кнопки назад
        self.path_fold = os.path.split(self.path_fold)[0]
        if os.path.split(self.path_fold)[0] == '':
            self.flag_start = True
        self.folders()

    def moving_folder(self, data):
        #  Передвижение по папкам
        self.flag_start = False
        if data == 'Назад':
            self.flag_step_back = True
            self.step_back()

        elif data == 'Создать папку':
            self.flag_create_foldier = True

        else:
            self.flag_step_back = False
            self.flag_create_foldier = False
            path_fold = data
            self.folders(path_fold)

    def delete_func(self):
        self.__init__()

    def create_folder(self):
        pass

    def delete_folder(self):
        folder = self.path_fold
        try:
            os.rmdir(folder)
        except FileNotFoundError:
            print(f'Папки {folder} не существует')
        except PermissionError:
            print(f'Папка {folder} заблокирована для удаления')
        except OSError:
            print(f'Папка {folder} не пустая')
        return True

    def bn_reaction(self, data):
        text = f'Нажата кнопка: {data}'
        if data in self.bn_list:
            self.moving_folder(data)
        elif data == 'Назад':
            self.moving_folder(data)
        elif data == 'Создать папку':
            text = 'Для создания новой папки нажми "Создать" или "Отмена"'
            self.bn_comand = self.bn_create
            self.bn_list = []
            data = ''
        elif data == 'Отмена':
            self.flag_step_back = True
            self.folders()
        elif data == 'Создать':
            text = 'Отправь название папки и после нажми "Готово"'
            data = ''
            self.bn_comand = ['Готово']
            self.flag_create_foldier = True
        elif data == 'Готово':
            self.flag_step_back = True
            self.folders()
        elif data == 'Удалить папку':
            if self.delete_folder():
                self.flag_step_back = True
                self.folders()
            else:
                data = 'Назад'
                self.moving_folder(data)
        print(text)
        return text