from general import EMPTY_MATRIX
from target import TARGET

if TARGET:
    import led_frame


digits = [[['X', 'X', 'X'],
           ['X', ' ', 'X'],
           ['X', ' ', 'X'],
           ['X', ' ', 'X'],
           ['X', 'X', 'X'],],
          [[' ', 'X', ' '],
           ['X', 'X', ' '],
           [' ', 'X', ' '],
           [' ', 'X', ' '],
           ['X', 'X', 'X'],],
          [['X', 'X', 'X'],
           [' ', ' ', 'X'],
           [' ', 'X', ' '],
           ['X', ' ', ' '],
           ['X', 'X', 'X'],],
          [['X', 'X', 'X'],
           [' ', ' ', 'X'],
           [' ', 'X', ' '],
           [' ', ' ', 'X'],
           ['X', 'X', 'X'],],
          [['X', ' ', 'X'],
           ['X', ' ', 'X'],
           ['X', 'X', 'X'],
           [' ', ' ', 'X'],
           [' ', ' ', 'X'],],
          [['X', 'X', 'X'],
           ['X', ' ', ' '],
           ['X', 'X', 'X'],
           [' ', ' ', 'X'],
           ['X', 'X', 'X'],],
          [['X', 'X', 'X'],
           ['X', ' ', ' '],
           ['X', 'X', 'X'],
           ['X', ' ', 'X'],
           ['X', 'X', 'X'],],
          [['X', 'X', 'X'],
           [' ', ' ', 'X'],
           [' ', 'X', ' '],
           ['X', ' ', ' '],
           ['X', ' ', ' '],],
          [['X', 'X', 'X'],
           ['X', ' ', 'X'],
           [' ', 'X', ' '],
           ['X', ' ', 'X'],
           ['X', 'X', 'X'],],
          [['X', 'X', 'X'],
           ['X', ' ', 'X'],
           ['X', 'X', 'X'],
           [' ', ' ', 'X'],
           ['X', 'X', 'X'],]]


def setup():
    if TARGET:
        led_frame.setup()


def print_stuff(matrix):
    if TARGET:
        led_frame.show_led_matrix(matrix)

    stuff = ''
    for row in matrix[::-1]:  # To be in the same orientation as the painting
        for letter in row:  # Same here
            if letter == 'X':
                stuff += '@'
            elif 'g' in letter:
                stuff += 'g'
            elif 'b' in letter:
                stuff += 'b'
            elif 'r' in letter:
                stuff += 'r'
            else:
                stuff += letter
        stuff += '\n'
    print(stuff)


def set_pos(y, x, color):
    if TARGET:
        led_frame.set_pixel(y, x, color)


def show_numbers(top, bottom, t_color, b_color):
    matrix = EMPTY_MATRIX.copy()

    set_digit(matrix, 11, 0, get_digit_from_numer(top, 2), t_color)
    set_digit(matrix, 11, 4, get_digit_from_numer(top, 1), t_color)
    set_digit(matrix, 11, 8, get_digit_from_numer(top, 0), t_color)

    set_digit(matrix, 5, 0, get_digit_from_numer(bottom, 2), b_color)
    set_digit(matrix, 5, 4, get_digit_from_numer(bottom, 1), b_color)
    set_digit(matrix, 5, 8, get_digit_from_numer(bottom, 0), b_color)

    print_stuff(matrix)


def get_digit_from_numer(number, n):
    return number // 10**n % 10


def set_digit(matrix, y, x, digt, color):
    digit_pattern = digits[digt]
    for row_num, row in enumerate(digit_pattern):
        for row_poss, grej in enumerate(row):
            if grej == 'X':
                matrix[y-row_num][x+row_poss] = color