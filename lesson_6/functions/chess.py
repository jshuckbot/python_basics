NUMBER_OF_CELLS = 8


def input_coordinate_cells():
    cells = []

    for _ in range(NUMBER_OF_CELLS):
        coordinate = [int(cell) for cell in input().split()]
        cells.append(coordinate)

    return cells


def check_coordinate_cells(cells):
    is_correct = True
    for i in range(NUMBER_OF_CELLS):
        x1, y1 = cells[i]
        for j in range(i + 1, NUMBER_OF_CELLS):
            x2, y2 = cells[j]
            if x1 == x2 or y1 == y2 or abs(x1 - x2) == abs(y1 - y2):
                is_correct = False

    return True if is_correct else False


if __name__ == '__main__':
    cells = input_coordinate_cells()
    print(check_coordinate_cells(cells))
