import streamlit as st
import pandas as pd
import plotly.express as px

def show():
    st.markdown("### 📈 Análise de Acidentes por Ano")

    # Carregar os dados
    csv_path = r'../data/data_cleaned.csv'
    df = pd.read_csv(csv_path)

    # Criar coluna com ano a partir da data de notificação
    df['NU_ANO'] = pd.to_datetime(df['DT_NOTIFIC'], errors='coerce').dt.year

    # Filtro dinâmico por ano
    anos_disponiveis = sorted(df['NU_ANO'].dropna().unique())
    anos_selecionados = st.multiselect("Selecione o(s) ano(s) para análise:", anos_disponiveis, default=anos_disponiveis)

    # Filtrar o DataFrame com os anos selecionados
    df_filtrado = df[df['NU_ANO'].isin(anos_selecionados)]

    # ──────────────────────────────────────────────────────
    st.markdown("### 📊 Total de Acidentes por Ano")

    acidentes_por_ano = df_filtrado.groupby('NU_ANO').size().reset_index(name='total_acidentes')
    st.dataframe(acidentes_por_ano, use_container_width=True)

    fig = px.line(acidentes_por_ano, x='NU_ANO', y='total_acidentes', title="Total de Acidentes por Ano")
    st.plotly_chart(fig, use_container_width=True)

    # ──────────────────────────────────────────────────────
    st.subheader("🧪 Distribuição dos Agravos por Ano")

    if 'EVOLUCAO' in df_filtrado.columns:
        agravos_por_ano = df_filtrado.groupby(['NU_ANO', 'EVOLUCAO']).size().reset_index(name='total_agravos')
        st.dataframe(agravos_por_ano, use_container_width=True)

        fig_agravos = px.bar(
            agravos_por_ano,
            x='NU_ANO',
            y='total_agravos',
            color='EVOLUCAO',
            title="Distribuição dos Agravos por Ano",
            barmode='stack'
        )
        st.plotly_chart(fig_agravos, use_container_width=True)
    else:
        st.warning("Coluna 'EVOLUCAO' não encontrada no dataset.")

    # ──────────────────────────────────────────────────────
    st.markdown("---")
    st.markdown("#### 📚 Fontes de dados:")
    st.markdown("""
- **SINAN (SUS)**: Sistema de Informação de Agravos de Notificação – acidentes notificados entre 2020 e 2024.  
- **INSS**: Registros de acidentes e óbitos de trabalhadores com vínculo formal.  
- **GeoJSON Estados IBGE**: [Fonte pública no GitHub](https://raw.githubusercontent.com/codeforamerica/click_that_hood/master/public/data/brazil-states.geojson)
    """)
