# MOVER ARQUIVOS  .ZIP e .DOCX PARA FORA DA PASTA

import os
import shutil

def mover_arquivos(pasta_raiz, diretorio_destino):
    for pasta, subpastas, arquivos in os.walk(pasta_raiz):
        tem_png_jpg = False
        tem_word = False
        tem_zip = False
        tem_pdf = False
        tem_outros = False

        for arquivo in arquivos:
            if arquivo.lower().endswith('.png') or arquivo.lower().endswith('.jpg'):
                tem_png_jpg = True
            elif arquivo.lower().endswith('.docx') or arquivo.lower().endswith('.doc'):
                tem_word = True
            elif arquivo.lower().endswith('.zip') or arquivo.lower().endswith('.rar'):
                tem_zip = True
            elif arquivo.lower().endswith('.pdf'):
                tem_pdf = True
            else:
                tem_outros = True

        if tem_png_jpg and tem_zip and not (tem_word or tem_pdf):
            # Condição 2: Mover apenas o arquivo .zip para fora da pasta
            for arquivo in arquivos:
                if arquivo.lower().endswith('.zip') or arquivo.lower().endswith('.rar'):
                    origem = os.path.join(pasta, arquivo)
                    destino = os.path.join(diretorio_destino, arquivo)
                    shutil.move(origem, destino)
            print(f"Arquivo .zip movido para '{diretorio_destino}'.")

        elif tem_word and not (tem_zip or tem_pdf):
            # Condição 1: Mover apenas o arquivo Word para fora da pasta
            for arquivo in arquivos:
                if arquivo.lower().endswith('.docx') or arquivo.lower().endswith('.doc'):
                    origem = os.path.join(pasta, arquivo)
                    destino = os.path.join(diretorio_destino, arquivo)
                    shutil.move(origem, destino)
            print(f"Arquivo Word movido para '{diretorio_destino}'.")

        else:
            # Se nenhuma das condições anteriores for atendida, mantenha os arquivos na pasta
            print(f"Nenhuma condição atendida para a pasta '{pasta}'. Mantendo arquivos.")

def explorar_pastas_raiz(diretorio_raiz, diretorio_destino):
    for pasta in os.listdir(diretorio_raiz):
        caminho_completo = os.path.join(diretorio_raiz, pasta)
        if os.path.isdir(caminho_completo):
            mover_arquivos(caminho_completo, diretorio_destino)

if __name__ == "__main__":
    diretorio_raiz = input("Digite o caminho da pasta raiz: ")
    diretorio_destino = input("Digite o caminho do diretório de destino: ")
    explorar_pastas_raiz(diretorio_raiz, diretorio_destino)
