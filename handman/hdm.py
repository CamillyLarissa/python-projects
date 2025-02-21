import random

class Animais:
    def __init__(self):
        self.ani = ['gato', 'cachorro', 'gaviao'] #criando os animais dentro de uma lista

    def random(self):
        return random.choice(self.ani) #aleatorizando o animal a ser pego
    
class Jogo:
    def __init__(self):
        self.palavras = Animais()
        self.palavra = self.palavras.random()
        self.index = []
        self.n = 0

    def calcularCaracteres(self):
        return len(self.palavra) #necessário para criar os traços
    
    def verificarPertencimento(self, letra):
        self.index.clear()
        for i, l in enumerate(self.palavra):
            if letra == l:
                self.index.append(i) 
        if len(self.index) == 0:
            return None
        return self.index
    
    def get_palavra(self):
        return self.palavra
    
    def dica(self):
        letra = ''
        palavra = self.get_palavra()
        letra = palavra[self.n]
        if self.n >= 2:
            return None
        self.n += 1
        return letra
    
if __name__ == '__main__':
    jogo = Jogo()
    print(jogo.palavra)
    print(jogo.verificarPertencimento('a'))
    print(jogo.dica())
    print(jogo.dica())
    print(jogo.dica())




        
    