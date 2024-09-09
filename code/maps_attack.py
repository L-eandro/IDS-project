import random
from prometheus_client import Counter, Gauge

attack_counter = Counter('map_attack_generated_total', 'Total de ataques gerados no mapa', ['country', 'attack_type'])
attack_latitude = Gauge('attack_latitude', 'Latitude do ataque', ['country', 'attack_type'])
attack_longitude = Gauge('attack_longitude', 'Longitude do ataque', ['country', 'attack_type'])


def random_attack():
    countries = ["United States", "Brazil", "Germany", "India", "China", "Russia"]
    attack_types = ["DDoS", "Phishing", "Malware"]

    country = random.choice(countries)
    attack_type = random.choice(attack_types)
    latitude = random.uniform(-90, 90)
    longitude = random.uniform(-180, 180)

    attack_counter.labels(country=country, attack_type=attack_type).inc()
    attack_latitude.labels(country=country, attack_type=attack_type).set(latitude)
    attack_longitude.labels(country=country, attack_type=attack_type).set(longitude)

    print(f"Ataque {attack_type} gerado em {country} ({latitude}, {longitude})")