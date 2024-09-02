from prometheus_client import start_http_server, Gauge
from ping3 import ping
import time

# Definir o endereço do servidor alvo
TARGET_SERVER = "http://dados.recife.pe.gov.br/"  # Altere para o IP ou domínio do servidor que deseja monitorar

# Criar uma métrica Gauge para o status do servidor
SERVER_STATUS = Gauge('server_status', 'Shows whether the target server is up (1) or down (0)')

def check_server():
    try:
        response = ping(TARGET_SERVER, timeout=2)  # Timeout de 2 segundos
        if response is None:
            SERVER_STATUS.set(0)  # Servidor está offline
        else:
            SERVER_STATUS.set(1)  # Servidor está online
    except Exception as e:
        SERVER_STATUS.set(0)  # Em caso de erro, considerar o servidor como offline

if __name__ == '__main__':
    start_http_server(8000)  # Inicia o servidor na porta 8000 para expor as métricas
    while True:
        check_server()
        time.sleep(30)  # Verifica a cada 30 segundos
