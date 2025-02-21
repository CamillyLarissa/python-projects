from tkinter import *
from tkinter import ttk
import customtkinter as ctk
import Binary_Tree as Binary_Tree

class Interface:
    def __init__(self, root):

        #janela principal
        self.root = root
        self.root.title("Árvores Binárias")
        self.root.geometry("1000x800")
        self.root.tk_setPalette(background='medium sea green')
        self.root.minsize(0, 1000)

        self.tree = Binary_Tree.Arvore()

        self.valores = []

        #criando a frame esquerda
        self.frm = ctk.CTkFrame(self.root, height=750, width=350, fg_color='sea green', corner_radius=10)
        self.frm.place(relx=0.030, rely=0.095, relheight=0.880,relwidth=0.230)

        #criando frame para barra de rolagem
        self.canvas_frame = ttk.Frame(self.root)
        self.canvas_frame.place(relx=0.29, rely=0.1, relwidth=0.7, relheight=0.870)

        #criando canvas
        self.canvas = Canvas(self.canvas_frame, background='gray75', borderwidth=10, relief="ridge")
        self.canvas.pack(side='left', fill='both', expand=True)
        self.canvas.place(relx=0.001, rely=0.001, relwidth=1, relheight=1)

        #style
        self.style = ttk.Style()
        self.style.configure('My.TLabel', background='medium sea green', foreground='medium sea green', font=('Balker.tff', 16))
        self.style.configure('My.TButton', background='sea green', foreground='black', font=('Balker.tff', 12))
        
        #icon para botões
        self.icon = PhotoImage(file='tree.png')  # Replace 'full/path/to' with the actual path to the image file
        self.icon = self.icon.subsample(15, 15)

        #abrindo a imagem
        self.photo = PhotoImage(file='tree_icon_245749.png')
        self.photo = self.photo.subsample(15, 15)

        #criando entrada
        self.nome = ttk.Entry(self.frm, width=20, cursor='xterm', font=('Luto Regular', 12), justify='center')
        self.nome.place(relx=0.15, rely=0.180, relheight=0.07, relwidth=0.700)
        self.nome.insert(0, "Insira o nome")
        self.nome.bind('<FocusIn>', lambda event: self.nome.delete(0, 'end'))
        self.nome.bind('<Return>', lambda event: self.addValue())


        self.barra_de_rolagem()
        self.upper_frame()
        self.buttons()

    def upper_frame(self):
        # criando uma frame
        frame = ctk.CTkFrame(self.root, width=2300, height=40, fg_color='medium sea green')
        frame.place(x=-1, y=0)

        #canvas para add img e texto
        my_canva = Canvas(frame, width=2300, height=40, bg='sea green')
        my_canva.pack()
        my_canva.create_text(200, 20, text="Árvore Binária", font=('dutismo_bold_italic.tff', 19), fill='black')
        my_canva.create_image(70, 3, image=self.photo, anchor='nw')

    def barra_de_rolagem(self):
        #criando barra de rolagem
        scroll_x = ttk.Scrollbar(self.canvas_frame, orient='horizontal', command=self.canvas.xview)
        scroll_x.pack(side='bottom', fill='x')
        scroll_y = ttk.Scrollbar(self.canvas_frame, orient='vertical', command=self.canvas.yview)
        scroll_y.pack(side='right', fill='y')
        self.canvas.configure(xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        #criando um retangulo para o canvas
        self.canvas.create_rectangle(0, 0, 2000, 2000, fill='gray75', outline='gray75')
        self.canvas.configure(scrollregion=self.canvas.bbox('all'))

        #local
        scroll_y.place(relx=0.979, rely=0.0, relheight=0.986)
        scroll_x.place(relx=0.0, rely=0.979, relwidth=0.989)
        scroll_y.place(relx=0.979, rely=0.0, relheight=0.986)
        scroll_x.place(relx=0.0, rely=0.979, relwidth=0.989)

        #ligando a rolagem do mouse com a barra de rolagem
        self.canvas.bind("<MouseWheel>", lambda event: self.canvas.yview_scroll(int(-1*(event.delta/120)), "units"))
        self.canvas.update()

    def buttons(self):
        ttk.Button(self.root, text="Inserir", width=20, command=lambda:self.addValue(), image=self.icon, compound="left", cursor='hand2', style='My.TButton').place(relx=0.055, rely=0.120, relheight=0.1,relwidth=0.180)
        ttk.Button(self.root, text="Mostrar Ordem de Inserção", width=20, command=lambda:self.mostrarValores(), image=self.icon, compound="left", cursor='hand2', style='My.TButton').place(relx=0.055, rely=0.350, relheight=0.1,relwidth=0.180)
        ttk.Button(self.root, text="Remover Nós", width=20, command=lambda:self.remover_nós(), image=self.icon, compound="left", cursor='hand2', style='My.TButton').place(relx=0.055, rely=0.450, relheight=0.1,relwidth=0.180)   
        ttk.Button(self.root, text="Mostrar Informações", width=20, command=lambda:self.info_window(), image=self.icon, compound="left", cursor='hand2', style='My.TButton').place(relx=0.055, rely=0.550, relheight=0.1,relwidth=0.180)
        ttk.Button(self.root, text="Internal Path Lenght", width=20, command=lambda:self.internal_path(), image=self.icon, compound="left", cursor='hand2',style='My.TButton').place(relx=0.055, rely=0.650, relheight=0.1,relwidth=0.180)
        ttk.Button(self.root, text="A árvore está balanceada?", width=20, command=lambda:self.balanceamento(), image=self.icon, compound="left",cursor='hand2', style='My.TButton' ).place(relx=0.055, rely=0.750, relheight=0.1,relwidth=0.180)
        ttk.Button(self.root, text="Mostrar Percursos", width=20, command=lambda:self.mostrar_percusos(), image=self.icon, compound="left",cursor='hand2', style='My.TButton' ).place(relx=0.055, rely=0.850, relheight=0.1,relwidth=0.180)

    def mini_window_erro(self, title, geometry, color, text):
        mini_window = Toplevel(self.root)
        mini_window.title(title)
        mini_window.geometry(geometry)
        mini_window.configure(bg=color)
        mini_window.resizable(False, False) 
        ctk.CTkLabel(mini_window, text=text, font=('Balker.tff', 16, 'bold'),  wraplength=600).pack(pady=20)

    def addValue(self):
        nome = self.nome.get()
        if nome == "":
            self.mini_window_erro("ERRO", "300x100", "#e11e1e", "Erro: Insira um nome!")
            return
        
        x = self.tree.insert(nome)
        self.nome.delete(0, 'end')

        if x == False:
            self.mini_window_erro("ERRO", "300x100", "#e11e1e", "Erro: Informação Já Cadastrada!")
            return
        else:
            self.tree.render_tree(self.canvas)
            self.valores.append(nome)
            self.canvas.update()

    def mostrarValores(self):
        mini_window = Toplevel(self.root)
        mini_window.title("Ordem de Inserção")
        mini_window.geometry("700x300")
        mini_window.resizable(False, False)
        mini_window.configure(bg='#6cca83')  
        if self.tree.raiz == None:
            ctk.CTkLabel(mini_window, text="Árvore vazia", font=('Lato Bold', 19), wraplength=600, bg_color='medium sea green').pack(pady=20)
        else:
            ctk.CTkLabel(mini_window, text=", ".join(self.valores), font=('Lato Bold', 19), wraplength=600, bg_color='medium sea green').pack(pady=20)
        

    def remover_nós(self):
        self.tree.remove_all_nodes(self.tree.raiz)
        self.canvas.delete("all")
        self.valores.clear()

    def showinfo(self, num):
        match num:
            case 1:
                tam = self.tree.tamanho(self.tree.raiz)
                myLabel.config(text=f"O tamanho da árvore é {tam}", background='sea green')
            case 2:
                altura = self.tree.altura(self.tree.raiz)
                myLabel.config(text=f"A altura da árvore é {altura}", background='sea green')
            case 3:
                maior = self.tree.Maior_Elemento(self.tree.raiz)
                if maior == None:
                    myLabel.config(text="A árvore não tem maior elemento", background='sea green')
                else:
                    myLabel.config(text=f"O maior elemento da árvore é {maior}")
            case 4:
                menor = self.tree.Menor_Elemento(self.tree.raiz)
                if menor == None:
                    myLabel.config(text="A árvore não tem menor elemento", background='sea green')
                else:
                    myLabel.config(text=f"O menor elemento da árvore é {menor}", background='sea green')

    def info_window(self):
        global myLabel, j

        top = Toplevel(self.root)
        top.geometry("600x300")
        top.resizable(False, False)
        top.title("Informações")
        top.configure(bg='#6cca83')
        j = IntVar()

        myLabel = ttk.Label(top, text="Escolha uma opção:",  font=('Lato Bold', 13), background='medium sea green')
        myLabel.pack(padx=10, pady=10)

        frame = ctk.CTkFrame(top, width=500, height=400, fg_color='medium sea green', corner_radius=10)
        frame.pack(pady=20)

        Radiobutton(frame, text='Tamanho         ', variable=j, value=1, command=lambda: self.showinfo(j.get()), 
                width=20, font=('Lato Regular', 15)).pack(padx=0, pady=10, anchor='center')
        Radiobutton(frame, text='Altura           ' , variable=j, value=2, command=lambda: self.showinfo(j.get()),
                font=('Lato Regular', 15)).pack(padx=0, pady=10, anchor='center')
        Radiobutton(frame, text='Maior Elemento', variable=j, value=3, command=lambda: self.showinfo(j.get()),
                    font=('Lato Regular', 15)).pack(padx=10, pady=10, anchor='center')
        Radiobutton(frame, text='Menor Elemento', variable=j, value=4, command=lambda: self.showinfo(j.get()),
                    font=('Lato Regular', 15)).pack(padx=10, pady=10, anchor='center')
   
    def internal_path(self):
        mini_window = Toplevel(self.root)
        mini_window.title("Internal Path Length")
        mini_window.geometry("300x200")
        mini_window.resizable(False, False) 
        mini_window.configure(bg='#6cca83')

        result = self.tree.Internal_Path_Length(self.tree.raiz,0)

        Label(mini_window, text="Internal Path Length:", font=('Lato Bold', 19),  background='#6cca83').pack(pady=20)
        frame = ttk.Frame(mini_window, width=200, height=200, relief="solid", borderwidth=1)
        frame.pack(pady=20)
        Label(frame, text=result, font=('Lato Bold', 19)).pack()

    def balanceamento(self):
        mini_window = Toplevel(self.root)
        mini_window.title("Balanceamento")
        mini_window.geometry("300x200")
        mini_window.resizable(False, False) 
        mini_window.configure(bg='#6cca83')

        b = self.tree.is_Balanceada(self.tree.raiz)
        
        if b == 0:
            x = "A árvore está vazia!"
        elif b == -1:
            x = "A árvore não está balanceada!"
        else:
            x = "A árvore está balanceada!"

        Label(mini_window, text="Balanceamento:", font=('Lato Regular', 16), background='#6cca83').pack(pady=20)
        frame = ctk.CTkFrame(mini_window, width=200, height=200, bg_color='#6cca83')
        frame.pack(pady=20)

        Label(frame, text=x, font=('Lato Regular', 16)).pack()

    def mostrar_percusos(self):
        result_em_ordem = self.tree.emOrdem(self.tree.raiz)
        result_pre_ordem = self.tree.preOrdem(self.tree.raiz)
        result_pos_ordem = self.tree.posOrdem(self.tree.raiz)
        result_level_ordem = self.tree.levelOrder(self.tree.raiz)
        
        mini_window = Toplevel(self.root)
        mini_window.title("Percursos")
        mini_window.geometry("800x500")
        mini_window.resizable(False, False)
        mini_window.configure(bg='#6cca83')

        frame = ctk.CTkFrame(mini_window, width=800, height=770, fg_color='#6cca83', corner_radius=20)
        frame.pack(pady=20)

        tabview = ctk.CTkTabview(frame, width=700, height=500, corner_radius=20, fg_color="medium sea green", segmented_button_fg_color="white", segmented_button_selected_color="green",
                                segmented_button_unselected_hover_color="medium sea green", segmented_button_unselected_color="grey")
       
        tabview.pack(fill='both', expand=True)
        tabview.pack() 
       
        tabview.add("Em Ordem")
        tabview.add("Pre Ordem")
        tabview.add("Pos Ordem")
        tabview.add("Level Ordem")
       
        tabview.tab("Em Ordem").grid_columnconfigure(0, weight=1)
        tabview.tab("Pre Ordem").grid_columnconfigure(0, weight=1)
        tabview.tab("Pos Ordem").grid_columnconfigure(0, weight=1)
        tabview.tab("Level Ordem").grid_columnconfigure(0, weight=1)

        ordem = ctk.CTkLabel(tabview.tab("Em Ordem"), text=result_em_ordem, font=('Lato Bold', 19), wraplength=600)
        ordem.pack()
        pre_ordem = ctk.CTkLabel(tabview.tab("Pre Ordem"), text=result_pre_ordem, font=('Lato Bold', 19), wraplength=600)
        pre_ordem.pack()
        pos_ordem = ctk.CTkLabel(tabview.tab("Pos Ordem"), text=result_pos_ordem, font=('Lato Bold', 19), wraplength=600)
        pos_ordem.pack()
        level_ordem = ctk.CTkLabel(tabview.tab("Level Ordem"), text=result_level_ordem, font=('Lato Bold', 19), wraplength=600)
        level_ordem.pack()
    

if __name__ == "__main__":
    root = Tk()
    app = Interface(root)
    root.mainloop()