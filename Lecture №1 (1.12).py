# Есть натуральное двузначное число n. Верно ли, что среди его цифр есть 1 или 9?
from random import *

number = str(randrange(100))
print('Случайное число:', number)
print('Да верно' if ('1' or '9') in number else 'Нет неверно')
