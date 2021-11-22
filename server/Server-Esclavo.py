from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import cv2 
import time
import os
import random
import zipfile
import zlib

compression = zipfile.ZIP_DEFLATED


def receive():


    while True:
        # msg = client_socket.recv(1024)
        # msg = msg.decode('utf-8')
        # print(msg)
        path_rev = client_socket.recv(BUFSIZ)
        path = path_rev.decode('utf-8')
      
        if not not path:

            if not  path == "Imagen enviada": 
                
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
                    print(img + " filtrada a B/N")


                # client_socket.send(bytes("Enviando", "utf8"))

                nombre ="example%d.zip" %random.randrange(10, 99)

                zf = zipfile.ZipFile(nombre, mode="w")

                for img in Images:

                    zf.write(img, compress_type=compression)
                    os.remove(img)
                zf.close()



                print("Terminado")

                client_socket.send(bytes(nombre, "utf8"))

                file = open(nombre, 'rb')
                archivo = file.read(BUFSIZ)
                client_socket.send(archivo)
                file.close()
                os.remove(nombre)
                # for img in Images:

                #     file = open(img, 'rb')

                #     client_socket.send(bytes(img, "utf8"))
                #     print(img)

                #     imagen = file.read(5242880)
                #     client_socket.send(imagen)

                #     print("enviada de regreso")
                #     file.close()

                #     # time.sleep(random.randrange(1,15))
                #     time.sleep(0.100)

                #     # client_socket.send(bytes("Enviando", "utf8"))

                # # client_socket.send(bytes("Terminado", "utf8"))


        else:
            print("bye")
  
            break


            
          

HOST = '127.0.0.1'
PORT = 33000
BUFSIZ = 15728640  

Images = []

ADDR = (HOST, PORT)
client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect(ADDR)

receive_thread = Thread(target=receive)
receive_thread.start()