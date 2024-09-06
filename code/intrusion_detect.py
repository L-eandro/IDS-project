from prometheus_client import start_http_server, Counter
import time

# Métrica para contar as tentativas de intrusão
intrusion_attempts = Counter('network_intrusion_attempts', 'Count of network intrusion attempts', ['source_ip'])

def simulate_intrusion_detection():
    # Simule a detecção de uma tentativa de intrusão
    # Normalmente, você integraria isso com seu IDS
    ips = ["192.168.1.1", "192.168.1.2", "192.168.1.3"]
    for ip in ips:
        intrusion_attempts.labels(source_ip=ip).inc()

if __name__ == "__main__":
    # Inicia o servidor HTTP no localhost na porta 8000
    start_http_server(8000)

    # Simulação de detecção de intrusão a cada 5 segundos
    while True:
        simulate_intrusion_detection()
        time.sleep(5)
