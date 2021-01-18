my_f = open('text.txt', 'w')
line = input('Введите произвольный текст: ')
while line:
    my_f.writelines(line)
    line = input('Введите произвольный текст: ')
    if not line:
        break
my_f.close()
with open('text.txt') as my_f:
    content = my_f.readlines()
    print(content)
