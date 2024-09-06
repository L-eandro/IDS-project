import psutil
import socket  # Biblioteca padrão para acessar SOCK_STREAM e SOCK_DGRAM
from prometheus_client import start_http_server, Gauge
import time

# Define a métrica do Prometheus para contagem de portas abertas por protocolo
tcp_ports_metric = Gauge('tcp_ports', 'Number of TCP ports open')
udp_ports_metric = Gauge('udp_ports', 'Number of UDP ports open')


def collect_port_data():
    tcp_ports = set()
    udp_ports = set()

    # Percorre as conexões de rede para verificar quais portas estão abertas
    for conn in psutil.net_connections():
        if conn.status == 'LISTEN':  # Verifica se a conexão está escutando
            if conn.type == socket.SOCK_STREAM:  # Conexões TCP
                tcp_ports.add(conn.laddr.port)
            elif conn.type == socket.SOCK_DGRAM:  # Conexões UDP
                udp_ports.add(conn.laddr.port)

    # Atualiza as métricas
    tcp_ports_metric.set(len(tcp_ports))
    udp_ports_metric.set(len(udp_ports))


if __name__ == '__main__':
    # Inicia o servidor Prometheus na porta 8000
    start_http_server(8000)

    while True:
        collect_port_data()
        time.sleep(5)  # Coleta dados a cada 5 segundos
