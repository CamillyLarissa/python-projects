import Grupo1
import Grupo2
import numpy as np
import matplotlib.pyplot as plt
import time


b1, b2, b3 = 0, 0, 0
s1,s2,s3 = 0,0,0
i1,i2,i3 = 0,0,0
m1,m2,m3 = 0,0,0
sh1,sh2,sh3 = 0,0,0
q1,q2,q3 = 0,0,0
h1, h2,h3 = 0,0,0

while(True):
    print("\n----------------------------MENU-------------------------")
    print(" 1 - Arquivo nomes 100k ")
    print(" 2 - Arquivo nomes 250k ")
    print(" 3 - Arquivo nomes 500k ")
    print(" 4 - Tempo médio de cada arquivo dos metodos de ordenação ")
    print(" 0 - SAIR")
    print("\nAo sair será mostrado os graficos dos tempos médios dos metódos de ordenção relacionado-se com os arquivos!\n")
    
    op = int(input("Digite a opção desejada: \n"))
    match op:
        case 1:
            with open("nomes100k.txt", "r", encoding="utf-8") as arquivo:
                texto = arquivo.read().split() 

            print("1- Bubble Sort, 2 -Selection Sort, 3 - Insertion")
            print("4 - Merge Sort, 5 - Shell Sort, 6 - Quick Sort, 7 - Heap Sort\n")

            x = int(input("Digite o numero do metodo de ordenação a qual deseja fazer o tempo médio: "))
            if x == 1:
                b1 = Grupo1.calcular_tempo_bubbleSort(texto)
                print(f"\nTempo médio de: {b1}")
            elif x == 2: 
                s1 = Grupo1.calcular_tempo_selectionSort(texto)
                print(f"\nTempo médio de: {s1}")
            elif x == 3:
                i1 = Grupo1.calcular_tempo_insertionSort(texto)
                print(f"\nTempo médio de: {i1}")
            elif x == 4: 
                m1 = Grupo2.calcular_tempo_mergeSort(texto)
                print(f"\nTempo médio de: {m1}")
            elif x == 5:
                sh1 = Grupo2.calcular_tempo_shellSort(texto)
                print(f"\nTempo médio de: {sh1}")
            elif x == 6: 
                q1 = Grupo2.calcular_tempo_quickSort(texto)
                print(f"\nTempo médio de: {q1}")
            elif x == 7:
                h1 = Grupo2.calcular_tempo_heapSort(texto)
                print(f"\nTempo médio de: {h1}")
            else:
                print("Valor inválido")

        case 2:
            with open("nomes250k.txt", "r", encoding="utf-8") as arquivo:
                texto = arquivo.read().split() 

            print("1- Bubble Sort, 2 -Selection Sort, 3 - Insertion")
            print("4 - Merge Sort, 5 - Shell Sort, 6 - Quick Sort, 7 - Heap Sort")

            x = int(input("Digite o numero do metodo de ordenação a qual deseja fazer o tempo médio: "))
            if x == 1:
                b2 = Grupo1.calcular_tempo_bubbleSort(texto)
                print(f"\nTempo médio de: {b2}")
            elif x == 2: 
                s2 = Grupo1.calcular_tempo_selectionSort(texto)
                print(f"\nTempo médio de: {s2}")
            elif x == 3:
                i2 = Grupo1.calcular_tempo_insertionSort(texto)
                print(f"\nTempo médio de: {i2}")
            elif x == 4: 
                m2 = Grupo2.calcular_tempo_mergeSort(texto)
                print(f"\nTempo médio de: {m2}")
            elif x == 5:
                sh2 =  Grupo2.calcular_tempo_shellSort(texto)
                print(f"\nTempo médio de: {sh2}")
            elif x == 6: 
                q2 =  Grupo2.calcular_tempo_quickSort(texto)
                print(f"\nTempo médio de: {q2}")
            elif x == 7:
                h2 = Grupo2.calcular_tempo_heapSort(texto)
                print(f"\nTempo médio de: {h2}")
            else:
                print("Valor inválido")

        case 3:
            with open("nomes500k.txt", "r", encoding="utf-8") as arquivo:
                texto = arquivo.read().split() 

            print("1- Bubble Sort, 2 -Selection Sort, 3 - Insertion")
            print("4 - Merge Sort, 5 - Shell Sort, 6 - Quick Sort, 7 - Heap Sort")

            x = int(input("Digite o numero do metodo de ordenação a qual deseja fazer o tempo médio: "))
            if x == 1:
                b3 = Grupo1.calcular_tempo_bubbleSort(texto)
                print(f"\nTempo médio de: {b3}")
            elif x == 2: 
                s3 = Grupo1.calcular_tempo_selectionSort(texto) 
                print(f"\nTempo médio de: {s3}")
            elif x == 3:
                i3 = Grupo1.calcular_tempo_insertionSort(texto)
                print(f"\nTempo médio de: {i3}")
            elif x == 4: 
                m3 = Grupo2.calcular_tempo_mergeSort(texto)
                print(f"\nTempo médio de: {m3}")
            elif x == 5:
                sh3 =  Grupo2.calcular_tempo_shellSort(texto)
                print(f"\nTempo médio de: {sh3}")
            elif x == 6: 
                q3 =  Grupo2.calcular_tempo_quickSort(texto) 
                print(f"\nTempo médio de: {q3}")
            elif x == 7:
                h3 = Grupo2.calcular_tempo_heapSort(texto)
                print(f"\nTempo médio de: {h3}")
            else:
                print("Opção Inválida")
        
        case 4:
            print("1- Bubble Sort, 2 -Selection Sort, 3 - Insertion")
            print("4 - Merge Sort, 5 - Shell Sort, 6 - Quick Sort, 7 - Heap Sort")

            m = int(input("Digite o metodo de ordenação a qual deseja vizualizar o tempo médio: "))
            if m == 1:
                print(f"Tempo médio em nomes100k: {b1}\nTempo médio em nomes250k: {b2}\nTempo médio em nomes500k: {b3}")
            elif m == 2: 
                print(f"Tempo médio em nomes100k: {s1}\nTempo médio em nomes250k: {s2}\nTempo médio em nomes500k: {s3}") 
            elif m == 3:
                print(f"Tempo médio em nomes100k: {i1}\nTempo médio em nomes250k: {i2}\nTempo médio em nomes500k: {i3}")
            elif m == 4: 
                print(f"Tempo médio em nomes100k: {m1}\nTempo médio em nomes250k: {m2}\nTempo médio em nomes500k: {m3}") 
            elif m == 5:
                print(f"Tempo médio em nomes100k: {sh1}\nTempo médio em nomes250k: {sh2}\nTempo médio em nomes500k: {sh3}")
            elif m == 6: 
                print(f"Tempo médio em nomes100k: {q1}\nTempo médio em nomes250k: {q2}\nTempo médio em nomes500k: {q3}") 
            elif m == 7:
                print(f"Tempo médio em nomes100k: {h1}\nTempo médio em nomes250k: {h2}\nTempo médio em nomes500k: {h3}")
            else:
                print("Opção Inválida")   
        case 0:
            break
        case others:
            print("Resposta Inválida!")
        

bubble = [b1,b2,b3]
selection = [s1,s2,s3]
insertion = [i1,i2,i3]

barWidth = 0.25

plt.figure(figsize=(10,5))

r1 = np.arange(len(bubble))
r2 = [x + barWidth for x in r1]
r3 = [x + barWidth for x in r2]

plt.bar(r1, bubble, color = '#6A5ACD', width=barWidth,label='Bubble')
plt.bar(r2, selection, color = "blue", width=barWidth,label='Selection')
plt.bar(r3, insertion, color = "green", width=barWidth,label='Insetion')


plt.xticks([r + barWidth for r in range (len(bubble))], ['Nomes 100k', 'Nomes 250k', 'Nomes 500k'])

plt.ylabel("segundos")

plt.xlabel("Arquivos")

plt.suptitle("Quadráticos")

plt.title("Tempo médio de execução")

plt.legend(["Bubble", "Selection", "Insertion"])

plt.show()


    
shellSort = [sh1,sh2,sh3]
mergeSort = [m1,m2,m3]
quickSort = [q1,q2,q3]
heapSort = [h1,h2,h3]

barWidth = 0.20

plt.figure(figsize=(10, 6))

r1 = np.arange(len(shellSort))
r2 = [x + barWidth for x in r1]
r3 = [x + barWidth for x in r2]
r4 = [x + barWidth for x in r3]

plt.bar(r1, shellSort, color = '#6A5ACD', width=barWidth,label='Shell Sort')
plt.bar(r2, mergeSort, color = "red", width=barWidth,label='Merge Sort')
plt.bar(r3, quickSort, color = "gray", width=barWidth,label='Quick Sort')
plt.bar(r4, heapSort, color = "pink", width=barWidth,label='Heap Sort')


plt.xticks([r + barWidth for r in range (len(shellSort))], ['Nomes 100k', 'Nomes 250k', 'Nomes 500k'])

plt.suptitle("Logaritmicos")

plt.ylabel("segundos")

plt.xlabel("Arquivos")

plt.legend(["Shell Sort", "Merge Sort", "Quick Sort", "Heap Sort"])

plt.title("Tempo médio de execução")

plt.show()

