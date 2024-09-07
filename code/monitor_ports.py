import psutil
import socket
from prometheus_client import start_http_server, Gauge
import time


tcp_ports_metric = Gauge('tcp_ports', 'Number of TCP ports open')
udp_ports_metric = Gauge('udp_ports', 'Number of UDP ports open')


def collect_port_data():
    tcp_ports = set()
    udp_ports = set()


    for conn in psutil.net_connections():
        if conn.status == 'LISTEN':
            if conn.type == socket.SOCK_STREAM:
                tcp_ports.add(conn.laddr.port)
            elif conn.type == socket.SOCK_DGRAM:
                udp_ports.add(conn.laddr.port)


    tcp_ports_metric.set(len(tcp_ports))
    udp_ports_metric.set(len(udp_ports))


if __name__ == '__main__':

    start_http_server(8000)

    while True:
        collect_port_data()
        time.sleep(5)
