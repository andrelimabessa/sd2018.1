from queue import Queue
from thread_server import server_thread
from thread_client import client_thread

server_q = Queue()
client_q = Queue()


class Queues:
    get_from_server_queue = server_q.get
    get_from_client_queue = client_q.get
    put_to_server = server_q.put
    put_to_client = client_q.put
    client_task_done = client_q.task_done
    server_task_done = server_q.task_done

    def stop_threads(self):
        self.put_to_server('STOP')

    def join(self):
        server_q.join()
        client_q.join()


q = Queues()

t1 = server_thread(q)
t2 = client_thread(q)

t1.start()
t2.start()
q.join()
