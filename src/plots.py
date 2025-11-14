import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def plot_top_products(df, n=10, output_path=None):
    # Plota top n produtos mais vendidos (salva imagem se output_path).
    if "produto" in df.columns and "unidades_vendidas" in df.columns:
        grp = df.groupby("produto")["unidades_vendidas"].sum().sort_values(ascending=False).head(n)
        plt.figure(figsize=(10,5))
        grp.plot(kind="bar")
        plt.title("Top produtos mais vendidos")
        plt.xlabel("Produto")
        plt.ylabel("Unidades vendidas")
        plt.tight_layout()
        if output_path:
            plt.savefig(output_path)
        else:
            plt.show()
        plt.close()

def plot_price_distribution(df, output_path=None):
    # Histograma de preços.
    if "preco" in df.columns:
        plt.figure(figsize=(8,5))
        sns.histplot(df["preco"].dropna(), kde=True)
        plt.title("Distribuição de Preços")
        plt.xlabel("Preço")
        plt.tight_layout()
        if output_path:
            plt.savefig(output_path)
        else:
            plt.show()
        plt.close()

def plot_corr_heatmap(df, output_path=None):
    # Heatmap de correlação entre colunas numéricas.
    nums = df.select_dtypes(include="number")
    if nums.shape[1] < 2:
        return
    plt.figure(figsize=(8,6))
    sns.heatmap(nums.corr(), annot=True, fmt=".2f")
    plt.title("Mapa de Correlação")
    plt.tight_layout()
    if output_path:
        plt.savefig(output_path)
    else:
        plt.show()
    plt.close()
