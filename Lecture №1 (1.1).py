# Ввести три числа m, n, p. Подсчитать количество отрицательных чисел.
from random import *

count = 0
m, n, p = [randint(-99, 100) for _ in 'mnp']
for i in m, n, p:
    if i < 0:
        count += 1
print(count)
