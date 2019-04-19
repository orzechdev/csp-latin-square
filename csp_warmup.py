from utils import print_title
import numpy as np


possible_values_size = 5


def start():
    print_title('CSP WARM-UP: start')

    print_title('CSP WARM-UP: init square with size 5')
    square = init_square(5)
    print(square)

    print_title('CSP WARM-UP: set possible values')
    possible_values = {1, 2, 3, 4, 5}
    print(possible_values)

    print_title('CSP WARM-UP: fill square non repeatedly')
    is_filled, square_filled = fill_square_non_repeatedly(square, possible_values, 0, 0)
    print(square_filled)

    # print_latin(7)

    print_title('CSP WARM-UP: end')


def init_square(size):
    square = np.zeros((size, size), dtype=np.int16)

    return square


def backtracking_search():
    pass


def fill_square_non_repeatedly(square, possible_vals, x, y):
    if len(possible_vals) == 0:
        return True, square

    for col in range(y, square.shape[0]):
        for row in range(x, square.shape[1]):
            is_possible, possible_vals_in_row_and_col = is_possible_assignment(square, possible_vals, row, col)
            if is_possible:
                is_filled = False
                square_part_filled = square
                for val in possible_vals_in_row_and_col:
                    # val = possible_vals_in_row_and_col.pop()
                    square[row, col] = val

                    possible_vals_next = possible_vals.copy()

                    possible_vals_next.remove(val)
                    next_x = (row + 1) % square.shape[1]
                    next_y = (col + 1) if row % square.shape[1] == 0 else col
                    is_filled, square_part_filled = fill_square_non_repeatedly(square, possible_vals_next, next_x, next_y)

                    if is_filled:
                        break
                if is_filled:
                    # print(square_part_filled)
                    # square[row, col] = val
                    square = square_part_filled
                    return True, square
                else:
                    square[row, col] = 0

            else:
                return False, square

            # if square[row, col] == 0:
            #     # print(square[row, col])
            #     # Create possible values in row and subtract from full set
            #     possible_vals_in_row = possible_vals - set(square[row])
            #     # print(possible_vals_in_row)
            #     # Create possible values in column and subtract
            #     possible_vals_in_col = possible_vals_in_row - set(square[:, col])
            #     # print(possible_vals_in_col)
            #     square[row, col] = possible_vals_in_col.pop()

    return False, square


def is_possible_assignment(square, possible_vals, row, col):
    possible_vals_in_row = possible_vals - set(square[row])
    possible_vals_in_row_and_col = possible_vals_in_row - set(square[:, col])
    return bool(possible_vals_in_row_and_col), possible_vals_in_row_and_col



# # Function to prn x n Latin Square
# def print_latin(n):
#     # A variable to control the
#     # rotation point.
#     k = n + 1
#
#     # Loop to prrows
#     for i in range(1, n + 1, 1):
#
#         # This loops runs only after first
#         # iteration of outer loop. It prints
#         # numbers from n to k
#         temp = k
#         while temp <= n:
#             print(temp, end=" ")
#             temp += 1
#
#         # This loop prints numbers
#         # from 1 to k-1.
#         for j in range(1, k):
#             print(j, end=" ")
#
#         k -= 1
#         print()

