import socket

'''
	create an INET, STREAMing socket 
	creando a socket do tipo INET, STREAM
'''
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

'''
	bind the socket to a public  host, and a well-known port
	diz á bibloteca de soquetes que queremos enfileirar no máximo n requisições de conexão (normalmente o máximo)
'''
n = 5
server_socket.listen(n)

while True:
	'''
		#accept connections from outside
	'''
	(clientsocket, address) =  server_socket.accept()
	
	'''
		now do something with the clientsocket
		in  this case, we'll pretend this is a theareaded server
	'''
	ct = client_thread(clientsocket)
	ct.run()

