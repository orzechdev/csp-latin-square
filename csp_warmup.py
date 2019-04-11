from utils import print_title
import numpy as np


possible_values_size = 5


def start():
    print_title('CSP WARM-UP: start')

    print_title('CSP WARM-UP: init square with size 5')
    # square = init_square(5)
    # print(square)
    #
    # print_title('CSP WARM-UP: set possible values')
    # possible_values = {1, 2, 3, 4, 5}
    # print(possible_values)
    #
    # print_title('CSP WARM-UP: fill square non repeatedly')
    # square_filled = fill_square_non_repeatedly(square, possible_values)
    # print(square_filled)

    print_latin(7)

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


# Function to prn x n Latin Square
def print_latin(n):
    # A variable to control the
    # rotation point.
    k = n + 1

    # Loop to prrows
    for i in range(1, n + 1, 1):

        # This loops runs only after first
        # iteration of outer loop. It prints
        # numbers from n to k
        temp = k
        while temp <= n:
            print(temp, end=" ")
            temp += 1

        # This loop prints numbers
        # from 1 to k-1.
        for j in range(1, k):
            print(j, end=" ")

        k -= 1
        print()

