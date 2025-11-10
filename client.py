import socket
import time
import random

HOST = '127.0.0.1'
PORT = 5000

# Conecta ao servidor
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

while True:
    # Simula temperatura
    temperatura = round(random.uniform(18.0, 35.0), 2)

    # Simula LED alternando a cada envio
    led_state = random.choice(["ON", "OFF"])

    mensagem = f"TEMP={temperatura}C | LED={led_state}"
    client_socket.send(mensagem.encode())

    time.sleep(2)  # espera 2 segundos entre envios
