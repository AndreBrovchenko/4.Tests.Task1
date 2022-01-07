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


def people(document_number):
    '''
    searches in list "documents_list" for a document with number "documents_number"
    and if it finds it, it displays the name of the person to whom it belongs,
    otherwise it writes that there is no such document.
    '''
    people_name = ''
    for document in documents:
        if document['number'] == document_number:
            people_name = document['name']
            break
    return people_name


def shelf(document_number):
    '''
    searches in list "directories_dict" for a document with number "documents_number"
    and if it finds it, it displays the number of the shelf on which it lies,
    otherwise it says that there is no such document.
    '''
    catalog_name = ''
    for catalog, numbers in directories.items():
        if document_number in numbers:
            catalog_name = catalog
            break
    return catalog_name


def doc_list():
    '''
    will display a list of all documents in list "documents_list" in the format:
    type "number" "name"
    '''
    for document in documents:
        print(f'{document["type"]} \"{document["number"]}\" \"{document["name"]}\"')
    print()
    print(directories)


def document_add(document_number, type_document, name, shelf_number):
    '''
    adds a new document "documents_number" to list "documents_list"
    and to the list of shelves "directories_dict",
    asking for its number, type, owner's name and the number of the shelf on which it will be stored
    '''
    documents.append({'type': type_document, 'number': document_number, 'name': name})
    directories[shelf_number].append(document_number)
    return documents, directories[shelf_number]
    # print(documents)
    # print(directories)
    # print()


def document_del(document_number):
    '''
    asks for document number "documents_number" and removes it from "documents_list"
    and from the list of shelves "directories_dict"
    '''
    document_found = False
    key_items = ''
    document_delete = {}
    for document in documents:
        if document_number == document['number']:
            document_delete = document
            documents.remove(document)
            for key, value in directories.items():
                if document_number in value:
                    key_items = key
                    value.remove(document_number)
                    document_found = True
                    # print(documents_list)
                    # print(directories_dict)
                    break
    if document_found:
        return document_found, documents, directories[key_items], document_delete, key_items
    else:
        return document_found, documents, directories['1'], document_delete, '1'
        # return 'Документ с таким номером не найден'


def document_move(documents_number, shelf_number):
    '''
    asks for document number "documents_number", target shelf number  P
    and moves the document from the current shelf to the target shelf
    in list "directories_dict".
    '''
    document_moved = False
    for key, value in directories.items():
        if documents_number in value:
            value.remove(documents_number)
            directories[shelf_number].append(documents_number)
            # print(documents_list)
            # print(directories_dict)
            document_moved = True
            break
    return document_moved, documents, directories[shelf_number], key


def add_shelf(shelf_number):
    '''
    asks for the number of the new shelf P
    and adds it to list "directories_dict".
    '''
    directories[shelf_number] = []
    return documents, directories[shelf_number]
    # print(directories)


def del_shelf(shelf_number):
    directories.pop(shelf_number)


def main():
    '''
    User dialogue function.
    Asks the user for a command name and, if necessary,
    additional parameters, and then runs the required function
    '''
    while True:
        user_input = input('Введите команду: ')
        if user_input == 'p':
            people_name = ''
            number_document = input('Введите номер документа: ')
            people_name = people(number_document)
            if people_name != '':
                print(people_name, end='\n\n')
            else:
                print(f'документ с номером {number_document} не найден\n')
            # print(people(documents_list, number_document), end='\n\n')
            # print(f'владелец документа {number_document} {people(documents_list, number_document)}\n')
        elif user_input == 's':
            number_document = input('Введите номер документа: ')
            number_shelf = ''
            number_shelf = shelf(number_document)
            if number_shelf != '':
                print(f'документ с номером {number_document} находится на полке {number_shelf}\n\n')
            else:
                print(f'документ с номером {number_document} не найден\n')
            # print(shelf(documents), end='\n\n')
            # print(f'документ с номером {number_document} находится на полке {shelf(documents)}\n')
        elif user_input == 'l':
            doc_list()
        elif user_input == 'a':
            number_document = input('Введите номер документа: ')
            type_document = input('Введите тип документа: ')
            owner_document = input('Введите владельца документа: ')
            number_shelf = input('Введите номер полки документа: ')
            while number_shelf not in directories:
                number_shelf = input('Полки с таким номером нет. Повторите ввод: \n')
            document_add(number_document, type_document, owner_document, number_shelf)
            print('документ добавлен\n')
        elif user_input == 'd':
            number_document = input('Введите номер документа который необходимо удалить: ')
            document_deleted, doc_second, dir_second, doc_delete, shelf_doc = document_del(number_document)
            if document_deleted:
                print(f'документ с номером {number_document} удален\n')
            else:
                print(f'документ с номером {number_document} не найден\n')
        elif user_input == 'm':
            number_document = input('Введите номер документа который необходимо переместить: ')
            while (people(number_document)) == '':
                number_document = input('Документа с таким номером нет. Повторите ввод: \n')
            number_shelf = input('Введите номер целевой полки на которую необходимо переместить документ: ')
            while number_shelf not in directories:
                number_shelf = input('Полки с таким номером нет. Повторите ввод: \n')
            document_move(number_document, number_shelf)
            print(f'документ с номером {number_document} перемещен на полку {number_shelf}\n')
        elif user_input == 'as':
            number_shelf = input('Введите номер новой полки: ')
            while number_shelf in directories:
                number_shelf = input('Полки с таким номером уже существует. Введите другой номер: \n')
            add_shelf(number_shelf)
            print(f'полка с номером {number_shelf} создана\n')
        elif user_input == 'quit':
            print('Выход из программы')
            break


if __name__ == '__main__':
    main()
