# Число делится на 3 тогда, когда сумма его цифр делится на 3.
# Проверить этот признак на примере заданного трехзначного числа.

from random import *

flag = True
while flag:
    num = (randrange(100, 1000))
    if num % 3 == 0:
        flag = False
numbers = [int(i) for i in str(num)]

print('Случайное число:', num)
print('Утверждение верно' if sum(numbers) % 3 == 0 else 'Утверждение неверно')
