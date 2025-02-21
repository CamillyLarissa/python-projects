import pandas as pd
import matplotlib.pyplot as plt


def insercao():
    tempo_medio_list = 0.31
    tempo_medio_tuple = 0.40
    tempo_medio_deque = 0.29
    tempo_medio_counter = 0.69
    tempo_medio_chainMap = 0.64
    tempo_medio_dict = 0.29
    tempo_medio_set = 0.51
    tempo_medio_namedTuple = 0.29

    data = {'Tempo Médio': [tempo_medio_list, tempo_medio_tuple, tempo_medio_deque, tempo_medio_counter, tempo_medio_chainMap, tempo_medio_dict, tempo_medio_set, tempo_medio_namedTuple]}
    df = pd.DataFrame(data, index=['List', 'Tuple', 'Deque', 'Counter', 'ChainMap', 'Dict', 'Set', 'NamedTuple'])

    ax = df.plot(kind='bar', figsize=(10, 9))
    plt.title('Tempo Médio de Inserção por Tipo de Estrutura')
    plt.ylabel('Tempo (s)')
    plt.xticks(rotation=0)

    for p in ax.patches:
        ax.annotate(str(p.get_height()), (p.get_x() + p.get_width() / 2, p.get_height()), ha='center', va='bottom')

    plt.show()

def pesquisar():
    tempo_medio_list = 205.30
    tempo_medio_tuple = 224.61
    tempo_medio_deque = 270.82
    tempo_medio_counter = 0.01
    tempo_medio_chainMap = 0.03
    tempo_medio_dict = 0.01
    tempo_medio_set = 0.01
    tempo_medio_namedTuple = 217.76

    data = {'Tempo Médio': [tempo_medio_list, tempo_medio_tuple, tempo_medio_deque, tempo_medio_counter, tempo_medio_chainMap, tempo_medio_dict, tempo_medio_set, tempo_medio_namedTuple]}
    df = pd.DataFrame(data, index=['List', 'Tuple', 'Deque', 'Counter', 'ChainMap', 'Dict', 'Set', 'NamedTuple'])

    ax = df.plot(kind='bar', figsize=(10, 9))
    plt.title('Tempo Médio de Pesquisa por Tipo de Estrutura')
    plt.ylabel('Tempo (milissegundos)')
    plt.xticks(rotation=0)

    for p in ax.patches:
        ax.annotate(str(p.get_height()), (p.get_x() + p.get_width() / 2, p.get_height()), ha='center', va='bottom')

    plt.show()

def remover():
    tempo_medio_list =  640.74
    tempo_medio_tuple = 3810.83
    tempo_medio_deque = 534.91
    tempo_medio_counter = 0.03
    tempo_medio_chainMap = 105.34
    tempo_medio_dict = 0.02
    tempo_medio_set = 0.01
    tempo_medio_namedTuple = 626.92

    data = {'Tempo Médio': [tempo_medio_list, tempo_medio_tuple, tempo_medio_deque, tempo_medio_counter, tempo_medio_chainMap, tempo_medio_dict, tempo_medio_set, tempo_medio_namedTuple]}
    df = pd.DataFrame(data, index=['List', 'Tuple', 'Deque', 'Counter', 'ChainMap', 'Dict', 'Set', 'NamedTuple'])

    ax = df.plot(kind='bar', figsize=(10, 9))
    plt.title('Tempo Médio de Remoção por Tipo de Estrutura')
    plt.ylabel('Tempo (milissegundos)')
    plt.xticks(rotation=0)

    for p in ax.patches:
        ax.annotate(str(p.get_height()), (p.get_x() + p.get_width() / 2, p.get_height()), ha='center', va='bottom')

    plt.show()

if __name__ == "__main__":
    insercao()
    pesquisar()
    remover()