# Удалить пять первых нечетных по значению элементов списка.
from random import randrange

print('Введите размерность списка:', end=' ')
numbers = [randrange(0, 100) for _ in range(int(input()))]
print('Исходный список:', numbers)

numbers_mod, counter = [], 0
for i in numbers:
    if i % 2 != 0 and counter == 5 or i % 2 == 0:
        numbers_mod.append(i)
    elif i % 2 != 0 and counter != 5:
        counter += 1

print('Нечетных чисел меньше 5, конечный список ' if counter < 5 else 'Конечный список:', numbers_mod)
