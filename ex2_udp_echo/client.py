# Exercício 2: Servidor Echo (UDP)
# INTEGRANTES: João Gabriel Barbosa Freire, João Vitor Almeida Silva e Marcos Vinicius Santos Cruz

import socket

# Configurações do cliente
SERVER_IP = 'localhost'  # IP do servidor (local: 127.0.0.1)
# Porta do servidor com número elevado para não atrapalhar outras aplicações
SERVER_PORT = 6000  # Porta padrão do servidor UDP
MAX_SIZE = 65507  # Tamanho máximo de um datagrama UDP (64KB - cabeçalho)
TIMEOUT = 1  # 1 segundo de timeout
MAX_ATTEMPTS = 3  # Tentativas de reenvio


def main():
    # Cria socket UDP
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:  # AF_INET = IPv4
        # Configura timeout para operações de socket
        s.settimeout(TIMEOUT)
        # Tupla com IP/porta do servidor
        server_adress = (SERVER_IP, SERVER_PORT)

        # Mensagem inicial
        print("Cliente UDP. Digite 'sair' para encerrar.")

        while True:                                              # Loop principal para entrada contínua
            # Entrada do usuário
            # Solicita mensagem ao usuário
            mensagem = input("Mensagem: ")
            if mensagem.lower() == 'sair':                       # Condição de saída
                break                                            # Encerra o loop

            # Valida tamanho da mensagem
            # Codifica mensagem para bytes
            data = mensagem.encode('utf-8')
            # Verifica se excede o tamanho máximo determinado para datagrama
            if len(data) > MAX_SIZE:
                print(f"Erro: Mensagem excede {MAX_SIZE} bytes!")
                continue                                        # Pula para a próxima iteração do loop

                # Envio com tratamento de erros
            attempts = 0                                        # Contador de tentativas
            while attempts < MAX_ATTEMPTS:                      # Loop de tentativas
                try:
                    # Envia dados para o servidor
                    s.sendto(data, server_adress)
                    # Aguarda resposta (ignora endereço)
                    response, _ = s.recvfrom(MAX_SIZE)
                    # Exibe resposta decodificada
                    # Decodifica mensagem de bytes
                    print(f"Eco: {response.decode('utf-8')}")
                    break                                       # Se bem sucedido sai do loop
                except socket.timeout:                          # Caso o servidor não responda
                    attempts += 1                               # Incrementa contador
                    # Log
                    print(
                        f"Timeout ({attempts}/{MAX_ATTEMPTS}). Reenviando...")
                except ConnectionResetError:
                    attempts += 1
                    print(f"Tentativa {attempts}/{MAX_ATTEMPTS}: Servidor inativo (porta fechada)")
                    if attempts == MAX_ATTEMPTS:
                        print("Servidor não respondeu após várias tentativas.")
                    continue
                # Captura outros erros (ex: conexão recusada)
                except Exception as e:
                    # Exibe mensagem de erro
                    print(f"Erro: {e}")
                    break                                       # Sai do loop em caso de erro crítico
            else:
                # Mensagem final
                print("Encerrando: Servidor não respondeu.")


if __name__ == "__main__":
    # Ponto de entrada do programa
    main()
