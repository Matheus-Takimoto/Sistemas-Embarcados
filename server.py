import socket

HOST = '127.0.0.1'   # Endereço local
PORT = 5000          # Porta de comunicação

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen()

print(f"Servidor iniciado em {HOST}:{PORT}. Aguardando conexão...")

conn, addr = server_socket.accept()
print(f"Cliente conectado: {addr}")

while True:
    data = conn.recv(1024).decode()
    if not data:
        break
    
    print(f"[CLIENTE] {data}")

conn.close()
server_socket.close()
print("Conexão encerrada.")
