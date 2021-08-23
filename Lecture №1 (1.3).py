'''' Даны три числа a, b и c. Найти среднее геометрическое этих чисел, если все они отличны от нуля,
 и среднее арифметическое в противном случае.'''
from statistics import geometric_mean
from random import *

a, b, c = [randint(0, 10) for _ in 'abc']
print("Случайные числа:", a, b, c)
if a * b * c != 0:
    print('Cреднее геометрическое:', geometric_mean([a, b, c]))
else:
    print('Cреднее арифметическое', sum([a, b, c]) / len('abc'))
