import socket
import sys
import os
from helpermod import send_file, send_listing,recv_listing,recv_file

#setting up the server
try:
	# Create the socket on which the server will receive new connections
	srv_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	srv_sock.bind(("0.0.0.0", int(sys.argv[1]))) # sys.argv[1] is the 1st argument on the command line
	print("server IP:"+sys.argv[0]+"port number:"+sys.argv[1]+"server is up and running")
	srv_sock.listen(5) #creating a queue of size 5 

#exception snippet		
except Exception as e:
	# Print the exception message
	print(e)
	# Exit with a non-zero value, to indicate an error condition
	exit(1)

#main loop
while True:
	try:
		print("wating for new client... ")
		cli_sock, cli_addr = srv_sock.accept()
		cli_addr_str = str(cli_addr) # Translate the client address to a string (to be used shortly)
		print("Client " + cli_addr_str + " ready to parse request...")
		#recieve the data from the client 
		arguements=cli_sock.recv(4096)
		decodedarguements=arguements.decode("utf-8")
		#split the type request and filename so they can be used seperately 
		decodedarguements=decodedarguements.split(",")

		if decodedarguements[0]=="get":
			send_file(cli_sock,decodedarguements[1])
		elif decodedarguements[0]=="put":
			if not(decodedarguements[1] in os.listdir()):  
				recv_file(cli_sock,decodedarguements[1])
			else:
				print("file already exists in directory")
		elif decodedarguements[0]=="list":
			send_listing(cli_sock)

	except Exception as e:
		print(e)
		exit(1)

	finally:	
		cli_sock.close()
	
	
	
	   

# Close the server socket as well to release its resources back to the OS
srv_sock.close()

# Exit with a zero value, to indicate success
exit(0)
