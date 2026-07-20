# Predição de Preços de Imóveis - King County

## Sobre o Projeto
Projeto avaliativo do curso **Desenvolvimento de IA para Análise Preditiva [T2]** (SCTEC / SESI-SENAI SC). 
Construção de um pipeline preditivo end-to-end para estimar o valor de venda de imóveis no condado de King County (EUA).

## O Problema de Negócio
 Um modelo preditivo com a finalizade de precificação imobiliária de uma variável contínua `price` (preço em dólares).

**Dataset:** King County House Sales (`data_raw.csv`), com ~21.600 registros.

## Tecnologias e Bibliotecas
* **Linguagem:** Python 3
* **Data Prep & EDA:** `pandas`, `numpy`, `scipy`
* **Visualização:** `matplotlib`, `seaborn`
* **Machine Learning:** `scikit-learn` (Linear Regression, Random Forest, Voting Regressor, RandomizedSearchCV), `xgboost` (XGBRegressor)
* **Persistência e Arquitetura:** Joblib (exportação de modelos), JSON (métricas), OS/Sys (roteamento de caminhos)

## Técnicas Aplicadas
1. **Análise Exploratória de Dados (EDA):** Verificação de cardinalidade, tipos primitivos e distribuição da variável-alvo.
2. **Data Prep:** 
   * Engenharia reversa para preenchimento de nulos (`sqft_above = sqft_living - sqft_basement`).
   * Confirmação de 'id' duplicado era relevante ao dataset
   * Supressão de outliers com base em limites do IQR (Capping exclusivo no conjunto de treino para mitigar vazamento de dados).
3. **Feature Engineering:**
   * Extração de matriz temporal (ano, mês, final de semana, estação, etc).
   * Criação de indicadores de densidade e proporção (`bath_per_bed`, `bed_per_floor`).
   * Cálculo de distâncias de infraestrutura utilizando a distância Euclidiana.
   * Índices Compostos: Interações multiplicativas, destacando o índice luxury (Grade × Preço/CEP × Área × Condição).
4. **Modelagem e Validação:**
   * Avaliação comparativa entre regressões lineares e ensembles baseados em árvores.
   * Tuning via `RandomizedSearchCV`.
   * Desenvolvimento de métrica customizada (Scorer) e comparativos.

## Versão do Modelo e Resultados
O campeão preditivo no conjunto de testes foi o **XGBoost Otimizado** utilizando a versão 2 do dataframe.

**Métricas (Dados de Teste):**
* **R² (Coeficiente de Determinação):** 0.9093
* **MAE (Erro Absoluto Médio):** U$ 60,627.38
* **Erro Quadrático Médio (MSE):** 13,824,602,817.36
* **Raiz do Erro Quadrático Médio (RMSE):** U$ 117,578.07

**Veredito de Negócio:**
As predições apresentam um desvio médio de US$ 60,7 mil do valor de mercado. Devido à presença massiva de imóveis de alto padrão em King County (muitos superando U$ 1M), uma explicabilidade da variância (R²) próxima de 91% consolida o algoritmo como um excelente balizador analítico para suporte rápido e escalável à decisão na corretagem apesar de que as métricas sensiveis a erros (MSE e RMSE) apontem valores altos chegando até o dobro do erro médio padrão (MAE) o que sugere que em alguns casos o erro é grande,

## Melhorias Futuras (v3)
* Buscar os resultados com os erros mais chamativos e entender o que pode ser feito a respeito

## Estrutura do Repositório
```text
SCTEC_PROJETO/
├── data/               # Armazenamento de dados
│   ├── processed_v1/   # Bases geradas na iteração 1 (Limpeza base e Feat. Eng. inicial)
│   ├── processed_v2/   # Bases geradas na iteração 2 (Refinamento de features)
│   └── raw/            # Base de dados original
├── funcoes/            # Scripts modulares com funções personalizadas de apoio
├── models/             # Artefatos e resultados dos modelos de Machine Learning
│   ├── v1/             # Modelo campeão e métricas da V1
│   └── v2/             # Modelo campeão e métricas da V2
├── notebook/           # Notebooks com a trilha de desenvolvimento e análises
├── README.md           # Documentação do projeto
└── requirements.txt    # Dependências e bibliotecas do ambiente Python
```

## Apresentação
https://drive.google.com/file/d/128ZaU3SYpxiMLUgjTwuBJ7gjTjlsvEYX/view?usp=sharing 
