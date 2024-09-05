from scapy.all import sniff
from scapy.layers.inet import ICMP, TCP
from config_logger import logger
from prometheus_metrics import intrusion_icmp_total, intrusion_tcp_total


def packet_callback(packet):
    try:
        if packet.haslayer(ICMP) and len(packet) > 1000:
            logger.warning(f"Pacote ICMP grande detectado: {packet.summary()}")
            intrusion_icmp_total.inc()

        if packet.haslayer(TCP):
            if packet[TCP].dport not in [80, 443]:
                logger.info(f"Pacote TCP para porta não padrão detectado: {packet.summary()}")
                intrusion_tcp_total.inc()
    except Exception as e:
        logger.error(f"Erro ao processar pacote: {e}")

def start_packet_sniffing(interface='Wi-Fi 2'):
    sniff(iface=interface, prn=packet_callback, store=0)
