import pandas as pd
import numpy as np

def colunas_datetime(df):
    """
    Ajusta o dataframe para o datetime e cria novas colunas de tempo
    
    Parâmetro:
    - df: DataFrame de entrada
    """
    # Preparação
    df_clean = df.copy()
    df_clean['date'] = pd.to_datetime(df_clean['date'])
    
    # Extrações básicas
    df_clean['ano'] = df_clean['date'].dt.year
    df_clean['mes'] = df_clean['date'].dt.month
    df_clean['dia_da_semana'] = df_clean['date'].dt.dayofweek  # 0 é Segunda-feira, 6 é Domingo
    df_clean['trimestre'] = df_clean['date'].dt.quarter
    df_clean['final_de_semana'] = df_clean['date'].dt.dayofweek.isin([5, 6]).astype(int)
    df_clean['fim_do_mes'] = df_clean['date'].dt.is_month_end.astype(int)
    df_clean['hora'] = df_clean['date'].dt.hour
    df_clean['semestre'] = np.where(df_clean['mes'] <= 6, 1, 2)
    df_clean['dias_desde_inicio'] = (df_clean['date'] - (df_clean['date'].min())).dt.days
    
    def mapear_estacao(mes):
        if mes in [3, 4, 5]:
            return 'Primavera'
        elif mes in [6, 7, 8]:
            return 'Verao'
        elif mes in [9, 10, 11]:
            return 'Outono'
        else:
            return 'Inverno'
    df_clean['estacao'] = df_clean['mes'].apply(mapear_estacao)
    lista_estacoes = ['Primavera', 'Verao', 'Outono', 'Inverno']
    df_clean['estacao'] = pd.Categorical(df_clean['estacao'], categories=lista_estacoes)
    df_clean = pd.get_dummies(df_clean, columns=['estacao'], dtype=int)
    df_clean.drop(columns=['date'], inplace=True)

    return df_clean