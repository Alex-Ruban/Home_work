# Удалить элементы, индексы которых кратны 3.
from random import *

print('Введите размерность списка:', end=' ')
numbers = [randrange(0, 100) for _ in range(int(input()))]
print('Исходный список:', numbers)
numbers_mod = [numbers[i] for i in range(len(numbers)) if i == 0 or i % 3 != 0]
print('Конечный список:', numbers_mod)
