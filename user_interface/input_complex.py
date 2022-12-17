from introduction import get_number, get_operation


def input_for_complex():
    print('Вы выбрали расчёт комплексных чисел')
    numb1 = get_number(complex, 'первое число вида -2.5+5j')
    numb2 = get_number(complex, 'второе число вида -2.5+5j')
    operation = get_operation()
    return numb1, numb2, operation
