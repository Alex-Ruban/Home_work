# Даны три числа a, b, c. Значение наибольшего из них присвоить переменной d.
from random import *

a, b, c = [randint(0, 100) for _ in 'abc']
print("Случайные числа:", a, b, c)
d = max(a, b, c)
print('Максимальное значение:', d)
