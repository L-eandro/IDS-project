from prometheus_client import start_http_server
from data_collection import collect_historical_data, fetch_external_data
from attack_prediction import analyze_and_predict
from packet_analysis import start_packet_sniffing
from server_status import check_server
from time_server import update_execution_time
from monitor_network import monitor_network
from monitor_ports import collect_port_data
from intrusion_detect import simulate_intrusion_detection
#from maps_attack import generate_random_attack
import time


def main():
    start_http_server(8000)

    historical_data = collect_historical_data()
    if not historical_data.empty:
        analyze_and_predict(historical_data)

    check_server()

    update_execution_time()

    monitor_network()

    collect_port_data()

    start_packet_sniffing()

    simulate_intrusion_detection()

  #  generate_random_attack()

    while True:
        fetch_external_data()
        collect_port_data()
        monitor_network()
        simulate_intrusion_detection()
     #   generate_random_attack()
        time.sleep(60)


if __name__ == "__main__":
    main()
