import threading
from queue import Queue, Empty
from time import sleep

import server
import gol
import snake
import contoller


def start():
    print('Program start')
    print('Creating threads')
    handler_queue = Queue()
    game_thread = threading.Thread(target=thread_handler, name='Game handler',
                                   args=(handler_queue,))
    gamepad_thread = threading.Thread(target=contoller.gamepad, name='Gamepad handler',
                                      args=(handler_queue,))
    server_thread = threading.Thread(target=server.server, name='server',
                                     args=(handler_queue,))

    print('Starting threads')
    server_thread.start()

    if handler_queue.get() == 'server started':
        print('starting gamepad')
        gamepad_thread.start()
    else:
        print('Failed to start server, or something')

    if handler_queue.get() == 'gamepad started':
        print('starting games')
        game_thread.start()
        game_thread.join()
    else:
        print('Failed to start gamepad, or something')

    server_thread.join()
    gamepad_thread.join()


def thread_handler(q: Queue):
    game_thread = None
    game_queue = Queue()
    while True:
        if not game_thread:
            print(f' ------------- NOTHING STARTED -------------')
            q.put('snake:first')
        try:
            data = q.get()
            print(f' ------------- TH data: {data} -------------')
            if 'quit' in data:
                game_queue.put('stop')
                game_thread.join()
                print('Thread handler stop')
                break
            elif 'gol' in data:
                if 'first' not in data:
                    game_queue.put('stop')
                print(f' ------------- STARING GOL -------------')
                game_thread = threading.Thread(target=gol.gol, name='Game of life',
                                           args=(game_queue, ))
                game_thread.start()
            elif 'tetris' in data:
                print('<<<<<<<<<<<<<<TETRIS NOT IMPLEMENTED>>>>>>>>>>>>>>>>')
            elif 'snake' in data:
                if 'first' not in data:
                    game_queue.put('stop')
                print(f' ------------- STARING SNAKE -------------')
                game_thread = threading.Thread(target=snake.snake, name='Snake',
                                           args=(game_queue, ))
                game_thread.start()
            elif 'scroll' in data:
                print('<<<<<<<<<<<<<<SCROLL NOT IMPLEMENTED>>>>>>>>>>>>>>>>')
            else:
                game_queue.put(data)

        except Empty:
            pass


if __name__ == '__main__':
    
    start()

