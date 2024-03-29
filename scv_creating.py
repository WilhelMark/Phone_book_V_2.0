def creating():
    """Создает файл Phonebook.csv и записывает в него шапку таблицы"""
    file = 'Phonebook.csv'
    header = 'Фамилия;Имя;Номер телефона;Описание\n'
    
    with open(file, 'w', encoding='utf-8') as data:
        data.write(header)