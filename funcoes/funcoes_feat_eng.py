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

def criar_painel_diagnostico(df):
    relatorio = []
    colunas_numericas = df.select_dtypes(include=[np.number]).columns
    
    for col in colunas_numericas:
        # Skew
        skew_val = df[col].skew()
        log_sugerido = "SIM" if abs(skew_val) > 1.5 else "Não"
        
        # Outliers (Método IQR)
        q1 = df[col].quantile(0.25)
        q3 = df[col].quantile(0.75)
        iqr = q3 - q1
        limite_sup = q3 + 1.5 * iqr
        limite_inf = q1 - 1.5 * iqr
        total_outliers = df[(df[col] > limite_sup) | (df[col] < limite_inf)].shape[0]
        pct_outliers = (total_outliers / len(df)) * 100
        
        # Ruídos (Valores zerados bizarros)
        min_val = df[col].min()
        ruido_zero = "Não"
        if min_val == 0 and col in ['bedrooms', 'bathrooms', 'sqft_living']:
            ruido_zero = "Suspeito (Zero)"
            
        # Conclusão
        acoes = []
        if abs(skew_val) > 1.5: acoes.append("Aplicar LOG")
        if pct_outliers > 5: acoes.append("Suavizar Outliers (Capping)")
        elif pct_outliers > 0: acoes.append("Checar Extremos")
        if ruido_zero != "Não": acoes.append("Tratar Zeros")
        
        acao_final = " + ".join(acoes) if acoes else "Manter como está"
        
        relatorio.append({
            'Coluna': col,
            'Assimetria (Skew)': round(skew_val, 2),
            'Precisa de LOG?': log_sugerido,
            'Qtd Outliers': total_outliers,
            '% Outliers': round(pct_outliers, 2),
            'Possível Ruído?': ruido_zero,
            'Ação Recomendada': acao_final})
        
    return pd.DataFrame(relatorio).sort_values(by='% Outliers', ascending=False)

def resumo_estatistico(df):
    resumo_completo = df.describe(include='all').round(2)
    resumo_completo = resumo_completo.fillna('-')

    return resumo_completo