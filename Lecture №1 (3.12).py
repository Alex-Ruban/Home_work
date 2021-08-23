# Найти номер минимального элемента списка.
from random import randrange

print('Введите размерность списка:', end=' ')
numbers = [randrange(0, 100) for _ in range(int(input()))]
print('Исходный список:', numbers)

print(numbers.index(min(numbers)))