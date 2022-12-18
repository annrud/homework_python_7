from datetime import datetime as dt


def logger(data):
    time = dt.now().strftime('%m.%d.%Y %H:%M')
    with open('result.txt', 'a') as f:
        f.write(f'{time} {data}\n')
    
