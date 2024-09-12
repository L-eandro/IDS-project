import xml.etree.ElementTree as ET
from prometheus_client import start_http_server, Gauge
import time


low_vuln_gauge = Gauge('vulnerabilities_low', 'Low severity vulnerabilities detected')
medium_vuln_gauge = Gauge('vulnerabilities_medium', 'Medium severity vulnerabilities detected')
high_vuln_gauge = Gauge('vulnerabilities_high', 'High severity vulnerabilities detected')
critical_vuln_gauge = Gauge('vulnerabilities_critical', 'Critical severity vulnerabilities detected')



def analyze_nessus_file(file_path):

    tree = ET.parse(file_path)
    root = tree.getroot()


    low_vulns = 0
    medium_vulns = 0
    high_vulns = 0
    critical_vulns = 0


    for report in root.iter('ReportItem'):
        severity = int(report.get('severity'))


        if severity == 0:
            continue
        elif severity == 1:
            low_vulns += 1
        elif severity == 2:
            medium_vulns += 1
        elif severity == 3:
            high_vulns += 1
        elif severity == 4:
            critical_vulns += 1


    return low_vulns, medium_vulns, high_vulns, critical_vulns



def update_prometheus_metrics(file_path):
    low, medium, high, critical = analyze_nessus_file(file_path)

    low_vuln_gauge.set(low)
    medium_vuln_gauge.set(medium)
    high_vuln_gauge.set(high)
    critical_vuln_gauge.set(critical)
    print(f"Métricas atualizadas: Low={low}, Medium={medium}, High={high}, Critical={critical}")


def main():

    start_http_server(8000)
    print("Servidor Prometheus rodando na porta 8000...")


    nessus_file_path = 'F:/Projeto-IDS/IDS-project/IDS-project/Others/Varredura.nessus'


    while True:
        update_prometheus_metrics(nessus_file_path)
        time.sleep(300)


if __name__ == "__main__":
    main()
