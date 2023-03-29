# Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных.
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал для изменения
# и удаления данных

def read_csv(filename: str) -> list:
    data = []
    fields = ["Фамилия", "Имя", "Телефон", "Описание"]
    with open('phonebook.csv', 'r', encoding='utf-8') as fin:
        for line in fin:
            record = dict(zip(fields, line.strip().split(',')))
            data.append(record)
    return data

def write_csv(filename: str, data) -> str:
    file = open(filename, 'w', encoding='utf-8')
    for lines in data:
        s = ', '.join(f'{v}' for k, v in lines.items())
        file.write(s + '\n')

def write_txt(filename: str, data) -> str:
    file = open(filename, 'w', encoding='utf-8')
    for lines in data:
        s = ', '.join(f'{v}' for k, v in lines.items())
        file.write(s + '\n')  

def get_file_name() -> str:
    name_of_the_file = input('Введите название файла, который хотите сохранить ->')
    return name_of_the_file






def show_menu() -> int:
    print("\nВыберите необходимое действие:\n"
          "1. Отобразить весь справочник\n"
          "2. Найти абонента по фамилии\n"
          "3. Найти абонента по номеру телефона\n"
          "4. Добавить абонента в справочник\n"
          "5. Сохранить справочник в текстовом формате\n"
          "6. Удалить абнента\n"
          "7. Закончить работу")
    choice = int(input())
    return choice

def print_result(data) -> list:
    print(*data, sep='\n')
          
def find_by_name(data, sirname) -> str:
    for key in data:
        if key['Фамилия'].upper() == sirname.upper():
            print(*key.values())

def find_by_number(data, telephone_number) -> str:
    for key in data:
        if key['Телефон'].upper() == telephone_number.upper():
            print(*key.values())

def get_new_user() -> dict:
    record = {
        'Фамилия' : input('Введите фамилию ->'),
        'Имя' : input('Введите имя ->'),
        'Телефон' : input('Введите номер телефона ->'),
        'Описание' : input('Введите описание ->'),
    }

    return record

def add_user(data, new_record) -> list:
    data.append(new_record)
    print(*data, sep='\n')

def delete_user(data, user_to_delete) -> list:
    for key in data:
        if key['Фамилия'].upper() == user_to_delete.upper():
            del key
            print(f'Абонент {user_to_delete} удален!')   


phone_book = read_csv('phonebook.csv')

choice = show_menu()

while (choice != 7):
    if choice == 1:
        print_result(phone_book)
    elif choice == 2:
        name = (input('Введите фамилию абонента ->'))
        print(find_by_name(phone_book, name))
    elif choice == 3:
        number = (input('Введите номер телефона абонента ->'))
        print(find_by_number(phone_book, number))
    elif choice == 4:
        user_data = get_new_user()
        add_user(phone_book, user_data)
        write_csv('phonebook.csv', phone_book)
    elif choice == 5:
        file_name = get_file_name()
        write_txt(file_name, phone_book)
    elif choice == 6:
        user_data = input('Введите фамилию пользователя которого хотите удалить -> ')
        delete_user(phone_book, user_data)
        write_csv('phonebook.csv', phone_book)
    choice = show_menu()

