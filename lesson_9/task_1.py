import math
import random
import csv
import json


MIN_NUMBER = -500
MAX_NUMBER = 1000


def from_file_csv_numbers(filename: str):
    def decorator(func):
        def wrapper():
            with open(filename, 'r', encoding='utf-8', newline='') as csv_input:
                reader = csv.reader(csv_input)
                for i, row in enumerate(reader):
                    if i == 0:
                        continue
                    args = (int(x) for x in row)
                    yield func(*args)

        return wrapper
    return decorator


def save_to_json(filename: str):
    def decorator(func):
        json_file = []

        def wrapper(*args, **kwargs):
            for result in func(*args, **kwargs):
                if result:
                    dct = {'roots': result}

                    json_file.append(dct)
                    with open(filename, 'w', encoding='utf-8') as json_f:
                        json.dump(json_file, json_f, indent=2, ensure_ascii=False)
                else:
                    break

        return wrapper
    return decorator


@save_to_json('result.json')
@from_file_csv_numbers('result.csv')
def finding_the_roots_of_quadratic_equation(a: int, b: int, c: int) -> str:
    discr = b ** 2 - 4 * a * c
    if discr > 0 and a != 0:
        x1 = (-b + math.sqrt(discr)) / (2 * a)
        x2 = (-b - math.sqrt(discr)) / (2 * a)
        return "x1 = %.2f x2 = %.2f" % (x1, x2)
    elif discr == 0 and a != 0:
        x = -b / (2 * a)
        return "x = %.2f" % x

    return "Корней нет"


def generate_csv_with_numbers(filename: str = 'result', count_rows: int = 100):
    rows = []
    fieldnames = ['a', 'b', 'c']

    for _ in range(count_rows):
        a, b, c = random.sample(range(MIN_NUMBER, MAX_NUMBER), 3)
        rows.append({'a': a, 'b': b, 'c': c})

    with open(f'{filename}.csv', 'w', newline='', encoding='utf-8') as csv_output:
        writer = csv.DictWriter(csv_output, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


if __name__ == '__main__':
    # print(finding_the_roots_of_quadratic_equation(a, b, c))
    generate_csv_with_numbers()
    print(finding_the_roots_of_quadratic_equation())
