import text

def main_menu ():
    
    print(text.main_menu[0])
    for i in range (len(text.main_menu)): 
        if i:
            print(f'\t{i:>3}. {text.main_menu[i]}')
    while True:

        choice = input(text.input_main_menu)
        #проверка
        if choice .isdigit() and 0 < int(choice) < len(text.main_menu):
            return choice
        print(text.input_main_menu_error)




def print_message(msg: str):
    print('\n' + '='*len(msg))
    print(msg)
    print('='*len(msg) + '\n')

def show_contacts(book: dict, msg: str):
    if book:
        print('\n' + '='* 66)
        for u_id, contact in book.items():
            print(f'{u_id:>3} {contact[0]:<20} {contact[1]:<20} {contact[2]:<20}')
        print('='*66 + '\n')
    else:
        print_message(msg)

def input_new_contact(msg: list)->list[str, str, str]:
    contact = []
    for field in msg:
        contact.append(input(field))
    return contact

def input_info(msg: str):
    return input(msg)
