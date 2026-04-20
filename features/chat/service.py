from time import sleep

clients = []


def stream():
    q = []

    clients.append(q)

    try:
        while True:
            if q:
                yield f"data: {q.pop(0)}\n\n"
            sleep(0.4)

    finally:
        clients.remove(q)


def sendMessageToAllClients(message: str):
    for q in clients:
        q.append(message)
