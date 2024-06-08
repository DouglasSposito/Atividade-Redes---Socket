import socket
import threading

# Escolha um apelido
nickname = input("Escolha seu apelido: ")

# Conecta ao servidor
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 65432))

# Escuta as mensagens do servidor e envia o apelido
def receive():
    while True:
        try:
            # Recebe a mensagem do servidor
            message = client.recv(1024).decode('utf-8')
            if message == 'NICK':
                client.send(nickname.encode('utf-8'))
            else:
                print(message)
        except:
            # Fecha a conexão se algo der errado
            print("Ocorreu um erro!")
            client.close()
            break

# Envia mensagens para o servidor
def write():
    while True:
        message = f'{nickname}: {input("")}'
        client.send(message.encode('utf-8'))

# Inicia as threads para escutar e escrever
receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()
