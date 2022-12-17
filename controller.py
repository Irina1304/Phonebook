from import_data import import_data, writing_scv, writing_txt
from export_data import export_data


def view():
    print(export_data('Phonebook.txt'))


def record_info():
    info = import_data()
    writing_scv(info)
    writing_txt(info)


def choice_todo():
    print("Доступные операции с телефонной книгой:\n\
    1 - импорт;\n\
    2 - просмотр телефонной книги")
    ch = input("Введите цифру: ")
    if ch == '1':
        record_info()
    else:
        view()