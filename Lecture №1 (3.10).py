# Найти среднее арифметическое трех последних элементов списка.
from random import randrange

print('Введите размерность списка:', end=' ')
numbers = [randrange(0, 100) for _ in range(int(input()))]
print('Исходный список:', numbers)
print(f'Cреднее арифметическое трех последних эл-в списка:', '{0:0.1f}'.format(sum(numbers[-3:]) / len(numbers[-3:])))
