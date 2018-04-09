# server.py 
import socket, pickle
from PIL import ImageGrab
import cv2
import numpy as np
# create a socket object
serversocket = socket.socket(
	        socket.AF_INET, socket.SOCK_STREAM) 

# get local machine name                
host = socket.gethostbyname( '0.0.0.0' )                           
# host = '192.168.7.242'                         

port = 9999                                           

# bind to the port
serversocket.bind((host, port))                                  

# queue up to 5 requests
serversocket.listen(5)                      
clientsocket,addr = serversocket.accept()                      
try: 	
	while True:
	    # establish a connection
		printscreen_pil =  ImageGrab.grab() 
		printscreen_numpy = np.array(printscreen_pil.getdata(),dtype='uint8').reshape((printscreen_pil.size[1],printscreen_pil.size[0],3))
		data_string = pickle.dumps(printscreen_numpy)
		clientsocket.sendall(data_string) 
except Exception as e:
	print(e)
finally: 
	print("Closing socket and exit") 
	clientsocket.close()
 