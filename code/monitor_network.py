import psutil
import time
from prometheus_client import start_http_server, Gauge


network_sent_metric = Gauge('network_bytes_sent', 'Total bytes sent over the network')
network_recv_metric = Gauge('network_bytes_recv', 'Total bytes received over the network')

def monitor_network():

    net_io = psutil.net_io_counters()


    network_sent_metric.set(net_io.bytes_sent)
    network_recv_metric.set(net_io.bytes_recv)

if __name__ == '__main__':

    start_http_server(8000)


    while True:
        monitor_network()
        time.sleep(5)
