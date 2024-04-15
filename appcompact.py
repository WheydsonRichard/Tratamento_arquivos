#Compactar pasta para arquivo .zip .rar

import os
import zipfile

def compactar_pasta(pasta_origem, destino):
    for pasta in os.listdir(pasta_origem):
        caminho_pasta = os.path.join(pasta_origem, pasta)
        if os.path.isdir(caminho_pasta):
            nome_zip = os.path.join(destino, f"{pasta}.zip")
            with zipfile.ZipFile(nome_zip, 'w', zipfile.ZIP_DEFLATED) as zipf:
                for raiz, _, arquivos in os.walk(caminho_pasta):
                    for arquivo in arquivos:
                        caminho_arquivo = os.path.join(raiz, arquivo)
                        zipf.write(caminho_arquivo, os.path.relpath(caminho_arquivo, pasta_origem))

# Exemplo de uso:
diretorio_origem = r"C:\Users\Richard\OneDrive - MEIRELES E FREITAS SERVICOS DE COBRANCAS LTDA\Área de Trabalho\EmailLaudos\09.10.11-04 zip"
diretorio_destino = r"C:\Users\Richard\OneDrive - MEIRELES E FREITAS SERVICOS DE COBRANCAS LTDA\Área de Trabalho\EmailLaudos\09.10.11-04 zip"

compactar_pasta(diretorio_origem, diretorio_destino)
