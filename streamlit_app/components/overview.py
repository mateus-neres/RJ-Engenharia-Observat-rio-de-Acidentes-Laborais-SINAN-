import streamlit as st
import os
import sys

# === Ajuste de path para encontrar o módulo scripts/indicadores.py ===
# Supondo que este arquivo está em streamlit_app/components,
# adicionamos a pasta principal do projeto (que contém scripts/) ao sys.path
proj_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
if proj_root not in sys.path:
    sys.path.append(proj_root)

from scripts.indicadores import (
    acidente_por_ano,
    acidente_por_SGUF,
    obitos_taxa_mortalidade,
    acidente_grave_incapacidade,
    distribuicao_por_cnae,
    por_regime_trabalho,
    por_sexo,
    por_raca,
    por_escolaridade
)

def show():
    st.markdown("### 📊 Indicadores Principais (2020–2024)")
    st.markdown("Principais métricas sobre acidentes de trabalho no Brasil, com base nas notificações do SINAN e dados complementares.")

    # Calcular indicadores
    total_acidentes = acidente_por_ano()["TOTAL_ACIDENTES"].sum()
    total_estados = acidente_por_SGUF().shape[0]
    obitos = obitos_taxa_mortalidade()
    graves = acidente_grave_incapacidade()
    total_cnaes = distribuicao_por_cnae().shape[0]
    total_regimes = por_regime_trabalho().shape[0]
    total_sexos = por_sexo().shape[0]
    total_racas = por_raca().shape[0]
    total_escolaridades = por_escolaridade().shape[0]

    # ─── Linha 1 ────────────────────────────────────────────────────────────────
    st.markdown("### Visão Geral")
    col1, col2, col3 = st.columns(3)
    col1.metric("🩺 Acidentes totais", f"{total_acidentes:,}")
    col2.metric("📍 Estados envolvidos", total_estados)
    col3.metric("⚰️ Óbitos registrados", obitos["TOTAL_OBITOS"])

    # ─── Linha 2 ────────────────────────────────────────────────────────────────
    col4, col5, col6 = st.columns(3)
    col4.metric("📉 Mortalidade (por 100 k acidentes)", f"{obitos['TAXA_MORTALIDADE_POR_100MIL']}")
    col5.metric("🚨 Acidentes graves", graves["TOTAL_GRAVES"])
    col6.metric("🔴 Proporção graves (%)", f"{graves['PROPORCAO_GRAVES_%']}%")

    # ─── Linha 3 ────────────────────────────────────────────────────────────────
    # st.markdown("### Perfil e Registros")
    # col7, col8, col9 = st.columns(3)
    # col7.metric("🏭 Categorias CNAE", total_cnaes)
    # col8.metric("💼 Regimes de trabalho", total_regimes)
    # col9.metric("🚻 Gênero (categorias)", total_sexos)

    # ─── Linha 4 ────────────────────────────────────────────────────────────────
    # col10, col11, col12 = st.columns(3)
    # col10.metric("🧬 Raça/Cor (categorias)", total_racas)
    # col11.metric("🎓 Escolaridade (níveis)", total_escolaridades)
    # col12.empty()  # coluna vazia para alinhamento

    # ─── Referências ────────────────────────────────────────────────────────────
    st.markdown("---")
    st.markdown("#### 📚 Fontes de dados:")
    st.markdown("""
- **SINAN (SUS)**: Sistema de Informação de Agravos de Notificação – acidentes notificados entre 2020 e 2024.  
- **INSS**: Registros de acidentes e óbitos de trabalhadores com vínculo formal (2020–2024).  
- **GeoJSON Estados IBGE**: [https://raw.githubusercontent.com/codeforamerica/click_that_hood/master/public/data/brazil-states.geojson](https://raw.githubusercontent.com/codeforamerica/click_that_hood/master/public/data/brazil-states.geojson)  
    """)

# Para testar de forma isolada
if __name__ == "__main__":
    show()
