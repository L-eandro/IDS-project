from prometheus_client import start_http_server, Gauge
import random
import time
import requests

attack_count = Gauge('attack_count', 'Número de ataques por IP', ['ip', 'country'])


def get_ip_location(ip):
    try:
        response = requests.get(f'http://ip-api.com/json/{ip}').json()
        return response['country']
    except Exception as e:
        return "Unknown"


def simulate_attacks():
    ip_list = [
        '192.168.0.1', '203.0.113.5', '198.51.100.14', '172.16.254.1', '203.0.113.20'
    ]

    while True:
        attacked_ip = random.choice(ip_list)
        country = get_ip_location(attacked_ip)

        attack_count.labels(ip=attacked_ip, country=country).inc()

        time.sleep(random.randint(1, 5))


if __name__ == '__main__':
    start_http_server(8000)

    simulate_attacks()
