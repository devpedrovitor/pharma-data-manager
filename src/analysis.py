import pandas as pd
from termcolor import colored

def total_vendas(df):
    #Soma unidades_vendidas (tratando NA).
    if "unidades_vendidas" not in df.columns:
        return 0
    return df["unidades_vendidas"].fillna(0).sum()

def media_preco(df):
    # Média de preços, ignorando NA.
    if "preco" not in df.columns:
        return 0
    return df["preco"].dropna().mean()

def estoque_baixo(df):
    #Retorna DataFrame com itens onde quantidade_estoque <= estoque_minimo.
    if not {"quantidade_estoque", "estoque_minimo"}.issubset(df.columns):
        return pd.DataFrame()
    # converte para numérico
    q = pd.to_numeric(df["quantidade_estoque"], errors="coerce").fillna(0)
    m = pd.to_numeric(df["estoque_minimo"], errors="coerce").fillna(0)
    return df[q <= m]

def produtos_mais_vendidos(df, n=10):
    # Agrupa por produto e soma unidades_vendidas, retorna top n.
    if "unidades_vendidas" not in df.columns:
        return pd.DataFrame()
    if "produto" in df.columns:
        grp = df.groupby("produto")["unidades_vendidas"].sum().sort_values(ascending=False).head(n)
        return grp.reset_index().rename(columns={"unidades_vendidas":"total_vendido"})
    else:
        # fallback por índice
        s = df["unidades_vendidas"].fillna(0).sort_values(ascending=False).head(n)
        return s

def resumo_analise(df):
    # Gera um dicionário com as principais métricas.#
    resumo = {}
    resumo["linhas"] = len(df)
    resumo["colunas"] = list(df.columns)
    resumo["total_vendas"] = total_vendas(df)
    resumo["media_preco"] = media_preco(df)
    resumo["produtos_mais_vendidos"] = produtos_mais_vendidos(df, n=5)
    resumo["estoque_baixo"] = estoque_baixo(df)
    return resumo
