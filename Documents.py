documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]

directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': []
}


def search_person(number):
    for i in documents:
        if i['number'] == number:
            return i['name']
    else:
        return f'Документ с номером {number} отсутствует'


def adding_to_the_archive(type, number, name, shelf_number):
    documents.append({'type': type, 'number': number, 'name': name})
    if shelf_number in directories:
        directories[shelf_number].append(number)
        return f'{type} с номером {number} с именем {name} добавлен в каталог и перечень полок'
    else:
        return f'Полка с номером {shelf_number} отсутствует'


def delete_document(number):
    for i in documents:
        find = False
        if i['number'] == number:
            documents.remove(i)
            for key, value in directories.items():
                if number in value:
                    shell = key
                    value.remove(number)
                    find = True
    if find:
        return f'Документ с номером {number} удален с полки {shell}'
    else:
        return f'Документа с номером {number} в каталоге нет'


def main():
    print('Поиск имени по номеру документа')
    for number in ['10006', '11-2', '2207 876234', '111']:
        print(search_person(number))
    print('-------------------')
    print('Добавление документов')
    print(adding_to_the_archive('паспорт', '123456789', 'Александр Пушкин', '2'))
    print(adding_to_the_archive('паспорт', '9876543219', 'Михаил Лермонтов', '4'))
    print('-------------------')
    print('Удаление документа')
    print(delete_document('123456789'))


if __name__ == '__main__':
    main()
