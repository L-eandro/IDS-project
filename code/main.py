from prometheus_client import start_http_server
from data_collection import collect_historical_data, fetch_external_data
from attack_prediction import analyze_and_predict
from packet_analysis import start_packet_sniffing
from server_status import check_server
from time_server import update_execution_time
from monitor_network import monitor_network
from monitor_ports import collect_port_data
from intrusion_detect import simulate_intrusion_detection
from geomap import simulate_attacks
from scan_ports import scan_vulnerabilities, start_nmap_prometheus_server
from teste_nessus import update_prometheus_metrics

import threading
import time


def start_attack_simulation():
    attack_thread = threading.Thread(target=simulate_attacks)
    attack_thread.daemon = True
    attack_thread.start()


def run_background_tasks():
    while True:
        fetch_external_data()
        collect_port_data()
        monitor_network()
        simulate_intrusion_detection()
        time.sleep(60)


def run_nessus_analysis():
    nessus_file_path = 'C:/Users/Aluno/Documents/IDS-project/Others/scan-teste_156pxn.nessus'
    while True:
        update_prometheus_metrics(nessus_file_path)
        time.sleep(10)


def start_all_threads():
    nessus_thread = threading.Thread(target=run_nessus_analysis)
    nessus_thread.daemon = True
    nessus_thread.start()

    background_thread = threading.Thread(target=run_background_tasks)
    background_thread.daemon = True
    background_thread.start()

    packet_sniffing_thread = threading.Thread(target=start_packet_sniffing)
    packet_sniffing_thread.daemon = True
    packet_sniffing_thread.start()


def main():
    start_http_server(8000)
    print("Servidor Prometheus rodando na porta 8000...")

    start_attack_simulation()

    start_nmap_prometheus_server()

    historical_data = collect_historical_data()
    if not historical_data.empty:
        analyze_and_predict(historical_data)

    check_server()

    update_execution_time()

    monitor_network()
    collect_port_data()

    target = '10.0.0.1'
    scan_vulnerabilities(target)

    start_all_threads()

    while True:
        time.sleep(8)


if __name__ == "__main__":
    main()
try:
    main()
except KeyboardInterrupt:
    print("Execução interrompida pelo usuário.")
