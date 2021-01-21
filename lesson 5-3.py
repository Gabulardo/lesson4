with open('lesson5-3.txt', 'r') as my_file:
    surname = []
    salary = []
    my_list = my_file.read().split('\n')
    for i in my_list:
        i = i.split()
        salary.append(i[1])
        if int(i[1]) < 20000:
           surname.append(i[0])
print(f'Оклад меньше 20.000 {surname}, средний оклад {sum(map(int, salary)) / len(salary)}')
