import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

def analise_orcamento_receita(df):
    df['ROI'] = (df['revenue'] - df['budget']) / df['budget']

    plt.figure(figsize=(10, 6))
    plt.scatter(df['budget'], df['revenue'], alpha=0.5)
    plt.xlabel('Orçamento')
    plt.ylabel('Receita')
    plt.title('Relação entre Orçamento e Receita')
    plt.show()

    correlacao = df['budget'].corr(df['revenue'])
    print(f"Correlação entre orçamento e receita: {correlacao}")


def analise_produtoras(df):
    print("Analisando: Como o número de produtoras envolvidas se correlaciona com orçamento e bilheteria?")

def analise_diretores_atores(df):
    print("Analisando: Quais diretores trabalham com os mesmos atores em múltiplos filmes?")

def analise_duracao_popularidade(df):
    print("Analisando: Existe relação entre duração do filme e sua popularidade/avaliação?")

def analise_diversidade_genero(df):
    print("Analisando: Qual a diversidade de gênero nas equipes de produção?")

def analise_generos_orcamento(df):
    print("Analisando: Quais gêneros têm maiores orçamentos e isso resulta em maior receita?")

def analise_equipe_orcamento(df):
    print("Analisando: Como o tamanho da equipe se relaciona com orçamento e sucesso?")

def analise_distribuicao_geografica(df):
    print("Analisando: Qual a distribuição geográfica das produções e sua relação com orçamento/receita?")

def analise_data_bilheteria(df):
    print("Analisando: Existe correlação entre data de lançamento e performance de bilheteria?")

def analise_orcamento_tempo(df):
    print("Analisando: Como orçamento e receita mudaram ao longo do tempo?")

ANALISE_FUNCTIONS = {
    "Qual a relação entre orçamento e receita dos filmes? Existe correlação e qual o ROI?": analise_orcamento_receita,
    "Como o número de produtoras envolvidas se correlaciona com orçamento e bilheteria?": analise_produtoras,
    "Quais diretores trabalham com os mesmos atores em múltiplos filmes?": analise_diretores_atores,
    "Existe relação entre duração do filme e sua popularidade/avaliação?": analise_duracao_popularidade,
    "Qual a diversidade de gênero nas equipes de produção?": analise_diversidade_genero,
    "Quais gêneros têm maiores orçamentos e isso resulta em maior receita?": analise_generos_orcamento,
    "Como o tamanho da equipe se relaciona com orçamento e sucesso?": analise_equipe_orcamento,
    "Qual a distribuição geográfica das produções e sua relação com orçamento/receita?": analise_distribuicao_geografica,
    "Existe correlação entre data de lançamento e performance de bilheteria?": analise_data_bilheteria,
    "Como orçamento e receita mudaram ao longo do tempo?": analise_orcamento_tempo
}

# Caminho certo para o dataset
script_dir = os.path.dirname(os.path.abspath(__file__))
DATASET_PATH = os.path.join(script_dir, 'movies.csv')

def buscar_dataset():
    try:
        df = pd.read_csv(DATASET_PATH)
        return df
    except FileNotFoundError:
        print("Error: movies.csv file not found")
        return None

def main():
    df = buscar_dataset()
    print(df.head())
    for analise, funcao in ANALISE_FUNCTIONS.items():
        print(f"\n{analise}")
        funcao(df)

if __name__ == "__main__":
    main()
