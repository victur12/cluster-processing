from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import cv2
import time
import os




def accept_incoming_connections():

    while True:

        client, client_address = serverMaestro.accept()
        #Guardamos la direccion IP 
        addresses[client] = client_address
        print("%s:%s se conecto." % client_address)

        #Usamos un hilo y lo dirigimos a la funcion, le pasamos como argumentos el sokect del cliente
        Thread().start()
        print(len(addresses) )
        print(addresses)
        print("Esperando")

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
              
              print ("a")

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
                  print("imagen enviada")
                  file.close() 
                  os.remove(path) 
  
                  count1 += 1

            
          if count1==count:
       
            for sock in addresses:
              sock.send(bytes("Imagen enviada", "utf8"))
              print("enviado")
          


          
          
          print("-----------------")
          # msg = client.recv(BUFSIZ)           
          # msg = msg.decode("utf8")
          # print(msg)

          # while msg == "Enviando":
          
          path_rev = client.recv(BUFSIZ)
          path = path_rev.decode('utf-8')
          print(path)
            
          print ("1")
                  
          print("path recibido")
          image=client.recv(BUFSIZ)
                  
          print(path)
          file = open(path, "wb")
          file.write(image)
          file.close()
          print("imagen guardada " ,path)
                


          
                  

          
                  
addresses = {}


HOST = '127.0.0.1'
PORT = 33000
BUFSIZ = 5242880 

serverMaestro = socket(AF_INET, SOCK_STREAM)
serverMaestro.bind((HOST, PORT))

if __name__ == "__main__":

    serverMaestro.listen()
    ACCEPT_THREAD = Thread(target=accept_incoming_connections)
    ACCEPT_THREAD.start()
    ACCEPT_THREAD.join()
    serverMaestro.close()