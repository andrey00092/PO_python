# TODO решите задачу
import json


def task() -> float:
    with open('input.json') as f:
        data = json.load(f)

    summ = 0

    for i in range(0, len(data)):
        res = data[i]['score'] * data[i]['weight']
        summ = summ + res

    return float(format(summ, '.4f'))

print(task())
