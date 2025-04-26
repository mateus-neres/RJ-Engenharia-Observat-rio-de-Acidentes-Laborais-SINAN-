import os, sys
import json

def caminho_absoluto_arquivo(nome_arquivo):
    diretorio_script = os.path.dirname(sys.argv[0])
    caminho_absoluto = os.path.join(diretorio_script, nome_arquivo)
    return caminho_absoluto
