import streamlit as st
from components import overview, demographics, geography, accidents_by_years

# Cria abas no Streamlit
tab1, tab2, tab3, tab4 = st.tabs([
    "📊 Dados Gerais",
    "👥 Dados Demográficos",
    "🗺️ Dados Geográficos",
    "📈 Acidentes por Ano"
])

# Chama as funções de exibição nas respectivas abas
with tab1:
    overview.show()  # Dados gerais com tipos de agravos

with tab2:
    demographics.show()  # Dados demográficos

with tab3:
    geography.show()  # Dados geográficos

with tab4:
    accidents_by_years.show()  # Análise de acidentes por ano com os agravos
