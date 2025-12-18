from fastapi import FastAPI, HTTPException
from schemas.request import FlightRequest
from schemas.response import PredictionResponse
from utils.preprocessing import preprocess_request

import joblib
import pandas as pd

app = FastAPI(
    title="FlightOnTime",
    description="ML microservice to predict flight delays",
)

# ============================================================
# CARREGAMENTO DO MODELO
# ============================================================
# TODO (Data Science):
# 1. Treinar o modelo final (ex: RandomForest)
# 2. Criar um pipeline com preprocessing + modelo
# 3. Salvar o pipeline completo em um arquivo .pkl
# 4. Atualizar o caminho abaixo para o arquivo correto
#
# Exemplo esperado:
# model = joblib.load("model/pipeline.pkl")
# ============================================================
try:
    model = joblib.load("CAMINHO_DO_MODELO_AQUI")
except Exception as e:
    raise RuntimeError(f"Error loading model: {e}")


# ============================================================
# ENDPOINT DE PREVISÃO
# ============================================================
@app.post("/predict", response_model=PredictionResponse)
def predict(request: FlightRequest):
    """
    Endpoint responsável por:
    - Receber os dados do voo (validados pelo schema)
    - Preparar os dados para o modelo
    - Executar a previsão
    - Retornar status e probabilidade
    """

    try:
        # ----------------------------------------------------
        # PREPARAÇÃO DOS DADOS
        # ----------------------------------------------------
        # Convertendo o objeto Pydantic para dict
        # by_alias=True garante compatibilidade com o JSON do backend Java
        data = request.model_dump(by_alias=True)

        # Envio dos dados crus para o preprocessing
        # O preprocessing será responsável por:
        # - Ajustar nomes de colunas
        # - Criar features derivadas
        # - Garantir o formato esperado pelo modelo
        df = preprocess_request(data)

        # ----------------------------------------------------
        # REALIZAÇÃO DA PREVISÃO
        # ----------------------------------------------------
        # TODO (Data Science):
        # - Utilizar model.predict(df)
        # - Utilizar model.predict_proba(df)
        # - Definir qual classe representa atraso (ex: 1)
        #
        # Exemplo futuro:
        # prediction = model.predict(df)[0]
        # probability = model.predict_proba(df)[0][1]

        # ----------------------------------------------------
        # CONVERSÃO DA CLASSE PARA TEXTO
        # ----------------------------------------------------
        # TODO (Backend + DS):
        # - Mapear:
        #   0 -> "PONTUAL"
        #   1 -> "ATRASADO"
        #
        # Exemplo futuro:
        # status = "ATRASADO" if prediction == 1 else "PONTUAL"

        # ----------------------------------------------------
        # RESPOSTA DA API
        # ----------------------------------------------------
        return PredictionResponse(
            # TODO:
            # previsao=status,
            # probabilidade=float(probability)
        )

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error processing forecast: {str(e)}"
        )
