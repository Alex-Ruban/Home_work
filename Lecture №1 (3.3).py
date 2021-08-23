# Удалить элементы, индексы которых кратны 7.
from random import *

print('Введите размерность списка:', end=' ')
numbers = [randrange(0, 100) for _ in range(int(input()))]
print('Исходный список:', numbers)
print([numbers[i] for i in range(len(numbers)) if i == 0 or i % 7 != 0])
