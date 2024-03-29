from os.path import exists
from scv_creating import creating
from file_writing import writing_scv, writing_txt, get_info
from export import from_file


def view():
    """Выводит содержимое телефонного справочника из файла Phonebook.txt"""
    print(from_file('Phonebook.txt'))


def record_info():
    """Записывает информацию в файлы CSV и TXT"""
    info = get_info()
    writing_scv(info)
    writing_txt(info)


def choice():
    """Предоставляет пользователю выбор продолжить работу или завершить, записать данные или вывести на экран"""
    while True:
        flag = input('Для продолжения работы нажмите \'да\', или любой символ для завершения работы... ')
        if flag.lower() != 'да':
            break

        path = 'Phonebook.csv'
        if not exists(path):
            creating()

        choice_action = input('Введите \'да\', если хотите записать новые данные, и любой другой символ, если хотите просмотреть справочник в консоли: ')
        if choice_action.lower() == 'да':
            record_info()
        else:
            view()

    print('Программа завершена.')