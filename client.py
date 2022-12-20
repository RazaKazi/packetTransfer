import socket
import sys
import os
from helpermod import send_file, send_listing,recv_listing,recv_file

# Create the socket with which we will connect to the server
cli_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# The server's address is a tuple, comprising the server's IP address or hostname, and port number
srv_addr = (sys.argv[1], int(sys.argv[2])) # sys.argv[x] is the x'th argument on the command line
# Convert to string, to be used shortly
srv_addr_str = str(srv_addr)

try:
	print("Connecting to " + srv_addr_str + "... ")
	cli_sock.connect(srv_addr)
	
	print("Connected...")
except Exception as e:
	# Print the exception message
	print(e)
	# Exit with a non-zero value, to indicate an error condition
	exit(1)
# "main" part of the program above workings down below

try:
	
	#check if right number of arguements are in the system
	if (len(sys.argv)==5):
		if sys.argv[3]=="put":
			#string containing the type of request and filename
			arguement_string=sys.argv[3]+","+sys.argv[4]
			encodedAS=arguement_string.encode("utf-8")
			cli_sock.sendall(encodedAS)
			send_file(cli_sock,sys.argv[4])
			print("server_information: "+srv_addr_str+"request type: "+sys.argv[3]+"filename: "+sys.argv[4]+"status:success")

		elif sys.argv[3]=="get":
			#string containing the type of request and filename
			arguement_string=sys.argv[3]+","+sys.argv[4]
			encodedAS=arguement_string.encode("utf-8")
			cli_sock.sendall(encodedAS)
			if not(sys.argv[4] in os.listdir()): 
				recv_file(cli_sock,sys.argv[4])
				print("server_information: "+srv_addr_str+"request type: "+sys.argv[3]+"filename: "+sys.argv[4]+"status:success")
			else:
				print("file already exists in directory")
		
	elif (len(sys.argv)==4) and (sys.argv[3]=="list"):
		encodedArgv=sys.argv[3].encode("utf-8")
		cli_sock.sendall(encodedArgv)
		recv_listing(cli_sock)
		print("server_information: "+srv_addr_str+"request type: "+sys.argv[3]+" status:succcess")
	else:
		print("incorrect input")

except Exception as e:
		print(e)
		exit(1)


		

finally:
	
	cli_sock.close()

# Exit with a zero value, to indicate success
exit(0)