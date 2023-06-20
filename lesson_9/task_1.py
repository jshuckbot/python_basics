import math


def input_ratio() -> tuple[float]:
    print("Введите коэффициенты для уравнения:")
    print("ax^2 + bx + c = 0:")
    a = float(input("a = "))
    b = float(input("b = "))
    c = float(input("c = "))

    return a, b, c


def finding_the_roots_of_quadratic_equation(a: int, b: int, c: int) -> str:
    discr = b ** 2 - 4 * a * c
    if discr > 0:
        x1 = (-b + math.sqrt(discr)) / (2 * a)
        x2 = (-b - math.sqrt(discr)) / (2 * a)
        return "x1 = %.2f \nx2 = %.2f" % (x1, x2)
    elif discr == 0:
        x = -b / (2 * a)
        return "x = %.2f" % x
    else:
        return "Корней нет"


if __name__ == '__main__':
    a, b, c = input_ratio()
    print(finding_the_roots_of_quadratic_equation(a, b, c))
