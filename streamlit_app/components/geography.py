import streamlit as st
import pandas as pd
import json
import plotly.express as px
import os
from scripts.indicadores import acidente_por_SGUF

def show():
    # Mapa de Calor - Acidentes por Estado
    st.markdown("### 🗺️ Mapa de Calor - Acidentes por Estado")

    # Verificando se os arquivos existem
    csv_path = r'../data/data_cleaned.csv'
    geojson_path = r'../data/brazil_states.geojson'

    if not os.path.exists(csv_path):
        st.error(f"Arquivo CSV não encontrado: `{csv_path}`")
        return

    if not os.path.exists(geojson_path):
        st.error(f"Arquivo GeoJSON não encontrado: `{geojson_path}`")
        return

    # Carregar dados
    df = pd.read_csv(csv_path)

    # Agrupar por estado
    df_estado = df.groupby("SG_UF").size().reset_index(name="total_acidentes")

    # Carregar GeoJSON dos estados
    with open(geojson_path, encoding="utf-8") as f:
        geojson = json.load(f)

    # Obter siglas do GeoJSON
    siglas_geojson = [f["properties"]["sigla"] for f in geojson["features"]]

    # Verificar se todas as siglas estão no CSV
    ufs_faltando = set(df_estado["SG_UF"]) - set(siglas_geojson)
    if ufs_faltando:
        st.warning(f"UFs presentes no CSV mas ausentes no GeoJSON: {ufs_faltando}")

    # Mapa de calor
    fig = px.choropleth(
        df_estado,
        geojson=geojson,
        locations="SG_UF",
        featureidkey="properties.sigla",
        color="total_acidentes",
        color_continuous_scale="Reds",
        scope="south america",
        labels={"total_acidentes": "Total de Acidentes"},
    )

    fig.update_geos(fitbounds="locations", visible=False)
    fig.update_layout(
        margin={"r": 0, "t": 0, "l": 0, "b": 0},
        height=600,
    )

    st.plotly_chart(fig, use_container_width=True)

    # Gráfico de barras - Acidentes por Estado
    st.markdown("### 🗺️ Distribuição por Estado")
    df_estado_sguf = acidente_por_SGUF()
    fig2 = px.bar(
        df_estado_sguf.sort_values(by="TOTAL_ACIDENTES", ascending=False),
        x="SG_UF",
        y="TOTAL_ACIDENTES",
        title="Acidentes por Estado",
        labels={"SG_UF": "UF", "TOTAL_ACIDENTES": "Total de Acidentes"},
    )
    st.plotly_chart(fig2, use_container_width=True)

    # Referências
    st.markdown("#### Fontes dos Dados:")
    st.markdown("Distribuição geográfica obtida a partir do SINAN (Sistema de Informação de Agravos de Notificação) e IBGE.")
