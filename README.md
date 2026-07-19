# Predição de Preços de Imóveis - King County

## Sobre o Projeto
Projeto avaliativo do Módulo 1 do curso **Desenvolvimento de IA para Análise Preditiva [T2]** (SCTEC / SESI-SENAI SC). 
Construção de um pipeline preditivo end-to-end para estimar o valor de venda de imóveis no condado de King County (EUA).

## O Problema de Negócio
A precificação imobiliária é sensível a múltiplas variáveis físicas e de localização. O objetivo é a predição da variável contínua `price` (preço em dólares). Um modelo preditivo preciso mitiga a subjetividade nas avaliações e otimiza a rentabilidade das negociações.

**Dataset:** King County House Sales (`data_raw.csv`), com ~21.600 registros.

## Tecnologias e Bibliotecas
* **Linguagem:** Python 3
* **Data Prep & EDA:** `pandas`, `numpy`, `scipy`
* **Visualização:** `matplotlib`, `seaborn`
* **Machine Learning:** `scikit-learn` (Linear Regression, Random Forest, Voting Regressor, RandomizedSearchCV), `xgboost` (XGBRegressor)

## Técnicas Aplicadas
1. **Análise Exploratória de Dados (EDA):** Verificação de cardinalidade, tipos primitivos e distribuição da variável-alvo.
2. **Data Prep:** 
   * Engenharia reversa para preenchimento de nulos (`sqft_above = sqft_living - sqft_basement`).
   * Supressão de outliers com base em limites do IQR (Capping exclusivo no conjunto de treino para mitigar vazamento de dados).
3. **Feature Engineering:**
   * Extração de matriz temporal (ano, mês, final de semana).
   * Criação de indicadores de densidade e proporção (`bath_per_bed`, `bed_per_floor`).
   * Cálculo esférico de distâncias de infraestrutura utilizando a fórmula de Haversine (substituindo aproximações planas).
4. **Modelagem e Validação:**
   * Avaliação comparativa entre regressões lineares e ensembles baseados em árvores.
   * Tuning via `RandomizedSearchCV`.
   * Desenvolvimento de métrica customizada (Scorer) baseada em MAE absoluto na escala nominal em Dólares após a transformação `np.log1p`.

## Versão do Modelo e Resultados
O campeão preditivo no conjunto de testes foi o **XGBoost Otimizado em Dólares**.

**Métricas (Dados de Teste):**
* **R² (Coeficiente de Determinação):** 0.9089
* **MAE (Erro Absoluto Médio):** U$ 60,686.89

**Veredito de Negócio:**
As predições apresentam um desvio médio de US$ 61 mil do valor de mercado. Devido à presença massiva de imóveis de alto padrão em King County (muitos superando U$ 1M), uma explicabilidade da variância (R²) próxima de 91% consolida o algoritmo como um excelente balizador analítico para suporte rápido e escalável à decisão na corretagem.

## Melhorias Futuras (v2)
* Eliminação formal de multicolinearidade com base no VIF (Variance Inflation Factor).
* Enriquecimento da base com taxas de juros macroeconômicas indexadas à data temporal da venda.
* Produtização do artefato `.pkl` usando FastAPI para inferências de precificação sob demanda.

## Estrutura do Repositório
```text
SCTEC_PROJETO/
├── funcoes/
│   ├── funcoes_exploratoria.py
│   └── funcoes_feat_eng.py
├── raw/                # Dados originais do repositório
├── processed/          # Dados processados pelo script de limpeza
├── tratamento/         # Notebooks de EDA e Limpeza Inicial
│   ├── data_cleaning.ipynb
│   └── feature_engineering.ipynb
│   └── machine_learning.ipynb
├── teste_final/        # Segunda tentativa de Feature Engineering e Modelagem
│   └── feature_engineering_2.ipynb
│   └── machine_learning_2.ipynb
├── README.md
└── requirements.txt
```

## Apresentação
https://drive.google.com/file/d/1oY9dalY69PAZ8tJ2nJRaow7d7DGiCpfB/view?usp=sharing 
