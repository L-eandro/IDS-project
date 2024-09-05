import pandas as pd
from statsmodels.tsa.arima.model import ARIMA
from config_logger import logger
from prometheus_metrics import attack_prediction_alert


def analyze_and_predict(df):
    try:
        df['timestamp'] = pd.to_datetime(df['timestamp'])
        df.set_index('timestamp', inplace=True)
        df = df['quantidade_ataques']

        model = ARIMA(df, order=(5, 1, 0))
        model_fit = model.fit()
        forecast = model_fit.forecast(steps=1)

        if forecast[0] > df.mean() + 2 * df.std():
            logger.warning(f"Alerta de previsão de ataque: previsão = {forecast[0]}")
            attack_prediction_alert.inc()
        else:
            logger.info(f"Previsão de ataques normal: {forecast[0]}")

    except Exception as e:
        logger.error(f"Erro na análise e previsão de ataques: {e}")
