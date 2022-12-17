def choice_calc():
    print('Программа "калькулятор для рациональных и компллексных чисел"')
    while True:
        print('Выберите калькулятор:')
        calc = input(
            'Если расчёт рациональных чисел, то введите "f", '
            'если комплексных чисел, то введите "c": ').lower()
        if calc == 'c' or calc == 'f':
            break
        else:
            print('Неверный ввод!')
    return calc


def get_number(func, title):
    while True:
        number = input(f'Введите {title}: ')
        try:
            number = func(number)
            break
        except ValueError:
            print('Неверно введено число!')
            continue
    return number


def get_operation():
    while True:
        operation = input(
            'Введите арифметический оперетор ("+", "-", "*", "/"): '
        )
        if operation not in ["+", "-", "*", "/"]:
            print('Неверно введен оператор!')
            continue
        break
    return operation
