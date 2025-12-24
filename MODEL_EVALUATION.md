# Avaliação de Modelos — FlightOnTime ✈️

## Modelos Baseline

### Logistic Regression (Baseline)
- Accuracy: ~82%
- Recall (Atraso): ~2%
- Problema: modelo quase nunca prevê atraso

### Logistic Regression (Balanced)
- Recall (Atraso): ~59%
- Queda de precisão
- Baseline mais honesto para problema desbalanceado

## Considerações
- Ambos são modelos baseline
- Não recomendados para produção
- Servem como referência mínima

## Próximos Passos
- Avaliar modelos mais robustos (Random Forest, Gradient Boosting)
- Ajustar `class_weight`
- Ajustar threshold via Curva Precision-Recall
- Escolher modelo campeão com foco em Recall/F1 da classe atraso
