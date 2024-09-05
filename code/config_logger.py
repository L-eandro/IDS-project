import logging
from logging.handlers import SysLogHandler


syslog_handler = SysLogHandler(address=('localhost', 514))
formatter = logging.Formatter('%(asctime)s - %(message)s')
syslog_handler.setFormatter(formatter)

# Configuração do logger
logger = logging.getLogger()
logger.setLevel(logging.INFO)
logger.addHandler(syslog_handler)
