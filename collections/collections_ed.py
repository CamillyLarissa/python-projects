from collections import deque
from collections import Counter
from collections import ChainMap
import time

class TSList:
    def __init__(self):
        self.collection = []

    def inserir(self, elementos: str):
        self.collection.extend(elementos.split())
        return self.collection

    def pesquisar(self, palavra: str) -> bool:
        return palavra in self.collection

    def remover(self, palavra: str):
        if palavra in self.collection:
            self.collection.remove(palavra)
        return self.collection

class TSTuple:
    def __init__(self):
        self.collection = ()

    def inserir(self, elementos: str):
        self.collection += tuple(elementos.split())
        return self.collection

    def pesquisar(self, palavra: str) -> bool:
        return palavra in self.collection

    def remover(self, palavra: str):
        if palavra in self.collection:
            temp_list = list(self.collection)
            temp_list.remove(palavra)
            self.collection = tuple(temp_list)
        return self.collection


class TSDeque:
    def __init__(self):
        self.collection = deque()

    def inserir(self, elementos: str):
        self.collection.extend(elementos.split())
        return self.collection

    def pesquisar(self, palavra: str) -> bool:
        return palavra in self.collection

    def remover(self, palavra: str):
        try:
            self.collection.remove(palavra)
        except ValueError:
            pass  
        return self.collection


class TSCounter:
    def __init__(self):
        self.collection = Counter()

    def inserir(self, elementos: str):
        self.collection.update(elementos.split())
        return self.collection

    def pesquisar(self, palavra: str) -> bool:
        return self.collection[palavra] > 0

    def remover(self, palavra: str):
        if self.collection[palavra] > 0:
            self.collection[palavra] -= 1
            if self.collection[palavra] == 0:
                del self.collection[palavra]
        return self.collection


class TSChainMap:
    def __init__(self):
        self.collection = ChainMap()

    def inserir(self, elementos: str):
        novo_mapa = {palavra: 1 for palavra in elementos.split()}
        self.collection = self.collection.new_child(novo_mapa)
        return self.collection

    def pesquisar(self, palavra: str) -> bool:
        return palavra in self.collection

    def remover(self, palavra: str):
        if palavra in self.collection:
            temp_map = dict(self.collection.maps[0])  # Copia o mapa mais recente
            if palavra in temp_map:
                del temp_map[palavra]  # Remove a palavra
            self.collection.maps[0] = temp_map  # Atualiza o ChainMap
        return self.collection
    
class TSdict:
    def __init__(self):
        self.collection = {}

    def inserir(self, elementos: str):
        for palavra in elementos.split():
            if palavra in self.collection:
                self.collection[palavra] += 1
            else:
                self.collection[palavra] = 1
        return self.collection

    def pesquisar(self, palavra: str) -> bool:
        return palavra in self.collection

    def remover(self, palavra: str):
        if palavra in self.collection:
            if self.collection[palavra] > 1:
                self.collection[palavra] -= 1
            else:
                del self.collection[palavra]
        return self.collection
    
class TSset:
    def __init__(self):
        self.collection = set()

    def inserir(self, elementos: str):
        self.collection.update(elementos.split())
        return self.collection

    def pesquisar(self, palavra: str) -> bool:
        return palavra in self.collection

    def remover(self, palavra: str):
        self.collection.discard(palavra)
        return self.collection
    
class TSnamedtuple:
    def __init__(self):
        self.collection = []

    def inserir(self, elementos: str):
        self.collection.extend(elementos.split())
        return self.collection

    def pesquisar(self, palavra: str) -> bool:
        return palavra in self.collection

    def remover(self, palavra: str):
        if palavra in self.collection:
            self.collection.remove(palavra)
        return self.collection

if __name__ == '__main__':
    
    with open('leipzig100k.txt', 'r') as file:
        texto = file.read()
    
    palavras_para_pesquisar =  ["Lisbon", "NASA", "Kyunghee", "Konkuk", "Sogang", "momentarily", 
                                "rubella", "vaccinations", "government", "Authorities"]
    tempo = []
    tempo_p = []
    tempo_r = []

    while True:
        
        print('\nMenu de escolha de estrutura de dados\n')
        print('Escolha a estrutura de dados que deseja utilizar:')
        print('1 - Lista')
        print('2 - Tupla')
        print('3 - Deque')
        print('4 - Counter')
        print('5 - ChainMap')
        print('6 - Dict')
        print('7 - Set')
        print('8 - Namedtuple')
        print('0 - Sair')

        name = int(input('Digite o número correspondente: '))

        if name == 0:
            break
        elif name == 1:
            ts = TSList()
        elif name == 2:
            ts = TSTuple()
        elif name == 3:
            ts = TSDeque()
        elif name == 4:
            ts = TSCounter()
        elif name == 5:
            ts = TSChainMap()
        elif name == 6:
            ts = TSdict()
        elif name == 7:
            ts = TSset()
        elif name == 8:
            ts = TSnamedtuple()
        else:
            print('Estrutura de dados inválida')
            continue

        print('\n\n')
        print('Qual operação deseja realizar?')
        print('1 - Inserir palavras')
        print('2 - Pesquisar palavras')
        print('3 - Remover palavras')

        operacao = int(input('Digite o número correspondente: '))
        if operacao == 1:
            for i in range(5):
                print('Inserindo palavras...')
                start = time.time()
                ts.inserir(texto)
                end = time.time()
                print(f'Inserção concluída em {end - start:.2f} segundos')
                tempo_insercao = end - start
                tempo.append(tempo_insercao)

            tempo_medio = sum(tempo) / len(tempo)
            print(f'Tempo médio de inserção: {tempo_medio:.2f} segundos')
            print('\n\n')
        elif operacao == 2:
            ts.inserir(texto)
            print(f'Inserção concluída')
   
            for i in range(5):
                print('Pesquisando palavras...')
                start = time.perf_counter()
                for palavra in palavras_para_pesquisar:
                    ts.pesquisar(palavra)
                end = time.perf_counter()
                tempo_pesquisa = (end - start) * 1000  
                print(f'Pesquisa concluída em {tempo_pesquisa:.2f} milissegundos')
                tempo_p.append(tempo_pesquisa)

            tempo_medio_p = sum(tempo_p) / len(tempo_p)
            print(f'Tempo médio de pesquisa: {tempo_medio_p:.2f} milissegundos')

        elif operacao == 3:
            ts.inserir(texto)
            print(f'Inserção concluída')

            for i in range(5):
                print('Removendo palavras...')
                start = time.perf_counter()
                for palavra in palavras_para_pesquisar:
                    ts.remover(palavra)
                end = time.perf_counter()
                tempo_remocao = (end - start) * 1000 
                print(f'Remoção concluída em {tempo_remocao:.2f} milissegundos')
                tempo_r.append(tempo_remocao)

            tempo_medio_r = sum(tempo_r) / len(tempo_r)
            print(f'Tempo médio de remoção: {tempo_medio_r:.2f} milissegundos')
        
        else:
            print('Operação inválida')
            continue
        if isinstance(ts.collection, tuple):
            ts.collection = ()
        else:
            ts.collection.clear()
        tempo.clear()
        tempo_p.clear()
        tempo_r.clear()
        tempo_medio = 0
        tempo_medio_p = 0
        tempo_medio_r = 0
