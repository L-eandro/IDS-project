import time
import logging
import requests
from logging.handlers import SysLogHandler
from prometheus_client import start_http_server, Counter, Gauge

# Configuração do SysLogHandler para enviar logs ao syslog
syslog_handler = SysLogHandler(address=('localhost', 514))  # Endereço e porta do syslog configurado no Loki
formatter = logging.Formatter('%(asctime)s - %(message)s')
syslog_handler.setFormatter(formatter)

# Configuração do logger
logger = logging.getLogger()
logger.setLevel(logging.INFO)
logger.addHandler(syslog_handler)

# Define as métricas do Prometheus
http_requests_total = Counter('http_requests_total', 'Número total de requisições HTTP')
response_duration_seconds = Gauge('http_response_duration_seconds', 'Duração da resposta HTTP em segundos')
data_gauge = Gauge('website_data_metric', 'Descrição da métrica de dados do site')

# Função para coletar dados de uma API externa
def fetch_external_data():
    try:
        # URL da API para recuperar dados específicos (ajuste conforme necessário)
        url = "ttps://www.virustotal.com/api/v3/urls/{id}"  # Substitua pelo endpoint correto
        
        # Faz a requisição HTTP para a API
        start_time = time.time()
        response = requests.get(url)
        response_duration = time.time() - start_time

        # Atualiza as métricas do Prometheus
        http_requests_total.inc()
        response_duration_seconds.set(response_duration)
        data_gauge.set(data)

        # Processa a resposta da API
        if response.status_code == 200:
            data = response.json()
            # Adicione lógica para processar os dados conforme necessário
            logger.info(f"Dados recuperados com sucesso: {data}")

        else:
            logger.error(f"Erro na requisição: {response.status_code} - {response.text}")

    except Exception as e:
        logger.error(f"Erro ao recuperar dados da API: {e}")

# Função principal
def main():
    start_http_server(8000)  # Inicia o servidor HTTP do Prometheus na porta 8000

    # Coleta dados de fontes externas em intervalos regulares
    while True:
        fetch_external_data()
        time.sleep(60)  # Coleta dados a cada 60 segundos

if __name__ == "__main__":
    main()