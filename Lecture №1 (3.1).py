# Удалить элемент с введенным номером a
from random import *
print('Введите размерность списка:', end=' ')
numbers = [randrange(0, 100) for _ in range(int(input()))]
print(numbers)
print(f'Какой элемент от 1 до {len(numbers)} удалить из списка?:', end=' ')
del numbers[int(input()) - 1]
print(numbers)