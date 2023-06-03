def return_kwargs(**kwargs):
    tmp_dict = {}

    for key, value in kwargs.items():
        try:
            hash(key)
            tmp_dict[value] = key
        except TypeError:
            tmp_dict[str(value)] = key

    return tmp_dict


if __name__ == '__main__':
    try:
        print(return_kwargs(a=[1, 2, 3], d=5))
    except TypeError:
        print('Вы ввели позиционный аргумент, а нужно именнованный')