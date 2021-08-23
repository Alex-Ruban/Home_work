# Дано натуральное четырехзначное число n. Верно ли, что все его цифры различны?

from random import *

count = 0
number = str(randrange(1000, 10000))
print('Случайное четырехзначное число:', number)
for i in number:
    count += number.count(i)

print('Да верно, все его цифры различны.' if count == 4 else 'Нет неверно')
