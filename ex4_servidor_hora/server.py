# Exercício 4: Servidor e Cliente Multithread
# INTEGRANTES: João Gabriel Barbosa Freire, João Vitor Almeida Silva e Marcos Vinicius Santos Cruz
import socket  # Importa biblioteca para comunicação de rede
import threading  # Importa biblioteca para uso de threads (execução paralela)
import datetime  # Importa biblioteca para pegar a hora atual

HOST = '0.0.0.0'  # Escuta em todas as interfaces de rede disponíveis
PORT = 700  # Porta escolhida para o servidor escutar

# Função que lida com cada cliente individualmente
def handle_client(conn, addr):
    print(f"[LOG] Conexão de {addr}")  # Loga o endereço do cliente que se conectou
    try:
        while True:  # Loop para manter a conexão enquanto o cliente estiver enviando dados
            data = conn.recv(1024)  # Recebe até 1024 bytes do cliente
            if not data:  # Se nada for recebido, o cliente desconectou
                break
            current_time = datetime.datetime.now().strftime("%H:%M:%S")  # Pega a hora atual no formato HH:MM:SS
            print(f"[LOG] Enviando hora para {addr}: {current_time}")  # Loga a hora que será enviada
            conn.sendall(current_time.encode())  # Envia a hora codificada para o cliente
    except Exception as e:  # Se ocorrer algum erro com esse cliente
        print(f"[ERRO] Falha com {addr}: {e}")  # Loga o erro
    finally:
        conn.close()  # Fecha a conexão com o cliente
        print(f"[LOG] Conexão encerrada: {addr}")  # Loga o encerramento da conexão

# Função principal que inicia o servidor
def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:  # Cria um socket TCP
        s.bind((HOST, PORT))  # Associa o socket ao endereço e porta definidos
        s.listen()  # Coloca o socket em modo de escuta (aguardando conexões)
        print(f"[SERVIDOR] Servidor rodando em {HOST}:{PORT}")  # Mensagem informando que o servidor está ativo

        while True:  # Loop principal do servidor
            conn, addr = s.accept()  # Aceita uma nova conexão e obtém o socket e endereço do cliente
            # Cria uma nova thread para lidar com esse cliente, sem bloquear o servidor
            thread = threading.Thread(target=handle_client, args=(conn, addr), daemon=True)
            thread.start()  # Inicia a thread

# Inicia o servidor se o arquivo for executado diretamente
if __name__ == "__main__":
    start_server()
