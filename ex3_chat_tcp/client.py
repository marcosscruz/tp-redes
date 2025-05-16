# Exercício 3: Chat em Rede (TCP)
# INTEGRANTES: João Gabriel Barbosa Freire, João Vitor Almeida Silva e Marcos Vinicius Santos Cruz

import socket
import threading

HOST = '127.0.0.1'
PORT = 50001

def recebe_mensagens(sock):
    while True:
        try:
            data = sock.recv(1024)
            if not data:
                break
            print(f"recebido: {data.decode()}")
        except: # captura qualquer exceção que ocorra durante a recepção de dados
            break

# objeto soquete criado e garantido que o socket seja fechado automaticamente com uso do with 
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as soquete:
    soquete.connect((HOST, PORT))
    # cria uma thread para receber mensagens do servidor, rodando a função recebe_mensagens
    threading.Thread(target=recebe_mensagens, args=(s, ), daemon=True).start()

    while True:
        mensagem = input()
        if mensagem.lower() == 'sair': # condição de saida do chat
            break
        soquete.sendall(mensagem.encode()) # envia a mensagem codificada para o servidor