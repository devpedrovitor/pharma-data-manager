import pandas as pd 
from termcolor import colored

def load_csv(path):
    # Carrega o arquivo csv
    try:
        df = pd.read_csv(path)
        print(colored("Arquvio csv carregado com sucesso!", "green"))
    except FileNotFoundError:
        print(colored("Arquivo não encontrado!", "red"))
        return None

def save_csv(df, path):
    # Salva o arquvio csv
    df.to_csv(path, index=False)
    print(colored("Arquivo salvo com sucesso", "green"))

        