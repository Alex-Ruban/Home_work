# Найти номера минимального и максимального элементов первой половины списка.
from random import *

print('Введите размерность списка:', end=' ')
numbers = [randrange(0, 100) for _ in range(int(input()))]
print('Исходный список:', numbers)

print('Минимальный элемент:', min(numbers[0:(len(numbers) // 2)]))
print('Максимальный элемент:', max(numbers[0:(len(numbers) // 2)]))
