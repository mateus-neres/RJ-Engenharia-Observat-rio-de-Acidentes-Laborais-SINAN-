# Resolvendo conflitos entre dependências do PySUS e garantindo compatibilidade
!pip install cffi>=1.17.0 tqdm>=4.64.1
!pip install pysus
!pip install --upgrade numpy==1.24.3

# Importando as bibliotecas necessárias
from pysus import SINAN
import pandas as pd

    # Carregando os arquivos do DATASUS
    sinan = SINAN().load()

    ACGRBR = sinan.get_files(dis_code=["ACGR"], year=[2020,2021,2022,2023,2024])

    file_path_data = r"../data/"
    file_path_paquets = r"../data/paquets/"

    # Realizando o Download dos dados no formato .parquet
    sinan.download(ACGRBR, local_dir=file_path_data)
    ACGRBR20, ACGRBR21, ACGRBR22, ACGRBR23, ACGRBR24 = ACGRBR

    # Transformando os arquivos .parquet em DataFrames
    ACGRBR20_parquet = ACGRBR20.download(local_dir=file_path_paquets)
    ACGRBR21_parquet = ACGRBR21.download(local_dir=file_path_paquets)
    ACGRBR22_parquet = ACGRBR22.download(local_dir=file_path_paquets)
    ACGRBR23_parquet = ACGRBR23.download(local_dir=file_path_paquets)
    ACGRBR24_parquet = ACGRBR24.download(local_dir=file_path_paquets)
    acgr_br_20_df = ACGRBR20_parquet.to_dataframe()
    acgr_br_21_df = ACGRBR21_parquet.to_dataframe()
    acgr_br_22_df = ACGRBR22_parquet.to_dataframe()
    acgr_br_23_df = ACGRBR23_parquet.to_dataframe()
    acgr_br_24_df = ACGRBR24_parquet.to_dataframe()

    acgr_br_df = pd.concat([acgr_br_20_df, acgr_br_21_df, acgr_br_22_df, acgr_br_23_df, acgr_br_24_df], axis=0, ignore_index=True)

    acgr_br_df.to_csv(f"{file_path_data}acgr_br_df.csv", encoding="utf-8", sep=",")