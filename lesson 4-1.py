#def func_wage():
#    try:
#        time = float(input('Введите выработку в часах: '))
#        salary = int(input('Введите ставку в руб.: '))
#        bonus = int(input('Введите премию в руб.: '))
#        res = time * salary + bonus
#        print(f'Заработная плата составляет: {res}')
#    except ValueError:
#        return print('Некорректный ввод')
#func_wage()

from sys import argv

script_name, time, money, bonus = argv
try:
    time = int(time)
    money = int(money)
    bonus = int(bonus)
    res = time * money + bonus
    print(f'Заработная плата сотрудника {res}')
except ValueError:
    print('Некорректный ввод!')