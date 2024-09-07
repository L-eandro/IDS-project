from prometheus_client import start_http_server, Gauge
from ping3 import ping
import time


TARGET_SERVER = "http://dados.recife.pe.gov.br/"


SERVER_STATUS = Gauge('server_status', 'Shows whether the target server is up (1) or down (0)')

def check_server():
    try:
        response = ping(TARGET_SERVER, timeout=2)
        if response is None:
            SERVER_STATUS.set(0)
        else:
            SERVER_STATUS.set(1)
    except Exception as e:
        SERVER_STATUS.set(0)

if __name__ == '__main__':
    start_http_server(8000)
    while True:
        check_server()
        time.sleep(30)
