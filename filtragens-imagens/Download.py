import requests
import os

class Download:
    def __init__(self, url, caminho):
        self.url = url
        self.caminho = caminho

    def download(self):
        try:
            response = requests.get(self.url)
            response.raise_for_status()  
            with open(self.caminho, 'wb') as file:
                file.write(response.content)
            print(f"Download completo. Arquivo salvo em: {self.caminho}")
        except requests.exceptions.MissingSchema:
            print("URL inválida. Certifique-se de fornecer uma URL válida.") 
            return None
        except requests.exceptions.RequestException as e:
            print(f"Erro na conexão: {e}") 

