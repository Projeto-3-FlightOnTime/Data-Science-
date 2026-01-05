# Notebook 02 — Modelagem Preditiva
## Projeto: Flight On-Time Prediction

## 1. Objetivo do Notebook
Construir, treinar e avaliar modelos de **Machine Learning** capazes de prever se um voo chegará no horário,
utilizando os dados explorados no notebook de EDA.

## 2. Estratégia de Modelagem
- Definição da variável alvo
- Separação treino / teste
- Criação de pipeline de pré-processamento
- Comparação entre modelos baseline e modelos avançados

## 3. Modelos Avaliados
- DummyClassifier (baseline)
- GradientBoostingClassifier
- CatBoostClassifier

## 4. Pré-processamento
- ColumnTransformer para separar variáveis numéricas e categóricas
- OneHotEncoder para variáveis categóricas
- TargetEncoder para variáveis de alta cardinalidade
- Pipeline para evitar vazamento de dados

## 5. Métricas de Avaliação
As métricas foram escolhidas considerando possível desbalanceamento da base:
- Accuracy
- Precision
- Recall
- F1-score
- ROC AUC
- Confusion Matrix

## 6. Interpretação do Modelo
- Análise de importância de variáveis
- Uso de SHAP para interpretabilidade local e global

## 7. Persistência do Modelo
- Salvamento do modelo treinado utilizando joblib
- Estrutura preparada para deploy futuro

## 8. Bibliotecas Utilizadas
- Python 3.11.2
- pandas 2.2.3
- numpy 1.24.0
- scikit-learn 1.4.2
- catboost 1.2.8
- shap n/a
- category-encoders n/a
- joblib 1.5.2
- matplotlib 3.7.5
- gdown n/a
- warnings (stdlib)

## 9. Resultado Final
- Modelo preditivo avaliado e comparado
- Métricas documentadas para tomada de decisão
- Base pronta para integração ou deploy