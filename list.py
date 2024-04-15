#LISTA ARQUIVO DA PASTA PARA EXCEL

import os
from openpyxl import Workbook

def listar_arquivos_em_excel(diretorio, nome_arquivo_excel):
    # Inicializa o objeto Workbook do openpyxl
    wb = Workbook()
    # Cria uma nova planilha
    planilha = wb.active
    planilha.title = "Lista de Arquivos"
    # Adiciona cabeçalhos
    planilha['A1'] = 'Arquivo'
    planilha['B1'] = 'Caminho'

    # Lista todos os arquivos no diretório especificado
    for indice, arquivo in enumerate(os.listdir(diretorio), start=2):
        # Obtém o caminho completo do arquivo
        caminho_arquivo = os.path.join(diretorio, arquivo)
        # Adiciona o nome do arquivo e o caminho à planilha
        planilha[f'A{indice}'] = arquivo
        planilha[f'B{indice}'] = caminho_arquivo

    # Define o caminho completo para salvar o arquivo Excel dentro do diretório
    caminho_arquivo_excel = os.path.join(diretorio, nome_arquivo_excel)
    # Salva o arquivo Excel dentro do diretório especificado
    wb.save(caminho_arquivo_excel)
    print(f'Lista de arquivos salva em {caminho_arquivo_excel}')

# Diretório que deseja listar os arquivos
diretorio = r'C:\Users\Richard\Downloads\ajustes\word22'
# Nome do arquivo Excel onde os arquivos serão salvos
nome_arquivo_excel = 'lista_de_arquivos.xlsx'

# Chamada da função para listar os arquivos no diretório especificado e salvar em um arquivo Excel dentro do diretório
listar_arquivos_em_excel(diretorio, nome_arquivo_excel)
