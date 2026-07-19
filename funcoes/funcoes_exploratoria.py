import pandas as pd

def analise_dados(df):
    tabela_resumo = pd.DataFrame({
        'Tipos de Dados': df.dtypes,        
        'Qtd_Não_Nulos': df.notna().sum(),
        'Valores Únicos': df.nunique(), 
        'Qtd_Nulos': df.isna().sum(),
        '% Nulos': ((df.isna().sum()) / len(df) * 100).round(2).astype(str) + '%', 
        'Duplicados': df.duplicated().sum()
    })

    return tabela_resumo
            