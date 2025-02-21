from tkinter import *
from tkinter import ttk
import customtkinter as ctk


class Arvore:
    def __init__(self):
        self.raiz = None

    class Node:
        def __init__(self, key):
            self.info = key
            self.esq = None
            self.dir = None
            self.x = 0
            self.y = 0

    def insert(self, val):
        if self.raiz is None:
            self.raiz = self.Node(val)

        else:
            v = self.get(val)
            if v is not None:
                return False
            else:
                self.put(self.raiz, val)
                
            

    def put(self, atual, val):
        if val == atual.info:
            return False
        elif val < atual.info: # ir para a esquerda
            if atual.esq is None:
                atual.esq = self.Node(val)
                
            else:
                self.put(atual.esq, val)

        else: # ir para a direita
            if atual.dir is None:
                atual.dir = self.Node(val)
            
            else:
                self.put(atual.dir, val)
    # fim do put

    def get(self, val):
        if self.raiz == None: # arvore vazia
            return "arvore vazia!"

        aux = self.raiz # comecar sempre pela raiz
        while aux.info != val:
            if val < aux.info:
                aux = aux.esq # ir para a esquerda
            else:
                aux = aux.dir # ir para a direita
            if aux == None:
                return None
        return aux
    # fim do get
    def render_tree(self, canvas):
        if self.raiz is not None:
            self.calculate_positions(self.raiz, 600, 50, 350)
            self.render(canvas, self.raiz)

    def calculate_positions(self, node, x, y, h_gap):
        MIN_DISTANCE = 30 
        if node is not None:
            node.x = x
            node.y = y
            if node.esq is not None:
                new_x = x - h_gap
                if abs(new_x - x) < MIN_DISTANCE:
                    new_x = x - MIN_DISTANCE
                self.calculate_positions(node.esq, new_x, y + 50, h_gap // 2)
            if node.dir is not None:
                new_x = x + h_gap
                if abs(new_x - x) < MIN_DISTANCE:
                    new_x = x + MIN_DISTANCE
                self.calculate_positions(node.dir, new_x, y + 50, h_gap // 2)

    def render(self, canvas, atual):
        if atual.esq is not None:
            canvas.create_line(atual.x, atual.y, atual.esq.x, atual.esq.y, fill="black", width=2)
            self.render(canvas, atual.esq)
        if atual.dir is not None:
            canvas.create_line(atual.x, atual.y, atual.dir.x, atual.dir.y, fill="black", width=2)
            self.render(canvas, atual.dir)
        
        if isinstance(atual.info, str):
            oval_width = len(atual.info) * 10
            oval_height = 30
            canvas.create_oval(atual.x - oval_width/2, atual.y - oval_height/2, atual.x + oval_width/2, atual.y + oval_height/2, fill="#00ffff", outline="#00bfff", width=5)
            canvas.create_text(atual.x, atual.y, text=atual.info, font=('Balker.tff', 16), fill='black')
        else:
            canvas.create_oval(atual.x - 15, atual.y - 15, atual.x + 15, atual.y + 15, fill="#00ffff", outline="#00bfff", width=10)
            canvas.create_text(atual.x, atual.y, text=atual.info, font=('Balker.tff', 16), fill='black')   
            
    def emOrdem(self, aux): # percurso em ordem: esq; raiz; dir
        esquerda = ""
        raiz = ""
        direita = ""
        if aux is not None:

            esquerda = self.emOrdem(aux.esq)
            raiz = str(aux.info)
            direita = self.emOrdem(aux.dir)

        return (esquerda + " " + raiz + " " + direita).strip()

    def preOrdem(self, aux): # percurso pre ordem: raiz; esq; dir
        esquerda = ""
        raiz = ""
        direita = ""
        if aux is not None:
            raiz = str(aux.info)
            esquerda = self.preOrdem(aux.esq)
            direita = self.preOrdem(aux.dir)

        return (raiz + " " + esquerda + " " + direita).strip()

    def posOrdem(self, aux): # percurso pos ordem: esq; dir; raiz --
        esquerda = ""
        raiz = ""
        direita = ""
        if aux is not None:
            esquerda = self.posOrdem(aux.esq)
            direita = self.posOrdem(aux.dir)
            raiz = str(aux.info)

        return (esquerda + " " + direita + " " + raiz).strip()

    def levelOrder(self, aux): # percurso em largura --
        if aux == None:
            return ""
        fila = []
        Level_order = []
        fila.append(aux)

        while len(fila) > 0:

            no = fila.pop(0)
            Level_order.append(str(no.info))

            if no.esq is not None:
                fila.append(no.esq)
            if no.dir is not None:
                fila.append(no.dir)

        return " ".join(Level_order)


    def altura(self, aux): # altura da arvore
        if aux == None:
            return 0
        else:
            Altura = 1 + max(self.altura(aux.esq), self.altura(aux.dir))
            return Altura

    def tamanho(self, aux): # tamanho da arvore
        if aux == None:
            return 0
        else:
            Tamanho = 1 + self.tamanho(aux.esq) + self.tamanho(aux.dir)
            return Tamanho

    def Maior_Elemento(self, aux): # maior elemento da arvore
        if aux == None:
            return None
        else:
            if aux.dir == None:
                return aux.info
            else:
                Maior_Elemento = self.Maior_Elemento(aux.dir)
                return Maior_Elemento

    def Menor_Elemento(self, aux): # menor elemento da arvore
        if aux == None:
            return None
        else:
            if aux.esq == None:
                return aux.info
            else:
                Menor_Elemento = self.Menor_Elemento(aux.esq)
                return Menor_Elemento


    def Internal_Path_Length(self, aux,level): #soma dos niveis de todos os nos internos(comprimento interno)

        if aux == None:
            return 0
        else:
            Comprimento_Interno = level + self.Internal_Path_Length(aux.esq, level+1) + self.Internal_Path_Length(aux.dir, level+1)
            return Comprimento_Interno

    def is_Balanceada(self, aux): 
        if aux == None:
            return 0
        elif(self.altura(aux.esq) - self.altura(aux.dir) > 1):
            return -1
        else:
            return True

    def remove_all_nodes(self, aux):
        if aux is not None:
            self.remove_all_nodes(aux.esq)
            self.remove_all_nodes(aux.dir)
        self.raiz = None
    

        