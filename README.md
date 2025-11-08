
# Pharma-data-manager

**Disciplina:** Programação para Ciência de Dados
**Curso:** MBA Ciência de Dados - UNIFOR
**Instrutor:** Cássio Pinheiro
**Integrantes:**
- Pedro Vitor Silva França (2527746)

**Repositório GitHub: [https://github.com/devpedrovitor/pharma-data-manager.git](https://github.com/devpedrovitor/pharma-data-manager.git)** 

**Data de Entrega:** 14/11/2024

## 2. Objetivo do Projeto 📍

O projeto tem como objetivo desenvolver um sistema em Python capaz de gerenciar e analisar informações de uma farmácia, com foco em estoque, vendas e controle de medicamentos.

O sistema permite a organização dos dados farmacêuticos e a geração de análises automatizadas que auxiliam na tomada de decisões, como:

- Identificação dos produtos mais vendidos;
- Monitoramento da validade dos medicamentos;
- Detecção de estoques baixos e necessidade de reposição

## 🧠 3. Diagrama de Contexto (Mermaid)
```mermaid
flowchart TD
    Cliente -->|Compra Medicamentos| Sistema
    Sistema -->|Registrar Dados| CSV 
    Sistema -->|Gerar| Relatorios
    Administrador -->|Analisa| Sistema
````
## ⚙️ 4. Funcionalidades Implementadas

- Leitura e escrita de arquivos CSV (dados de medicamentos e vendas)
- Cálculo de estatísticas básicas (total de vendas, média de preços, etc.)
- Limpeza e tratamento de dados ausentes
- Geração de gráficos com Matplotlib e Seaborn
- Identificação de produtos com baixo estoque
