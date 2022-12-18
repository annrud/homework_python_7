from logger import logger


def calculator(numb1, numb2, act):
    res = None
    if act == '*':
        res = numb1 * numb2
    elif act == '/':
        res = numb1 / numb2
    elif act == '+':
        res = numb1 + numb2
    elif act == '-':
        res = numb1 - numb2
    logger(f'{numb1} {act} {numb2} = {res}')
    return res
