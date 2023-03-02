year = int(input('Введите год: '))
a = 0
if year <= 0:
    print('Значение года введено неверно!')
else:
    if year % 4 == 0 and year % 100 != 0:
        a = 1
    elif year % 400 == 0:
        a = 1
    if a == 1:
        print('Год ', year, ' - високосный')
    else:
        print('Этот год не високосный')
