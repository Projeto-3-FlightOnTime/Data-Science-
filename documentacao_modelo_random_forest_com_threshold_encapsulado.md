# 📄 Documentação de Governança – Modelo Random Forest com Threshold Encapsulado

## 1. Identificação do Modelo

- **Nome do artefato**: `modelo_rf_atrasos_thr_0_4.pkl`
- **Algoritmo**: Random Forest Classifier
- **Tipo de problema**: Classificação binária (atraso vs não atraso)
- **Versão lógica do modelo**: RF_ATRASOS_V1_THR_0_4
- **Data de geração**: _(preencher)_
- **Responsável**: _(preencher)_

---

## 2. Objetivo do Modelo

Este modelo tem como objetivo estimar a **probabilidade de atraso** com base nas variáveis de entrada fornecidas. A decisão binária (atraso / não atraso) é derivada a partir de um **threshold de 0.4**, definido com base em análises offline de performance (trade-off entre recall e precision).

---

## 3. Regra de Negócio (Threshold)

- **Threshold aplicado**: `0.4`
- **Justificativa**:
  - Definido após análises comparativas de métricas (ROC, Precision-Recall, F1, impacto de negócio)
  - Prioriza maior sensibilidade para a classe positiva (atraso)

### Importante
O threshold **não é aplicado no backend** nem na API Java. Ele está **encapsulado no artefato do modelo**, garantindo:
- Consistência entre ambientes
- Versionamento da regra de decisão
- Eliminação de lógica duplicada fora do modelo

---

## 4. Arquitetura e Contrato de Uso

### 4.1 Contrato da API

O contrato atual da API **não foi alterado**:

- A API carrega o modelo serializado (`.pkl`)
- A API utiliza exclusivamente:

```python
model.predict_proba(X)
```

- O retorno é a **probabilidade da classe positiva (atraso)**

### 4.2 Encapsulamento do Threshold

O modelo disponibiliza internamente:

```python
model.predict(X)
```

Que aplica a regra:

```
probabilidade >= 0.4 → classe 1
probabilidade <  0.4 → classe 0
```

⚠️ **Observação**: este método não é utilizado pela API no momento, mas está disponível para uso futuro sem necessidade de reprocessamento ou reexportação do modelo.

---

## 5. Implementação Técnica

### 5.1 Wrapper do Modelo

O modelo final é um wrapper (`ModeloComThreshold`) que envolve o Random Forest treinado.

Principais características:
- Stateless (sem estado mutável)
- Thread-safe
- Compatível com sklearn
- Serializável via joblib

### Métodos expostos

| Método | Finalidade | Impacto no contrato |
|------|-----------|--------------------|
| `predict_proba(X)` | Retorna probabilidade | Nenhum |
| `predict(X)` | Retorna decisão com threshold | Opcional |
| `decision_function(X)` | Score relativo ao threshold | Auditoria / Monitoramento |

---

## 6. Estrutura dos Artefatos

```
entrega_modelo/
├── modelo_rf_atrasos_thr_0_4.pkl
└── ml_model/
    ├── __init__.py
    └── threshold_wrapper.py
```

⚠️ **Nota técnica**: o módulo `ml_model.threshold_wrapper` deve estar disponível no ambiente de execução para que o `joblib.load` funcione corretamente.

---

## 7. Versionamento e Ciclo de Vida

### Alterações que exigem nova versão do modelo

- Mudança de threshold
- Retreinamento do Random Forest
- Alteração de features
- Mudança na lógica de decisão

Cada alteração gera:
- Novo artefato `.pkl`
- Novo identificador de versão

### Convenção de nomes

```
modelo_<algoritmo>_<problema>_thr_<valor>.pkl
```

Exemplo:
```
modelo_rf_atrasos_thr_0_4.pkl
```

---

## 8. Riscos Conhecidos e Mitigações

| Risco | Mitigação |
|-----|-----------|
| Uso incorreto do threshold fora do modelo | Threshold encapsulado |
| Divergência entre ambientes | Versionamento por artefato |
| Concorrência na API | Wrapper stateless |

---

## 9. Observações Finais

Este modelo foi projetado para **equilibrar governança, robustez técnica e restrições arquiteturais** existentes, garantindo que regras de negócio críticas estejam versionadas junto ao modelo, sem impacto no contrato atual das APIs.
