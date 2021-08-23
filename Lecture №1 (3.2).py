# Все четные по значению элементы исходного списка A поместить в новый список B.
from random import *

print('Введите размерность списка:', end=' ')
numbers = [randrange(0, 100) for _ in range(int(input()))]
print('Исходный список:', numbers)
b = [i for i in numbers if i % 2 == 0]
print('Новый список:', b)