from prometheus_client import Counter


intrusion_attempts = Counter('network_intrusion_attempts', 'Count of network intrusion attempts', ['source_ip'])

def simulate_intrusion_detection():

    ips = ["192.168.1.1", "192.168.1.2", "192.168.1.3"]

    for ip in ips:

        intrusion_attempts.labels(source_ip=ip).inc()

    print(f"Tentativas de intrusão detectadas: {len(ips)} IPs.")
