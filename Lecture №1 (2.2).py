# Торговая фирма в первый день работы реализовала товаров на P тыс. руб., а затем ежедневно
# увеличивала выручку на 3%. Какой будет выручка фирмы в тот день, когда она впервые превысит
# заданное значение Q? Сколько дней придется торговать фирме для достижения этого результата?

from random import *

p = (randrange(1, 10))
print('Выручка в первый день:', '${0:5.3f}'.format(p))
q = randrange(100, 1000)
print('Ожидаемое значение:', '${0:4.3f}'.format(q))
count = 1
while p < q:
    p += p * 0.03
    count += 1

print('Необходимое количество дней:', count)
