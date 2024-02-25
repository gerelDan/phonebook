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

print("""Выберите нужный пункт меню: 
1. Показывать все контакты
2. Добавлять контакт
3. Найти контакт
4. Изменять контакт
5. Удалить контакт
6. Выход из программы""")

while True:
    try:
        menu_item=int(input())-1
        break
    except ValueError:
        print("Вы ввели неверное значение. Выберите пункт из меню")
        next
    menu

def show_all(my_dict):
    table = PrettyTable()
    columns = ['№'] + list(my_dict[0].keys())
    table.field_names = columns
    rows = [list(row.values()) for row in my_dict]
    for row in range(len(rows)):
        table.add_row([row+1]+ rows[row])
    print(table)

def add_contact(my_dict):
    name=input("Введите имя:\n").lower()
    phone=input("Введите номер телефона:\n").lower()
    comment=input("Введите комментарий:\n").lower()
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

def change_contact(my_dict,index):
    fields=list(my_dict[0].keys())
    
    temp_dict=my_dict[index]
    to_change=int(input("В какое поле вносим изменения: 1. Имя 2. Телефон 3. Комментарий?"))
    new_value=input("Введите новое значение поля")
    temp_dict[fields[to_change-1]]=new_value
    my_dict[index]=temp_dict
    with open('phone_numbers.txt', 'w') as file:
        for i in my_dict:
            file.write(f'{i["Имя"]} {i["Телефон"]} {i["Комментарий"]}\n')

def del_contacts(my_dict):
    to_del = find_contact(my_dict)
    while True:
        try:
            answer = int(input("Какую из найденых записей нужно удалить?\n"))
            break
        except ValueError:
            print("Нужно ввести номер по порядку")
            next
    if answer != 0:
        result = [my_dict.pop(to_del[answer-1])]
        print(f"Контакт указанный ниже удален")
        show_all(result)


#show_all(my_dict)
#add_contact(my_dict)
show_all(my_dict)
#find_contact(my_dict)
#change_contact(my_dict,1)
#show_all(my_dict)
del_contacts(my_dict)
show_all(my_dict)