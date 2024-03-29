def get_info():
    """Запрашивает у пользователя данные для записи в телефонный справочник"""
    info = []
    
    last_name = input('Введите фамилию: ')
    info.append(last_name)
    
    first_name = input('Введите имя: ')
    info.append(first_name)
    
    phone_number = ''
    valid = False
    while not valid:
        try:
            phone_number = input('Введите номер телефона: ')
            if len(phone_number) != 11:
                print('В номере телефона должно быть 11 цифр.')
            else:
                phone_number = int(phone_number)
                valid = True
        except ValueError:
            print('Номер телефона должен состоять только из цифр.')
    
    info.append(phone_number)
    
    description = input('Введите описание: ')
    info.append(description)
    
    return info


def writing_scv(info):
    """Записывает данные в файл Phonebook.csv"""
    file = 'Phonebook.csv'
    with open(file, 'a', encoding='utf-8') as data:
        data.write(f'{info[0]};{info[1]};{info[2]};{info[3]}\n')


def writing_txt(info):
    """Записывает данные в файл Phonebook.txt"""
    file = 'Phonebook.txt'
    with open(file, 'a', encoding='utf-8') as data:
        data.write(
            f'Фамилия: {info[0]}\n\nИмя: {info[1]}\n\nНомер телефона: {info[2]}\n\nОписание: {info[3]}\n\n\n')
        
def delete_info(info):
    """Удаляет данные из файла Phonebook.csv"""
    file = 'Phonebook.csv'
    try:
        with open(file, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        with open(file, 'w', encoding='utf-8') as file:
            for line in lines:
                if info[0] not in line:  # Предположим, что фамилия используется для удаления
                    file.write(line)
        print(f'Данные с фамилией {info[0]} удалены успешно.')
    except FileNotFoundError:
        print('Файл Phonebook.csv не найден.')

def update_info(info):
    """Изменяет данные в файлах Phonebook.csv и Phonebook.txt"""
    file_csv = 'Phonebook.csv'
    file_txt = 'Phonebook.txt'
    try:
        with open(file_csv, 'r', encoding='utf-8') as csv_file:
            lines = csv_file.readlines()
        with open(file_csv, 'w', encoding='utf-8') as csv_file:
            for line in lines:
                if info[0] in line:  # Предположим, что фамилия используется для обновления
                    csv_file.write(f'{info[0]};{info[1]};{info[2]};{info[3]}\n')
                else:
                    csv_file.write(line)
        print(f'Данные с фамилией {info[0]} успешно изменены в файле Phonebook.csv.')

        with open(file_txt, 'r', encoding='utf-8') as txt_file:
            lines = txt_file.readlines()
        with open(file_txt, 'w', encoding='utf-8') as txt_file:
            for line in lines:
                if info[0] in line:
                    txt_file.write(
                        f'Фамилия: {info[0]}\n\nИмя: {info[1]}\n\nНомер телефона: {info[2]}\n\nОписание: {info[3]}\n\n\n')
                else:
                    txt_file.write(line)
        print(f'Данные с фамилией {info[0]} успешно изменены в файле Phonebook.txt.')
    except FileNotFoundError:
        print('Файл Phonebook.csv или Phonebook.txt не найден.')