# Exercício 1: Cliente-Servidor (TCP)
# INTEGRANTES: João Gabriel Barbosa Freire, João Vitor Almeida Silva e Marcos Vinicius Santos Cruz

import socket # soquete é a combinção de um IP com um nº de PORTA
import threading # modulo para cirar e manipular threads

HOST = 'localhost'
PORT = 50000 # definir o nº da porta elevado para não interferir em outros serviços

def manipula_client(conexao, endereco):
    print(f"conectado: {endereco}")    
    # laço para a troca de mensagens entre o cliente e o servidor
    while True:
        data = conexao.recv(1024)
        if not data:
            print("encerrando conexao.")
            break
        mensagem = data.decode().strip() # decodifica a mensagem recebida
        if mensagem:
            print(f"recebido de {endereco}: {mensagem}")
            conexao.sendall(b"mensagem recebida") # confirma recebimento
        else:
            conexao.sendall(b"mensagem vazi n permitida")
    conexao.close()
    print(f"encerrando conexao: {endereco}")
    
# objeto soquete criado e garantido que o socket seja fechado automaticamente com uso do with
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as soquete: 
    soquete.bind((HOST, PORT)) # vinculando os valores ao objeto
    soquete.listen() # colocando o objeto no modo de escuta
    print(f"ouvidno a porta: {PORT}")
    while True:
        conexao, endereco = soquete.accept() # aceitando a conexão 
        thread = threading.Thread(target=manipula_client, args=(conexao, endereco)) # criando uma thread para mexer com o cliente
        thread.start()