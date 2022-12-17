from fractions import Fraction

from introduction import get_number, get_operation


def input_for_fractions():
    print('Вы выбрали расчёт рациональных чисел')
    numb1 = get_number(Fraction, 'первое число вида 5.73 или дробь, например, 3/7')
    numb2 = get_number(Fraction, 'второе число вида 5.73 или дробь, например, 3/7')
    operation = get_operation()
    return numb1, numb2, operation



