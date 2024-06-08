import socket
import threading

# Configurações do servidor
host = '127.0.0.1'
port = 65432

# Inicializa o socket do servidor
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

# Lista para manter as conexões dos clientes
clients = []
nicknames = []

# Envia a mensagem para todos os clientes conectados
def broadcast(message):
    for client in clients:
        client.send(message)

# Lida com as mensagens dos clientes
def handle(client):
    while True:
        try:
            # Recebe a mensagem do cliente
            message = client.recv(1024)
            broadcast(message)
        except:
            # Remove e fecha a conexão se algo der errado
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            broadcast(f'{nickname} saiu do chat!'.encode('utf-8'))
            nicknames.remove(nickname)
            break

# Recebe conexões de novos clientes
def receive():
    while True:
        client, address = server.accept()
        print(f"Conectado com {str(address)}")

        # Solicita e armazena o apelido do cliente
        client.send('NICK'.encode('utf-8'))
        nickname = client.recv(1024).decode('utf-8')
        nicknames.append(nickname)
        clients.append(client)

        # Imprime e transmite o apelido do novo cliente
        print(f'Apelido do cliente é {nickname}')
        broadcast(f'{nickname} entrou no chat!'.encode('utf-8'))
        client.send('Conectado ao servidor!'.encode('utf-8'))

        # Inicia o tratamento de mensagens em uma nova thread
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

print("Servidor está ouvindo...")
receive()
