MATRIX_X = 12
MATRIX_Y = 12

EMPTY_MATRIX = [[' ' for i in range(MATRIX_X)] for __ in range(MATRIX_Y)]

gamepad_connected = 'NAAADAAAAAA'


def gamepad_connected_get():
    return gamepad_connected


def gamepad_connected_set(new):
    global gamepad_connected
    gamepad_connected = new
