"""
1) Создать программно файл в текстовом формате,
записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""

with open('file1.txt', 'w') as data:
    while True:
        str = input('Введите строку: ')
        if str == '':
            break
        else:
            data.write(f'{str}\n')