START_SIDE = 1
END_SIDE = 4

TEXT = {
    'not exist': 'Такого треугольника не существует',
    'equilateral': 'Треугольник равносторонний',
    'isosceles': 'Треугольник равнобедренный',
    'versatile': 'Треугольник разносторонний',
    'value_error': 'Вы ввели не корректные данные. Попробуйте еще!',
    'input_side': 'Введите %d сторону треугольника: ',
}


def input_sides_triangle() -> list[int]:
    """Вводит сторони треугольника"""
    sides = []
    for i in range(START_SIDE, END_SIDE):
        try:
            side = int(input(TEXT['input_side'] % i))
        except ValueError:
            print(TEXT['value_error'])
            return input_sides_triangle()
        else:
            sides.append(side)

    return sides


def check_triangle(sides) -> str:
    """Проверяет треугольник"""
    sides.sort()
    if not is_triangle(sides):
        return TEXT['not exist']

    sides = set(sides)

    match len(sides):
        case 1:
            return TEXT['equilateral']
        case 2:
            return TEXT['isosceles']
        case 3:
            return TEXT['versatile']


def is_triangle(sides) -> bool:
    """Проверяет стороны """
    return True if sum(sides[:2]) > sides[-1] else False


def main() -> None:
    """Основная функция"""
    sides = input_sides_triangle()
    msg = check_triangle(sides)
    print(msg)


if __name__ == '__main__':
    main()
