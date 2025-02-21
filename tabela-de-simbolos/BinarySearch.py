class BinarySearchST:
    INIT_CAPACITY = 2
    
    def __init__(self, capacity=None):
        if capacity is None:
            capacity = self.INIT_CAPACITY
        self.key_list = [None] * capacity
        self.vals = [None] * capacity
        self.n = 0

    def _resize(self, capacity):
        tempk = [None] * capacity
        tempv = [None] * capacity
        for i in range(self.n):
            tempk[i] = self.key_list[i]
            tempv[i] = self.vals[i]
        self.vals = tempv
        self.key_list = tempk

    def size(self):
        return self.n

    def is_empty(self):
        return self.size() == 0

    def contains(self, key):
        if key is None:
            raise ValueError("o argumento para contains() é nulo")
        return self.get(key) is not None

    def get(self, key):
        if key is None:
            raise ValueError("o argumento para get() é nulo")
        if self.is_empty():
            return None
        i = self.rank(key)
        if i < self.n and self.key_list[i] == key:
            return self.vals[i]
        return None

    def rank(self, key):
        if key is None:
            raise ValueError("o argumento para rank() é nulo")
        lo, hi = 0, self.n - 1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if key < self.key_list[mid]:
                hi = mid - 1
            elif key > self.key_list[mid]:
                lo = mid + 1
            else:
                return mid
        return lo

    def put(self, key, val):
        if key is None:
            raise ValueError("primeiro argumento para put() é nulo")

        if val is None:
            self.delete(key)
            return

        i = self.rank(key)

        if i < self.n and self.key_list[i] == key:
            self.vals[i] = val
            return

        if self.n == len(self.key_list):
            self._resize(2 * len(self.key_list))

        for j in range(self.n, i, -1):
            self.key_list[j] = self.key_list[j-1]
            self.vals[j] = self.vals[j-1]

        self.key_list[i] = key
        self.vals[i] = val
        self.n += 1

    def delete(self, key):
        if key is None:
            raise ValueError("argumento para delete() é nulo")
        if self.is_empty():
            return

        i = self.rank(key)

        if i == self.n or self.key_list[i] != key:
            return

        for j in range(i, self.n - 1):
            self.key_list[j] = self.key_list[j+1]
            self.vals[j] = self.vals[j+1]

        self.n -= 1
        self.key_list[self.n] = None  
        self.vals[self.n] = None

        if self.n > 0 and self.n == len(self.key_list) // 4:
            self._resize(len(self.key_list) // 2)

    def delete_min(self):
        if self.is_empty():
            raise ValueError("Erro de subfluxo na tabela de símbolos")
        self.delete(self.min())

    def delete_max(self):
        if self.is_empty():
            raise ValueError("Erro de subfluxo na tabela de símbolos")
        self.delete(self.max())

    def min(self):
        if self.is_empty():
            raise ValueError("min() chamado com tabela de símbolos vazia")
        return self.key_list[0]

    def max(self):
        if self.is_empty():
            raise ValueError("max() chamado com tabela de símbolos vazia")
        return self.key_list[self.n - 1]

    def select(self, k):
        if k < 0 or k >= self.size():
            raise ValueError("select() chamado com argumento inválido: " + k)
        return self.key_list[k]

    def floor(self, key):
        if key is None:
            raise ValueError("argumento para floor() é nulo")
        i = self.rank(key)
        if i < self.n and key == self.key_list[i]:
            return self.key_list[i]
        if i == 0:
            raise ValueError("argumento para floor() é muito pequeno")
        return self.key_list[i - 1]

    def ceiling(self, key):
        if key is None:
            raise ValueError("argumento para ceiling() é nulo")
        i = self.rank(key)
        if i == self.n:
            raise ValueError("argumento para ceiling() é muito grande")
        return self.key_list[i]

    def size_range(self, lo, hi):
        if lo is None:
            raise ValueError("o primeiro argumento para size_range() é nulo")
        if hi is None:
            raise ValueError("o segundo argumento para size_range() é nulo")
        if lo > hi:
            return 0
        if self.contains(hi):
            return self.rank(hi) - self.rank(lo) + 1
        else:
            return self.rank(hi) - self.rank(lo)

    def keys_range(self, lo, hi):
        if lo is None:
            raise ValueError("primeiro argumento para keys_range() é nulo")
        if hi is None:
            raise ValueError("o segundo argumento para keys_range() é nulo")
        queue = []
        if lo > hi:
            return queue
        for i in range(self.rank(lo), self.rank(hi)):
            queue.append(self.key_list[i])
        if self.contains(hi):
            queue.append(self.key_list[self.rank(hi)])
        return queue

    def _check(self):
        return self._is_sorted() and self._rank_check()

    def _is_sorted(self):
        for i in range(1, self.size()):
            if self.key_list[i] < self.key_list[i - 1]:
                return False
        return True

    def _rank_check(self):
        for i in range(self.size()):
            if i != self.rank(self.select(i)):
                return False
        for i in range(self.size()):
            if self.key_list[i] != self.select(self.rank(self.key_list[i])):
                return False
        return True


if __name__ == "__main__":
    st = BinarySearchST()
    for i in range(100):  #simulando entrada
        key = str(i)
        st.put(key, i)
    for s in st.key_list:
        if s is not None:
            print(s, st.get(s))
