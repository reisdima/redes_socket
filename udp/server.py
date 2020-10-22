import socket
import struct

UDP_IP = "127.0.0.1"
UDP_PORT = 5005
BUFFER_SIZE = 1024

print("==================================================")
print('Propriedades do servidor:')
print('Porta do servidor: {}'.format(UDP_PORT))
print('Ip do servidor: {}'.format(UDP_IP))
print('Tamanho do buffer (número de bytes): {}'.format(BUFFER_SIZE))
print("==================================================")

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))

print("Executando servidor...")
while True:
    data, addr = sock.recvfrom(BUFFER_SIZE) # buffer size is 1024 bytes
    print('=======================================')
    print('Bytes recebidos: {}'.format(data))
    try:
        print('Tentando realizar a operação...')
        result = eval(data)
        print("Resultado: {}".format(result))
        resultString = str(result).encode()
        sent = sock.sendto(resultString, addr)
        print ("Enviado '{}' bytes para {}".format(sent, addr))
    except:
        print("A operação não é válida")
        sent = sock.sendto(b"A operacao %s nao e valida" % data , addr)