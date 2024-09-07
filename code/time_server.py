from prometheus_client import start_http_server, Gauge
import time


execution_start_time = time.time()
execution_time_gauge = Gauge('server_uptime_seconds', 'Tempo total de execução do servidor em segundos')

def update_execution_time():

    current_time = time.time()
    uptime = current_time - execution_start_time
    execution_time_gauge.set(uptime)

if __name__ == '__main__':

    start_http_server(8000)
    print("Servidor de métricas Prometheus iniciado na porta 8000")

    try:
        while True:

            update_execution_time()
            time.sleep(10)
    except KeyboardInterrupt:
        print("Servidor encerrado")
