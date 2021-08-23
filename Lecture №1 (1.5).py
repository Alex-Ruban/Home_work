'''	Определить, есть ли среди заданных целых чисел A, B, C, D хотя бы одно нечётное.'''
from random import *

a, b, c, d = [randint(0, 100) for _ in 'abcd']
print("Случайные числа:", a, b, c, d)
for i in a, b, c, d:
    if i % 2 != 0:
        print('Нечетное число:', i)
        break

else:
    print('Нечетных чисел нет.')
