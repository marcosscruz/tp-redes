# Exercício 1: Cliente-Servidor (TCP)
# INTEGRANTES: João Gabriel Barbosa Freire, João Vitor Almeida Silva e Marcos Vinicius Santos Cruz

import socket

# Configuração do servidor
HOST = ''  # Endereço vazio = todos os interface
PORT = 6000  # Porta para execurar
MAX_SIZE = 65507  # Tamanho máximo UDP (64KB - cabeçalho)


def main():
    # cria sockect UDP (SOCK_DGRAM)
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.bind((HOST, PORT))
        print(f"Servidor UDP ouvindo em {PORT}...")

        while True:
            # recebe dados e endereço do cliente
            data, addr = s.recvfrom(MAX_SIZE)
            mensagem = data.decode('utf-8')
            print(f"Recebido de {addr}: {mensagem}")

            # envia eco de volta
            s.sendto(data, addr)


if __name__ == "__main__":
    main()
