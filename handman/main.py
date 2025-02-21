import hdm 
import customtkinter as ctk
from tkinter import *
from tkinter import Canvas
from tkinter import ttk


class GUI:
    def __init__(self, root):
        self.root = root
        self.root.title('Forca')
        self.root.geometry("1000x730")
        self.root.resizable(False, False)
        
        self.colorRoot = '#84b6f4'
        colorframe = '#fdcae1'

        self.root.tk_setPalette(self.colorRoot)

        self.hdm = hdm.Jogo()

        self.frame1 = ctk.CTkFrame(self.root, 100, 200, fg_color= colorframe)
        self.frame1.place(relx = 0.3, rely = 0.13, relwidth = 0.68, relheight = 0.58 )

        self.frame2= ctk.CTkFrame(self.root, fg_color=colorframe)
        self.frame2.place(relx=0.3, rely=0.75, relwidth=0.68, relheight=0.229)

        self.frame3 = ctk.CTkFrame(self.root, 100,200, fg_color=colorframe)
        self.frame3.place(relx=0.01, rely=0.02, relwidth=0.26, relheight=0.96)


        self.canvas = Canvas(self.root, width=100, height=100, background='white', highlightthickness=0)
        self.canvas.place(relx=0.32, rely=0.15, relheight=0.53, relwidth=0.640)

        self.n = 0
        self.i = []
        self.indice = 0
        self.bt = []
        self.ini = False


        self.titulo()
        self.linha()
        self.botoes_letras()
        self.botoesPrincipais()
        self.desenhar_forca()


    def titulo(self):
        canvas = Canvas(self.root, width=100, height=100, background=self.colorRoot)
        canvas.place(relx=0.63,rely=0.05,relheight=0.09,relwidth=0.7, anchor='center')
        canvas.create_text(370,30,text='Jogo da Forca', font=('Momcake',40, 'bold'), fill='white')

    def linha(self):
        canvas = Canvas(self.root, width=100, height=100,background=self.colorRoot)
        canvas.place(relx=0.28,rely=0.498,relheight=1,relwidth=0.02, anchor='e')
        canvas.create_line(10,759,10,0, fill='white')

    def desenhar_forca(self):
        self.canvas.create_line(40,20,40,320, fill='#bf9780', width=10)
        self.canvas.create_line(40,80,100,30, fill='#bf9780', width=20)
        self.canvas.create_line(50,20,50,320, fill='#a68069', width=10)
        self.canvas.create_line(74,50,98,30,fill='#a68069', width=20)
        self.canvas.create_line(25,30,350,30,fill='#bf9780', width=20)
        
        
        self.canvas.create_line(340,30,340,60, fill='#bf9780', width=20)
        self.canvas.create_line(333,38,333,60,fill='#a68069', width=7)
    
    def winner(self):
        self.canvas.destroy()
        self.canvas = Canvas(self.root, width=100, height=100, background='white', highlightthickness=0)
        self.canvas.place(relx=0.32, rely=0.15, relheight=0.53, relwidth=0.640)
        self.canvas.create_text(320,50,text='Boa! Voce ganhou', font=('Lato', 30), fill='#c94139')
        self.canvas.create_text(320,150,text='A palavra era:', font=('Lato', 40),fill='#c94139')
        self.canvas.create_text(320,250,text=self.hdm.palavra, font=('Momcake', 40),fill='#c94139')
        
        self.espera_construir()
        

    def loser(self):
        self.canvas.destroy()
        self.canvas = Canvas(self.root, width=100, height=100, background='white', highlightthickness=0)
        self.canvas.place(relx=0.32, rely=0.15, relheight=0.53, relwidth=0.640)
        self.canvas.create_text(320,50,text='Que pena! Voce perdeu', font=('Lato', 30), fill='#c94139')
        self.canvas.create_text(320,150,text='A palavra era:', font=('Lato', 40),fill='#c94139')
        self.canvas.create_text(320,250,text=self.hdm.palavra, font=('Momcake', 40),fill='#c94139')

        self.espera_construir()


    def espera_construir(self):
        self.root.after(3000, self.construir_canvas)   

    def espera_winner(self):
        if self.indice == len(self.hdm.palavra):
            self.root.after(800, self.winner)
            self.root.after(3000, self.restart)
            self.ini = False
    
    def espera_loser(self):
        if self.n == 6:
            self.root.after(800, self.loser)
            self.root.after(3000, self.restart)
            self.ini = False

        
    def desenhar_corpo(self):
        color = '#ff8097'
        if self.n == 0:
            self.canvas.create_oval(289,60,389,140, width=10, outline=color)
        elif self.n == 1:
            self.canvas.create_line(340,140,340,260, fill=color ,width=10, )
        elif self.n == 2:
            self.canvas.create_line(340,160,290,200, fill=color, width=10)
        elif self.n == 3:
            self.canvas.create_line(340,160,390,200, fill=color, width=10)
        elif self.n == 4:
            self.canvas.create_line(340,260,290,300, fill=color, width=10)
        elif self.n == 5:
            self.canvas.create_line(340,260,390,300, fill=color, width=10)

        '''elif self.n == 6:
            self.canvas.create_oval(310,90,330,110)
            self.canvas.create_oval(370,90,350,110)
        else:
            self.canvas.create_line(330,120,350,120, fill='black')'''
        
        self.n += 1

        self.espera_loser()
        
       
    def desenhar_letra(self,indices,letra):
        for i, x in enumerate(self.i):
            for indice in indices:
                if indice == i:
                    self.canvas.create_text(x,350,text=letra, font=('Montcake',15))
                    self.indice += 1

        self.espera_winner()

    def letras(self, letra):
        self.hdm.index.clear()
        indice = self.hdm.verificarPertencimento(letra)
        
        if self.ini == True:
            if indice is None:
                self.desenhar_corpo()
            else:
                self.desenhar_letra(indice, letra)
        

    def dica_is_over(self):
        window = Toplevel(self.root)
        window.geometry('300x300')

    def dica(self):
        letra = self.hdm.dica()
        if letra is not None:
            self.letras(letra)
        else:
            self.dica_is_over()

    def construir_canvas(self):
        self.canvas = Canvas(self.root, width=100, height=100, background='white', highlightthickness=0)
        self.canvas.place(relx=0.32, rely=0.15, relheight=0.53, relwidth=0.640)
        self.desenhar_forca()

    def restart(self):
        self.hdm = hdm.Jogo()
        self.hdm.index.clear()
        self.hdm.n = 0
        self.canvas.destroy()
        self.n = 0
        self.i.clear()
        self.indice = 0
        self.construir_canvas()
        
        for botao in self.bt:
            botao.configure(state='normal')

    def desenhar_linha(self):
        self.restart()
        self.ini = True
        n = self.hdm.calcularCaracteres()
        y0 = 370; y1 = 370 
        for i in range(n):
            if i == 0:
                if n <= 4:
                    x0 = 250
                    x1 = 200
                elif n > 4 and n < 7:
                    x0 = 180
                    x1 = 130
                else:
                    x0 = 100
                    x1 = 50

            self.canvas.create_line(x0,y0,x1,y1, fill='black')
            self.canvas.create_text(x0-25,350, font=('Momcake', 25))
            self.i.append(x0-25)
            x0 += 70
            x1 += 70

    def botoesPrincipais(self):
        width = 0.6
        height = 0.13
        color = '#ff8097'
        x = 0.17
        y = 0.07

        ini = ctk.CTkButton(self.frame3, text='Novo jogo',font=('Momcake', 30, 'bold'), 
                            command=lambda:self.desenhar_linha(), text_color='white')
        ini.place(relx=x, rely=y, relwidth=width, relheight=height)
        

        dica = ctk.CTkButton(self.frame3, text='Dica',font=('Momcake', 35, 'bold'), 
                                command=lambda:self.dica(), text_color='white', fg_color=color )
        dica.place(relx=x, rely=y+0.2, relwidth=width, relheight=height)

        palavra = ctk.CTkButton(self.frame3, text='palavra',font=('Momcake', 35, 'bold'), text_color='white')
        palavra.place(relx=x, rely=y+0.2*2, relwidth=width, relheight=height)

        sair = ctk.CTkButton(self.frame3, text='Sair', font=('Momcake', 35, 'bold'),
                                command=lambda:self.root.quit(), text_color='white', fg_color=color)
        sair.place(relx=x, rely=y+0.2*3, relwidth=width, relheight=height)

               
    def botoes_letras(self):
        width = 0.085
        height = 0.27
        dx = 0.02

        Q = ctk.CTkButton(self.frame2, text='Q', command=lambda:self.letras('q'))
        Q.place(relx=0.02,rely=0.05, relwidth=width, relheight=height)
        self.bt.append(Q)
          
        W = ctk.CTkButton(self.frame2, text='W', command=lambda:self.letras('w'))
        W.place(relx=dx + 0.092, rely=0.05, relwidth=width, relheight=height)
        self.bt.append(W)

        E = ctk.CTkButton(self.frame2, text='E', command=lambda:self.letras('e'))
        E.place(relx=dx+0.188, rely=0.05, relwidth=width, relheight=height)
        self.bt.append(E)

        R = ctk.CTkButton(self.frame2, text='R', command=lambda:self.letras('r'))
        R.place(relx=dx+0.283, rely=0.05, relwidth=width, relheight=height)
        self.bt.append(R)

        T = ctk.CTkButton(self.frame2, text='T', command=lambda:self.letras('t'))
        T.place(relx=dx+0.378, rely=0.05, relwidth=width, relheight=height)
        self.bt.append(T)

        Y = ctk.CTkButton(self.frame2, text='Y', command=lambda:self.letras('y'))
        Y.place(relx=dx+0.471, rely=0.05, relwidth=width, relheight=height)
        self.bt.append(Y)

        U = ctk.CTkButton(self.frame2, text='U', command=lambda:self.letras('u'))
        U.place(relx=dx+0.567, rely=0.05, relwidth=width, relheight=height)
        self.bt.append(U)

        I = ctk.CTkButton(self.frame2, text='I', command=lambda:self.letras('i'))
        I.place(relx=dx+0.663, rely=0.05, relwidth=width, relheight=height)
        self.bt.append(I)

        O = ctk.CTkButton(self.frame2, text='O', command=lambda:self.letras('o'))
        O.place(relx=dx+0.758, rely=0.05, relwidth=width, relheight=height)
        self.bt.append(O)

        P = ctk.CTkButton(self.frame2, text='P', command=lambda:self.letras('p'))
        P.place(relx=dx+0.853, rely=0.05, relwidth=width, relheight=height)
        self.bt.append(P)

        #
        A = ctk.CTkButton(self.frame2, text='A',command=lambda:self.letras('a'))
        A.place(relx=dx +0.02, rely=0.35, relwidth=width, relheight=height)
        self.bt.append(A)

        S = ctk.CTkButton(self.frame2, text='S', command=lambda:self.letras('s'))
        S.place(relx=dx +0.115, rely=0.35, relwidth=width, relheight=height)
        self.bt.append(S)

        D = ctk.CTkButton(self.frame2, text='D', command=lambda:self.letras('d'))
        D.place(relx=dx +0.2094, rely=0.35, relwidth=width, relheight=height)
        self.bt.append(D)

        F = ctk.CTkButton(self.frame2, text='F', command=lambda:self.letras('f'))
        F.place(relx=dx +0.304, rely=0.35, relwidth=width, relheight=height)
        self.bt.append(F)

        G = ctk.CTkButton(self.frame2, text='G', command=lambda:self.letras('g'))
        G.place(relx=dx +0.399, rely=0.35, relwidth=width, relheight=height)
        self.bt.append(G)

        H = ctk.CTkButton(self.frame2, text='H', command=lambda:self.letras('h'))
        H.place(relx=dx +0.493, rely=0.35, relwidth=width, relheight=height)
        self.bt.append(H)

        J = ctk.CTkButton(self.frame2, text='J', command=lambda:self.letras('j'))
        J.place(relx=dx +0.589, rely=0.35, relwidth=width, relheight=height)
        self.bt.append(J)

        K = ctk.CTkButton(self.frame2, text='K', command=lambda:self.letras('k'))
        K.place(relx=dx +0.684, rely=0.35, relwidth=width, relheight=height)
        self.bt.append(K)

        L = ctk.CTkButton(self.frame2, text='L', command=lambda:self.letras('l'))
        L.place(relx=dx +0.78, rely=0.35, relwidth=width, relheight=height)
        self.bt.append(L)

        Ç = ctk.CTkButton(self.frame2, text='Ç', command=lambda:self.letras('ç'))
        Ç.place(relx=dx +0.875, rely=0.35, relwidth=width, relheight=height)
        self.bt.append(Ç)


        #

        Z = ctk.CTkButton(self.frame2, text='Z' , command=lambda:self.letras('z'))
        Z.place(relx=0.08, rely=0.65, relwidth=width, relheight=height)
        self.bt.append(Z)

        X = ctk.CTkButton(self.frame2, text='X' , command=lambda:self.letras('x'))
        X.place(relx=0.08+0.095, rely=0.65, relwidth=width, relheight=height)
        self.bt.append(X)

        C = ctk.CTkButton(self.frame2, text='C', command=lambda:self.letras('c') )
        C.place(relx=0.08+0.19, rely=0.65, relwidth=width, relheight=height)
        self.bt.append(C)

        V = ctk.CTkButton(self.frame2, text='V', command=lambda:self.letras('v') )
        V.place(relx=0.08+0.095*3, rely=0.65, relwidth=width, relheight=height)
        self.bt.append(V)
        V.bind('<Button 1>', lambda event:V.configure(state='disabled'))

        B = ctk.CTkButton(self.frame2, text='B', command=lambda:self.letras('b') )
        B.place(relx=0.08+0.095*4, rely=0.65, relwidth=width, relheight=height)
        self.bt.append(B)

        N = ctk.CTkButton(self.frame2, text='N' , command=lambda:self.letras('n'))
        N.place(relx=0.08+0.095*5, rely=0.65, relwidth=width, relheight=height)
        self.bt.append(N)
        

        M = ctk.CTkButton(self.frame2, text='M', command=lambda:self.letras('m'))
        M.place(relx=0.08+0.095*6, rely=0.65, relwidth=width, relheight=height)
        self.bt.append(M)

        Q.bind('<Button 1>', lambda event:Q.configure(state='disabled'))
        W.bind('<Button 1>', lambda event:W.configure(state='disabled'))
        E.bind('<Button 1>', lambda event:E.configure(state='disabled'))
        R.bind('<Button 1>', lambda event:R.configure(state='disabled'))
        T.bind('<Button 1>', lambda event:T.configure(state='disabled'))
        Y.bind('<Button 1>', lambda event:Y.configure(state='disabled'))
        U.bind('<Button 1>', lambda event:U.configure(state='disabled'))
        I.bind('<Button 1>', lambda event:I.configure(state='disabled'))
        O.bind('<Button 1>', lambda event:O.configure(state='disabled'))
        P.bind('<Button 1>', lambda event:P.configure(state='disabled'))

        A.bind('<Button 1>', lambda event:A.configure(state='disabled'))
        S.bind('<Button 1>', lambda event:S.configure(state='disabled'))
        D.bind('<Button 1>', lambda event:D.configure(state='disabled'))
        F.bind('<Button 1>', lambda event:F.configure(state='disabled'))
        G.bind('<Button 1>', lambda event:G.configure(state='disabled'))
        H.bind('<Button 1>', lambda event:H.configure(state='disabled'))
        J.bind('<Button 1>', lambda event:J.configure(state='disabled'))
        K.bind('<Button 1>', lambda event:K.configure(state='disabled'))
        L.bind('<Button 1>', lambda event:L.configure(state='disabled'))
        Ç.bind('<Button 1>', lambda event:Ç.configure(state='disabled'))
        
        X.bind('<Button 1>', lambda event:X.configure(state='disabled'))
        Z.bind('<Button 1>', lambda event:Z.configure(state='disabled'))
        C.bind('<Button 1>', lambda event:C.configure(state='disabled'))
        B.bind('<Button 1>', lambda event:B.configure(state='disabled'))
        N.bind('<Button 1>', lambda event:N.configure(state='disabled'))
        M.bind('<Button 1>', lambda event:M.configure(state='disabled'))


    
if __name__ == "__main__":

    root = Tk()
    app = GUI(root)
    root.mainloop() 