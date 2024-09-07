from prometheus_client import start_http_server, Counter
import time


intrusion_attempts = Counter('network_intrusion_attempts', 'Count of network intrusion attempts', ['source_ip'])

def simulate_intrusion_detection():

    ips = ["192.168.1.1", "192.168.1.2", "192.168.1.3"]
    for ip in ips:
        intrusion_attempts.labels(source_ip=ip).inc()

if __name__ == "__main__":

    start_http_server(8000)


    while True:
        simulate_intrusion_detection()
        time.sleep(5)
