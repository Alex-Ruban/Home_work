# Найти индексы первого и последнего нулевых элементов списка.
from random import randrange

print('Введите размерность списка:', end=' ')
numbers_a = [randrange(0, 10) for _ in range(int(input()))]
print('Исходный список:', numbers_a)

numbers_b = [i for i in range(len(numbers_a)) if numbers_a[i] == 0]
print(len(numbers_b))
print('Нулевых элементов в списке нет' if len(numbers_b) == 0 else (numbers_b[0], numbers_b[-1]))





