import nmap
import logging
from prometheus_client import Gauge, start_http_server


logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


open_ports_gauge = Gauge('vulnerability_open_ports', 'Número de portas abertas detectadas', ['port'])


def start_nmap_prometheus_server():
    logger.info("Iniciando o servidor Prometheus na porta 8001 para Nmap.")
    start_http_server(8001)


def scan_vulnerabilities(target):
    nm = nmap.PortScanner()
    logger.info(f"Iniciando escaneamento do alvo: {target}")


    scan_result = nm.scan(target, arguments='-sV')


    for host in scan_result['scan']:
        for port, data in scan_result['scan'][host]['tcp'].items():
            state = data['state']
            service = data.get('name', 'unknown')
            version = data.get('version', 'unknown')

            if state == 'open':
                logger.info(f"Porta {port}/tcp aberta - Serviço: {service} - Versão: {version}")
                open_ports_gauge.labels(port=port).inc()
