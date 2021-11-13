from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import cv2
import time




def accept_incoming_connections():

    while True:

        client, client_address = serverMaestro.accept()
        #Guardamos la direccion IP 
        addresses[client] = client_address
        print("%s:%s se conecto." % client_address)

        #Usamos un hilo y lo dirigimos a la funcion, le pasamos como argumentos el sokect del cliente
        Thread().start()
        print(len(addresses) )

        vidcap = cv2.VideoCapture('video.mp4')
        success,image = vidcap.read()

        count = 0
        count1=0
        while success:

          cv2.imwrite("frame%d.jpg" % count, image)     # save frame as JPEG file      
          success,image = vidcap.read()
          # print('Read a new frame: ', success)
          count += 1


        # while count1 < count:
        #   for sock in addresses:

        #     if  count1 <=count:

        #       path = "frame%d.jpg" % count1
        #       file = open(path, 'rb')

        #       print("frame%d.jpg" % count1)

        #       sock.send(bytes(path, "utf8"))
        #       print(sock.send(bytes(path, "utf8")))

        #       imagen = file.read(5242880)

        #       sock.send(imagen)
        #       file.close()  
        #       count1 += 1
          

        for j in range(count):

          print("frame%d.jpg" % j)
          path = "frame%d.jpg" % j
          file = open(path, 'rb')

          client.send(bytes(path, "utf8"))

          imagen = file.read(5242880)

          client.send(imagen)
          file.close()
          time.sleep(0.1)
          # print(j)

      
        print('Image saved')
        


  


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

  


