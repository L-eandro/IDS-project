import time
import logging
import requests
import pandas as pd
from logging.handlers import SysLogHandler
from scapy.all import sniff
from scapy.layers.inet import ICMP, TCP
from prometheus_client import start_http_server, Counter, Gauge
from statsmodels.tsa.arima.model import ARIMA

# Configuração do SysLogHandler para enviar logs ao syslog (substitua localhost pelo endereço correto)
syslog_handler = SysLogHandler(address=('localhost', 514))
formatter = logging.Formatter('%(asctime)s - %(message)s')
syslog_handler.setFormatter(formatter)

# Configuração do logger
logger = logging.getLogger()
logger.setLevel(logging.INFO)
logger.addHandler(syslog_handler)

# Definição das métricas do Prometheus
http_requests_total = Counter('http_requests_total', 'Número total de requisições HTTP')
response_duration_seconds = Gauge('http_response_duration_seconds', 'Duração da resposta HTTP em segundos')
intrusion_icmp_total = Counter('intrusion_icmp_total', 'Número de pacotes ICMP grandes')
intrusion_tcp_total = Counter('intrusion_tcp_total', 'Número de pacotes TCP com portas não padrão')
attack_prediction_alert = Counter('attack_prediction_alert', 'Alerta de previsão de ataque')

# Função para capturar e analisar pacotes de rede em tempo real
def packet_callback(packet):
    try:
        # Análise de pacotes ICMP
        if packet.haslayer(ICMP) and len(packet) > 1000:
            logger.warning(f"Pacote ICMP grande detectado: {packet.summary()}")
            intrusion_icmp_total.inc()

        # Análise de pacotes TCP
        if packet.haslayer(TCP):
            if packet[TCP].dport not in [80, 443]:  # Detecta portas TCP não padrão
                logger.info(f"Pacote TCP para porta não padrão detectado: {packet.summary()}")
                intrusion_tcp_total.inc()
    except Exception as e:
        logger.error(f"Erro ao processar pacote: {e}")

# Função para coletar dados históricos de ataques do site
def collect_historical_data():
    try:
        # URL para coleta de dados históricos do site
        url = "http://dados.recife.pe.gov.br/api/3/action/datastore_search?resource_id=<ID_DO_RECURSO>"  # Substitua pelo ID correto do recurso
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            # Convertendo para DataFrame (ajuste conforme a estrutura dos dados)
            records = data['result']['records']
            df = pd.DataFrame(records)
            logger.info("Dados históricos coletados com sucesso.")
            return df
        else:
            logger.error(f"Erro na coleta de dados históricos: {response.status_code} - {response.text}")
            return pd.DataFrame()
    except Exception as e:
        logger.error(f"Erro ao coletar dados históricos: {e}")
        return pd.DataFrame()

# Função para análise e previsão de possíveis ataques com dados históricos
def analyze_and_predict(df):
    try:
        # Ajuste do DataFrame com base nos dados históricos
        df['timestamp'] = pd.to_datetime(df['timestamp'])  # Ajuste conforme o nome do campo de tempo no DataFrame
        df.set_index('timestamp', inplace=True)

        # Exemplo: Filtrar dados de uma métrica relevante
        df = df['quantidade_ataques']  # Substitua pelo nome correto da coluna

        # Aplicação do modelo ARIMA para previsão de ataques
        model = ARIMA(df, order=(5, 1, 0))  # Parâmetros de ordem ajustáveis
        model_fit = model.fit()
        forecast = model_fit.forecast(steps=1)  # Prever o próximo ponto

        # Checar se a previsão indica um possível aumento em ataques
        if forecast[0] > df.mean() + 2 * df.std():  # Critério de alerta ajustável
            logger.warning(f"Alerta de previsão de ataque: previsão = {forecast[0]}")
            attack_prediction_alert.inc()
        else:
            logger.info(f"Previsão de ataques normal: {forecast[0]}")

    except Exception as e:
        logger.error(f"Erro na análise e previsão de ataques: {e}")

# Função para coletar dados em tempo real do site
def fetch_external_data():
    try:
        # URL da API para coletar dados em tempo real
        url = "http://dados.recife.pe.gov.br/dataset/8b5a0fd4-5f6e-4bde-8cf0-253900b81132/resource/1493bd03-da92-4d06-be3d-f49a803b7660/download/metadados_cras.json"
        start_time = time.time()
        response = requests.get(url)
        response_duration = time.time() - start_time

        # Atualiza as métricas do Prometheus
        http_requests_total.inc()
        response_duration_seconds.set(response_duration)

        if response.status_code == 200:
            data = response.json()
            logger.info(f"Dados recuperados com sucesso: {data}")
        else:
            logger.error(f"Erro na requisição: {response.status_code} - {response.text}")

    except Exception as e:
        logger.error(f"Erro ao recuperar dados da API: {e}")

# Função principal para iniciar o monitoramento e análise
def main():
    start_http_server(8000)  # Inicia o servidor HTTP do Prometheus na porta 8000

    # Coleta e análise de dados históricos na inicialização
    historical_data = collect_historical_data()
    if not historical_data.empty:
        analyze_and_predict(historical_data)

    # Inicia a captura de pacotes na interface de rede especificada
    sniff(iface="Wi-Fi 2", prn=packet_callback, store=0)

    # Coleta dados de fontes externas em intervalos regulares
    while True:
        fetch_external_data()
        time.sleep(60)  # Ajuste o tempo de coleta conforme necessário

if __name__ == "__main__":
    main()
