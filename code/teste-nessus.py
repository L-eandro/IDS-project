import xml.etree.ElementTree as ET
from prometheus_client import start_http_server, Gauge
import time

# Define métricas Prometheus para cada nível de severidade
low_vuln_gauge = Gauge('vulnerabilities_low', 'Low severity vulnerabilities detected')
medium_vuln_gauge = Gauge('vulnerabilities_medium', 'Medium severity vulnerabilities detected')
high_vuln_gauge = Gauge('vulnerabilities_high', 'High severity vulnerabilities detected')
critical_vuln_gauge = Gauge('vulnerabilities_critical', 'Critical severity vulnerabilities detected')


# Função para analisar vulnerabilidades a partir de um arquivo .nessus (XML)
def analyze_nessus_file(file_path):
    # Carrega o arquivo .nessus (XML)
    tree = ET.parse(file_path)
    root = tree.getroot()

    # Inicializa contadores de vulnerabilidades por severidade
    low_vulns = 0
    medium_vulns = 0
    high_vulns = 0
    critical_vulns = 0

    # Itera sobre os resultados das vulnerabilidades
    for report in root.iter('ReportItem'):
        severity = int(report.get('severity'))

        # Atribui severidade de acordo com os níveis
        if severity == 0:
            continue  # Ignora vulnerabilidades informativas
        elif severity == 1:
            low_vulns += 1
        elif severity == 2:
            medium_vulns += 1
        elif severity == 3:
            high_vulns += 1
        elif severity == 4:
            critical_vulns += 1

    # Retorna o total de vulnerabilidades categorizadas por severidade
    return low_vulns, medium_vulns, high_vulns, critical_vulns


# Função para atualizar as métricas do Prometheus
def update_prometheus_metrics(file_path):
    low, medium, high, critical = analyze_nessus_file(file_path)

    low_vuln_gauge.set(low)
    medium_vuln_gauge.set(medium)
    high_vuln_gauge.set(high)
    critical_vuln_gauge.set(critical)
    print(f"Métricas atualizadas: Low={low}, Medium={medium}, High={high}, Critical={critical}")


def main():
    # Inicia o servidor HTTP para o Prometheus na porta 8000
    start_http_server(8000)
    print("Servidor Prometheus rodando na porta 8000...")

    # Arquivo Nessus exportado (modifique o caminho conforme necessário)
    nessus_file_path = 'C:\\Users\\João\\Documents\\MeusProjetos\\projeto\\IDS-project\\Others\\Varredura.nessus'

    # Atualiza as métricas periodicamente
    while True:
        update_prometheus_metrics(nessus_file_path)
        time.sleep(300)  # Atualiza as métricas a cada 5 minutos


if __name__ == "__main__":
    main()
