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
s.bind((TCP_IP, TCP_PORT))
s.listen(1)
print("Executando servidor...")
while True:
    conn, addr = s.accept()
    print ('Cliente: ', addr)
    while True:
        print("==================================================")
        data = conn.recv(BUFFER_SIZE)
        if not data: break
        print ("Mensagem em string: ", data.decode())
        print("Digite a mensagem para o cliente...")
        mensagemDeVolta = input()
        conn.send(mensagemDeVolta.encode())
    print ('Finalizando conexao do cliente', addr)
    conn.close()