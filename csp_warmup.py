from utils import print_title
import numpy as np
import time


possible_values_size = 5


def start():
    size_min = 1
    size_max = 13
    start_backtracking_algorithm(size_min, size_max)
    # start_forward_check_algorithm(size_min, size_max)

    # print_title('CSP WARM-UP: start')
    #
    # print_title('CSP WARM-UP: init square with size 5')
    # square = init_square(13)
    # # square = init_square(4)
    # print(square)

    # print_title('CSP WARM-UP: set possible values')
    # possible_values = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13}
    # # possible_values = {1, 2, 3, 4}
    # print(possible_values)

    # print_title('CSP WARM-UP: fill square non repeatedly')
    # start = time.time()
    # is_filled, square_filled = fill_square_non_repeatedly_backtracked(square, possible_values, False)
    #
    # possible_values_table = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])
    # square_possible_values = np.full((13, 13, 13), possible_values_table, dtype=np.int16)
    # # print(square_possible_values)
    # start = time.time()
    # is_filled, square_filled = fill_square_non_repeatedly_forward_checking(square, square_possible_values, False, 0)
    # end = time.time()
    # print(end - start)
    # print(square_filled)

    # print_latin(7)

    # print_title('CSP WARM-UP: end')


def start_backtracking_algorithm(size_min, size_max):
    for size in range(size_min, size_max + 1):
        print_title('CSP WARM-UP: start')
        print_title('CSP WARM-UP: init square with size ' + str(size))
        square = init_square(size)
        print_title('CSP WARM-UP: set possible values')
        possible_values = set()
        for i in range(1, size + 1):
            possible_values.add(i)
        print_title('CSP WARM-UP: fill square non repeatedly (backward algorithm)')
        start_time = time.time()
        is_filled, square_filled = fill_square_non_repeatedly_backtracked(square, possible_values, False)
        end_time = time.time()
        print('Time elapsed: ', end_time - start_time)
        print('Result')
        for y in range(0, square_filled.shape[0]):
            square_filled_str = np.array2string(square_filled[y], precision=2, separator=', ', max_line_width=60)
            print(' ' + square_filled_str[1:-1])
        print_title('CSP WARM-UP: end')


def start_forward_check_algorithm(size_min, size_max):
    for size in range(size_min, size_max + 1):
        print_title('CSP WARM-UP: start')
        print_title('CSP WARM-UP: init square with size ' + str(size))
        square = init_square(size)
        print_title('CSP WARM-UP: set possible values')
        possible_values_table = np.array([])
        for i in range(1, size + 1):
            possible_values_table = np.append(possible_values_table, i)
        print_title('CSP WARM-UP: fill square non repeatedly (forward check algorithm)')
        square_possible_values = np.full((size, size, size), possible_values_table, dtype=np.int16)
        start_time = time.time()
        is_filled, square_filled = fill_square_non_repeatedly_forward_checking(square, square_possible_values, False, 0)
        end_time = time.time()
        print('Time elapsed: ', end_time - start_time)
        print('Result')
        for y in range(0, square_filled.shape[0]):
            square_filled_str = np.array2string(square_filled[y], precision=2, separator=', ', max_line_width=60)
            print(' ' + square_filled_str[1:-1])
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
    # print('recurence_num: ', recurence_num)
    # if np.sum(square_possible_vals[square_possible_vals.shape[0] - 1, square_possible_vals.shape[1] - 1]) == 0:
    #     return True, square

    for col in range(0, square.shape[0]):
        for row in range(0, square.shape[1]):
            if square[row, col] == 0:
                sq_ps_vl_rc = square_possible_vals[row, col]
                square_possible_vals_non_zero = square_possible_vals[row, col, np.nonzero(sq_ps_vl_rc)][0]
                for val in square_possible_vals_non_zero:
                    # print('possible vals loop val: ', val)
                    # if val == 0:
                    #     continue
                    square_possible_vals_copy = square_possible_vals.copy()
                    is_possible, square_possible_vals_next = is_possible_assignment_foreward_check(square_possible_vals_copy, row, col, val)
                    # print(is_possible, val, square_possible_vals_next)

                    if is_possible:
                        square[row, col] = val
                        # print(square)

                        if np.sum(square_possible_vals_next) == 0:
                            # print()
                            return True, square

                        is_filled, square_part_filled = fill_square_non_repeatedly_forward_checking(square, square_possible_vals_next, True, recurence_num + 1)

                        # if is_filled:
                        #     break

                        if is_filled:
                            square = square_part_filled
                            if square[square.shape[1] - 1, square.shape[0] - 1] != 0:
                                return True, square

                            if np.sum(square_possible_vals_next) == 0:  # and is_recursive:
                                return True, square
                            else:
                                continue
                        else:
                            square[row, col] = 0
                            # return False, square
                            continue
                return False, square

    return False, square


def is_possible_assignment(square, possible_vals, row, col):
    possible_vals_in_row = possible_vals - set(square[row])
    possible_vals_in_row_and_col = possible_vals_in_row - set(square[:, col])
    return bool(possible_vals_in_row_and_col), possible_vals_in_row_and_col


def is_possible_assignment_foreward_check(square_possible_vals, x, y, val):
    # print(x, y)
    for col in range(0, square_possible_vals.shape[0]):
        # print('col iteration', col, y, x)
        # if col < y and square_possible_vals[x, col, val - 1] != val:
        #     return False, square_possible_vals
        square_possible_vals[x, col, val - 1] = 0
        # print('col iteration', val)
        if col > y and np.sum(square_possible_vals[x, col]) == 0:
            return False, square_possible_vals
    for row in range(0, square_possible_vals.shape[1]):
        # print('row iteration', row, x, y)
        # if row < x and square_possible_vals[row, y, val - 1] != val:
        #     return False, square_possible_vals
        square_possible_vals[row, y, val - 1] = 0
        if row > x and np.sum(square_possible_vals[row, y]) == 0:
            return False, square_possible_vals

    return True, square_possible_vals

