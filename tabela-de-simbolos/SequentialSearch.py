class SequentialSearchST:
    class Node:
        def __init__(self, key, val, prox):
            self.key = key
            self.value = val
            self.prox = prox
    
    def __init__(self):
        self.n = 0
        self.ini = None

    def size(self):
        return self.n
    
    def isEmpty(self):
        return self.size() == 0
    
    def contains(self, key):
        if key is None:
            raise ValueError("Argumento para contains() e nulo")
        return self.get(key) is not None
    
    def get(self, key):
        if key is None:
             raise ValueError("Argumento para get() e nulo")
        atual = self.ini
        while atual is not None:
            if key == atual.key:
                return atual.value
            atual = atual.prox
        return None
    
    def put(self, key, val):
        if key is None:
             raise ValueError("O primeiro argumento para put() e nulo")
        if val is None:
            self.delete(key)
            return
        
        atual = self.ini
        while atual is not None:
            if key == atual.key:
               atual.value = val
               return
            atual = atual.prox

        self.ini = self.Node(key,val,self.ini)
        self.n +=1

    def delete(self, key):
        if key is None:
             raise ValueError("Argumento para delete() e nulo")
        
        self.ini = self._delete(self.ini, key)

    def _delete(self, atual,key):     
        if atual is None:
            return None

        if key == atual.key:
            self.n -=1
            return atual.prox
        
        atual.prox = self._delete(atual.prox, key)
        return atual
    
    def keys(self):
        queue = []
        atual = self.ini
        while atual is not None:
            queue.append(atual.key)
            atual = atual.prox
        return queue

if __name__ == "__main__":
    st = SequentialSearchST()
    for i in range(100):  #simulando entrada
        key = str(i)
        st.put(key, i)
    for s in st.keys():
        if s is not None:
            print(s, st.get(s))
