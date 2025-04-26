
Autor: Mateus Neres da SIlva
- Objetivo do projeto: Construção de um Observatório de Acidentes de Trabalho (DRT)

No projeto você deve gerar um Notebook ou um website com a análise de dados escolhida. Fique livre para escolher a base de dados e as perguntas do seu interesse. Envie o código do projeto para este repositório.

# Observatório de Acidentes de Trabalho (DRT)

Este projeto tem como objetivo criar um observatório interativo utilizando **Streamlit** para visualização e análise de dados de acidentes de trabalho, com base nas notificações do SINAN (DRT - Doenças Relacionadas ao Trabalho).

## Autor

- **Mateus Neres da Silva**

---

## Objetivos

- Monitorar e analisar dados de acidentes de trabalho no Brasil.
- Gerar indicadores de gravidade, perfil do trabalhador e evolução temporal.
- Exibir visualizações interativas para facilitar a compreensão dos dados.
- Identificar padrões e fatores de risco.

---

## Estrutura do Projeto

```plaintext
observatorio_acidentes_trabalho/
│
├── data/                   # Dados brutos, tratados e dicionários
│   ├── acgr_br_df.csv
│   ├── data_cleaned.csv
│   ├── brazil_states.geojson
│   └── DIC_DADOS_DRT_...pdf
│
├── notebooks/              # Análises exploratórias e limpeza
│   ├── eda.ipynb
│   ├── data_cleaning.ipynb
│   └── download_acgrbr.ipynb
│
├── scripts/                # Funções auxiliares e indicadores
│   └── indicadores.py
│
├── streamlit_app/          # Interface interativa+65
│   ├── main.py
│   └── components/
│       ├── overview.py
│       ├── accidents_by_years.py
│       ├── geography.py
│       └── demographics.py
│
├── requirements/           # Dependências do projeto
│   ├── requirements.txt
│   └── environment.yml
│
├── README.md               # Documentação do projeto
└── structure.md            # Estrutura detalhada do repositório
```

---

## Tecnologias Utilizadas

- **Python** (Pandas, NumPy)
- **Streamlit** (dashboard interativo)
- **Plotly / Seaborn** (gráficos)
- **GeoPandas / Folium** (mapas interativos)
- **Jupyter Notebooks**

---

## 🚀 Como Executar o Projeto

### 1. Clone o repositório:

```bash
git clone https://github.com/seu-usuario/observatorio_acidentes_trabalho.git
cd observatorio_acidentes_trabalho
```

### 2. Crie um ambiente virtual com `conda` (recomendado):

```bash
conda env create -f requirements/environment.yml
conda activate observatorio_drt
```

**Ou, com `pip`**:

```bash
python -m venv venv
source venv/bin/activate  # no Windows: venv\Scripts\activate
pip install -r requirements/requirements.txt
```

### 3. Execute o Streamlit:

```bash
cd streamlit_app
streamlit run main.py
```

O aplicativo será aberto automaticamente no navegador, geralmente em `http://localhost:8501`.

---

## Pré-requisitos

- Python 3.9 ou superior
- Conda (opcional, mas recomendado)
- Acesso aos arquivos `data_cleaned.csv` e `brazil_states.geojson` (já incluídos na pasta `data/`)

---

## Funcionalidades

- Visão geral com números totais e estatísticas rápidas
- Evolução dos acidentes ao longo dos anos
- Análise por faixa etária, gênero, setor econômico
- Distribuição geográfica com mapas interativos
- Indicadores de gravidade e mortalidade

---

## Licença

Este projeto é de uso acadêmico e segue os termos da [Licença MIT](https://opensource.org/licenses/MIT).

---

## 📬 Contato

Caso tenha dúvidas ou sugestões:

- **Email**: mateus.neres@dcx.ufpb.br
- **GitHub**: [https://github.com/mateus-neres](https://github.com/mateus-neres)
