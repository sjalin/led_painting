import copy
import os
import random
import time
import vis_output
from queue import Queue, Empty

from general import MATRIX_X, MATRIX_Y, EMPTY_MATRIX


class SnakeError(Exception):
    """Base class for exceptions in this module."""
    pass


def snake(q: Queue):
    the_snake = []
    points = 0
    points_last = 0
    points_max = 0
    direction = 'n'
    dir = direction
    universe_number = 1

    cycle_time = 0.2
    easy_mode = False

    vis_output.setup()
    matrix, the_snake = reset_univers()
    run = True

    while run:
        reset = False
        os.system('clear')
        vis_output.print_stuff(matrix)
        print(f'Points:       {points}')
        print(f'Points last:  {points_last}')
        print(f'Points max:   {points_max}')
        print(f'Direction:    {direction}')
        time.sleep(cycle_time)

        try:
            while not q.empty():
                data = q.get(block=False)
                if data == 'stop':
                    print('Sanke stop')
                    run = False
                    break
                elif 'reset' in data:
                    reset = True
                elif 'd:' in data:
                    dir = data.split(':')[1]
                    if dir not in ['n', 's', 'w', 'e']:
                        dir = direction
                else:
                    print(f'Invalid command:{data}')
        except Empty:
            pass

        if ((dir == 's' and direction == 'n') or
                (dir == 'n' and direction == 's') or
                (dir == 'w' and direction == 'e') or
                (dir == 'e' and direction == 'w')):
            pass
        else:
            direction = dir

        try:
            points += calc_next(matrix, the_snake, direction, easy_mode)
        except SnakeError:
            reset = True

        if reset:
            print(f'DEAD/reset {reset}')
            time.sleep(2)
            points_last = points
            if points > points_max:
                points_max = points
            points = 0
            points_max = points if points > points_max else points_max
            universe_number += 1
            direction = 'n'
            dir = direction
            vis_output.show_numbers(points_last, points_max, 'b', 'r')
            time.sleep(5)
            matrix, the_snake = reset_univers()


def reset_univers(rate=0.3):
    matrix = copy.deepcopy(EMPTY_MATRIX)
    the_snake = [(6, 5), (5, 5), (4, 5)]
    matrix[the_snake[0][0]][the_snake[0][1]] = 'b'

    for y, x in the_snake[1:]:
        matrix[y][x] = 'g'

    while True:
        rand_y = random.randint(0, 11)
        rand_x = random.randint(0, 11)
        if (rand_y, rand_x) not in the_snake:
            matrix[rand_y][rand_x] = 'r'
            break

    return matrix, the_snake


def calc_next(matrix, the_snake, direction, easy):
    x_diff = 0
    y_diff = 0
    ret_point = 0

    if direction == 'n':
        y_diff = 1
    elif direction == 's':
        y_diff = -1
    elif direction == 'e':
        x_diff = 1
    elif direction == 'w':
        x_diff = -1
    else:
        print(f'Invalid direction: {direction}')
        return ret_point

    next_cord = (the_snake[0][0] + y_diff, the_snake[0][1] + x_diff)

    if next_cord[0] < 0 or next_cord[1] < 0:
        if not easy:
            raise SnakeError()
        return ret_point

    try:
        if matrix[next_cord[0]][next_cord[1]] == 'r':
            the_snake.insert(0, next_cord)
            ret_point = 1
        else:
            tail = the_snake.pop()
            matrix[tail[0]][tail[1]] = ' '
            the_snake.insert(0, next_cord)
            if matrix[next_cord[0]][next_cord[1]] == 'g':
                vis_output.set_pos(next_cord[0], next_cord[1], 'rg')
                print('DEADDDDDDDD 3')
                raise SnakeError()
        matrix[the_snake[0][0]][the_snake[0][1]] = 'b'
        matrix[the_snake[1][0]][the_snake[1][1]] = 'g'

        if ret_point:
            while True:
                rand_y = random.randint(0, 11)
                rand_x = random.randint(0, 11)
                if (rand_y, rand_x) not in the_snake:
                    matrix[rand_y][rand_x] = 'r'
                    break
    except IndexError:
        if not easy:
            raise SnakeError()
        return ret_point

    return ret_point
