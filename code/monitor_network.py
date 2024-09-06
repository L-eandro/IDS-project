import psutil
import time
from prometheus_client import start_http_server, Gauge

# Cria métricas Prometheus
network_sent_metric = Gauge('network_bytes_sent', 'Total bytes sent over the network')
network_recv_metric = Gauge('network_bytes_recv', 'Total bytes received over the network')

def monitor_network():
    # Obtém o tráfego de rede
    net_io = psutil.net_io_counters()

    # Atualiza as métricas do Prometheus
    network_sent_metric.set(net_io.bytes_sent)
    network_recv_metric.set(net_io.bytes_recv)

if __name__ == '__main__':
    # Inicia o servidor HTTP para expor as métricas na porta 8000
    start_http_server(8000)

    # Coleta métricas a cada 5 segundos
    while True:
        monitor_network()
        time.sleep(5)
