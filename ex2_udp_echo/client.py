# Exercício 2: Cliente-Servidor (TCP)
# INTEGRANTES: João Gabriel Barbosa Freire, João Vitor Almeida Silva e Marcos Vinicius Santos Cruz

import socket

# Configurações do cliente
SERVER_IP = 'localhost'  # IP do servidor
SERVER_PORT = 6000  # Porta do servidor com número elevado para não atrapalhar outras aplicações
MAX_SIZE = 65507  # Tamanho máximo UDP
TIMEOUT = 1  # 1 segundo de timeout
MAX_ATTEMPTS = 3  # Tentativas de reenvio


def main():
    # Cria socket UDP
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.settimeout(TIMEOUT)
        server_adress = (SERVER_IP, SERVER_PORT)

        print("Cliente UDP. Digite 'sair' para encerrar.")

        while True:
            # Entrada do usuário
            mensagem = input("Mensagem: ")
            if mensagem.lower() == 'sair':
                break

            # Valida tamanho da mensagem
            data = mensagem.encode('utf-8')
            if len(data) > MAX_SIZE:
                print(f"Erro: Mensagem excede {MAX_SIZE} bytes!")
                continue

            # Envio com tratamento de erros
            attempts = 0
            while attempts < MAX_ATTEMPTS:
                try:
                    s.sendto(data, server_adress)
                    response, _ = s.recvfrom(MAX_SIZE)
                    print(f"Eco: {response.decode('utf-8')}")
                    break
                except socket.timeout:
                    attempts += 1
                    print(
                        f"Timeout ({attempts}/{MAX_ATTEMPTS}). Reenviando...")
                except Exception as e:
                    print(f"Erro: {e}")
                    break
                else:
                    print("Servidor não respondeu após várias tentativas.")


if __name__ == "__main__":
    main()
