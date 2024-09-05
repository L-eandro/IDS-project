import requests
import pandas as pd
import time
from config_logger import logger
from prometheus_metrics import http_requests_total, response_duration_seconds

def collect_historical_data():
    try:
        url = "http://dados.recife.pe.gov.br/api/3/action/datastore_search?resource_id=<ID_DO_RECURSO>"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
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

def fetch_external_data():
    try:
        url = "http://dados.recife.pe.gov.br/dataset/8b5a0fd4-5f6e-4bde-8cf0-253900b81132/resource/1493bd03-da92-4d06-be3d-f49a803b7660/download/metadados_cras.json"
        start_time = time.time()
        response = requests.get(url)
        response_duration = time.time() - start_time

        http_requests_total.inc()
        response_duration_seconds.set(response_duration)

        if response.status_code == 200:
            data = response.json()
            logger.info("Dados recuperados com sucesso.")
        else:
            logger.error(f"Erro na requisição: {response.status_code} - {response.text}")

    except Exception as e:
        logger.error(f"Erro ao recuperar dados da API: {e}")
