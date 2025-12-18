import pandas as pd
from datetime import datetime


def preprocess_input(request_data: dict) -> pd.DataFrame:
    """
    Responsável por preparar os dados de entrada da API
    para o formato EXATO esperado pelo modelo treinado.

    Este método deverá replicar 100% o pipeline de pré-processamento
    utilizado pelo time de Data Science durante o treinamento.

    Parâmetro:
    - request_data: dicionário recebido da API (dados brutos do voo)

    Retorno:
    - DataFrame pandas pronto para ser consumido pelo modelo 
    """

    # ------------------------------------------------------------------
    # 1. Criar DataFrame inicial a partir dos dados recebidos da API
    #    - Cada request representa uma única observação (1 linha)
    # ------------------------------------------------------------------

    # TODO: construir o DataFrame inicial com os dados do request

    # ------------------------------------------------------------------
    # 2. Mapear nomes de campos da API para os nomes usados no dataset
    #    - Exemplo: "companhia" -> "sigla_icao_empresa_aerea"
    #    - Este mapeamento deve refletir exatamente o dataset da ANAC
    # ------------------------------------------------------------------

    # TODO: aplicar mapeamento de colunas conforme padrão do dataset

    # ------------------------------------------------------------------
    # 3. Converter tipos de dados
    #    - Datas para datetime
    #    - Campos numéricos para int/float
    # ------------------------------------------------------------------

    # TODO: garantir tipos corretos das colunas

    # ------------------------------------------------------------------
    # 4. Feature Engineering
    #    Criar variáveis derivadas usadas no treino do modelo:
    #    - hora da partida
    #    - dia da semana
    #    - mês
    #    - dia ou noite
    #    - rota (origem + destino)
    # ------------------------------------------------------------------

    # TODO: criar features temporais e categóricas

    # ------------------------------------------------------------------
    # 5. Remover colunas que não são utilizadas pelo modelo
    #    - Exemplo: data original após extração das features
    # ------------------------------------------------------------------

    # TODO: remover colunas não utilizadas

    # ------------------------------------------------------------------
    # 6. Garantir a mesma ordem de colunas do treino
    #    - A ordem deve ser idêntica à usada no model.pkl
    # ------------------------------------------------------------------

    # TODO: reordenar colunas conforme padrão do modelo

    # ------------------------------------------------------------------
    # 7. Retornar DataFrame final pronto para predição
    # ------------------------------------------------------------------

    # TODO: retornar DataFrame final
