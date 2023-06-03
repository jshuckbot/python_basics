def return_kwargs(**kwargs):
    return {v: k for k, v in kwargs.items()}


if __name__ == '__main__':
    try:
        print(return_kwargs(a=3, d=5))
    except TypeError:
        print('Вы ввели позиционный аргумент, а нужно именнованный')