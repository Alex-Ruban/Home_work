# Найти для каждого элемента списка А сумму предыдущих элементов и записать эти суммы в новый список B.
from random import randrange

print('Введите размерность списка:', end=' ')
numbers_a = [randrange(0, 100) for _ in range(int(input()))]
print('Исходный список:', numbers_a)

numbers_b = []
for i in range(1, len(numbers_a)):
    numbers_b.append(sum(numbers_a[:i]))

print('Конечный список:', numbers_b)
