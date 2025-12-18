from pydantic import BaseModel, Field, ConfigDict

class PredictionResponse(BaseModel):
    previsao: str = Field(alias = "status_predicao", description = "punctual or late")
    probabilidade: float = Field(alias = "probabilidade", description = "Probability of flight delay")

    model_config = ConfigDict(populate_by_name=True)
