import time

REPETICOES = 5
tempos = []

def quickSort(alist):
   quickSortHelper(alist,0,len(alist)-1)

def quickSortHelper(alist,first,last):
   if first<last:

       splitpoint = partition(alist,first,last)

       quickSortHelper(alist,first,splitpoint-1)
       quickSortHelper(alist,splitpoint+1,last)


def partition(alist,first,last):
   pivotvalue = alist[first]

   leftmark = first+1
   rightmark = last

   done = False
   while not done:

       while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
           leftmark = leftmark + 1

       while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
           rightmark = rightmark -1

       if rightmark < leftmark:
           done = True
       else:
           temp = alist[leftmark]
           alist[leftmark] = alist[rightmark]
           alist[rightmark] = temp

   temp = alist[first]
   alist[first] = alist[rightmark]
   alist[rightmark] = temp


   return rightmark
        
def mergeSort(alist):
    #print("Splitting ",alist)
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1
    #print("Merging ",alist)

def shellSort(alist):
    sublistcount = len(alist)//2
    while sublistcount > 0:

      for startposition in range(sublistcount):
        gapInsertionSort(alist,startposition,sublistcount)

      #print("After increments of size",sublistcount,
                                   #"The list is",alist)

      sublistcount = sublistcount // 2

def gapInsertionSort(alist,start,gap):
    for i in range(start+gap,len(alist),gap):

        currentvalue = alist[i]
        position = i

        while position>=gap and alist[position-gap]>currentvalue:
            alist[position]=alist[position-gap]
            position = position-gap

        alist[position]=currentvalue

def heapify(arr, n, i):
        largest = i  
        l = 2 * i + 1  
        r = 2 * i + 2  

        if l < n and arr[i] < arr[l]:
            largest = l
 
        if r < n and arr[largest] < arr[r]:
            largest = r
 
        if largest != i:
            (arr[i], arr[largest]) = (arr[largest], arr[i]) 
        
            heapify(arr, n, largest)
 

def heapSort(arr):
    n = len(arr)

    for i in range(n // 2, -1, -1):
        heapify(arr, n, i)


    for i in range(n - 1, 0, -1):
        (arr[i], arr[0]) = (arr[0], arr[i])  
        heapify(arr, i, 0)


def calcular_tempo_quickSort(texto):
    for vezes in range(0, REPETICOES):
        inicio = time.time()
        quickSort(texto)
        fim = time.time()
        tempos.append(fim - inicio)
        print("Tempo finalizado!")
    
    for i in range(len(tempos)):
        print(f"tempo {i}: {tempos[i]}")
    media = sum(tempos) / REPETICOES
    tempos.clear()
    return media

def calcular_tempo_mergeSort(texto):
    for vezes in range(0, REPETICOES):
        inicio = time.time()
        mergeSort(texto)
        fim = time.time()
        tempos.append(fim - inicio)
        print("Tempo finalizado!")

    for i in range(len(tempos)):
        print(f"tempo {i}: {tempos[i]}")
    media = sum(tempos) / REPETICOES
    tempos.clear()
    return media

def calcular_tempo_shellSort(texto):
    for vezes in range(0, REPETICOES):
        inicio = time.time()
        shellSort(texto)
        fim = time.time()
        tempos.append(fim - inicio)
        print("Tempo finalizado!")

    for i in range(len(tempos)):
        print(f"tempo {i}: {tempos[i]}")
    media = sum(tempos) / REPETICOES
    tempos.clear()
    return media

def calcular_tempo_heapSort(texto):
    for vezes in range(0, REPETICOES):
        inicio = time.time()
        heapSort(texto)
        fim = time.time()
        tempos.append(fim - inicio)
        print("Tempo finalizado!")

    for i in range(len(tempos)):
        print(f"tempo {i}: {tempos[i]}")
    media = sum(tempos) / REPETICOES
    tempos.clear()
    return media