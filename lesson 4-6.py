#from itertools import count
#
#a = int(input('Введите стартовое число: '))
#for el in count(a):
#    if el > a + 10:
#        break
#    else:
#        print(el)

from itertools import cycle

c = 0
my_list = [13, 'Ford', 12, True]
for el in cycle(my_list):
    if c > 11:
        break
    print(el)
    c += 1