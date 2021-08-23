# Определить, имеется ли среди трёх чисел a, b и c хотя бы одна пара равных между собой чисел.

from random import *

a, b, c = [randint(0, 7) for _ in 'abc']
print('YES' if a == b | a == c | b == c else 'NO')
