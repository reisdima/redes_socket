import socket
import struct

UDP_IP = "127.0.0.1"
UDP_PORT = 5005
print("==================================================")
print('Propriedades do servidor:')
print('Porta do servidor: {}'.format(UDP_PORT))
print('Ip do servidor: {}'.format(UDP_IP))
print("==================================================")


sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
try:
    print('Digite uma opração aritmética...')
    print("Por exemplo: 10 + 89")
    mensagem = input()
    sock.sendto(str.encode(mensagem), (UDP_IP, UDP_PORT))
    
    # Resposta obtida
    print ('Esperando resposta do servidor...')
    data, server = sock.recvfrom(4096)
    # print ("Bytes recebidos: {}".format(data))
    print ("Mensagem do servidor: {}".format(data.decode()))

finally:
    print ('Fechando socket do cliente...')
    sock.close()