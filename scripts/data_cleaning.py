import pandas as pd

def data_cleaning():
    df = pd.read_csv('../data/acgr_br_df.csv', encoding="utf-8", sep=",")
    columns_drop = [
    'Unnamed: 0', 'TP_NOT', 'ID_AGRAVO', 'SEM_NOT', 'ID_REGIONA', 'ID_UNIDADE', 'SEM_ACID',
    'ID_RG_RESI', 'ID_PAIS', 'NUTEMPO', 'TPTEMPO', 'HORA_ACID', 'MIN_ACID', 'HORA_JOR',
    'MIN_JOR', 'MAIS_TRAB', 'NU_TRAB', 'ATENDE_MED', 'UNI_ATENDE', 'PART_CORP1', 'PART_CORP2',
    'PART_CORP3', 'CS_GESTANT', 'CID_LESAO', 'CAT', "SG_UF_NOT", "DT_ACID", "ANO_NASC",
    "ID_MN_RESI", "ID_OCUPA_N", "UF_EMP", "MUN_EMP", "TERCEIRIZA", "CNAE_PRIN", "MUN_ACID",
    "DT_ATENDE", "UF_ATENDE", "MUN_ATENDE", "REGIME"
    ]

    df = df.drop(columns_drop, axis=1)

    df['NU_IDADE_N'].fillna(df['NU_IDADE_N'].median(), inplace=True)

    df['CNAE'] = df.groupby('TIPO_ACID')['CNAE'].transform(lambda x: x.fillna(x.mode()[0] if not x.mode().empty else "DESCONHECIDO"))

    df['CS_ESCOL_N'].fillna("DESCONHECIDA", inplace=True)
    df['CS_RACA'].fillna("NÃO INFORMADO", inplace=True)
    df['SIT_TRAB'].fillna("NÃO ESPECIFICADO", inplace=True)

    df['CS_SEXO'] = df['CS_SEXO'].replace({'I': 'IGNORADO', '0': 'IGNORADO'})

    df['DT_NOTIFIC'] = pd.to_datetime(df['DT_NOTIFIC'], errors='coerce').dt.date
    df['DT_OBITO'] = pd.to_datetime(df['DT_OBITO'], errors='coerce').dt.date

    df['NU_IDADE_N'] = pd.to_numeric(df['NU_IDADE_N'], errors='coerce')
    df['CNAE'] = pd.to_numeric(df['CNAE'], errors='coerce')

    categorical_cols = [
    'CS_SEXO', 
    'CS_RACA', 
    'CS_ESCOL_N', 
    'SIT_TRAB', 
    'CNAE', 
    'TIPO_ACID'
    ]
    df[categorical_cols] = df[categorical_cols].astype('category')

    df.columns = df.columns.str.upper().str.replace(' ', '_')

    categorical_cols = ['DT_NOTIFIC', 'ID_MUNICIP', 'NU_IDADE_N', 'CS_SEXO', 'CS_RACA',
       'CS_ESCOL_N', 'SIT_TRAB', 'CNAE', 'TIPO_ACID', 'EVOLUCAO', 'DT_OBITO']

    for col in categorical_cols:
        df[col] = df[col].astype(str).str.strip().str.upper()

    evolucao_map = {
    '1.0' : 'CURA',
    '2.0' : 'INCAPACIDADE TEMPORARIA',
    '3.0' : 'INCAPACIDADE PARCIAL PERMANENTE',
    '4.0' : 'INCAPACIDADE TOTAL PERMANENTE',
    '5.0' : 'ÓBTO POR ACIDENTE DE TRABALHO GRAVE',
    '6.0' : 'ÓBTO POR OUTRAS CAUSAS',
    '7.0' : 'OUTROS',
    '9.0' : 'IGNORADO'
    }

    df['EVOLUCAO'] = df['EVOLUCAO'].astype(str).replace(evolucao_map)

    situacao_map = {
    '1.0' : 'CLT',
    '2.0' : 'NÃO REGISTRADO',
    '3.0' : 'AUTÔNOMO',
    '4.0' : 'SERVIDOR PÚBRICO ESTATUTÁRIO',
    '5.0' : 'SERVIDOR PÚBLICOCELETISTA',
    '6.0' : 'APOSENTADO',
    '7.0' : 'DESEMPREGADO',
    '8.0' : 'TRABALHO TEMPÓRARIO',
    '9.0' : 'COOPERATIVADO',
    '10.0' : 'TRABALHO AVULSO',
    '11.0' : 'EMPREGADOR',
    '12.0' : 'OUTROS',
    '99.0' : 'IGNORADO'
    }

    df['SIT_TRAB'] = df['SIT_TRAB'].astype(str).replace(situacao_map)

    raca_cor_map = {
    '1.0' : 'Branca',
    '2.0' : 'Preta',
    '3.0' : 'Amarela',
    '4.0' : 'Parda',
    '5.0' : 'Indígena',
    '9.0' : 'Ignorado'
    }

    df['CS_RACA'] = df['CS_RACA'].astype(str).replace(raca_cor_map)

    escolaridade_map = {
    '0.0' : 'Analfabeto', 
    '1.0' : '1ª a 4ª série incompleta do EF',
    '2.0' : '4ª série completa do EF',
    '3.0' : '5ª à 8ª série incompleta do EF',
    '4.0' : 'Ensino fundamental completo',
    '5.0' : 'Ensino médio incompleto',
    '6.0' : 'Ensino médio completo',
    '7.0' : 'Educação superior incompleta',
    '8.0' : 'Educação superior completa',
    '9.0' : 'Ignorado',
    '10.0' : 'Não se aplica'
    }

    df['CS_ESCOL_N'] = df['CS_ESCOL_N'].astype(str).replace(escolaridade_map)

    local_acid = {
    "1.0": "Instalações do Contratante",
    "2.0": "Via Pública" ,
    "3.0": "Instalações de terceiros",
    "4.0": "Domicílio próprio",
    "9.0": "Ignorado"
    }
    df['LOCAL_ACID'] = df['LOCAL_ACID'].astype(str).replace(local_acid)

    df['CD_UF'] = df['SG_UF']

    codigo_sigla = {
    '12.0': 'AC', '27.0': 'AL', '16.0': 'AP', '13.0': 'AM', '29.0': 'BA', 
    '23.0': 'CE', '53.0': 'DF', '32.0': 'ES', '52.0': 'GO', '21.0': 'MA',
    '51.0': 'MT', '50.0': 'MS', '31.0': 'MG', '15.0': 'PA', '25.0': 'PB',
    '41.0': 'PR', '26.0': 'PE', '22.0': 'PI', '33.0': 'RJ', '24.0': 'RN',
    '43.0': 'RS', '11.0': 'RO', '14.0': 'RR', '42.0': 'SC', '35.0': 'SP',
    '28.0': 'SE', '17.0': 'TO'
    }

    df['SG_UF'] = df['SG_UF'].astype(str).replace(codigo_sigla)

    # 1. Converter NU_IDADE_N para string (caso esteja no formato 5035 ou similar) e remover prefixo
    df['NU_IDADE_N'] = df['NU_IDADE_N'].astype(str).str[2:]

    # 2. Converter para numérico (idade em anos), erros vão virar NaN
    df['NU_IDADE_N'] = pd.to_numeric(df['NU_IDADE_N'], errors='coerce')

    # 3. Criar faixas etárias com binning
    bins = [0, 18, 25, 35, 45, 55, 65, 100]
    labels = ['<18', '18-25', '26-35', '36-45', '46-55', '56-65', '65+']
    df['FAIXA_ETARIA'] = pd.cut(df['NU_IDADE_N'], bins=bins, labels=labels, right=False)

    # 4. Organizar a ordem das categorias (útil para gráficos)
    df['FAIXA_ETARIA'] = pd.Categorical(df['FAIXA_ETARIA'], categories=labels, ordered=True)

    df.to_csv('../data/data_cleaned.csv', encoding="utf-8", sep=",")

    