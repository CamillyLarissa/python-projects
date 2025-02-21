import time

def menu():
    while(True):
        print('\n--------------------- MENU ---------------------\n')
        print('1 - 1k palavras')
        print('2 - 10k palavras')
        print('0 - Sair')
        print('\n----------------------------------------------- \n')
        time.sleep(1)
        escolha = int(input('Escolha: '))
        
        if escolha == 1:
            repeticoes = int(input('Digite a quantidade de repetições: '))
            palavra = menu_palavras()
            mil(repeticoes, palavra)
        elif escolha == 2:
            repeticoes = int(input('Digite a quantidade de repetições: '))
            palavra = menu_palavras()
            dez(repeticoes, palavra)
        elif escolha == 0:
            print('Saindo...')
            time.sleep(2)
            break
        else:
            print('Opção inválida! Tente novamente.')
            continue

def menu_palavras():
    while(True):
        print('--------------------- MENU ---------------------')
        print('1 - abacaxi')
        print('2 - goiaba')
        print('3 - manga')
        print('4 - uva')
        print('5 - zumbu')
        escolha = input('Escolha: ')
        if escolha == '1':
            return 'abacaxi'
        elif escolha == '2':
            return 'goiaba'
        elif escolha == '3':
            return 'manga'
        elif escolha == '4':
            return 'uva'
        elif escolha == '5':
            return 'zumbu'
        else:
            print('Opção inválida! Tente novamente.')
            continue

def procurar_nome(texto_lista, palavra):
    if palavra in texto_lista:
        print("A palavra foi encontrada!\n")
    else:
        print("A palavra não foi encontrada!\n")

def imprimir_tempo(tempo, repeticoes):
    for i in range(repeticoes):
        print(f"Tempo de execucao numero {i+1}: {tempo[i]:.6f} segundos\n")
        time.sleep(1)

    print(f'Tempo médio de {repeticoes} execucoes: {sum(tempo) / repeticoes:.6f} segundos')

def mil(repeticoes, palavra):
    tempo = []
    for vezes in range(repeticoes):
        inicio = time.perf_counter()  
        with open("palavras1k.txt", "r", encoding="utf8") as texto:
            texto = str(texto.read())
            texto_lista = texto.splitlines()
            procurar_nome(texto_lista, palavra)
        fim = time.perf_counter()
        tempo.append(fim - inicio)

    imprimir_tempo(tempo, repeticoes)

def dez(repeticoes, palavra):
    tempo = []
    for vezes in range(repeticoes):
        inicio = time.perf_counter()  
        with open("palavras10k.txt", "r", encoding="utf8") as texto:
            texto = str(texto.read())
            texto_lista = texto.splitlines()
            procurar_nome(texto_lista, palavra)
        fim = time.perf_counter()
        tempo.append(fim - inicio)

    imprimir_tempo(tempo, repeticoes)

if __name__ == "__main__":
    menu()