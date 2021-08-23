# Для каждого четного по номеру элемента списка A найти его сумму со следующим элементом
# и записать эти суммы в новый список B.
from random import *

print('Введите размерность списка:', end=' ')
numbers = [randrange(0, 100) for _ in range(int(input()))]
print('Исходный список:', numbers)
b = [numbers[i] + numbers[i + 1] for i in range(len(numbers)) if i % 2 == 0]
print('Сумма четного элемента со следующим:', b)