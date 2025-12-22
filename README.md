# anac-vra-2024-hackathon
Dataset de voos ANAC + análise preditiva de atrasos (hackathon 2025 Alura/ Oracle Next Education)


# ✈️ FlightOnTime — Previsão de Atrasos de Voos

## 📌 Descrição
O FlightOnTime é um MVP de ciência de dados que prevê a probabilidade de atraso de um voo antes da decolagem, utilizando dados históricos e informações pré-voo.

## 🎯 Objetivo
Classificar voos como:
- 0 → Provavelmente pontual
- 1 → Provavelmente atrasado

## 🧠 Modelagem
- Logistic Regression
- One-Hot Encoding
- Balanceamento de classes
- Ajuste de threshold (0.4)

O modelo prioriza **recall da classe atraso**, alcançando aproximadamente **84% de detecção de atrasos**.

## 📊 Métricas principais
- Recall (atraso): ~84%
- F1-score (atraso): ~0.34

## 🌐 API
O modelo é disponibilizado via API REST usando FastAPI.

### Endpoint
`POST /predict`

### Exemplo de entrada
```json
{
  "sigla_icao_empresa_aerea": "GLO",
  "codigo_tipo_linha": "N",
  "modelo_equipamento": "B738",
  "numero_de_assentos": 186,
  "sigla_icao_aeroporto_origem": "SBGR",
  "sigla_icao_aeroporto_destino": "SBRJ",
  "periodo_dia": "Tarde",
  "hora_partida_prevista": 14
}


Exemplo de saída
{
  "atraso_previsto": 1,
  "probabilidade_atraso": 0.73,
  "threshold_utilizado": 0.4
}

🚀 Como executar
pip install -r requirements.txt
uvicorn app:app --reload

Acesse:
http://127.0.0.1:8000/docs

---

# ✅ 5️⃣ Simulação de execução da API

### ▶️ Subir a API
```bash
uvicorn app:app --reload

🌐 Swagger
Abra no navegador:
http://127.0.0.1:8000/docs

🔁 Teste via curl
curl -X POST "http://127.0.0.1:8000/predict" \
-H "Content-Type: application/json" \
-d '{
  "sigla_icao_empresa_aerea": "GLO",
  "codigo_tipo_linha": "N",
  "modelo_equipamento": "B738",
  "numero_de_assentos": 186,
  "sigla_icao_aeroporto_origem": "SBGR",
  "sigla_icao_aeroporto_destino": "SBRJ",
  "periodo_dia": "Tarde",
  "hora_partida_prevista": 14
}'
