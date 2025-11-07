import csv
import os

def salvar_dados(dados_atleta, caminho_arquivo='Cadastro-Atletas/data'):
    
        # Caminho absoluto da pasta atual do arquivo (onde está app.py)
    base_dir = "cadastro-atletas"

    # Caminho completo até a subpasta 'data'
    pasta_dados = 'data'

    # Garante que a pasta exista
    os.makedirs(pasta_dados, exist_ok=True)

    # Caminho completo do CSV dentro da pasta 'data'
    caminho_arquivo = os.path.join(pasta_dados, 'dados_formulario.csv')

    #comando para verificar se o arquivo já existe
    arquivo_existe = os.path.isfile(caminho_arquivo)
    
    with open(caminho_arquivo, mode="a", newline="", encoding="utf-8") as arquivo_csv:
            campos = ['nome_atleta', 'idade', 'posicao']
            escritor_csv = csv.DictWriter(arquivo_csv, fieldnames=campos)
            
            #se o arquivo não existir, escreve o cabeçalho
            if not arquivo_existe:
                escritor_csv.writeheader()
            
            escritor_csv.writerow(dados_atleta)