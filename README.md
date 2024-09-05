<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Network Monitoring and Attack Prediction System</title>
</head>
<body>
    <h1>Network Monitoring and Attack Prediction System</h1>
    <p>Este projeto é uma solução integrada para monitoramento de rede, previsão de ataques cibernéticos e coleta de dados em tempo real. Utiliza várias bibliotecas e ferramentas para capturar, analisar e prever possíveis ameaças em um ambiente de rede.</p>
    
    <h2>Funcionalidades</h2>
    <ul>
        <li><strong>Monitoramento de Rede:</strong> Captura e analisa pacotes de rede em tempo real para identificar potenciais intrusões, como pacotes ICMP grandes ou pacotes TCP em portas não padrão.</li>
        <li><strong>Previsão de Ataques:</strong> Utiliza dados históricos de ataques para treinar um modelo ARIMA, que prevê a probabilidade de futuros ataques.</li>
        <li><strong>Coleta de Dados em Tempo Real:</strong> Faz requisições a APIs externas para coletar dados em tempo real, que são analisados e registrados para futuras previsões.</li>
        <li><strong>Métricas de Monitoramento:</strong> Expõe métricas personalizadas ao Prometheus, como contadores de requisições HTTP e duração das respostas, permitindo o monitoramento contínuo do sistema.</li>
        <li><strong>Logging Centralizado:</strong> Envia logs detalhados para um servidor Syslog, facilitando o monitoramento centralizado de eventos e possíveis problemas.</li>
    </ul>
    
    <h2>Tecnologias Utilizadas</h2>
    <ul>
        <li><strong>Python:</strong> Linguagem principal do projeto.</li>
        <li><strong>scapy:</strong> Biblioteca para captura e análise de pacotes de rede.</li>
        <li><strong>requests:</strong> Biblioteca para fazer requisições HTTP.</li>
        <li><strong>pandas:</strong> Biblioteca para manipulação e análise de dados.</li>
        <li><strong>prometheus_client:</strong> Biblioteca para exposição de métricas ao Prometheus.</li>
        <li><strong>statsmodels (ARIMA):</strong> Usado para modelagem e previsão de séries temporais.</li>
        <li><strong>Syslog:</strong> Para centralização de logs de eventos.</li>
    </ul>
    
    <h2>Como Funciona</h2>
    <ol>
        <li><strong>Captura de Pacotes:</strong> A função <code>packet_callback</code> utiliza <code>scapy</code> para capturar pacotes de rede. Pacotes ICMP grandes e pacotes TCP com portas não padrão são identificados e registrados nos logs e nas métricas do Prometheus.</li>
        <li><strong>Coleta de Dados Históricos:</strong> A função <code>collect_historical_data</code> faz requisições a uma API para coletar dados históricos de ataques, que são então processados e analisados com <code>pandas</code>.</li>
        <li><strong>Previsão de Ataques:</strong> A função <code>analyze_and_predict</code> utiliza um modelo ARIMA para prever futuros ataques com base nos dados históricos coletados. Se a previsão indicar um aumento significativo no número de ataques, um alerta é registrado.</li>
        <li><strong>Monitoramento de APIs Externas:</strong> A função <code>fetch_external_data</code> faz requisições periódicas a uma API externa para coletar dados em tempo real, que são analisados e registrados em logs e nas métricas do Prometheus.</li>
        <li><strong>Métricas e Logging:</strong> As métricas são expostas em um servidor Prometheus rodando na porta 8000. Logs detalhados são enviados a um servidor Syslog para monitoramento centralizado.</li>
    </ol>
    
    <h2>Configuração e Uso</h2>
    
    <h3>Pré-requisitos</h3>
    <ul>
        <li>Python 3.x</li>
        <li>Bibliotecas Python:
            <ul>
                <li><code>scapy</code></li>
                <li><code>requests</code></li>
                <li><code>pandas</code></li>
                <li><code>prometheus_client</code></li>
                <li><code>statsmodels</code></li>
            </ul>
        </li>
        <li>Servidor Syslog para receber os logs.</li>
        <li>Servidor Prometheus para coletar as métricas.</li>
    </ul>
    
    <h3>Instalação</h3>
    <ol>
        <li>Clone este repositório:
            <pre><code>git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio</code></pre>
        </li>
        <li>Instale as dependências:
            <pre><code>pip install -r requirements.txt</code></pre>
        </li>
        <li>Substitua os placeholders no código:
            <ul>
                <li><strong>ID do Recurso:</strong> Substitua <code>&lt;ID_DO_RECURSO&gt;</code> na função <code>collect_historical_data</code> pelo ID correto da API que você deseja usar.</li>
                <li><strong>Interface de Rede:</strong> Substitua <code>"Ethernet"</code> pela interface de rede correta na função <code>sniff</code>.</li>
            </ul>
        </li>
    </ol>
    
    <h3>Execução</h3>
    <p>Inicie o script com o seguinte comando:</p>
    <pre><code>python main.py</code></pre>
    <p>O servidor Prometheus será iniciado na porta 8000, e o sistema começará a capturar pacotes de rede, coletar dados e fazer previsões de ataques.</p>
    
    <h3>Estrutura do Projeto</h3>
    <pre><code>.
├── main.py                # Script principal
├── requirements.txt       # Dependências do Python
├── README.md              # Documentação do projeto
├── server_status.py       # Módulo para verificar o status do servidor (não fornecido)
├── time_server.py         # Módulo para atualizar o tempo de execução (não fornecido)
└── ...
</code></pre>
    
    <h2>Contribuição</h2>
    <p>Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e pull requests.</p>
    
    <h2>Licença</h2>
    <p>Este projeto está licenciado sob a MIT License - veja o arquivo <a href="LICENSE">LICENSE</a> para mais detalhes.</p>
</body>
</html>
