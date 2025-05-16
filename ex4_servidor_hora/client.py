# Exercício 4: Servidor e Cliente Multithread
# INTEGRANTES: João Gabriel Barbosa Freire, João Vitor Almeida Silva e Marcos Vinicius Santos Cruz
import socket # Importa a biblioteca socket, usada para comunicação de rede (cliente-servidor)
import threading
import time

# Define a função cliente_hora que conecta a um servidor para receber a hora atual.
def cliente_hora(host='localhost', port=700): # Define o host (endereço) e a porta padrão
    try: # Inicia um bloco try para capturar e tratar erros de conexão

        # Cria um socket TCP/IP (AF_INET = IPv4, SOCK_STREAM = TCP)
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.connect((host, port))  # Conecta ao servidor usando o endereço e porta informados
            print(f"Conectado ao servidor {host}:{port}") # Exibe no console que a conexão foi realizada com sucesso

            sock.sendall(b"hora") # Envia uma mensagem qualquer para o servidor (nesse caso, "hora"),Isso serve apenas para ativar a resposta do servidor

            # Espera e recebe a resposta do servidor (até 1024 bytes), decodificando de bytes para string
            time_data = sock.recv(1024).decode('utf-8')  
            print(f"Hora recebida do servidor: {time_data}") # Exibe a hora recebida no console

    # Caso o servidor não esteja rodando ou recuse a conexão        
    except ConnectionRefusedError:
        print("Não foi possível conectar ao servidor. Verifique se o servidor está rodando.")

    # Captura qualquer outro erro e exibe a mensagem    
    except Exception as e:
        print(f"Erro no cliente: {str(e)}")

def main():
    num_clientes = 5  # Número de clientes simultâneos a serem simulados
    threads = []  # Lista para armazenar as threads dos clientes

    # Cria e inicia as threads dos clientes
    for i in range(num_clientes):
        thread = threading.Thread(target=cliente_hora, args=(i,))  # Cria uma thread para executar a função cliente_hora com o número do cliente
        threads.append(thread)  # Adiciona a thread criada à lista de threads
        thread.start()  # Inicia a execução da thread (cliente se conecta ao servidor)
        time.sleep(0.1)  # Aguarda 0.1 segundo antes de iniciar a próxima conexão para evitar sobrecarga instantânea no servidor

    # Aguarda todas as threads terminarem antes de encerrar o programa
    for thread in threads:
        thread.join()  # Espera a thread atual finalizar sua execução
        
# Verifica se este arquivo está sendo executado diretamente
if __name__ == "__main__":
    main() # Chama a função
