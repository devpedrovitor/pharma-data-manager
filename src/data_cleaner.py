import pandas as pd
from termcolor import colored

def clear_data(path, output_path=None, fill_value=0):
    df = pd.read_csv(path)
    resumo = {}
    resumo["linhas_antes"] = len(df)
    resumo["nulos_antes"] = df.isnull().sum().to_dict()

    # Remover duplicatas
    df_dedup = df.drop_duplicates()
    resumo["duplicatas_removidas"] = resumo["linhas_antes"] - len(df_dedup)
    df = df_dedup

    # Colunas a preencher
    cols = ["unidades_vendidas", "quantidade_estoque", "preco", "estoque_minimo"]
    nulos_preenchidos = {}
    for c in cols:
        if c in df.columns:
            antes = df[c].isnull().sum()
            # preencher com 0 por padrão; manter tipo numérico quando possível
            df[c] = pd.to_numeric(df[c], errors="coerce")
            df[c].fillna(fill_value, inplace=True)
            depois = df[c].isnull().sum()
            nulos_preenchidos[c] = antes - depois
    resumo["nulos_preenchidos"] = nulos_preenchidos

    # Validade -> datetime coerção
    if "validade" in df.columns:
        antes_invalidas = df["validade"].isnull().sum()
        df["validade"] = pd.to_datetime(df["validade"], errors="coerce")
        depois_invalidas = df["validade"].isnull().sum()
        resumo["novas_datas_invalidas"] = max(0, depois_invalidas - antes_invalidas)

    # Salvar resultado
    if output_path is None:
        output_path = path.replace(".csv", "_clean.csv")
    df.to_csv(output_path, index=False)

    # Mensagens
    print(colored(f"Arquivo limpo salvo em: {output_path}", "green"))
    print(colored(f"Duplicatas removidas: {resumo['duplicatas_removidas']}", "yellow"))
    print(colored("Nulos preenchidos por coluna:", "yellow"))
    for k,v in nulos_preenchidos.items():
        print(colored(f"  - {k}: {v}", "cyan"))
    if "novas_datas_invalidas" in resumo:
        print(colored(f"Novas datas inválidas após coerção: {resumo['novas_datas_invalidas']}", "yellow"))

    return df, resumo
