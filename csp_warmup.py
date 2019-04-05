from utils import print_title
import numpy as np


def start():
    print_title('CSP WARM-UP: start')

    print_title('CSP WARM-UP: init square with size 5')
    square = init_square(4)
    print(square)

    print_title('CSP WARM-UP: set possible values')
    possible_values = {1, 2, 3, 4, 5}
    print(possible_values)

    print_title('CSP WARM-UP: fill square non repeatedly')
    square_filled = fill_square_non_repeatedly(square, possible_values)
    print(square_filled)

    print_title('CSP WARM-UP: end')


def init_square(size):
    square = np.zeros((size, size), dtype=np.int16)

    return square


def fill_square_non_repeatedly(square, possible_vals):
    for row in range(0, square.shape[0]):
        for col in range(0, square.shape[1]):
            if square[row, col] == 0:
                # print(square[row, col])
                # Create possible values in row and subtract from full set
                possible_vals_in_row = possible_vals - set(square[row])
                # print(possible_vals_in_row)
                # Create possible values in column and subtract
                possible_vals_in_col = possible_vals_in_row - set(square[:, col])
                # print(possible_vals_in_col)
                square[row, col] = possible_vals_in_col.pop()

    return square

