#MOVER ARQUIVO DE UMA PASTA PARA OUTRA

import pandas as pd
import shutil
import os

# Função para mover os arquivos
def mover_arquivos(origem, destino, lista_arquivos):
    for arquivo in lista_arquivos:
        origem_arquivo = os.path.join(origem, arquivo)
        destino_arquivo = os.path.join(destino, arquivo)
        shutil.move(origem_arquivo, destino_arquivo)
        print(f"Arquivo {arquivo} movido para {destino}")

# Ler a planilha Excel
def mover_arquivos_por_planilha(planilha, coluna_arquivo, origem, destino):
    # Carregar a planilha
    df = pd.read_excel(planilha)
    
    # Obter os nomes dos arquivos da coluna especificada
    arquivos_a_mover = df[coluna_arquivo].tolist()
    
    # Mover os arquivos
    mover_arquivos(origem, destino, arquivos_a_mover)

# Diretórios de origem e destino
diretorio_origem = r'C:\Users\Richard\Downloads\ajustes\word22'
diretorio_destino = r'C:\Users\Richard\Downloads\ajustes\word'

# Caminho para a planilha Excel
planilha_excel = r'C:\Users\Richard\Downloads\ajustes\word22\lista_de_arquivos 2.xlsx'

# Nome da coluna que contém os nomes dos arquivos
coluna_arquivo = 'Arquivo'

# Movendo os arquivos conforme a planilha
mover_arquivos_por_planilha(planilha_excel, coluna_arquivo, diretorio_origem, diretorio_destino)
