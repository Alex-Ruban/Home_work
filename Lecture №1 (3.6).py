# Удалить все элементы с заданным значением, если они имеются в списке.
from random import *

print('Введите размерность списка:', end=' ')
numbers = [randrange(0, 100) for _ in range(int(input()))]
print('Исходный список:', numbers)

print('Какое значие удалить?:', end=' ')
num_del = (int(input()))

for i in range(numbers.count(num_del)):
    numbers.remove(num_del)
print('Конечный список:', numbers)
