# Exercício 2: Servidor Echo (UDP)
# INTEGRANTES: João Gabriel Barbosa Freire, João Vitor Almeida Silva e Marcos Vinicius Santos Cruz

import socket

# Configuração do servidor
HOST = ''  # Endereço vazio = todos os interface
PORT = 6000  # Porta para execurar
MAX_SIZE = 65507  # Tamanho máximo UDP (64KB - cabeçalho)
TIMEOUT = 10  # 10 segundos sem atividade


def main():
    # cria sockect UDP (SOCK_DGRAM)
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.bind((HOST, PORT))
        s.settimeout(TIMEOUT)  # Configura timeout
        print(
            f"Servidor UDP ouvindo em {PORT}... Encerrando após {TIMEOUT} segundos de inatividade.")

        try:
            while True:
                try:
                    # recebe dados e endereço do cliente
                    data, addr = s.recvfrom(MAX_SIZE)
                    mensagem = data.decode('utf-8')
                    print(f"Recebido de {addr}: {mensagem}")
                    # envia ECO de volta
                    s.sendto(data, addr)

                #tratamento de erros
                except socket.timeout:              # Mata o processo para evitar zumbis
                    print(
                        f"Nenhuma mensagem recebida em {TIMEOUT} segundos. Encerrando...")
                    break
                except Exception as e:              # Permite que o servidor não quebre em caso de erros genericos
                    print(f"Erro inesperado: {e}")
                    break

        except KeyboardInterrupt:
            print("Servidor ocioso interrompido.")


if __name__ == "__main__":
    main()
