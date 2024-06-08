import socket

def server(host = 'localhost', port=8082):

    data_payload = 2048 
    
    sock = socket.socket(socket.AF_INET,  socket.SOCK_STREAM)
    
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    server_address = (host, port)
    print ("Iniciando o servidor no endereço %s e porta %s" % server_address)
    sock.bind(server_address)
    
    sock.listen(5) 
    i = 0
    while True: 
        print ("Aguardando mensagens de clientes")
        client, address = sock.accept() 
        data = client.recv(data_payload) 
        if data:
            print ("Dados: %s" %data)
            client.send(data)
            print ("enviando %s de volta para  %s" % (data, address))
        
            client.close()
            i+=1
            if i>=3: break           
server()