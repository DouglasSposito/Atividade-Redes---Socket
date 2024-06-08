
import socket
def client(host = 'localhost', port=8082): 
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    
    server_address = (host, port) 
    print ("Conectando em %s na porta %s" % server_address) 
    sock.connect(server_address) 
    
    msn = input("Digite aqui a mensagem a ser enviada: ")
    try: 
        
        print ("Enviando: %s" % mensagem) 
        sock.sendall(mensagem.encode('utf-8')) 
        
        # Tratando a resposta 
        amount_received = 0 
        amount_expected = len(mensagem) 
        while amount_received < amount_expected: 
            data = sock.recv(16) 
            amount_received += len(data) 
            print ("Recebido: %s" % data) 
    except socket.error as e: 
        print ("Erro no socket: %s" %str(e)) 
    except Exception as e: 
        print ("Excecao generica: %s" %str(e)) 
    decisao = int(input("Deseja fechar a conexão ? \n 1 Sim \n 2 Não \n"))
    if decisao == 1:
        print ("Fechando conexao com o servidor.") 
        sock.close()
    else:
        msn = input("Digite uma nova mensagem")
    
                  
client()