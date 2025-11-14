from datetime import datetime
import pandas as pd

def gerar_relatorio_texto(resumo, caminho, df=None):
    # Gera um relatório de texto simples com métricas do resumo.
    lines = []
    lines.append(f"Relatório gerado em: {datetime.now().isoformat()}")
    lines.append("")
    lines.append("Resumo de limpeza e análise")
    lines.append("--------------------------")
    lines.append(f"Linhas antes: {resumo.get('linhas_antes', 'N/A')}")
    lines.append(f"Duplicatas removidas: {resumo.get('duplicatas_removidas', 'N/A')}")
    lines.append("")
    lines.append("Nulos preenchidos por coluna:")
    for k,v in resumo.get("nulos_preenchidos", {}).items():
        lines.append(f" - {k}: {v}")
    lines.append("")
    if df is not None:
        lines.append(f"Total de vendas (unidades): {int(df['unidades_vendidas'].sum()) if 'unidades_vendidas' in df.columns else 'N/A'}")
    lines.append("")
    with open(caminho, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    return caminho
