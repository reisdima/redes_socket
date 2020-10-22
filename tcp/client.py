import socket


TCP_IP = '127.0.0.1'
TCP_PORT = 3030
BUFFER_SIZE = 1024

print("==================================================")
print('Propriedades do servidor:')
print('Porta do servidor: {}'.format(TCP_PORT))
print('Ip do servidor: {}'.format(TCP_IP))
print('Tamanho do buffer (número de bytes): {}'.format(BUFFER_SIZE))
print("==================================================")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    s.connect((TCP_IP, TCP_PORT))
except:
    print("Não foi possível se conectar com o servidor.")
    exit()
while True:
    try:
        print("==================================================")
        print("Digite uma mensagem...")
        mensagem = input().encode()
        if mensagem == b'exit()':
            s.close()
            break
        s.send(mensagem)
        print("Aguardando mensagem do servidor...")
        data = s.recv(BUFFER_SIZE)
        print ("Mensagem recebida do servidor: ", data.decode())
    except:
        print("Conexao interrompida com o servidor")
        s.close()
        break
    
