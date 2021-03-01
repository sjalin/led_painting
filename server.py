import socket

from queue import Queue
from time import sleep

from target import TARGET



def server(q:Queue):
    print('Starting server')
    address_bound = False
    while not address_bound:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        if TARGET:
            server_address = ('192.168.1.34', 7777)
        else:
            server_address = ('localhost', 7777)


        try:
            sock.bind(server_address)
            address_bound = True
        except OSError as e:
            print(f'Cant bind socket, retrying in 5 sec')
            sleep(5)

    sock.listen()
    print('Socket listened')
    q.put('server started')
    be_alive = True
    while be_alive:
        connection, client_address = sock.accept()
        try:
            while be_alive:
                data = connection.recv(16)
                if data:
                    in_data = data.decode('utf-8')
                    print(f'{data} -- {in_data}')
                    connection.sendall(data)
                    q.put(in_data)
                    if 'quit' in in_data:
                        print('Server stop')
                        be_alive = False
                else:
                    break
        finally:
            connection.close()
    connection.close()

