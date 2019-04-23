from utils import print_title
import numpy as np
import time


possible_values_size = 5


def start():
    print_title('CSP WARM-UP: start')

    print_title('CSP WARM-UP: init square with size 5')
    # square = init_square(12)
    square = init_square(4)
    print(square)

    print_title('CSP WARM-UP: set possible values')
    # possible_values = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}
    possible_values = {1, 2, 3, 4}
    print(possible_values)

    print_title('CSP WARM-UP: fill square non repeatedly')
    start = time.time()
    # is_filled, square_filled = fill_square_non_repeatedly_backtracked(square, possible_values, False)

    possible_values_table = np.array([1, 2, 3, 4])
    square_possible_values = np.full((4, 4, 4), possible_values_table, dtype=np.int16)
    is_filled, square_filled = fill_square_non_repeatedly_forward_checking(square, square_possible_values, False, 0)
    end = time.time()
    print(end - start)
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


def fill_square_non_repeatedly_forward_checking(square, square_possible_vals, is_recursive, recurence_num):
    print('recurence_num: ', recurence_num)
    if np.sum(square_possible_vals) == 0:
        return True, square

    for col in range(0, square.shape[0]):
        for row in range(0, square.shape[1]):
            if square[row, col] == 0:
                for val in square_possible_vals[col, row]:
                    if val == 0:
                        continue
                    if col < square.shape[0]:
                        is_possible, square_possible_vals_next = is_possible_assignment_foreward_check(square_possible_vals, row, col, val)
                        print(is_possible, val, square_possible_vals_next)

                        if is_possible:
                            is_filled = False
                            square_part_filled = square
                            # val = possible_vals_in_row_and_col.pop()
                            square[row, col] = val

                            # square_possible_vals_next = square_possible_vals.copy()

                            is_filled, square_part_filled = fill_square_non_repeatedly_forward_checking(square, square_possible_vals_next, True, recurence_num + 1)

                            # if is_filled:
                            #     break

                            if is_filled:
                                square = square_part_filled
                                if is_recursive:
                                    return True, square
                            else:
                                square[row, col] = 0
                                return False, square
                        else:
                            return False, square
                    else:
                        square[row, col] = val
                        return True, square

    return False, square


def is_possible_assignment(square, possible_vals, row, col):
    possible_vals_in_row = possible_vals - set(square[row])
    possible_vals_in_row_and_col = possible_vals_in_row - set(square[:, col])
    return bool(possible_vals_in_row_and_col), possible_vals_in_row_and_col


def is_possible_assignment_foreward_check(square_possible_vals, x, y, val):
    print(x, y)
    for col in range(0, square_possible_vals.shape[0]):
        print('col iteration')
        if col < y and square_possible_vals[col, x, val - 1] != val:
            return False, square_possible_vals
        square_possible_vals[col, x, val - 1] = 0
        print('col iteration', val)
        if col > y and np.sum(square_possible_vals[col, x]) == 0:
            return False, square_possible_vals
    for row in range(0, square_possible_vals.shape[1]):
        print('row iteration')
        if row < x and square_possible_vals[y, row, val - 1] != val:
            return False, square_possible_vals
        square_possible_vals[y, row, val - 1] = 0
        if row > x and np.sum(square_possible_vals[y, row]) == 0:
            return False, square_possible_vals

    return True, square_possible_vals


def forward_check(square, possible_vals, x, y):
    for col in range(y, square.shape[0]):
        for row in range(0, square.shape[1]):
            if y == col and x <= row:
                continue
            if not is_possible_assignment(square, possible_vals, row, col):
                return False
    return True
