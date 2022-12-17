import sys
from calculator import calculator
sys.path.append('./user_interface')

from user_interface.input_complex import input_for_complex
from user_interface.input_fractions import input_for_fractions
from user_interface.introduction import choice_calc


if __name__ == '__main__':
    if choice_calc() == 'c':
        number1, number2, act = input_for_complex()
        print(f'Результат: {calculator(number1, number2, act)}')

    else:
        number1, number2, act = input_for_fractions()
        print(f'Результат: {calculator(number1, number2, act)}')
