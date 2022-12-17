# модуль импорта данных 

def import_data():
    info = []
    last_name = input('Введите фамилию: ')
    info.append(last_name)
    first_name = input('Введите имя: ')
    info.append(first_name)
    second_name = input('Введите отчество: ')
    info.append(second_name)
    phone_number = input('Введите номер телефона: ')
    info.append(phone_number)
    description = input('Введите описание: ')
    info.append(description)
    return info


def writing_scv(info):
    file = 'Phonebook.csv'
    with open(file, 'a', encoding='utf-8') as data:
        data.write(f'{info[0]};{info[1]};{info[2]};{info[3]};{info[4]}\n')


def writing_txt(info):
    file = 'Phonebook.txt'
    with open(file, 'a', encoding='utf-8') as data:
        data.write(
            f'Фамилия: {info[0]}\n\nИмя: {info[1]}\n\nОтчество: {info[2]}\n\nНомер телефона: {info[3]}\n\nОписание: {info[4]}\n\n\n')
