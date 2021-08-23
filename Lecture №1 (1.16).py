# По введенному числу (от 0 до 7) напечатать название цифры.
from random import randrange

numbers_txt = ('Ноль', 'Один', 'Два', 'Три', 'Четыре', 'Пять', 'Шесть', 'Семь')
num = randrange(0, 8)
print(num)
print(numbers_txt[num])
