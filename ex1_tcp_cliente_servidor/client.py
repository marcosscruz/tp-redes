# Exercício 1: Cliente-Servidor (TCP)
# INTEGRANTES: João Gabriel Barbosa Freire, João Vitor Almeida Silva e Marcos Vinicius Santos Cruz

import socket

HOST = '127.0.0.1'
PORTA = 50000

soquete = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
soquete.connect((HOST, PORTA)) # pedindo a conexão com o servirdor
mensagem = input("Digite sua mensagem: ").strip()

# garantindo uma mensagem válida
if mensagem:
    soquete.sendall(mensagem.encode()) # eviando mnsg para o sever e garantindo que chegue no formato correto
    data = soquete.recv(1024)
    print(f"Resposta: {data.decode()}") # exibindo que a conexão realemnte aconteceu
else:
    print("Mensagem vazia ou n enviada.")
