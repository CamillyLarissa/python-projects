import re
import time
from PIL import Image  
import Download   
import Imagem
import os 
from urllib.parse import urlparse


def extrair_nome_extensao_url(url):
    # Faz o parse da URL
    parsed_url = urlparse(url)
    # Obtém o caminho do arquivo
    caminho_arquivo = parsed_url.path
    # Extrai o nome do arquivo e a extensão
    nome_arquivo, extensao = os.path.splitext(os.path.basename(caminho_arquivo))
    return nome_arquivo, extensao

def wait_for_file(file_path, interval=1):
    print('Aguarde...')
    while not os.path.exists(file_path):
      time.sleep(interval)
      interval = interval + 1
      print(".", end=" ")

def caminho_imagem(path):
    nome_arquivo, extensao_arquivo = extrair_nome_extensao_url(path)
    return nome_arquivo + extensao_arquivo

def caminhos_imagens(paths):
    caminhos = []
    for path in paths:
        caminho = caminho_imagem(path)
        if os.path.exists(caminho):
            caminhos.append(caminho)
    return caminhos

def cria_imagem(minha_url):
    print(f'URL: {minha_url}')
    nome_arquivo, extensao_arquivo = extrair_nome_extensao_url(minha_url)
    arquivo = nome_arquivo + extensao_arquivo
    print(f'Arquivo: {arquivo}')
    meu_download = Download.Download(url=minha_url, caminho=arquivo)
    print(f'Inicia download...') 
    #verificar se a url é valida
    imagem = meu_download.download() 
    print(f'Download concluído!')
    imagem_teste = Imagem.Imagem( nome=arquivo, path=arquivo)
    print(imagem_teste)
    return imagem_teste.conteudo() 


def validar_url(url: str) -> bool:
    regex = re.compile(
        r'^(?:http|ftp)s?://'
        r'(?:\S+(?::\S)?@)?'
        r'(?:[A-Za-z0-9.-]+|[[A-Fa-f0-9:.]+])'
        r'(?::\d+)?'
        r'(?:[/?#]\S)?$'
    )
    if re.match(regex, url):
        # Verifica se a URL termina com .jpg, .jpeg ou .png
        if url.lower().endswith(('.jpg', '.jpeg', '.png')):
            return True
    return False

def diferenciar_caminho(caminho): 

    if (caminho.startswith('http') and caminho.endswith(('.jpg', '.png'))) or 'encrypted' in caminho: 
        return 1
    elif os.path.exists(caminho): 
        return 2 
    else: 
        return 0
    
def listar_arquivos(): 
    #listando imagens .jpg e .png no diretorio atual
    arquivos = os.listdir() 
    lista = [] 
    for arquivo in arquivos: 
        if arquivo.endswith(('.jpg', '.png')): 
            lista.append(arquivo)
    #devolvendo a lista em string separada por virgula 
    return ', '.join(lista)
    
    