# client.py  
import socket, pickle
from PIL import ImageGrab
import numpy as np
import cv2
# create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

# get local machine name
host = socket.gethostname()                           
#host = '192.168.0.102'
port = 9999

# connection to hostname on the port. 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((host, port))                              

# Receive no more than 1024 bytes
try:
	while True:
		# printscreen_numpy = s.recv(40960000)  
		printscreen_pil =  ImageGrab.grab() 
		printscreen_numpy = np.array(printscreen_pil.getdata(),dtype='uint8').reshape((printscreen_pil.size[1],printscreen_pil.size[0],3))
		data_string = pickle.dumps(printscreen_numpy)
		s.sendall(data_string) 
except Exception as e:
	 print(e)
finally: 
	print("Closing socket and exit")
	s.close() 