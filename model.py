import csv
# Добавление контактов в список
def add (datasave):
    file = 'Phonebook.csv'
    with open (file, 'a', encoding = 'utf-8') as data:
        data.write(f'{datasave}\n')



# Поиск по имени 
def search (name):
    with open("Phonebook.csv", newline = '') as csvfile:
        reader = csv.DictReader(csvfile,delimiter=";")
        for row in reader:
            if row['First name'] == name or row['Last name'] == name:
                print(row['First name'],'|',row['Last name'],'|',row['Phone number'])

