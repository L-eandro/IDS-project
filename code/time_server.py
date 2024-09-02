from prometheus_client import start_http_server, Gauge
import time

# Criação de uma métrica Gauge para medir o tempo de execução
execution_start_time = time.time()
execution_time_gauge = Gauge('server_uptime_seconds', 'Tempo total de execução do servidor em segundos')

def update_execution_time():
    # Atualiza o valor da métrica com o tempo total de execução
    current_time = time.time()
    uptime = current_time - execution_start_time
    execution_time_gauge.set(uptime)

if __name__ == '__main__':
    # Inicia o servidor de métricas na porta 8000
    start_http_server(8000)
    print("Servidor de métricas Prometheus iniciado na porta 8000")

    try:
        while True:
            # Atualiza o tempo de execução a cada 10 segundos
            update_execution_time()
            time.sleep(10)
    except KeyboardInterrupt:
        print("Servidor encerrado")
