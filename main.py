from src.data_loader import load_csv, save_csv
from src.data_cleaner import clear_data
from src.analysis import resumo_analise
from src.plots import plot_top_products, plot_price_distribution, plot_corr_heatmap
from src.reports import gerar_relatorio_texto
from pathlib import Path

def main():
    data_in = Path("data/pharmacy_data_dirty_invalid_only.csv")
    if not data_in.exists():
        data_in = Path("data/pharmacy_data_dirty.csv")
    # Limpeza
    df_clean, resumo = clear_data(str(data_in), output_path="data/pharmacy_data_clean.csv")
    # Análise
    resumo_analitico = resumo_analise(df_clean)
    # Plots
    Path("relatorios").mkdir(exist_ok=True)
    plot_top_products(df_clean, n=10, output_path="relatorios/top_products.png")
    plot_price_distribution(df_clean, output_path="relatorios/price_dist.png")
    plot_corr_heatmap(df_clean, output_path="relatorios/corr_heatmap.png")
    # Relatório texto
    gerar_relatorio_texto(resumo, "relatorios/relatorio.txt", df=df_clean)
    print("Processamento concluído. Verifique a pasta relatorios/ e data/")

if __name__ == "__main__":
    main()
