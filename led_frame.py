from time import sleep
import RPi.GPIO as GPIO

DIODS_PER_PIXEL = 3
GRID_SIZE = 12
TOTAL_LEDS = GRID_SIZE * DIODS_PER_PIXEL
GREEN_POS = 0
RED_POS = 1
BLUE_POS = 2

on_grid = [[127 for _ in range(12)] for __ in range(TOTAL_LEDS)]
off_grid = [[0 for _ in range(12)] for __ in range(TOTAL_LEDS)]


green_grid = [[127 for _ in range(12)] if i % 3 == GREEN_POS else [0 for _ in range(12)] for i in range(TOTAL_LEDS)]
blue_grid = [[127 for _ in range(12)] if i % 3 == BLUE_POS else [0 for _ in range(12)] for i in range(TOTAL_LEDS)]
red_grid = [[127 for _ in range(12)] if i % 3 == RED_POS else [0 for _ in range(12)] for i in range(TOTAL_LEDS)]

current_matrix = []

def setup():
    print('Led setup')
    GPIO.setmode(GPIO.BCM)

    for i in range(2, 15):
        print(i)
        GPIO.setup(i, GPIO.OUT)


def start():
    setup()

    set_leds(off_grid)

    on = True
    while True:
        if on:
            set_leds(green_grid)
        else:
            set_leds(off_grid)
        on = not on

        sleep(1)
        print(f'here we go again {on}')
    

def show_led_matrix(matrix):
    led_matrix = []

    for y in matrix:
        led_matrix.append([127 if 'g' in x or 'X' in x else 0 for x in y[::-1]])
        led_matrix.append([127 if 'r' in x or 'X' in x else 0 for x in y[::-1]])
        led_matrix.append([127 if 'b' in x or 'X' in x else 0 for x in y[::-1]])
    set_leds(led_matrix)
    global current_matrix
    current_matrix = matrix


def set_leds(grid):
    # Might add range check here
    reset()

    for line in grid+[grid[0]]:  #H ave to write to an extra diod to set the last
        # always set first bit
        row_on()
        GPIO.output(2, True)
        GPIO.output(2, False)
    
        for i in range(6, -1, -1):
            for index, value in enumerate(line):
                try: 
                    if line[index] >> i & 1:
                        GPIO.output(index+3, True)
                    else:
                        GPIO.output(index+3, False)
                except Exception as e:
                    print(index+3)

            GPIO.output(2, True)
            GPIO.output(2, False)


def reset():
    row_off()
    for _ in range(8):
        GPIO.output(2, True)
        GPIO.output(2, False)


def row_on():
    for i in range(3, 15):
        GPIO.output(i, True)


def row_off():
    for i in range(3, 15):
        GPIO.output(i, False)


def set_pixel(y, x, color):
    temp_matrix = current_matrix.copy()
    temp_matrix[y][x] = color
    show_led_matrix(temp_matrix)
