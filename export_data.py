# модуль экспорта данных 

def export_data(file):
    with open(file, 'r', encoding='utf-8') as data:
        dictionary = data.read()
    return dictionary