from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import cv2 


def receive():
    while True:

        # msg = client_socket.recv(1024)
        # msg = msg.decode('utf-8')
        # print(msg)
        print ("1")
        path_rev = client_socket.recv(BUFSIZ)
        path = path_rev.decode('utf-8')
        print("path recibido")
        image=client_socket.recv(BUFSIZ)
        
      
        print(path)
        file = open(path, "wb")
        file.write(image)
        file.close()
        print("imagen guardada " ,path)
        
        
        

        # print ("asdasd")

HOST = '127.0.0.1'
PORT = 33000
BUFSIZ = 5242880 

ADDR = (HOST, PORT)
client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect(ADDR)

receive_thread = Thread(target=receive)
receive_thread.start()