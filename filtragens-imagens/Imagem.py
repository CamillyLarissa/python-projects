import os 
from PIL import Image 

class Imagem:  
    imagem = None 
    def __init__(self, nome, path): 
        self.nome = nome 
        self.path = path 
        try: 
            self.imagem = Image.open(path) 
        except Exception as ex: 
            print(f'Erro ao criar a imagem com o arquivo {nome} na referência {path}: {str(str)}') 
        
    def dimensoes(self): 
        return self.imagem.size 

    def tamanho(self): 
        return os.path.getsize(self.path) 
    
    def formato(self): 
        return self.imagem.format 
    
    def conteudo(self): 
        return self.imagem 
    
    def __str__(self): 
        return f'Nome: {self.nome}, Dimensões: {self.dimensoes()}, Formato: {self.formato()}, Tamanho: {self.tamanho()} Bytes'