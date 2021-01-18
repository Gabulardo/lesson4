def my_sum():
    try:
        with open('lesson5-5.txt', 'w+') as file_obj:
            line = input('Введите цифры через пробел \n')
            file_obj.writelines(line)
            my_numb = line.split()
            print(sum(map(int, my_numb)))
    except IOError:
        print('Ошибка')
    except ValueError:
        print('Ошибка ввода-вывода: необходимо было ввести цифры.')
my_sum()