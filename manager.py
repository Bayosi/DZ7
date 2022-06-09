"""
5. В программе консольный файловый менеджер есть пункт "просмотр содержимого рабочей директории";
6. Добавить пункт "сохранить содержимое рабочей директории в файл";

7. При выборе этого пункта создать файл listdir.txt (если он есть то пересоздать) и сохранить туда содержимое
рабочей директории следующим образом: сначала все файлы, потом все папки, пример как может выглядеть итоговый файл.


files: victory.py, bill.py, main.py
dirs: modules, packages
"""


import os
import shutil
import sys

LIST = 'listdir.txt'

while True:
    print('1. Создать папку')
    print('2. Удалить (файл/папку)')
    print('3. Копировать (файл/папку)')
    print('4. Просмотр содержимого рабочей директории')
    print('5. Посмотреть только папки')
    print('6. Посмотреть только файлы')
    print('7. Просмотр информации об операционной системе')
    print('8. Создатель программы')
    print('9. Играть в викторину')
    print('10. Мой банковский счет')
    print('11. Смена рабочей директории (*необязательный пункт)')
    print('12. Cохранить содержимое рабочей директории в файл')
    print('13. Выход')


    choice = input('Выберите пункт: ')
    if choice == '1':
        os.mkdir(input('Введите название папки: '))

    elif choice == '2':
        os.rmdir(input('Введите название папки для удаления: '))

    elif choice == '3':
        shutil.copy(input('Введите название файла для копирования: '), input('Введите название нового файла: '))

    elif choice == '4':
        print(os.listdir())

    elif choice == '5':
        dir = 'C:/Users/Сережа/Desktop/Учеба/Python разработчик/lesson7DZ'
        contdir = []
        papki = []
        for i in os.walk(dir):
            contdir.append(i)
        papki = list(contdir[0])
        print(papki[1])

    elif choice == '6':
        print(papki[2])

    elif choice == '7':
        print(sys.platform)

    elif choice == '8':
        print('C.И.Б.')

    elif choice == '9':
        import victory

    elif choice == '10':
        import Bank

    elif choice == '11':
        os.chdir('new direct')

    elif choice == '12':
        dir = 'C:/Users/Сережа/Desktop/Учеба/Python разработчик/lessonDZ7'
        contdir = []
        papki = []
        for i in os.walk(dir):
            contdir.append(i)
        papki = list(contdir[0])
        print(papki[1])
        print(papki[2])
        with open(LIST, 'w') as f:
            f.write(f' dirs: {papki[1]} \n files: {papki[2]}')


    elif choice == '13':
        break


    else:
        print('Не верный пункт!')