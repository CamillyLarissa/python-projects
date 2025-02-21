class Node:
    def __init__(self, nome, id, pri):
        self.nome = nome
        self.next = 0
        self.id = id
        self.prio = pri
    def getNome(self):
        return self.nome

class Fila:
    def __init__(self):
        self.head = None
        self.quant = 0
        self.cont = 0

    def isEmpty(self):
        return self.head is None

    def enqueue(self, item, idade, pri):
        novo = Node(item, idade, pri)
        novo.next = None

        if self.head is None:
                self.head = novo

        else:
            atual = self.head
            while atual.next is not None:
                atual = atual.next
            atual.next = novo

        self.quant += 1
    def dequeue(self):
            atual = self.head
            atendida = atual

            if atual is not None:
                atual = atual.next
                self.head = atual
                self.cont += 1
                self.quant -=1
                return atendida.nome
            else:
                return None

    def size(self):
        if self.quant == 0:
            print("Fila vazia")
            return self.quant
        return self.quant

    def __str__(self):
        msg = ""
        atual = self.head
        if atual is not None:
            while atual is not None:
                msg = msg + str(atual.nome) +' '
                atual = atual.next
            return msg
        else:
            return 'A fila está vazia'

class FilaPrioridade:
    def __init__(self):
        self.head = None
        self.quant = 0
        self.cont = 0

    def isEmptyPP(self):
        return self.head is None
    def add_prioridade_minima(self, item, idade, pri):
        novo = Node(item, idade, pri)
        novo.next = None
        if self.head is None:
            self.head = novo
        else:
            atual = self.head
            while atual.next is not None:
                atual = atual.next
            atual.next = novo
    def add_prioridade_maxima(self, item, idade, pri):
        novo = Node(item, idade, pri)
        atual = self.head
        aux = atual

        if self.head is None:
            novo.next = self.head
            self.head = novo

        else:
            while atual is not None:
                if novo.id <= atual.id:
                    aux = atual
                atual = atual.next

            if aux == self.head:
                if novo.id <= aux.id:
                    novo.next = aux.next
                    aux.next = novo
                else:
                    novo.next = self.head
                    self.head = novo

            elif aux.next is None:
                novo.next = None
                atual.next = novo

            else:
                novo.next = aux.next
                aux.next = novo

    def enqueuePP(self, item, idade, pri):
        if idade >= 60:
            self.add_prioridade_maxima(item, idade, pri)
        else:
            self.add_prioridade_minima(item, idade, pri)

        self.quant += 1
    def sizePP(self):
        if self.quant == 0:
            print("Fila vazia")
            return self.quant
        return self.quant


    def listarprioridades(self):
        print('0 - Idosos com mais de 60 anos')
        print('1 - Pessoa Portadora de Deficiencia: ')
        print('2 - Pessoa Gestante: ')
        print('3 - Pessoa Lactante: ')
        print('4 - Pessoa acompanhadas por crianças de colo: ')

    def dequeuePP(self):
        atual = self.head
        atendida = atual
        if atual is not None:
            self.head = atual.next
            atual = self.head
            self.quant -=1
            self.cont +=1
            return atendida.nome

    def __str__(self):
        msg = ""
        atual = self.head
        if atual is not None:
            while atual is not None:
                msg = msg + str((atual.getNome())) + ' '
                atual = atual.next
            return msg
        else:
            return "A fila está vazia"