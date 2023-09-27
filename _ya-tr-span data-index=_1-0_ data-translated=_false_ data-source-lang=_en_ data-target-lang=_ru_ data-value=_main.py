import random

x = random.randint(1, 10)
print('Старт!')

while True:
    print(f'Число x: {x}')
    print('1 ) x/6 - x/7')
    print('2 ) x**2 - 5*x + 3')
    print('3 ) x*2 - 25')
    print('0 ) Выход')
    i = int(input('Введите 1, 2, 3: '))
    if i == 1:
        x = x/6 - x/7
        if x == 0:
            print('GAME OVER')
            break
    elif i == 2:
        x = x**2 - 5*x + 3
        if x == 0:
            print('GAME OVER')
            break
    elif i == 3:
        x = x*2 - 25
        if x == 0:
            print('GAME OVER')
            break
    elif i == 0:
        print('GAME OVER')
        break
    else:
        print('Некорректный ввод')