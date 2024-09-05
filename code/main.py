from prometheus_client import start_http_server
from data_collection import collect_historical_data, fetch_external_data
from attack_prediction import analyze_and_predict
from packet_analysis import start_packet_sniffing
from server_status import check_server
from time_server import update_execution_time
import time

def main():
    start_http_server(8000)

    historical_data = collect_historical_data()
    if not historical_data.empty:
        analyze_and_predict(historical_data)

    check_server()
    update_execution_time()


    start_packet_sniffing()


    while True:
        fetch_external_data()
        time.sleep(60)

if __name__ == "__main__":
    main()
