phone_book = {}
path = 'phones.txt'

def open_file():
    with open(path, 'r', encoding='UTF-8') as file:
        contacts = file.readlines()
    for i, contact in enumerate(contacts, 1):
        phone_book[i] = contact.strip().split(';')
    #print(phone_book) # но можно раскрыть и каждый новый контакт выводился бы с новой строки.
    #print(**phone_book, sep='\n') но тогда элементы должны быть сторокой == 
    # выше [str(i)] не пошло...

def save_file():
    data = []
    for contact in phone_book.values():
        contact = ';'.join(contact)
        data.append(contact)
    data = '\n'.join(data)    
    with open(path, 'w', encoding='UTF-8') as file:
        file.write(data)    
        

def show_contacts(pb: dict):
    print()
    for i, contact in pb. items(): #проходим циклом по ключам i полученным от enumerate и по значениям. контакт - список имя тел комментарий уже разделенный
        print(f'{i:>3}. {contact[0]:<20} {contact[1]:<20} {contact[2]:<20}') # f строка проходим по ID выделяем 3 ячейки равняем по правому краю
                                       # контакт[0]-имя, равняем по левому краю выделяем 20 ячеек, контакт[1]-телефон, контакт [2] - комментарий
    print()

def new_contact():
    name = input('Введите имя контакта: ')
    phone = input('Введите телефон: ')
    comment = input('Введите комментарий: ')
    u_id = max(phone_book.keys()) + 1 #u_id user id берем тел книгу и вычисляем максимальный ключ, увеличиваем его на единицу, т.е. добавляем берем следующий.
    phone_book[u_id] = [name, phone, comment] # в тел книгу добавляем новый id
    return name

def find_contact():
    result = {}
    word = input('Введите ключевое слово для поиска: ').lower() #перевод в нижний регистр чтобы не влияло на поиск
    for i, contacts in phone_book.items(): # ищем по ключам и значениям все совпадения
        if word in ''.join(contacts).lower(): # здесь также в нижний иначе поиск не получися # из списка делаем строку но не меняем ничего внутри, а берем текущ контакт и склеивам
            # для того чтобы в не запускать очередной раз цикл. Если ключ слово найдем в склеенном контакте
            # и если есть добавляем по id в контакт, но не склеиваем, склейка только для поиска.
            result[i] = contacts
    return result        

def edit_contact():
    result = find_contact()
    show_contacts(result)
    u_id = int(input('Введите ID контакта котрый хотите изменить: '))
    c_name, c_phone, c_comment = phone_book[u_id] # получаем от поль ID к/й нужно изм. раскрываем его и получаем текущ имя, текущ телефон и комментарий.
    # затем вводим новые
    name = input('Введите новое имя контакта: ')
    phone = input('Введите новый телефон: ')
    comment = input('Введите новый комментарий: ')
    phone_book[u_id] = [name if name else c_name, phone if phone else c_phone, 
                        comment if comment else c_comment] # тернарный оператор если есть имя тел или соммент то запишем если нет вернем старый


def del_contact():
    result = find_contact()
    show_contacts(result)
    u_id = int(input('Введите ID контакта котрый хотите удалить: '))
    name = phone_book.pop(u_id)
    return name[0]








menu = '''Главное меню
    1. Открыть файл
    2. Сохранить файл
    3. Показать все контакты
    4. Создать контакт
    5. Найти контакт
    6. Изменить контакт
    7. Удалить контакт
    8. Выход'''

while True:
    print(menu)
    choice = input('Выберите пункт меню: ')
    match choice:
        case '1':
            open_file()
            print('\nТелефонная книга успешно загружена!\n')
        case '2':
            save_file()
            print('\nТелефонная книга успешно сохранена!\n')
        case '3':
            show_contacts(phone_book) # печатаетс вся тел книга
        case '4':
            name= new_contact()
            print(f'\nКонтакт {name} удачно создан\n')
        case '5':
            result = find_contact()
            show_contacts(result) # печатается только результат
        case '6':
            name = edit_contact()
            print(f'Контакт {name} успешно изменен.')
        case '7':
            name = del_contact()
            print(f'Контакт {name} успешно удален.')
        case '8':
            print('До свидания, всего хорошего!')
            break
        case _:
            print('Ошибка ввода! Выберите пункт меню от 1 до 8')