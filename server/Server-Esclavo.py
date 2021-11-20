from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import cv2 
import time


def receive():


    while True:
        # msg = client_socket.recv(1024)
        # msg = msg.decode('utf-8')
        # print(msg)
        path_rev = client_socket.recv(BUFSIZ)
        path = path_rev.decode('utf-8')
      
        if not not path:

            if not  path == "Imagen enviada": 
                print ("1")
                
                print("path recibido")
                image=client_socket.recv(BUFSIZ)
                
            
                print(path)
                file = open(path, "wb")
                file.write(image)
                file.close()
                print("imagen guardada " ,path)
                
                Images.append(path)
                print(len(Images))
                

            # print ("asdasd")

            else: 
            
                # print(Images)
                for img in Images: 
                    
                    # print("adentro") 
                    # print(img)
                    imagen = cv2.imread(img)
                    imagen = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
                    cv2.imwrite(img,imagen)

        else:

            for img in Images:

                file = open(img, 'rb')
                image = file.read(BUFSIZ)

                client_socket.send(imagen)
                print("a fuera")
                # time.sleep(1000)



            
          

HOST = '127.0.0.1'
PORT = 33000
BUFSIZ = 5242880 

Images = []

ADDR = (HOST, PORT)
client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect(ADDR)

receive_thread = Thread(target=receive)
receive_thread.start()