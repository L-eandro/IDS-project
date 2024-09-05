from prometheus_client import Counter, Gauge


http_requests_total = Counter('http_requests_total', 'Número total de requisições HTTP')
response_duration_seconds = Gauge('http_response_duration_seconds', 'Duração da resposta HTTP em segundos')
intrusion_icmp_total = Counter('intrusion_icmp_total', 'Número de pacotes ICMP grandes')
intrusion_tcp_total = Counter('intrusion_tcp_total', 'Número de pacotes TCP com portas não padrão')
attack_prediction_alert = Counter('attack_prediction_alert', 'Alerta de previsão de ataque')
