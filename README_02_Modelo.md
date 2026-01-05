# Notebook 02 — Modelo Preditivo Flight On-Time

## Descrição
Este notebook desenvolve e avalia modelos de Machine Learning para prever se um voo chegará no horário, utilizando os dados preparados no EDA.

## Modelos utilizados
- DummyClassifier (baseline)
- GradientBoostingClassifier
- CatBoostClassifier

## Pipeline
- Pré-processamento com ColumnTransformer
- Codificação de variáveis categóricas (OneHotEncoder, TargetEncoder)
- Treinamento e validação com Pipeline do scikit-learn

## Métricas de avaliação
- Accuracy (via classification_report)
- Precision
- Recall
- F1-score
- ROC AUC

## Bibliotecas utilizadas
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
