import pandas as pd

def analise_dados(df):
    '''Cria uma tabela informativa com o type, quantidade não nulo, valores únicos, quantidade de nulos, porcentagem de nulos e duplicados
        Parâmetro:
    - df: DataFrame de entrada'''
    tabela_resumo = pd.DataFrame({
        'Tipos de Dados': df.dtypes,        
        'Não Nulos': df.notna().sum(),
        'Valores Únicos': df.nunique(), 
        'Nulos': df.isna().sum(),
        '% Nulos': ((df.isna().sum()) / len(df) * 100).round(2).astype(str) + '%', 
        'Duplicados': df.duplicated().sum()
    })

    return tabela_resumo
            