import pandas as pd
import geopandas as gpd
from libs.path_handle import caminho_absoluto_arquivo

def carregar_dados():
        
    # Criando DataFrame geografico
    municipios = gpd.read_file(caminho_absoluto_arquivo('BR_Municipios_2023.shp'))
    municipios_df = gpd.GeoDataFrame(municipios)

    # DataFrame
    acgr_df = pd.read_csv(caminho_absoluto_arquivo('acgr_br_df_cleaned.csv'), encoding="utf-8", sep=",")

    acgr_df["ID_MUNICIP"] = acgr_df["ID_MUNICIP"].astype(str).str.strip().str.upper()

    municipios_df["CD_MUN"] = municipios_df["CD_MUN"].astype(str).fillna("").str[:-1]

    acgr_br_df = acgr_df.merge(municipios_df, left_on="ID_MUNICIP", right_on="CD_MUN", how="left")

    acgr_br_df["NU_IDADE_N"] = pd.to_numeric(
        acgr_br_df["NU_IDADE_N"].astype(str).str[2:], errors='coerce'
    )

    drop_columns = {"Unnamed: 0","NU_ANO","SG_UF_NOT","ID_MUNICIP","DT_ACID","ANO_NASC","SG_UF","ID_MN_RESI","ID_OCUPA_N",
                    "LOCAL_ACID","UF_EMP","MUN_EMP","TERCEIRIZA","CNAE_PRIN","UF_ACID","MUN_ACID","CID_ACID","DT_ATENDE",
                    "UF_ATENDE","MUN_ATENDE","REGIME","CD_MUN","CD_RGI","NM_RGI","CD_RGINT","NM_RGINT","CD_UF","CD_REGIAO",
                    "CD_CONCURB","AREA_KM2"    
    }

    acgr_br_df_geo = acgr_br_df.drop(drop_columns, axis=1)

    print(acgr_br_df_geo)
    return acgr_br_df_geo