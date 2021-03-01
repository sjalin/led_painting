from general import EMPTY_MATRIX
from target import TARGET

if TARGET:
    import led_frame


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


def show_numbers(top, botton, t_color, b_color):
    matrix = EMPTY_MATRIX.copy()


def set_digit(matrix, y, x, digt, color):
    pass
