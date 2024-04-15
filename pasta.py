#RENOMAR PASTA PEGANDO DE ARQUIVO .DOCX

import os
import re
import docx

def encontrar_numero_processo(texto):
    # Encontra o número do processo no texto
    padrao_numero_processo = re.compile(r'PROCESSO_(.*?)AUTOR_', re.DOTALL)
    match = re.search(padrao_numero_processo, texto)
    if match:
        return match.group(1).strip()
    else:
        return None

def ler_arquivo_word_para_texto(caminho_arquivo):
    try:
        doc = docx.Document(caminho_arquivo)
        texto = '\n'.join([paragrafo.text for paragrafo in doc.paragraphs])
        return texto
    except Exception as e:
        print(f"Erro ao ler o arquivo Word: {e}")
        return None

def renomear_pastas_com_numero_processo(diretorio_base):
    for pasta in os.listdir(diretorio_base):
        pasta_path = os.path.join(diretorio_base, pasta)
        if os.path.isdir(pasta_path):
            arquivo_word_encontrado = False
            numero_processo = None
            for arquivo in os.listdir(pasta_path):
                if arquivo.endswith('.docx'):  # Verifica se é um arquivo Word
                    arquivo_word_encontrado = True
                    texto = ler_arquivo_word_para_texto(os.path.join(pasta_path, arquivo))
                    if texto:
                        numero_processo = encontrar_numero_processo(texto)
                        break
                    else:
                        print(f"Arquivo Word '{arquivo}' em '{pasta}' não pôde ser lido.")
            
            if arquivo_word_encontrado and numero_processo:
                novo_nome = f"{numero_processo}"
                novo_caminho = os.path.join(diretorio_base, novo_nome)
                os.rename(pasta_path, novo_caminho)
                print(f"Pasta '{pasta}' renomeada para '{novo_nome}'")
            elif arquivo_word_encontrado:
                print(f"Número do processo não encontrado no arquivo Word em '{pasta}', mantendo o nome da pasta.")
            else:
                print(f"Arquivo Word não encontrado em '{pasta}', mantendo o nome da pasta.")

# Diretório base onde estão as pastas
diretorio_base = r'C:\Users\Richard\Documents\teste'

renomear_pastas_com_numero_processo(diretorio_base)
