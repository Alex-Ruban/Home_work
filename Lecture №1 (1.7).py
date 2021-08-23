# В переменную Y ввести номер года. Определить, является ли год високосным.

from random import *

yars = randrange(1, 2022)
print('Случайный год:', yars)
print('Год високосный' if yars % 4 == 0 and yars % 100 != 0 or yars % 400 == 0 else 'Год невисокосный')
