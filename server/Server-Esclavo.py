from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import cv2 


def receive():
    count = 0
    while True:

        print ("1")
        path_rev = client_socket.recv(BUFSIZ)
        path = path_rev.decode("utf-8")
        image=client_socket.recv(BUFSIZ)
        
        # image = cv2.imdecode(image, cv2.IMREAD_COLOR)
        # cv2.imwrite("Hola2%d.jpg" %count, image)
        # cv2.show("asd", image)

        # count+=1
        
        print(path)
        file = open(path, "wb")
        file.write(image)
        file.close()
        
        
        

        print ("asdasd")

HOST = '127.0.0.1'
PORT = 33000
BUFSIZ = 5242880 

ADDR = (HOST, PORT)
client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect(ADDR)

receive_thread = Thread(target=receive)
receive_thread.start()