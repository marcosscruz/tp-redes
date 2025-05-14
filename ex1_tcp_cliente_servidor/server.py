# Exercício 1: Cliente-Servidor (TCP)
# INTEGRANTES: João Gabriel Barbosa Freire, João Vitor Almeida Silva e Marcos Vinicius Santos Cruz

import socket # soquete é a combinção de um IP com um nº de PORTA
import threading


HOST = 'localhost'
PORTA = 50000 # definir o nº da porta elevado para não interferir em outros serviços

soquete = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # objeto soquete criado
soquete.bind((HOST, PORTA)) # vinculando os valores ao objeto
soquete.listen() # colocando o objeto no modo de escuta
print("Aguardando conexão.")

conexao, endereco = soquete.accept() # aceitando a conexão 
print(f"Conectado: {endereco}")

# laço para a troca de mensagens entre o cliente e o servidor
while True:
    data = conexao.recv(1024)
    if not data:
        print("Encerrando conexão.")
        conexao.close()
        break
    conexao.sendall(data)
