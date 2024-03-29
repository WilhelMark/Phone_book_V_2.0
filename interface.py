from os.path import exists
from scv_creating import creating
from file_writing import writing_scv, writing_txt, get_info, delete_info, update_info
from export import from_file


def view():
    """Выводит содержимое телефонного справочника из файла Phonebook.txt"""
    print(from_file('Phonebook.txt'))


def record_info():
    """Записывает информацию в файлы CSV и TXT"""
    info = get_info()
    writing_scv(info)
    writing_txt(info)

def delete_data():
    """Удаляет данные из телефонного справочника"""
    info = get_info()
    delete_info(info)

def update_data():
    """Изменяет данные в телефонном справочнике"""
    info = get_info()
    update_info(info)

def choice():
    """Предоставляет пользователю выбор продолжить работу или завершить, записать данные или вывести на экран"""
    while True:
        flag = input('Для продолжения работы нажмите \'да\', или любой символ для завершения работы... ')
        if flag.lower() != 'да':
            break

        path = 'Phonebook.csv'
        if not exists(path):
            creating()

        choice_action = input('Введите \'да\' для записи новых данных, \'удалить\' для удаления данных, \'изменить\' для изменения данных, или любой другой символ для просмотра справочника в консоли: ')
        if choice_action.lower() == 'да':
            record_info()
        elif choice_action.lower() == 'удалить':
            delete_data()
        elif choice_action.lower() == 'изменить':
            update_data()
        else:
            view()

    print('Программа завершена.')