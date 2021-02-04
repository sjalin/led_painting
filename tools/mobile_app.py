import socket

import keyboard

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#d:e
# server_address = ('localhost', 7777)
server_address = ('192.168.1.34', 7777)
sock.connect(server_address)

try:

    # Send data
#    message = 'rand:33'
#    message = 'quit'
#    message = 'gol'
#    message = 'snake'
    message = 'd:e'

    while True:
#        message = input()
        if keyboard.read_key() == 'w':
            message = 'd:n'
        elif keyboard.read_key() == 's':
            message = 'd:s'
        elif keyboard.read_key() == 'a':
            message = 'd:w  '
        elif keyboard.read_key() == 'd':
            message = 'd:e'
        sock.sendall(message.encode('utf-8'))

        # Look for the response
        amount_received = 0
        amount_expected = len(message)

        while amount_received < amount_expected:
            data = sock.recv(16)
            amount_received += len(data)
            print(data)
        if message == 'DIE':
            break

finally:
    sock.close()
