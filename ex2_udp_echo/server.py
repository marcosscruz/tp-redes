# Exercício 2: Servidor Echo (UDP)
# INTEGRANTES: João Gabriel Barbosa Freire, João Vitor Almeida Silva e Marcos Vinicius Santos Cruz

import socket

# Configuração do servidor
HOST = '127.0.0.1'  # Aceita apenas conexões da própria máquina (localhost)
PORT = 6000  # Porta para execurar
MAX_SIZE = 65507  # Tamanho máximo UDP (64KB - cabeçalho)
TIMEOUT = 15  # 15 segundos sem atividade


def main():
    # cria sockect UDP (SOCK_DGRAM) usando IPv4 (AF_INET)
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.bind((HOST, PORT))  # Associa socket ao endereço e porta

        s.settimeout(TIMEOUT)  # Configura timeout
        print(
            f"Servidor UDP ouvindo em {PORT}... Encerrando após {TIMEOUT} segundos de inatividade.")

        try:
            # Loop principal do servidor
            while True:
                try:
                    # recebe dados e endereço do cliente
                    data, addr = s.recvfrom(MAX_SIZE)
                    # Decodifica mensagem UTF-8
                    mensagem = data.decode('utf-8')
                    # Exibe mensagem recebida
                    print(f"Recebido de {addr}: {mensagem}")
                    # envia ECO de volta
                    s.sendto(data, addr)

                # tratamento de erros
                except socket.timeout:                                          # Timeout de inatividade
                    print(
                        f"Nenhuma mensagem recebida em {TIMEOUT} segundos. Encerrando...")
                    break
                except Exception as e:                                          # Erros genéricos
                    print(f"Erro inesperado: {e}")
                    break

        except KeyboardInterrupt:                                               # Captura interrupção por teclado
            print("Servidor interrompido.")


if __name__ == "__main__":
    # Ponto de entrada do programa
    main()
