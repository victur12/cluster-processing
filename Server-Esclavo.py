from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
def receive():

    while True:
        print (client_socket.recv(BUFSIZ).decode("utf8"))
        print ("asdasd")

HOST = '127.0.0.1'
PORT = 33000
BUFSIZ = 1024

ADDR = (HOST, PORT)
client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect(ADDR)

receive_thread = Thread(target=receive)
receive_thread.start()