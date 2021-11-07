from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread


def accept_incoming_connections():

    while True:

        client, client_address = serverMaestro.accept()
        #Guardamos la direccion IP 
        addresses[client] = client_address

        #Usamos un hilo y lo dirigimos a la funcion, le pasamos como argumentos el sokect del cliente
        Thread().start()
        print(addresses[client] )
        client.send(bytes("hola", "utf8" ))



addresses = {}



HOST = '127.0.0.1'
PORT = 33000

serverMaestro = socket(AF_INET, SOCK_STREAM)
serverMaestro.bind((HOST, PORT))

if __name__ == "__main__":

    serverMaestro.listen()
    ACCEPT_THREAD = Thread(target=accept_incoming_connections)
    ACCEPT_THREAD.start()
    ACCEPT_THREAD.join()
    serverMaestro.close()

  


