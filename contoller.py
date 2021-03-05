from queue import Queue
from time import sleep

from evdev import InputDevice, ecodes
from general import *

# Button code variables
nvidia_btn = 217
dpad_x = 16
dpad_y = 17


def gamepad(q: Queue):
    print('Start gamepad thread')
    xdir = ''
    ydir = ''
    totdir = ''

    gamepad_input = None

    # Wait until
    q.put('gamepad started')
    while not gamepad_input:
        try:
            gamepad_input = InputDevice('/dev/input/event0')
            global gamepad_connected
            gamepad_connected = InputDevice.info

            break
        except (FileNotFoundError, PermissionError) as e:
            pass

    print('Gamepad found and started')
    # loop and filter by event code and print the mapped label
    for event in gamepad_input.read_loop():
        sleep(0.001)
        tempdir = totdir
        if event.type == ecodes.EV_KEY:
            if event.value == 1:
                if event.code == nvidia_btn:
                    q.put('next game')
                else:
                    print(f'Unknown keypress: {event.code}')
        elif event.type == ecodes.EV_ABS:
            if event.code == dpad_x:
                if event.value == 1:
                    xdir = 'e'
                elif event.value == -1:
                    xdir = 'w'
                else:
                    xdir = ''
            if event.code == dpad_y:
                if event.value == 1:
                    ydir = 's'
                elif event.value == -1:
                    ydir = 'n'
                else:
                    ydir = ''
            if xdir or ydir:
                if bool(xdir) != bool(ydir):
                    if xdir:
                        tempdir = xdir
                    else:
                        tempdir = ydir

            print(f'new dir {tempdir}')
            totdir = tempdir
            q.put('d:'+tempdir)
