''' По номеру месяца напечатать пору года.'''
from random import *

num = randint(1, 12)
print('Случайный месяц:', num)
season = [['Лето', 6, 7, 8], ['Осень', 9, 10, 11], ['Зима', 12, 1, 2], ['Весна', 3, 4, 5]]
for i in season:
    if num in i:
        print('Пора года:', i[0])
