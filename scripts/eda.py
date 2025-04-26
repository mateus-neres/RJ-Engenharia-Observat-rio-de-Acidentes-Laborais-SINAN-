import pandas as pd

file_path = r"../data/data_cleaned.csv"
df = pd.read_csv(file_path, sep=',', encoding='utf-8')

def acidente_por_ano():
    return df.groupby("NU_ANO").size().reset_index(name="TOTAL_ACIDENTES")

def acidente_por_CDUF():
    return df.groupby("CD_UF").size().reset_index(name="TOTAL_ACIDENTES")

def acidente_por_SGUF():
    return df.groupby("SG_UF").size().reset_index(name="TOTAL_ACIDENTES")

def acidente_por_genero_faixaEtaria():
    proporcao = df.groupby(["CS_SEXO", "FAIXA_ETARIA"]).size().reset_index(name="TOTAL_ACIDENTES")
    proporcao["PROPORCAO"] = (proporcao["TOTAL_ACIDENTES"] / proporcao["TOTAL_ACIDENTES"].sum()) * 100
    return proporcao

def obitos_taxa_mortalidade():
    df["DATA_OBITO"] = pd.to_datetime(df["DT_OBITO"], errors='coerce')
    total_obitos = df["DATA_OBITO"].notna().sum()
    total_acidentes = len(df)
    taxa = (total_obitos / total_acidentes) * 100000 if total_acidentes else 0
    return {"TOTAL_OBITOS": total_obitos, "TAXA_MORTALIDADE_POR_100MIL": round(taxa, 2)}

def acidente_grave_incapacidade():
    categorias_graves = [
        "INCAPACIDADE PARCIAL PERMANENTE",
        "INCAPACIDADE TOTAL PERMANENTE",
        "ÓBITO POR ACIDENTE DE TRABALHO GRAVE"
    ]
    graves = df[df["EVOLUCAO"].isin(categorias_graves)]
    total_graves = len(graves)
    proporcao = (total_graves / len(df)) * 100 if len(df) else 0
    return {"TOTAL_GRAVES": total_graves, "PROPORCAO_GRAVES_%": round(proporcao, 2)}

def distribuicao_por_cnae():
    distribuicao_cnae = df["CNAE"].value_counts().reset_index()
    distribuicao_cnae.columns = ["CNAE", "TOTAL_ACIDENTES"]
    return distribuicao_cnae

def por_regime_trabalho():
    distribuicao_regime = df["SIT_TRAB"].value_counts().reset_index()
    distribuicao_regime.columns = ["REGIME_TRABALHO", "TOTAL_ACIDENTES"]
    return distribuicao_regime

def por_sexo():
    distribuicao_sexo = df["CS_SEXO"].value_counts().reset_index()
    distribuicao_sexo.columns = ["CS_SEXO", "TOTAL_ACIDENTES"]
    return distribuicao_sexo

def por_raca():
    return df["CS_RACA"].value_counts().reset_index(name="TOTAL_ACIDENTES").rename(columns={"index": "RACA"})


def por_escolaridade():
    return df["CS_ESCOL_N"].value_counts().reset_index(name="TOTAL_ACIDENTES").rename(columns={"index": "ESCOLARIDADE"})


def tendencia_em_anos():
    evolucao = df.groupby("NU_ANO").size().reset_index(name="TOTAL_ACIDENTES")
    evolucao = evolucao.sort_values("NU_ANO")
    evolucao["VARIACAO_%"] = evolucao["TOTAL_ACIDENTES"].pct_change() * 100
    return evolucao