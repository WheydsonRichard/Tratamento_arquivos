#RENOMEAR ARQUIVOS .RAR .ZIP pegando do texto de DOCX


import os
import re
from docx import Document
import zipfile
import shutil

def encontrar_numero_processo(texto):
    # Encontra o número do processo no texto
    padrao_numero_processo = re.compile(r'PROCESSO_(.*?)AUTOR_', re.DOTALL)
    match = re.search(padrao_numero_processo, texto)
    if match:
        return match.group(1).strip()
    else:
        return None

def extrair_texto_docx(caminho_arquivo):
    # Extrai o texto de um arquivo docx
    doc = Document(caminho_arquivo)
    texto_completo = ''
    for paragraph in doc.paragraphs:
        texto_completo += paragraph.text + '\n'
    return texto_completo

def renomear_pasta_com_numero_processo(diretorio):
    for nome_arquivo in os.listdir(diretorio):
        caminho_arquivo = os.path.join(diretorio, nome_arquivo)
        if nome_arquivo.endswith('.zip') and os.path.isfile(caminho_arquivo):
            with zipfile.ZipFile(caminho_arquivo, 'r') as zip_ref:
                for nome_arquivo_zipado in zip_ref.namelist():
                    if nome_arquivo_zipado.endswith('.docx'):
                        with zip_ref.open(nome_arquivo_zipado) as file:
                            texto = extrair_texto_docx(file)
                            numero_processo = encontrar_numero_processo(texto)
                            if numero_processo:
                                novo_nome_pasta = os.path.join(diretorio, f'{numero_processo}')
                                os.makedirs(novo_nome_pasta, exist_ok=True)
                                with open(os.path.join(novo_nome_pasta, nome_arquivo_zipado), 'wb') as f:
                                    f.write(file.read())
                                for nome_arquivo_zip in zip_ref.namelist():  # Extrair todos os arquivos da pasta zipada
                                    if nome_arquivo_zip:  # Ignorar o arquivo .docx já extraído
                                        with zip_ref.open(nome_arquivo_zip) as file_zip:
                                            with open(os.path.join(novo_nome_pasta, os.path.basename(nome_arquivo_zip)), 'wb') as f:
                                                f.write(file_zip.read())
                                print(f'Arquivos da pasta zipada movidos para pasta {numero_processo}')
                                break
                            else:
                                print(f'Número do processo não encontrado no arquivo: {nome_arquivo_zip}')

def renomear_arquivos_com_numero_processo(diretorio):
    for nome_pasta in os.listdir(diretorio):
        caminho_pasta = os.path.join(diretorio, nome_pasta)
        if os.path.isdir(caminho_pasta):
            numero_processo = encontrar_numero_processo(nome_pasta)
            if numero_processo:
                novo_nome_pasta = os.path.join(diretorio, f'{numero_processo}')
                shutil.move(caminho_pasta, novo_nome_pasta)
                print(f'Pasta renomeada: {nome_pasta} para {numero_processo}')
            else:
                print(f'Número do processo não encontrado no nome da pasta: {nome_pasta}')

def executar_codigo():
    diretorio = input("Digite o caminho do diretório que deseja renomear: ")
    if os.path.exists(diretorio):
        renomear_pasta_com_numero_processo(diretorio)
        renomear_arquivos_com_numero_processo(diretorio)
    else:
        print("O diretório especificado não existe.")

# Executar o código
executar_codigo()
