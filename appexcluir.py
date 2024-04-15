#Excluir pasta que tenha somente .JPG . PNG

import os
import shutil

def verificar_e_remover_pasta(pasta):
    arquivos = os.listdir(pasta)
    num_png = 0
    num_jpg = 0

    for arquivo in arquivos:
        if arquivo.lower().endswith('.png'):
            num_png += 1
        elif arquivo.lower().endswith('.jpg'):
            num_jpg += 1

    if (num_png > 0 or num_jpg > 0) and (num_png + num_jpg == len(arquivos)):
        print(f"A pasta '{pasta}' contém apenas arquivos PNG ou JPG. Excluindo...")
        shutil.rmtree(pasta)
    else:
        print(f"A pasta '{pasta}' não atende a condição para exclusão. Mantendo.")

def explorar_pastas_raiz(diretorio_raiz):
    for pasta in os.listdir(diretorio_raiz):
        caminho_completo = os.path.join(diretorio_raiz, pasta)
        if os.path.isdir(caminho_completo):
            verificar_e_remover_pasta(caminho_completo)

if __name__ == "__main__":
    diretorio_raiz = input("Digite o caminho da pasta raiz: ")
    explorar_pastas_raiz(diretorio_raiz)