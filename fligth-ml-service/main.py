from fastapi import FastAPI, HTTPException
from schemas.request import FligthRequest
from schemas.response import PredictionResponse

import joblib
import pandas as pd

app = FastAPI(
    title="FlightOnTime",
    description="ML microservice to predict flight delays",
)

try:
    model = joblib.load("model/fligth_delay_model_v3.pkl")
except Exception as e:
    raise RuntimeError(f"Error loading model: {e}")


# ============================================================
# ENDPOINT DE PREVISÃO
# ============================================================
@app.post("/predict", response_model=PredictionResponse)
def predict(request: FligthRequest):
    """
    Endpoint responsável por:
    - Receber os dados do voo (validados pelo schema)
    - Preparar os dados para o modelo
    - Executar a previsão
    - Retornar status e probabilidade
    """

    try:
        
        data = request.model_dump(by_alias=True)

        data_hora = pd.to_datetime(data["data_hora_partida"])

        df = pd.DataFrame([{
            "sigla_icao_empresa_aerea": data["cod_companhia"],
            "sigla_icao_aeroporto_origem": data["cod_aeroporto_origem"],
            "sigla_icao_aeroporto_destino": data["cod_aeroporto_destino"],
            "hora_partida_prevista_num": data_hora.hour,
            "mes": data_hora.month,
            "dia_semana": data_hora.weekday()
        }])

        prediction = model.predict(df)[0]
        probability = model.predict_proba(df)[0][1]

        status = "ATRASADO" if prediction == 1 else "PONTUAL"

        return PredictionResponse(
            status_predicao=status,
            probabilidade=float(probability)
        )

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error processing forecast: {str(e)}"
        )
