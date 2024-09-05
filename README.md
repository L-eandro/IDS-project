# Network Monitoring and Attack Prediction System

Este projeto é uma solução integrada para monitoramento de rede, previsão de ataques cibernéticos e coleta de dados em tempo real. Utiliza várias bibliotecas e ferramentas para capturar, analisar e prever possíveis ameaças em um ambiente de rede.

## Funcionalidades

- **Monitoramento de Rede:** Captura e analisa pacotes de rede em tempo real para identificar potenciais intrusões, como pacotes ICMP grandes ou pacotes TCP em portas não padrão.
- **Previsão de Ataques:** Utiliza dados históricos de ataques para treinar um modelo ARIMA, que prevê a probabilidade de futuros ataques.
- **Coleta de Dados em Tempo Real:** Faz requisições a APIs externas para coletar dados em tempo real, que são analisados e registrados para futuras previsões.
- **Métricas de Monitoramento:** Expõe métricas personalizadas ao Prometheus, como contadores de requisições HTTP e duração das respostas, permitindo o monitoramento contínuo do sistema.
- **Logging Centralizado:** Envia logs detalhados para um servidor Syslog, facilitando o monitoramento centralizado de eventos e possíveis problemas.

## Tecnologias Utilizadas

- **Python:** Linguagem principal do projeto.
- **scapy:** Biblioteca para captura e análise de pacotes de rede.
- **requests:** Biblioteca para fazer requisições HTTP.
- **pandas:** Biblioteca para manipulação e análise de dados.
- **prometheus_client:** Biblioteca para exposição de métricas ao Prometheus.
- **statsmodels (ARIMA):** Usado para modelagem e previsão de séries temporais.
- **Syslog:** Para centralização de logs de eventos.

## Como Funciona

1. **Captura de Pacotes:** A função `packet_callback` utiliza `scapy` para capturar pacotes de rede. Pacotes ICMP grandes e pacotes TCP com portas não padrão são identificados e registrados nos logs e nas métricas do Prometheus.

2. **Coleta de Dados Históricos:** A função `collect_historical_data` faz requisições a uma API para coletar dados históricos de ataques, que são então processados e analisados com `pandas`.

3. **Previsão de Ataques:** A função `analyze_and_predict` utiliza um modelo ARIMA para prever futuros ataques com base nos dados históricos coletados. Se a previsão indicar um aumento significativo no número de ataques, um alerta é registrado.

4. **Monitoramento de APIs Externas:** A função `fetch_external_data` faz requisições periódicas a uma API externa para coletar dados em tempo real, que são analisados e registrados em logs e nas métricas do Prometheus.

5. **Métricas e Logging:** As métricas são expostas em um servidor Prometheus rodando na porta 8000. Logs detalhados são enviados a um servidor Syslog para monitoramento centralizado.

## Configuração e Uso

### Pré-requisitos

- Python 3.x
- Bibliotecas Python:
  - `scapy`
  - `requests`
  - `pandas`
  - `prometheus_client`
  - `statsmodels`
  - `logging`
- Servidor Syslog para receber os logs.
- Servidor Prometheus para coletar as métricas.

