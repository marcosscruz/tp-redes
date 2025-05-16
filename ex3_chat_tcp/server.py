# Exercício 3: Chat em Rede (TCP)
# INTEGRANTES: João Gabriel Barbosa Freire, João Vitor Almeida Silva e Marcos Vinicius Santos Cruz

import socket
import threading

HOST = 'localhost'
PORT = 51000

clientes = [] # lista para armazenar as conexões dos clientes

def manipula_client(conexao, endereco):
    print(f"{endereco} conectado")
    while True: # loop para verificar se há dados
        try:
            data = conexao.recv(1024)
            if not data:
                break
            for cliente in clientes:
                if cliente != conexao:
                    cliente.sendall(data)
        except: # captura qualquer exceção que ocorra durante a recepção de dados
            break
    conexao.close()
    clientes.remove(conexao) # remove o cliente da lista de clientes
    print(f"{endereco} desconectado")

# objeto soquete criado e garantido que o socket seja fechado automaticamente com uso do with
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as soquete:
    soquete.bind((HOST, PORT))
    soquete.listen(2) # colocando o objeto no modo de escuta, permitindo até 2 conexões
    print(f"ouvindo a porta: {PORT}")
    while len(clientes) < 2: # aceita conexão até que 2 clientes estejam conectados
        conexao, endereco = soquete.accept()
        clientes.append(conexao) # adiciona a conexão a lista de clientes 
        thread = threading.Thread(target=manipula_client, args=(conexao, endereco))
        thread.start()