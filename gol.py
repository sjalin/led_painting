import copy
import os
import random
import time
import vis_output
from queue import Queue, Empty
from general import *

CYCLE_TIME = 1


def gol(q: Queue):
    vis_output.setup()

    matrix, matrix_list = reset_univers()
    iterations = 0
    last_iterations = 0
    total_iterations = 0
    universe_number = 1
    rate = 0.3
    run = True

    while run:
        os.system('clear')
        vis_output.print_stuff(matrix)
        print(f'Iterations:       {iterations}')
        print(f'Last iterations:  {last_iterations}')
        print(f'Total iterations: {total_iterations}')
        print(f'Total universes:  {universe_number}')
        time.sleep(CYCLE_TIME)
        matrix_copy = copy.deepcopy(matrix)
        for y, line in enumerate(matrix):
            for x, place in enumerate(line):
                matrix_copy[y][x] = calc_place(matrix, x, y)
        matrix_list.insert(0, copy.deepcopy(matrix))
        if len(matrix_list) > 10:
            matrix_list.pop()
        matrix = matrix_copy
        iterations += 1
        total_iterations += 1

        reset = False
        try:
            data = q.get(block=False)
            if data == 'stop':
                print('GOL stop')
                run = False
                break
            elif 'rand:' in data:
                rate = float(data.split(':')[1])/100
                reset = True
            elif 'reset' in data:
                reset = True
            else:
                print(f'Invalid command:{data}')
        except Empty:
            pass

        if matrix in matrix_list or reset:
            print(f'Stable/reset {reset}')
            time.sleep(1)
            last_iterations = iterations
            iterations = 0
            universe_number += 1
            matrix, matrix_list = reset_univers(rate)


def reset_univers(rate=0.3):
    if rate == 0 or rate > 1:
        rate = 0.3
    matrix = [['X' if random.random() < rate else 'r' for _ in range(MATRIX_X)] for __ in range(MATRIX_Y)]
    matrix_list = []
    return matrix, matrix_list


def calc_place(matrix, x, y):
    total = 0

    for dy in [-1, 0, 1]:
        for dx in [-1, 0, 1]:
            try:
                if y+dy == -1 or x+dx == -1:
                    continue
                if matrix[y+dy][x+dx] == 'X':
                    total += 1
            except IndexError:
                pass

    if matrix[y][x] == 'X':
        total -= 1 # Don't count oneself
        if total == 2 or total == 3:
            return 'X'
        else:
            return ' '
    else:
        if total == 3:
            return 'X'
        else:
            return ' '

