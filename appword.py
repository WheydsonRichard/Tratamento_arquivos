#RENOMEAR ARQUIVOS DORCX pegando do texto de DOCX

import os
import re
import textract

def extrair_nome_autor(caminho_arquivo):
    if caminho_arquivo.endswith('.docx'):
        try:
            texto = textract.process(caminho_arquivo).decode('utf-8')
            padrao_nome_autor = re.compile(r'AUTOR_(.*?)CLIENTE_', re.DOTALL)
            match = re.search(padrao_nome_autor, texto)
            if match:
                return match.group(1).strip()
            else:
                return None
        except Exception as e:
            print(f"Erro ao extrair texto do arquivo {caminho_arquivo}: {e}")
            return None
    elif caminho_arquivo.endswith('.doc'):
        try:
            texto = textract.process(caminho_arquivo).decode('utf-8')
            padrao_nome_autor = re.compile(r'AUTOR_(.*?)CLIENTE_', re.DOTALL)
            match = re.search(padrao_nome_autor, texto)
            if match:
                return match.group(1).strip()
            else:
                return None
        except Exception as e:
            print(f"Erro ao extrair texto do arquivo {caminho_arquivo}: {e}")
            return None
    else:
        return None

def renomear_arquivos(diretorio):
    concluido = True
    for nome_arquivo in os.listdir(diretorio):
        caminho_arquivo = os.path.join(diretorio, nome_arquivo)
        if os.path.isfile(caminho_arquivo):
            nome_autor = extrair_nome_autor(caminho_arquivo)
            if nome_autor:
                # Remover quebras de linha do nome do autor
                nome_autor = nome_autor.replace('\n', '').strip()
                 # Substituir '/' por '_'
                nome_autor = nome_autor.replace('/', '_')
                 # Substituir ':' por '_'
                nome_autor = nome_autor.replace(':', ';')
                
                
                novo_nome = f'{nome_autor}.docx'
                caminho_novo = os.path.join(diretorio, novo_nome)
                contador = 1
                while os.path.exists(caminho_novo):
                    novo_nome = f'{nome_autor}_copia_{contador}.docx'
                    caminho_novo = os.path.join(diretorio, novo_nome)
                    contador += 1
                os.rename(caminho_arquivo, caminho_novo)
                print(f'Arquivo renomeado: {nome_arquivo} para {novo_nome}')
            else:
                print(f'Nome do autor não encontrado no arquivo: {nome_arquivo}')
                concluido = False
        else:
            print(f'{nome_arquivo} não é um arquivo')
            concluido = False
    if concluido:
        print("Todos os arquivos foram renomeados com sucesso!")


def executar_codigo(diretorio):
    if diretorio:
        renomear_arquivos(diretorio)

# Defina o diretório aqui
diretorio = r"C:\Users\Richard\OneDrive - MEIRELES E FREITAS SERVICOS DE COBRANCAS LTDA\Área de Trabalho\EmailLaudos\WORD"

executar_codigo(diretorio)
