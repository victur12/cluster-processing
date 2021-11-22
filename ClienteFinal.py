from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import time


def receive():

    # while bandera != 0:

        client_socket.send(bytes("Cliente", "utf-8"))

        path = input("Ingrese el path de su video ")

        file = open(path, "rb")

        video = file.read(BUFSIZ)
        client_socket.send(video)

        file.close()
        # time.sleep(100)
        videoBlancoNegro = client_socket.recv(BUFSIZ)
        file = open("videoBlancoNegro.mp4", "wb")
        file.write(videoBlancoNegro)
        file.close()


        








bandera =1
HOST = '127.0.0.1'
PORT = 33000
BUFSIZ = 15728640  

Images = []

ADDR = (HOST, PORT)
client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect(ADDR)

receive_thread = Thread(target=receive)
receive_thread.start()