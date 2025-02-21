import time

REPETICOES = 5
tempos = []


def bubbleSort(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp


def selection_sort(arr):
    if not arr:
        return arr
    for i in range(len(arr)):
        min_i = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_i]:
                min_i = j
        arr[i], arr[min_i] = arr[min_i], arr[i]
    


def insertionSort(alist):
    for index in range(1,len(alist)):

        currentvalue = alist[index]
        position = index

        while position>0 and alist[position-1]>currentvalue:
            alist[position]=alist[position-1]
            position = position-1

            alist[position]=currentvalue

def calcular_tempo_bubbleSort(texto):
    for vezes in range(0, REPETICOES):
        inicio = time.time()
        bubbleSort(texto)
        fim = time.time()
        tempos.append(fim - inicio)
        print("Tempo finalizado!")

    for i in range(len(tempos)):
        print(f"tempo {i}: {tempos[i]}")
    media = sum(tempos) / REPETICOES
    tempos.clear()
    return media

def calcular_tempo_selectionSort(texto):
    for vezes in range(0, REPETICOES):
        inicio = time.time()
        selection_sort(texto)
        fim = time.time()
        tempos.append(fim - inicio)
        print("Tempo finalizado!")

    for i in range(len(tempos)):
        print(f"tempo {i}: {tempos[i]}")
    media = sum(tempos) / REPETICOES
    tempos.clear()
    return media

def calcular_tempo_insertionSort(texto):
    for vezes in range(0, REPETICOES):
        inicio = time.time()
        insertionSort(texto)
        fim = time.time()
        tempos.append(fim - inicio)
        print("Tempo finalizado!")

    for i in range(len(tempos)):
        print(f"tempo {i}: {tempos[i]}")
    media = sum(tempos) / REPETICOES
    tempos.clear()
    return media