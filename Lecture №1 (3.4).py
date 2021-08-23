# Найти значение минимального элемента списка.
from random import *

print('Введите размерность списка:', end=' ')
numbers = [randrange(0, 100) for _ in range(int(input()))]
print('Исходный список:', numbers)
print('Минимальное значение:', min(numbers))
