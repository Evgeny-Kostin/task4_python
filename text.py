main_menu = ['\nГлавное меню',
             'Открыть файл',
             'Сохранить файл',
             'Показать все контакты',
             'Создать контакт',
             'Найти контакт',
             'Изменить контакт',
             'Удалить контакт',
             'Выход\n']

input_main_menu = 'Выберите пункт меню: '
input_main_menu_error = f'Выберите пункт меню! Цифры от 1 до {len(main_menu)-1}'

open_successful = 'Телефонная книга успешно открыта!'
save_successful = 'Телефонная книга успешно сохранена!'
empty_phone_book_error = 'Телефонная клига пуста или не открыта!'

input_new_contact = ['Введите имя контакта: ', 'Введите телефон контакта: ', 'Введите комментарий: ']
input_edit_contact = ['Введите имя контакта или Enter (оставить без изменений): ', 
                      'Введите телефон контакта или Enter (оставить без изменений): ', 
                      'Введите комментарий или Enter (оставить без изменений): ']

input_search_word = 'Введите ключевое слово для поиска: '
input_edt_word = 'Введите ключевое слово для поиска контакта, который хотите изменить: '
input_delete_word = 'Введите ключевое слово для поиска контакта, который хотите удалить: '

input_edt_id = 'Введите ID контакта, который хотите изменить: '
input_delete_id = 'Введите ID контакта, который хотите удалить: '


contact_actions = ['сохранен', 'изменен', 'удален']

good_bay = 'До свидания, до новых встреч!'

def contact_successful_result(name: str, mode:int)->str:
    return f'Контакт {name} успешно {contact_actions [mode]}'

def search_contact_error(word: str) -> str:
    return f'Контакты содержащие {word} не найдены!'

