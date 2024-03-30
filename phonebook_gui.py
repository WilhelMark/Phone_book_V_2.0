import tkinter as tk

def get_info():
    """Запрашивает у пользователя данные для записи в телефонный справочник"""
    last_name = entry_last_name.get()
    first_name = entry_first_name.get()
    phone_number = entry_phone_number.get()
    description = entry_description.get()
    return [last_name, first_name, phone_number, description]

def writing_csv(info):
    """Записывает данные в файл Phonebook.csv"""
    with open('Phonebook.csv', 'a', encoding='utf-8') as file:
        file.write(f'{info[0]};{info[1]};{info[2]};{info[3]}\n')

def writing_txt(info):
    """Записывает данные в файл Phonebook.txt"""
    with open('Phonebook.txt', 'a', encoding='utf-8') as file:
        file.write(f'Фамилия: {info[0]}\nИмя: {info[1]}\nНомер телефона: {info[2]}\nОписание: {info[3]}\n\n')

def delete_info(last_name):
    """Удаляет данные из файлов Phonebook.csv и Phonebook.txt по фамилии"""
    with open('Phonebook.csv', 'r', encoding='utf-8') as csv_file:
        lines = csv_file.readlines()
    with open('Phonebook.csv', 'w', encoding='utf-8') as csv_file:
        for line in lines:
            if last_name not in line.split(';')[0]:
                csv_file.write(line)

    with open('Phonebook.txt', 'r', encoding='utf-8') as txt_file:
        lines = txt_file.readlines()
    with open('Phonebook.txt', 'w', encoding='utf-8') as txt_file:
        for line in lines:
            if last_name not in line:
                txt_file.write(line)

def update_info(last_name, new_info):
    """Изменяет данные в файлах Phonebook.csv и Phonebook.txt по фамилии"""
    with open('Phonebook.csv', 'r', encoding='utf-8') as csv_file:
        lines = csv_file.readlines()
    with open('Phonebook.csv', 'w', encoding='utf-8') as csv_file:
        for line in lines:
            if last_name in line:
                csv_file.write(f'{new_info[0]};{new_info[1]};{new_info[2]};{new_info[3]}\n')
            else:
                csv_file.write(line)

    with open('Phonebook.txt', 'r', encoding='utf-8') as txt_file:
        lines = txt_file.readlines()
    with open('Phonebook.txt', 'w', encoding='utf-8') as txt_file:
        for line in lines:
            if last_name in line:
                txt_file.write(f'Фамилия: {new_info[0]}\nИмя: {new_info[1]}\nНомер телефона: {new_info[2]}\nОписание: {new_info[3]}\n\n')
            else:
                txt_file.write(line)

def import_data(filename):
    """Импортирует данные из указанного файла в телефонный справочник"""
    with open(filename, 'r', encoding='utf-8') as import_file:
        for line in import_file:
            data = line.strip().split(';')
            writing_csv(data)
            writing_txt(data)

def view_contacts():
    """Просмотр всех контактов из файлов Phonebook.csv и Phonebook.txt"""
    contacts = []
    with open('Phonebook.csv', 'r', encoding='utf-8') as csv_file:
        for line in csv_file:
            contacts.append(line.strip().split(';'))

    with open('Phonebook.txt', 'r', encoding='utf-8') as txt_file:
        txt_data = txt_file.read()

    # Вывод данных на экран или в новом окне
    view_window = tk.Toplevel()
    view_window.title("Список контактов")
    for contact in contacts:
        contact_label = tk.Label(view_window, text=f'Фамилия: {contact[0]}, Имя: {contact[1]}, Номер телефона: {contact[2]}, Описание: {contact[3]}')
        contact_label.pack()

def on_submit():
    info = get_info()
    writing_csv(info)
    writing_txt(info)

def on_delete():
    last_name = entry_last_name.get()
    delete_info(last_name)

def on_update():
    last_name = entry_last_name.get()
    new_info = get_info()
    update_info(last_name, new_info)

# Создание графического интерфейса с использованием Tkinter
root = tk.Tk()
root.title("Телефонный справочник")

# Добавление элементов интерфейса
label = tk.Label(root, text="Введите данные для телефонного справочника:")
label.pack()

# Поля для ввода
entry_last_name = tk.Entry(root, width=30)
entry_last_name.pack()
entry_first_name = tk.Entry(root, width=30)
entry_first_name.pack()
entry_phone_number = tk.Entry(root, width=30)
entry_phone_number.pack()
entry_description = tk.Entry(root, width=30)
entry_description.pack()

# Кнопки
submit_button = tk.Button(root, text="Добавить", command=on_submit)
submit_button.pack()
delete_button = tk.Button(root, text="Удалить", command=on_delete)
delete_button.pack()
update_button = tk.Button(root, text="Изменить", command=on_update)
update_button.pack()

view_button = tk.Button(root, text="Просмотреть контакты", command=view_contacts)
view_button.pack()

# Запуск главного цикла обработки событий
root.mainloop()
