# client.py  
import socket, pickle
import numpy as np
import cv2
# create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

# get local machine name
# host = socket.gethostname()                           
host = '192.168.7.242'
port = 9999

# connection to hostname on the port. 
s.connect((host, port))                              

# Receive no more than 1024 bytes
try:
	while True:
		# printscreen_numpy = s.recv(40960000)  
		data = s.recv(40960000)
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
	s.close() 