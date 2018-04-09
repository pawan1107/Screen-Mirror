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
		data = serversocket.recv(40960000)
		printscreen_numpy = pickle.loads(data) 
		# printscreen_numpy = np.array(printscreen_pil.getdata(),dtype='uint8')\
		# .reshape((printscreen_pil.size[1],printscreen_pil.size[0],3))  
		cv2.imshow('window',printscreen_numpy)
		if cv2.waitKey(25) & 0xFF == ord('q'):
			cv2.destroyAllWindows()
			break 
except Exception as e:
	print(e)
finally: 
	print("Closing socket and exit") 
	clientsocket.close()
 