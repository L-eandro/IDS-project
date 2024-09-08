import folium
import random
import pycountry
import time
from prometheus_client import start_http_server, Counter


attack_counter = Counter('map_attack_generated_total', 'Total de ataques gerados no mapa')


def generate_random_attack():

    country = random.choice(list(pycountry.countries))


    coordinates = [random.uniform(-90, 90), random.uniform(-180, 180)]


    attack_type = random.choice(["DDoS", "Phishing", "Malware"])


    attack_counter.inc()

    return country.name, coordinates, attack_type



m = folium.Map(location=[0, 0], zoom_start=2)


start_http_server(8001)


while True:
    # Gera um ataque aleatório
    country, coordinates, attack_type = generate_random_attack()

    # Adiciona um marcador no mapa com o ataque
    folium.Marker(location=coordinates, popup=f"Ataque {attack_type} de {country}").add_to(m)


    m.save("mapa_ataques.html")


    time.sleep(5)
