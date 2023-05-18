from random import randint

LOWER_LIMIT = 0
UPPER_LIMIT = 1000
ATTEMPTS = 10

MSG_GUESS = 'Вы угадали число'
MSG_LESS = 'Вы ввели число меньше загадонного'
MSG_MORE = 'Вы ввели число больше загадонного'
MSG_LOSE = 'Вы проиграли! кончились попытки'
MSG_INPUT_NUMBER = 'Введите загаданное число: '


def guess_number(happy_number, number) -> tuple:
    """Угадывает число"""
    if number == happy_number:
        return True, MSG_GUESS
    elif number > happy_number:
        return False, MSG_MORE
    elif number < happy_number:
        return False, MSG_LESS


def generate_number() -> int:
    return randint(LOWER_LIMIT, UPPER_LIMIT)


def run():
    """Запускает игровой цикл"""
    happy_number = generate_number()
    attempts = 10
    running = True

    while running:
        number = int(input(MSG_INPUT_NUMBER))
        is_gues, msg = guess_number(happy_number, number)
        if not is_gues:
            print(msg)
        else:
            print(msg)
            break
        
        attempts -= 1
        
        if not attempts:
            print(MSG_LOSE)
            running = False


def main():
    """Основная функция"""
    run()


if __name__ == '__main__':
    run()
