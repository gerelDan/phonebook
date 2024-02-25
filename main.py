# 1. Показывать все контакты!
# 2. Добавлять контакт!
# 3. Найти контакт!
# 4. Изменять контакт!
# 5. Удалить конаткт

#Имя Номер Коммент
from prettytable import PrettyTable

my_dict = []
with open('phone_numbers.txt','r') as file:
    for i in file:
        my_list=i.split()
        my_dict.append({'Имя':my_list[0], 'Телефон':my_list[1], 'Комментарий':my_list[2]})

print(my_dict)

quest = """Выберите нужный пункт меню: 
 1. Показывать все контакты
 2. Добавлять контакт
 3. Найти контакт
 4. Изменять контакт
 5. Удалить контакт
 6. Выход из программы\n"""
 
# print("""Выберите нужный пункт меню: 
# 1. Показывать все контакты
# 2. Добавлять контакт
# 3. Найти контакт
# 4. Изменять контакт
# 5. Удалить контакт
# 6. Выход из программы""")

def questions(quest: str):
    while True:
        try:
            menu_item = int(input(quest)) - 1
            return menu_item
        except ValueError:
            print("Вы ввели неверное значение. Выберите пункт из меню")
            next

menu_item = questions(quest)
# while True:
#     try:
#         menu_item=int(input())-1
#         break
#     except ValueError:
#         print("Вы ввели неверное значение. Выберите пункт из меню")
#         next


def show_all(my_dict):
    table = PrettyTable()
    columns = ['№'] + list(my_dict[0].keys())
    table.field_names = columns
    rows = [list(row.values()) for row in my_dict]
    for row in range(len(rows)):
        table.add_row([row+1]+ rows[row])
    print(table)

def add_contact(my_dict):
    name=input("Введите имя:\n").title()
    phone=input("Введите номер телефона:\n").title()
    comment=input("Введите комментарий:\n").title()
    new_string=f'{name} {phone} {comment}'
    my_dict.append({'Имя':name, 'Телефон':phone, 'Комментарий':comment})
    with open('phone_numbers.txt', 'a+') as file:
        file.write(new_string)

def find_contact(my_dict):
    search_word=input("Введите текст для поиска контакта:\n")
    result = []
    return_result=[]
    for item in range(len(my_dict)):
        for i in my_dict[item].values():
            if search_word in i:
                result.append(my_dict[item])
                print(my_dict[item])
                return_result.append(item)
    show_all(result)
    return return_result

def change_contact(my_dict):
    fields=list(my_dict[0].keys())
    finder = find_contact(my_dict)
    answer = questions("Какую из найденых записей нужно изменить?\n")
    if answer != 0:
        index = finder[answer - 1]

    quest_to_change = '''В какое поле вносим изменения:
1. Имя
2. Телефон
3. Комментарий\n'''
    to_change = questions(quest_to_change)
    new_value=input("Введите новое значение поля\n")
    my_dict[index][fields[to_change-1]] = new_value.title()
    with open('phone_numbers.txt', 'w') as file:
        for i in my_dict:
            file.write(f'{i["Имя"]} {i["Телефон"]} {i["Комментарий"]}\n')

def del_contacts(my_dict):
    to_del = find_contact(my_dict)
    answer = questions("Какую из найденых записей нужно удалить?\n")
    if answer != 0:
        result = [my_dict.pop(to_del[answer-1])]
        print(f"Контакт указанный ниже удален")
        show_all(result)
    with open('phone_numbers.txt', 'w') as file:
        for i in my_dict:
            file.write(f'{i["Имя"]} {i["Телефон"]} {i["Комментарий"]}\n')


#show_all(my_dict)
#add_contact(my_dict)
show_all(my_dict)
#find_contact(my_dict)
#change_contact(my_dict)
#show_all(my_dict)
del_contacts(my_dict)
show_all(my_dict)