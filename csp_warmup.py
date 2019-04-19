from utils import print_title
import numpy as np


possible_values_size = 5


def start():
    print_title('CSP WARM-UP: start')

    print_title('CSP WARM-UP: init square with size 5')
    square = init_square(12)
    print(square)

    print_title('CSP WARM-UP: set possible values')
    possible_values = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}
    print(possible_values)

    print_title('CSP WARM-UP: fill square non repeatedly')
    is_filled, square_filled = fill_square_non_repeatedly_backtracked(square, possible_values, False)
    print(square_filled)

    # print_latin(7)

    print_title('CSP WARM-UP: end')


def init_square(size):
    square = np.zeros((size, size), dtype=np.int16)

    return square


def fill_square_non_repeatedly_backtracked(square, possible_vals, is_recursive):
    if len(possible_vals) == 0:
        return True, square

    for col in range(0, square.shape[0]):
        for row in range(0, square.shape[1]):
            if square[row, col] == 0:
                is_possible, possible_vals_in_row_and_col = is_possible_assignment(square, possible_vals, row, col)
                if is_possible:
                    is_filled = False
                    square_part_filled = square
                    for val in possible_vals_in_row_and_col:
                        # val = possible_vals_in_row_and_col.pop()
                        square[row, col] = val

                        possible_vals_next = possible_vals.copy()

                        possible_vals_next.remove(val)
                        is_filled, square_part_filled = fill_square_non_repeatedly_backtracked(square, possible_vals_next, True)

                        if is_filled:
                            break
                    if is_filled:
                        square = square_part_filled
                        if is_recursive:
                            return True, square
                    else:
                        square[row, col] = 0
                        return False, square
                else:
                    return False, square

    return False, square


def is_possible_assignment(square, possible_vals, row, col):
    possible_vals_in_row = possible_vals - set(square[row])
    possible_vals_in_row_and_col = possible_vals_in_row - set(square[:, col])
    return bool(possible_vals_in_row_and_col), possible_vals_in_row_and_col

