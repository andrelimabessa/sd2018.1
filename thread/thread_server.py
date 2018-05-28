from threading import Thread
from core import start_game


game = None


def server(queue):
    while True:
        action = queue.get_from_server_queue()

        if(action == 'STOP'):
            queue.server_task_done()
            break

        type = action['type']

        response = None

        if(type == 'new_game'):
            game = start_game()
            response = game.get_status()
        else:
            execute = getattr(game, type)

            state = game.get_status()

            if ('game_board' in state):
                game = start_game()
            elif 'payload' in action:
                execute(**action['payload'])
            else:
                execute()

            response = game.get_status()

        queue.put_to_client(response)
        queue.server_task_done()


def server_thread(queue):
    return Thread(target=server, args=(queue,))
