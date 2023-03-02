place = int(input('Введите место: '))
if place <= 0 or place > 54:
    print('Номер места введён неверно!')
else:
    if place > 35:
        print('Ваше место: боковое')
    else:
        print('Ваше место: в купе')
    if place % 2 == 0:
        print('Ваше место: верхнее')
    else:
        print('Ваше место: нижнее')