
from datetime import datetime
def write_into_file():
    print('Выберете вариант обращения в справочник: \n 1 - Запись новых данных \n 2 - Поиск  ')
    key = str(f'Запись от:{datetime.now().date()}')
    while True:
        option=int(input())
        if option<1 or option > 2:
            print("Попробуйте еще раз, такого варианта нет")
        else:
            break 
    if option == 2:
        name_or_last = input("Введите имя или фамилию человека, которого хотите найти : ")
        return name_or_last 

    elif option == 1:
        name = input("Введите имя человека, которого хотите добавить : ")
        surname = input("Введите фамилию человека, которого хотите добавить : ") 
        phone_number = input("Введите номер телефона человека, которого хотите добавить : ") 
        print("Человек добавлен!") 
        return (f'{name};{surname};{phone_number};{key}')

      


