from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import cv2
import time
import os
from zipfile import ZipFile
import shutil
import numpy as np
import glob


def accept_incoming_connections():

    while True:

        client, client_address = serverMaestro.accept()
        #Guardamos la direccion IP 
        addresses[client] = client_address
        print("%s:%s se conecto." % client_address)

        #Usamos un hilo y lo dirigimos a la funcion, le pasamos como argumentos el sokect del cliente
        Thread(target = handle_client, args=(client,)).start()
        
        print(len(addresses) )
        print(addresses)
        print("Esperando")

        
              
def handle_client(client):

     if not len(addresses)<3:
       
          vidcap = cv2.VideoCapture('VideoCompressorResizeCompressVideo2021_11_15_12_11_21.mp4')
          success,image = vidcap.read()

          count = 0
          count1=0

          while success:

            cv2.imwrite("frame%d.jpg" % count, image)     # save frame as JPEG file      
            success,image = vidcap.read()
            # print('Read a new frame: ', success)
            count += 1


          while count1 < count:

              for sock in addresses:
                # print (sock)

                if  count1 < count:

                  # sock.send(bytes("Hola", "utf8"))

                  path = "frame%d.jpg" % count1
                  file = open(path, 'rb')

                  sock.send(bytes(path, "utf8"))
                  print(path)

                  imagen = file.read(5242880)

                  sock.send(imagen)
                  # print("imagen enviada")
                  file.close() 
                  os.remove(path) 
  
                  count1 += 1

            
          if count1==count:
       
            for sock in addresses:
              sock.send(bytes("Imagen enviada", "utf8"))
              print("enviado")

          
          print("-----------------")

          # for sock in addresses:
          #   msg = sock.recv(BUFSIZ)           
          #   msg = msg.decode('utf-8')
          #   print(msg)

          # while True:
          #   print("Recibiendo adentro")
          #   for sock in addresses:

          #     path_rev = sock.recv(100)
          #     print(path_rev)

          #     # print(sock)
          #     path = path_rev.decode('utf-8')
                
                      
          #     print("path recibido")
          #     image=sock.recv(BUFSIZ)
                      
          #     print(path)
          #     file = open(path, "wb")
          #     file.write(image)
          #     file.close()
          #     print("imagen guardada " ,path)
          #     time.sleep(0.500)
          #     # msg = client.recv(BUFSIZ)           
          #     # msg = msg.decode('utf-8')
          #     # print(msg)

          for sock in addresses:

            # # while True:
            path_rev = sock.recv(13)
            print(path_rev)
  
            # # print(sock)
            path = path_rev.decode('utf-8')
              
            archivo = sock.recv(BUFSIZ)

            file = open(path, "wb")
            file.write(archivo)
            file.close()

                    
            # print("path recibido")
            # image=sock.recv(BUFSIZ)
                    
            # print(path)
            # file = open(path, "wb")
            # file.write(image)
            # file.close()

          print("terminado")
          
          for filename in glob.glob('*.zip'):
            shutil.unpack_archive(filename)
            os.remove(filename)
          


          frameSize = (426, 240)

          out = cv2.VideoWriter('videoBlancoNegro.mp4',cv2.VideoWriter_fourcc(*'mp4v'), 30, frameSize)

          for filename in glob.glob('*.jpg'):
              img = cv2.imread(filename)
              out.write(img)
              os.remove(filename)

          out.release()
          print("Video convertido a blanco/negro exitosamente :)")
          


      
                  
addresses = {}


HOST = '127.0.0.1'
PORT = 33000
BUFSIZ = 15728640  

serverMaestro = socket(AF_INET, SOCK_STREAM)
serverMaestro.bind((HOST, PORT))

if __name__ == "__main__":

    serverMaestro.listen()
    ACCEPT_THREAD = Thread(target=accept_incoming_connections)
    ACCEPT_THREAD.start()
    ACCEPT_THREAD.join()
    serverMaestro.close()