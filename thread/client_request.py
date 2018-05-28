def request(queue, action):
    queue.put_to_server(action)
