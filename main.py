# 1. Показывать все контакты!
# 2. Добавлять контакт!
# 3. Найти контакт!
# 4. Изменять контакт!
# 5. Удалить конаткт

#Имя Номер Коммент
from prettytable import PrettyTable
import sys


PATH = 'phone_numbers.txt'

def start_menu():
    global my_dict
    quest = """Выберите нужный пункт меню: 
 1. Показывать все контакты
 2. Добавлять контакт
 3. Найти контакт
 4. Изменять контакт
 5. Удалить контакт
 6. Сохранить изменения
 7. Выход из программы\n"""

    while True:
        menu_item = questions(quest)
        match menu_item:
            case 1:
                show_all(my_dict)
            case 2:
                add_contact()
            case 3:
                find_contact()
            case 4:
                change_contact()
            case 5:
                del_contacts()
            case 6:
                save_contacts()
            case 7:
                quit()

def questions(quest: str):
    while True:
        try:
            menu_item = int(input(quest))
            return menu_item
        except ValueError:
            print("Вы ввели неверное значение. Выберите пункт из меню")
            next

def show_all(my_dict):
    table = PrettyTable()
    columns = ['№'] + list(my_dict[0].keys())
    table.field_names = columns
    rows = [list(row.values()) for row in my_dict]
    for row in range(len(rows)):
        table.add_row([row+1]+ rows[row])
    print(table)

def add_contact():
    global my_dict
    name=input("Введите имя:\n").title()
    phone=input("Введите номер телефона:\n")
    comment=input("Введите комментарий:\n").title()
    my_dict.append({'Имя':name, 'Телефон':phone, 'Комментарий':comment})
    message = f'Контакт с именем {name} успешно добавлен'
    print('-'* len(message))
    print(message)
    print('-'* len(message))
    

def find_contact() -> list:
    global my_dict
    search_word=input("Введите текст для поиска контакта:\n").lower()
    result = []
    return_result=[]
    for item in range(len(my_dict)):
        for i in my_dict[item].values():
            if search_word in i.lower():
                result.append(my_dict[item])
                return_result.append(item)
    if result:
        show_all(result)
    else:
        print(f'Контактов содержащих "{search_word}" не найдено')
    return return_result

def change_contact():
    global my_dict
#    fields=list(my_dict[0].keys())
    finder = find_contact()
    if finder:
        answer = questions("Какую из найденых записей нужно изменить?\n")
        if answer > 0 and answer <= len(finder):
            index = finder[answer-1]
        temp_dict = my_dict[index].copy()
        for key in temp_dict.keys():
            new_value = input(f'Введите новое значение поля "{key}" Или Enter для пропуска\n')
            if new_value:
                temp_dict[key] = new_value
        show_all([temp_dict])
        quest = '''Сохранить выбранные изменения?
1. Да
2. Нет
'''
        save_or_not = questions(quest)
        match save_or_not:
            case 1:
                my_dict[index] = temp_dict

def del_contacts():
    global my_dict
    to_del = find_contact()
    if to_del:
        answer = questions("Какую из найденых записей нужно удалить?\n")
        if answer != 0:
            result = [my_dict.pop(to_del[answer-1])]
            print(f"Контакт указанный ниже удален")
            show_all(result)
        save_contacts()

def quit():
    global my_dict
    global PATH
    if my_dict != open_phonebook(PATH):
        quest = ''' Сохранить изменения?
1. Да
2. Нет
'''     
        answer = questions(quest)
        if answer == 1:
            save_contacts()
            print("Телефонная книга обновлена")
    sys.exit()

def save_contacts():
    global my_dict
    with open('phone_numbers.txt', 'w') as file:
        for i in my_dict:
            file.write(f'{i["Имя"]};{i["Телефон"]};{i["Комментарий"]}\n')


def open_phonebook(path):
    my_dict = []
    with open('phone_numbers.txt','r') as file:
        for i in file:
            my_list=i.split(';')
            my_dict.append({'Имя': my_list[0].strip(),
                            'Телефон': my_list[1].strip(),
                            'Комментарий': my_list[2].strip()})
    return my_dict

my_dict = open_phonebook(PATH)



if __name__ == '__main__':
    start_menu()