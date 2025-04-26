import streamlit as st
import plotly.express as px
from scripts.indicadores import acidente_por_genero_faixaEtaria, por_raca, por_escolaridade

def show():
    st.markdown("### 👥 Indicadores Demográficos")
    df_genero_faixa = acidente_por_genero_faixaEtaria()
    fig1 = px.bar(
        df_genero_faixa,
        x="FAIXA_ETARIA",
        y="TOTAL_ACIDENTES",
        color="CS_SEXO",
        barmode="group",
        title="Acidentes por Gênero e Faixa Etária"
    )
    st.plotly_chart(fig1, use_container_width=True)

    st.markdown("### 🌎 Distribuição por Raça/Cor")
    df_raca = por_raca()
    fig2 = px.pie(
        df_raca,
        names="CS_RACA",
        values="TOTAL_ACIDENTES",
        title="Distribuição por Raça/Cor"
    )
    st.plotly_chart(fig2, use_container_width=True)

    st.markdown("### 🎓 Escolaridade")
    df_esc = por_escolaridade()
    fig3 = px.bar(
        df_esc,
        x="CS_ESCOL_N",
        y="TOTAL_ACIDENTES",
        title="Distribuição por Escolaridade"
    )
    st.plotly_chart(fig3, use_container_width=True)

    # Referências
    st.markdown("#### Fontes dos Dados:")
    st.markdown("Dados de gênero, raça e escolaridade obtidos do SINAN (Sistema de Informação de Agravos de Notificação).")
