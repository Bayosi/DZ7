"""
1. В подпрограмме Мой банковский счет;
2. Добавить сохранение суммы счета в файл.

При первом открытии программы на счету 0
После того как мы воспользовались программой и вышли сохранить сумму счета
При следующем открытии программы прочитать сумму счета, которую сохранили
...
3. Добавить сохранение истории покупок в файл

При первом открытии программы истории нет.
После того как мы что нибудь купили и закрыли программу сохранить историю покупок.
При следующем открытии программы прочитать историю и новые покупки уже добавлять к ней;
...
4. Формат сохранения количество файлов и способ можно выбрать самостоятельно.
"""

import os

balans = 0
items = []
orders = []

FILE = 'balans.txt'
ITEM = 'items.txt'

if os.path.exists(ITEM):
    with open(ITEM, 'r') as f:
        for item in f:
            items.append(item.replace('\n', ''))

while True:
    print('1. пополнение счета')
    print('2. покупка')
    print('3. история покупок')
    print('4. выход')

    choice = input('Выберите пункт меню: ')
    if choice == '1':
        money = int(input('Введите сумму пополнения: '))
        balans += money
        print(f'Баланс: , {balans}')
        orders.append(balans)


        print()

    elif choice == '2':
        buy = int(input('Введите сумму покупки: '))
        if buy > money:
            print('Денег не достаточно!')
        else:
            balans -= buy
            item = input('Введите название покупки: ')
            items.append((item, buy))
            print(balans)
            with open(FILE, 'w') as f:
                f.write(f'{balans}')
            with open(ITEM, 'w') as f:
                for i in items:
                    f.write(f'{i}\n')

    elif choice == '3':
        print('История покупок :', *items, sep='\n')



    elif choice == '4':
        break