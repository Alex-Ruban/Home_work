# Удалить из списка все элементы, совпадающие с его минимальным значением.
from random import randrange

print('Введите размерность списка:', end=' ')
numbers = [randrange(0, 100) for _ in range(int(input()))]
print('Исходный список:', numbers)

print(f'Минимальное значение списка: {min(numbers)}')

for i in range(numbers.count(min(numbers))):
    numbers.remove(min(numbers))
print('Конечный список:', numbers)
