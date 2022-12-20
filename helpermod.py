import os
import sys
import socket

def send_file(socket,filename):
	with open(filename,"rb") as file:
		while True:
			bytes_sent=file.read(4096)
			if not bytes_sent:
				#nothing is sent
				#file transmitting is done
				break
			#write bytes to the socket
			socket.sendall(bytes_sent)


def recv_file(socket,filename):
	with open(filename,"wb") as file:
		while True:
			# read bytes from the socket
			bytes_received = socket.recv(4096)
			if not bytes_received:    
				# nothing is received
				# file transmitting is done
				break
			file.write(bytes_received)


def send_listing(socket):
	#retrieving the list of files from the directory
	filenames=os.listdir()
	#joining the list as a string
	strFilenames=",".join(filenames)
	#encoding list to be sent
	encoded_string=strFilenames.encode("utf-8")
	socket.sendall(encoded_string)



def recv_listing(socket):
	#recieve 4096 bytes
	data=socket.recv(4096)
	#decode datat as it is a string
	decodedData=data.decode("utf-8")
	print("files in the current directory:"+ decodedData)



