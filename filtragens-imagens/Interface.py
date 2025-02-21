from tkinter import *
from tkinter import ttk
import customtkinter as ctk
from PIL import Image
import cv2
import CaminhoDaImagem as cdi
import Filtro as ft
import os 
import numpy as np

class Interface:
    def __init__(self, root):

        #janela principal
        self.root = root
        self.root.title("Projeto Final - Processamento de Imagens")
        self.root.geometry("1200x750")
        self.root.tk_setPalette(background='MediumPurple3')

        self.root.state('zoomed')

        #frame para mostrar titulo
        self.canvas = Canvas(self.root, width=100, height=100, bg='MediumPurple3')
        self.canvas.create_text(850, 130, text="Projeto Final", font=('Momcake', 50, 'bold'), fill='white')
        self.canvas.create_text(850, 200, text="Processamento de Imagens", font=('Momcake', 30, 'bold'), fill='white')
        self.canvas.place(relx=0.450, rely=0.0399, relwidth=1, relheight=0.299, anchor='center')

        #criando a frame e canva 1
        self.frm = ctk.CTkFrame(self.root, height=750, width=350, fg_color='MediumPurple1', corner_radius=10)
        self.frm.place(relx=0.055, rely=0.195, relheight=0.300,relwidth=0.400)

        self.canva1 = Canvas(self.frm, width=750, height=250, bg='MediumPurple1', highlightthickness=0)
        self.canva1.create_text(300, 40, text="Informe o caminho da imagem", font=('Momcake', 20, 'bold'),anchor='center', fill='white')
        self.canva1.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.5)


        #criando a frame e canva 2
        
        self.frm1 = ctk.CTkFrame(self.root, height=750, width=350, fg_color='MediumPurple1', corner_radius=10)
        self.frm1.place(relx=0.055, rely=0.53, relheight=0.200,relwidth=0.400)

        self.canva2 = Canvas(self.frm1, width=750, height=250, bg='MediumPurple1', highlightthickness=0)
        self.canva2.create_text(170, 70, text="Imagem Adicionada ", font=('Momcake', 20, 'bold'),anchor='center', fill='white')
        self.canva2.create_rectangle(370, 18, 540, 140, outline='white', width=3)
        self.canva2.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.9)
        self.inserir = self.canva2.create_text(455, 70, text="Insira uma Imagem", font=('Momcake', 14),anchor='center', fill='white')

        
        #criando a frame e canva 3

        self.frm2 = ctk.CTkFrame(self.root, height=750, width=350, fg_color='MediumPurple1', corner_radius=10)
        self.frm2.place(relx=0.505, rely=0.195, relheight=0.770,relwidth=0.490)

        self.canva3 = Canvas(self.frm2, width=750, height=250, bg='MediumPurple1', highlightthickness=0)
        self.canva3.create_text(375, 20, text="Filtros", font=('Momcake', 30, 'bold'),anchor='center', fill='white')
        self.canva3.create_text(375, 50, text="Selecione um filtro para realizar o download", font=('Jacques Francois', 15, 'bold'),anchor='center', fill='white')
        self.canva3.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.97)

        self.p = None

        self.e = 0
        self.pb = 0
        self.c = 0
        self.n = 0
        self.co = 0
        self.b = 0

        self.caminho_da_imagem()
        self.filtro()
        self.imagem_filtro()
        self.buttons()
        self.buttons_filtro()

    def caminho_da_imagem(self):
        entry = ctk.CTkEntry(self.frm, width=440, height=35, font=('Jacques Francois', 15),
                             bg_color='transparent',placeholder_text="Digite o caminho... ", placeholder_text_color="grey"
                             , text_color="gray", state="normal" ,fg_color='lavender', border_color='lavender')
        
        entry.place(relx=0.5, rely=0.5, anchor='center')
      
        entry.bind("<Return>", lambda _: self.process_image_path(entry.get()))

        img = ctk.CTkImage(light_image=Image.open("C:/Users/camil/.vscode/cli/Mon/UFPI/2 periodo/Laboratorio de Progamacao/tf/img/link.png"), 
                   dark_image=Image.open("C:/Users/camil/.vscode/cli/Mon/UFPI/2 periodo/Laboratorio de Progamacao/tf/img/link.png"), 
                   size=(30,30))

        ctk.CTkLabel(self.frm, text='', image=img).place(relx=0.10, rely=0.5, anchor='center')


        bt1 = ctk.CTkButton(self.frm, text="OK", width=150,height=40, anchor='center', cursor='hand2',font=('Momcake', 20, 'bold'),
                            fg_color='MediumPurple4', background_corner_colors=['MediumPurple1', 'MediumPurple1', 'MediumPurple1', 'MediumPurple1'])
        bt1.bind("<Return>", lambda _: self.process_image_path(entry.get()))
        bt1.bind("<Button-1>", lambda _: self.process_image_path(entry.get()))
        bt1.bind("<Button-1>", lambda _: self.mostrar_imagem(entry.get()))
        bt1.bind("<Return>", lambda _: self.mostrar_imagem(entry.get()))
        bt1.place(relx=0.35, rely=0.7, anchor='center')

        bt2 = ctk.CTkButton(self.frm, text="Limpar", width=150,height=40, anchor='center', cursor='hand2',font=('Momcake', 20, 'bold'),
                            fg_color='MediumPurple4', background_corner_colors=['MediumPurple1', 'MediumPurple1', 'MediumPurple1', 'MediumPurple1'])
        bt2.bind("<Button-1>", lambda _: entry.delete(0, END))
        bt2.bind('<Button-1>', lambda _: self.fechar_img())
        bt2.place(relx=0.65, rely=0.7, anchor='center')
 
    def process_image_path(self, path):  
        x = cdi.diferenciar_caminho(path)
        self.p = path
        if x == 0: 
            if path == "":
                texto = "Insira um caminho válido"
            else:
                texto = "Caminho não encontrado!"

            new_window = Toplevel(self.root)
            new_window.title("Erro")
            new_window.geometry("200x200")
            new_window.tk_setPalette(background='MediumPurple3')
            new_window.minsize(300, 200)
            new_window.resizable(False, False)

            canvas = Canvas(new_window, width=3100, height=300, bg='MediumPurple3')
            canvas.create_text(170, 20, text=texto, font=('Jacques Francois', 15, 'bold'), fill='white')
            canvas.place(relx=0.450, rely=0.499, relwidth=1, relheight=0.4, anchor='center')

            ctk.CTkButton(new_window, text="OK", command=new_window.destroy,
                          fg_color='MediumPurple4', background_corner_colors=['MediumPurple3', 'MediumPurple3',
                         'MediumPurple3', 'MediumPurple3'], font=('Momcake', 20, 'bold')).place(relx=0.300, rely=0.599, relheight=0.3,relwidth=0.380)

        elif x != 0:
            new_window = Toplevel(self.root)
            new_window.title("Sucesso")
            new_window.geometry("400x200")
            new_window.tk_setPalette(background='MediumPurple3')
            new_window.minsize(300, 200)
            new_window.resizable(False, False)

            canvas = Canvas(new_window, width=3100, height=300, bg='MediumPurple3')
            canvas.create_text(220, 20, text='Caminho carregado com sucesso!', font=('Jacques Francois', 15, 'bold'), fill='white')
            canvas.place(relx=0.450, rely=0.499, relwidth=1, relheight=0.4, anchor='center')

            ctk.CTkButton(new_window, text="OK", command=new_window.destroy,
                          fg_color='MediumPurple4', background_corner_colors=['MediumPurple3', 'MediumPurple3',
                         'MediumPurple3', 'MediumPurple3'], font=('Momcake', 20, 'bold')).place(relx=0.300, rely=0.599, relheight=0.3,relwidth=0.380)


    def mostrar_imagem(self, path):
        self.canva2.delete('all')
        self.canva2.create_text(170, 70, text="Imagem Adicionada ", font=('Momcake', 20),anchor='center', fill='white')
        self.canva2.create_rectangle(370, 18, 540, 140, outline='white', width=3)

        if path.startswith("http"):
            path = cdi.cria_imagem(path)
            img = ctk.CTkImage(light_image=path, dark_image=path, size=(100,100))
            ctk.CTkLabel(self.canva2,text='', image=img).place(relx=0.655, rely=0.2, relheight=0.7, relwidth=0.2)

        else:
            img = ctk.CTkImage(light_image=Image.open(path), dark_image=Image.open(path),
                   size=(100,100))
            
            ctk.CTkLabel(self.canva2,text='', image=img).place(relx=0.655, rely=0.2, relheight=0.7, relwidth=0.2)

    def fechar_img(self):
        self.canva2.delete('all')
        self.canva2.create_text(170, 70, text="Imagem Adicionada ", font=('Momcake', 20),anchor='center', fill='white')
        self.canva2.create_rectangle(370, 18, 540, 140, outline='white', width=3)
        ctk.CTkLabel(self.canva2,text='').place(relx=0.655, rely=0.2, relheight=0.7, relwidth=0.2)

    def filtro(self):
        self.canva3.create_rectangle(10, 140, 230, 325, outline='white', width=3)
        self.canva3.create_rectangle(260, 140, 480, 325, outline='white', width=3)
        self.canva3.create_rectangle(510, 140, 730, 325, outline='white', width=3)
        
        self.canva3.create_rectangle(10, 400, 230, 585, outline='white', width=3)
        self.canva3.create_rectangle(260, 400, 480, 585, outline='white', width=3)
        self.canva3.create_rectangle(510, 400, 730, 585, outline='white', width=3)

    def imagem_filtro(self):
        img = ctk.CTkImage(light_image=Image.open("C:/Users/camil/.vscode/cli/Mon/UFPI/2 periodo/Laboratorio de Progamacao/tf/img/preto_e_branco.jpg"), 
                       dark_image=Image.open("C:/Users/camil/.vscode/cli/Mon/UFPI/2 periodo/Laboratorio de Progamacao/tf/img/preto_e_branco.jpg"), 
                       size=(212,212))
        ctk.CTkLabel(self.canva3, text='', image=img).place(relx=0.36, rely=0.245, relheight=0.3, relwidth=0.29)

        img2 = ctk.CTkImage(light_image=Image.open("C:/Users/camil/.vscode/cli/Mon/UFPI/2 periodo/Laboratorio de Progamacao/tf/img/escala_cinza.jpg"), 
                            dark_image=Image.open("C:/Users/camil/.vscode/cli/Mon/UFPI/2 periodo/Laboratorio de Progamacao/tf/img/escala_cinza.jpg"), 
                            size=(212,212))
        ctk.CTkLabel(self.canva3, text='', image=img2).place(relx=0.02, rely=0.245, relheight=0.3, relwidth=0.29)

        img3 = ctk.CTkImage(light_image=Image.open("C:/Users/camil/.vscode/cli/Mon/UFPI/2 periodo/Laboratorio de Progamacao/tf/img/cartoon.jpg"), 
                            dark_image=Image.open("C:/Users/camil/.vscode/cli/Mon/UFPI/2 periodo/Laboratorio de Progamacao/tf/img/cartoon.jpg"), 
                            size=(212,212))
        ctk.CTkLabel(self.canva3, text='', image=img3).place(relx=0.70, rely=0.245, relheight=0.3, relwidth=0.29)

        img4 = ctk.CTkImage(light_image=Image.open("C:/Users/camil/.vscode/cli/Mon/UFPI/2 periodo/Laboratorio de Progamacao/tf/img/foto_negativa.jpg"), 
                            dark_image=Image.open("C:/Users/camil/.vscode/cli/Mon/UFPI/2 periodo/Laboratorio de Progamacao/tf/img/foto_negativa.jpg"), 
                            size=(212,212))
        ctk.CTkLabel(self.canva3, text='', image=img4).place(relx=0.02, rely=0.686, relheight=0.3, relwidth=0.29)

        img5 = ctk.CTkImage(light_image=Image.open("C:/Users/camil/.vscode/cli/Mon/UFPI/2 periodo/Laboratorio de Progamacao/tf/img/contorno.jpg"), 
                        dark_image=Image.open("C:/Users/camil/.vscode/cli/Mon/UFPI/2 periodo/Laboratorio de Progamacao/tf/img/contorno.jpg"), 
                        size=(212,212))
        ctk.CTkLabel(self.canva3, text='', image=img5).place(relx=0.36, rely=0.686, relheight=0.3, relwidth=0.29)

        img6 = ctk.CTkImage(light_image=Image.open("C:/Users/camil/.vscode/cli/Mon/UFPI/2 periodo/Laboratorio de Progamacao/tf/img/blurred.jpg"), 
                        dark_image=Image.open("C:/Users/camil/.vscode/cli/Mon/UFPI/2 periodo/Laboratorio de Progamacao/tf/img/blurred.jpg"), 
                        size=(212,212))
        ctk.CTkLabel(self.canva3, text='', image=img6).place(relx=0.70, rely=0.686, relheight=0.3, relwidth=0.29)
        
    def escala_cinza(self):  
        path = Interface.path(self)
        if path is None:
            self.erro_salvar()
            return
        imagem = cdi.cria_imagem(path) 
        nome, extensao = cdi.extrair_nome_extensao_url(path) 
        caminho = os.path.abspath(nome + extensao)
        #path = '11215319-planeta-terra-com-nascer-do-sol-no-espaco-foto.jpg'
        img = Image.open(caminho) 
        img = np.array(img) 
        imgcv = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
        
        filtro = ft.EscalaCinza(imgcv)
        entrada = 'escala_cinza' + str(self.e) + '.jpg'
        self.e += 1
        
        if entrada:
            filtro.salvar(entrada)
            janela = Toplevel(self.root)
            janela.title("Imagem")
            janela.geometry("400x100")
            janela.tk_setPalette(background='MediumPurple3')
            janela.minsize(700, 700)
            janela.resizable(False, False)
    
            
            pil_image = Image.open(entrada)
            img = ctk.CTkImage(light_image=pil_image, dark_image=pil_image, size=(500,500))
            
            label = ctk.CTkLabel(janela,text='', font=('Jacques Francois', 15, 'bold'), fg_color='white', 
                                 bg_color='MediumPurple3', image=img)
            label.image = img 
            label.place(relx=0.490, rely=0.499, anchor='center')

        else:
            self.erro_salvar()

    def preto_e_branco(self):
        path = Interface.path(self)
        if path is None:
            self.erro_salvar()
            return
        imagem =  cdi.cria_imagem(path) 
        nome, extensao = cdi.extrair_nome_extensao_url(path) 
        caminho = os.path.abspath(nome + extensao) 
        img = Image.open(caminho) 
        img = np.array(img) 
        imgcv = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

        filtro = ft.PretoEBranco(imgcv)
        entrada = 'pretoebranco' + str(self.pb) + '.jpg'
        self.pb += 1
        
        if entrada:
            filtro.salvar(entrada)
            janela = Toplevel(self.root)
            janela.title("Imagem")
            janela.geometry("400x100")
            janela.tk_setPalette(background='MediumPurple3')
            janela.minsize(700, 700)
            janela.resizable(False, False)
    
            
            pil_image = Image.open(entrada)
            img = ctk.CTkImage(light_image=pil_image, dark_image=pil_image, size=(500,500))
            
            label = ctk.CTkLabel(janela,text='', font=('Jacques Francois', 15, 'bold'), fg_color='white', 
                                 bg_color='MediumPurple3', image=img)
            label.image = img 
            label.place(relx=0.490, rely=0.499, anchor='center')

        else:
            self.erro_salvar()
    
    def path(self): 
        return self.p    
    
    def cartoon(self):
        
        path = Interface.path(self)
        if path is None:
            self.erro_salvar()
            return
        imagem =  cdi.cria_imagem(path) 
        nome, extensao = cdi.extrair_nome_extensao_url(path) 
        caminho = os.path.abspath(nome + extensao) 
        img = Image.open(caminho) 
        img = np.array(img) 
        imgcv = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
        filtro = ft.Cartoon(imgcv)
        entrada = 'cartoon' + str(self.c) + '.jpg'
        self.c += 1

        if entrada:
            filtro.salvar(entrada)
            janela = Toplevel(self.root)
            janela.title("Imagem")
            janela.geometry("400x100")
            janela.tk_setPalette(background='MediumPurple3')
            janela.minsize(700, 700)
            janela.resizable(False, False)
            
            pil_image = Image.open(entrada)
            img = ctk.CTkImage(light_image=pil_image, dark_image=pil_image, size=(500,500))
            
            label = ctk.CTkLabel(janela,text='', font=('Jacques Francois', 15, 'bold'), fg_color='white', 
                                 bg_color='MediumPurple3', image=img)
            label.image = img 
            label.place(relx=0.490, rely=0.499, anchor='center')

        else:
            self.erro_salvar()

    def erro_salvar(self):
        new_window = Toplevel(self.root)
        new_window.title("Erro")
        new_window.geometry("200x200")
        new_window.tk_setPalette(background='MediumPurple3')
        new_window.minsize(300, 200)
        new_window.resizable(False, False)

        canvas = Canvas(new_window, width=3100, height=300, bg='MediumPurple3')
        canvas.create_text(170, 20, text='Erro ao salvar a imagem!', font=('Jacques Francois', 15, 'bold'), fill='white')
        canvas.place(relx=0.450, rely=0.499, relwidth=1, relheight=0.4, anchor='center')

        ctk.CTkButton(new_window, text="OK", command=new_window.destroy,
                      fg_color='MediumPurple4', background_corner_colors=['MediumPurple3', 'MediumPurple3',
                     'MediumPurple3', 'MediumPurple3'], font=('Momcake', 20, 'bold')).place(relx=0.300, rely=0.599, relheight=0.3,relwidth=0.380)
    
    def negativo(self): 

        path = Interface.path(self)
        if path is None:
            self.erro_salvar()
            return
        imagem =  cdi.cria_imagem(path) 
        nome, extensao = cdi.extrair_nome_extensao_url(path) 
        caminho = os.path.abspath(nome + extensao) 
        img = Image.open(caminho) 
        img = np.array(img) 
        imgcv = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
        filtro = ft.FotoNegativa(imgcv)
        entrada = 'negativo' + str(self.n) + '.jpg'
        self.n += 1

        if entrada:
            filtro.salvar(entrada)
            janela = Toplevel(self.root)
            janela.title("Imagem")
            janela.geometry("400x100")
            janela.tk_setPalette(background='MediumPurple3')
            janela.minsize(700, 700)
            janela.resizable(False, False)
    
            
            pil_image = Image.open(entrada)
            img = ctk.CTkImage(light_image=pil_image, dark_image=pil_image, size=(500,500))
            
            label = ctk.CTkLabel(janela,text='', font=('Jacques Francois', 15, 'bold'), fg_color='white', 
                                 bg_color='MediumPurple3', image=img)
            label.image = img 
            label.place(relx=0.490, rely=0.499, anchor='center')  

        else:
            self.erro_salvar()

    def contorno(self):
         
        path = Interface.path(self)
        if path is None:
            self.erro_salvar()
            return
        imagem =  cdi.cria_imagem(path) 
        nome, extensao = cdi.extrair_nome_extensao_url(path) 
        caminho = os.path.abspath(nome + extensao) 
        img = Image.open(caminho) 
        img = np.array(img) 
        imgcv = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
        filtro = ft.Contorno(imgcv)
        entrada = 'cortono' + str(self.co) + '.jpg'
        self.co += 1

        if entrada:
            filtro.salvar(entrada)
            janela = Toplevel(self.root)
            janela.title("Imagem")
            janela.geometry("400x100")
            janela.tk_setPalette(background='MediumPurple3')
            janela.minsize(700, 700)
            janela.resizable(False, False)
               
            pil_image = Image.open(entrada)
            img = ctk.CTkImage(light_image=pil_image, dark_image=pil_image, size=(500,500))
            
            label = ctk.CTkLabel(janela,text='', font=('Jacques Francois', 15, 'bold'), fg_color='white', 
                                 bg_color='MediumPurple3', image=img)
            label.image = img 
            label.place(relx=0.490, rely=0.499, anchor='center')

        else:
            self.erro_salvar()

    def blurred(self):
         
        path = Interface.path(self)
        if path is None:
            self.erro_salvar()
            return
        imagem =  cdi.cria_imagem(path) 
        nome, extensao = cdi.extrair_nome_extensao_url(path) 
        caminho = os.path.abspath(nome + extensao) 
        img = Image.open(caminho) 
        img = np.array(img) 
        imgcv = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
        filtro = ft.Blurred(imgcv)
        entrada = 'blurred' + str(self.b) + '.jpg'
        self.b += 1

        if entrada:
            filtro.salvar(entrada)
            janela = Toplevel(self.root)
            janela.title("Imagem")
            janela.geometry("400x100")
            janela.tk_setPalette(background='MediumPurple3')
            janela.minsize(700, 700)
            janela.resizable(False, False)
      
            pil_image = Image.open(entrada)
            img = ctk.CTkImage(light_image=pil_image, dark_image=pil_image, size=(500,500))
            
            label = ctk.CTkLabel(janela,text='', font=('Jacques Francois', 15, 'bold'), fg_color='white', 
                                 bg_color='MediumPurple3', image=img)
            label.image = img 
            label.place(relx=0.490, rely=0.499, anchor='center')

        else:
            self.erro_salvar()
            
    def buttons_filtro(self):
        bt = ctk.CTkButton(self.frm2, text="Escala Cinza", width=20, anchor='center',command=lambda:self.escala_cinza(), cursor='hand2',font=('Momcake', 20, 'bold'),
                            fg_color='MediumPurple4', background_corner_colors=['MediumPurple1', 'MediumPurple1', 'MediumPurple1', 'MediumPurple1'])
       
        bt2 = ctk.CTkButton(self.frm2, text="Preto e Branco", width=20, anchor='center',command=lambda:self.preto_e_branco(), cursor='hand2',font=('Momcake', 20, 'bold'),
                            fg_color='MediumPurple4', background_corner_colors=['MediumPurple1', 'MediumPurple1', 'MediumPurple1', 'MediumPurple1'])

        bt3 = ctk.CTkButton(self.frm2, text="Cartoon", width=20, anchor='center',command=lambda:self.cartoon(), cursor='hand2',font=('Momcake', 20, 'bold'),
                            fg_color='MediumPurple4', background_corner_colors=['MediumPurple1', 'MediumPurple1', 'MediumPurple1', 'MediumPurple1'])
        
        bt4 = ctk.CTkButton(self.frm2, text="Foto Negativo", width=20, anchor='center',command=lambda:self.negativo(), cursor='hand2',font=('Momcake', 20, 'bold'),
                            fg_color='MediumPurple4', background_corner_colors=['MediumPurple1', 'MediumPurple1', 'MediumPurple1', 'MediumPurple1'])
        
        bt5 = ctk.CTkButton(self.frm2, text="Contorno", width=20, anchor='center',command=lambda:self.contorno(), cursor='hand2',font=('Momcake', 20, 'bold'),
                            fg_color='MediumPurple4', background_corner_colors=['MediumPurple1', 'MediumPurple1', 'MediumPurple1', 'MediumPurple1'])
        
        bt6 = ctk.CTkButton(self.frm2, text="Blurred", width=20, anchor='center', cursor='hand2',command=lambda:self.blurred(),font=('Momcake', 20, 'bold'),
                            fg_color='MediumPurple4', background_corner_colors=['MediumPurple1', 'MediumPurple1', 'MediumPurple1', 'MediumPurple1'])
        
        bt.place(relx=0.1, rely=0.140, relheight=0.07,relwidth=0.160)
        bt2.place(relx=0.41, rely=0.140, relheight=0.07,relwidth=0.190)
        bt3.place(relx=0.75, rely=0.140, relheight=0.07,relwidth=0.160)

        bt4.place(relx=0.08, rely=0.570, relheight=0.07,relwidth=0.190)
        bt5.place(relx=0.41, rely=0.570, relheight=0.07,relwidth=0.190)
        bt6.place(relx=0.75, rely=0.570, relheight=0.07,relwidth=0.160)


    def listar_arquivos(self):
        new_window = Toplevel(self.root)
        new_window.title("Lista de arquivos")
        new_window.geometry("900x900")
        new_window.tk_setPalette(background='MediumPurple3')

        lista = []
        canvas = Canvas(new_window, width=700, height=200, bg='MediumPurple3')
        canvas.place(relx=0.490, rely=0.0699, relwidth=0.700, relheight=0.199, anchor='center')
        canvas.create_text(540, 80, text="Lista de arquivos", font=('Momcake', 40, 'bold'), fill='white')

        frm = ctk.CTkFrame(new_window, height=750, width=350, fg_color='MediumPurple1', corner_radius=10)
        frm.place(relx=0.020, rely=0.195, relheight=0.770, relwidth=0.960)

        canva = Canvas(frm, width=1000, height=2000, bg='MediumPurple1', highlightthickness=0)
        canva.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.97)

        scroll_y = ttk.Scrollbar(canva, orient='vertical', command=canva.yview)
        scroll_y.pack(side='right', fill='y')

        canva.configure(yscrollcommand=scroll_y.set)
        canva.create_rectangle(0, 0, 2000, 2000, fill='MediumPurple1', outline='MediumPurple1')
        canva.configure(scrollregion=canva.bbox('all'))

        # Ligando a rolagem do mouse com a barra de rolagem
        canva.bind("<MouseWheel>", lambda event: canva.yview_scroll(int(-1*(event.delta/120)), "units"))
        canva.update()

        lista = cdi.listar_arquivos()
        lista_nova = lista.split(',')

        for i in range(len(lista_nova)):
            canva.create_text(700, 50 + 50*i, text=f"{' ' * 10}{lista_nova[i]}{' ' * 10}", font=('Jacques Francois', 15, 'bold'), fill='white')
            #img = ctk.CTkImage(light_image=Image.open(lista_nova[i]), dark_image=Image.open(lista_nova[i]), size=(100,100))
            #ctk.CTkLabel(canva,text='', image=img).place(relx=0.008, rely=0.020 + 0.1*2, relheight=0.5, relwidth=0.1)

    def buttons(self):
        photo = PhotoImage(file="C:/Users/camil/.vscode/cli/Mon/UFPI/2 periodo/Laboratorio de Progamacao/tf/img/rectangle-list.png")
        photo = photo.subsample(15, 15)

        bt = ctk.CTkButton(self.root, text=" Listar arquivos de imagens do diretório corrente", width=20, anchor='center',command=lambda:self.listar_arquivos(), cursor='hand2',font=('Momcake', 20, 'bold'),
                            fg_color='MediumPurple4', background_corner_colors=['MediumPurple3', 'MediumPurple3', 'MediumPurple3', 'MediumPurple3'],
                            image=photo, compound='left')  
            
        bt2 = ctk.CTkButton(self.root, text="Sair", width=140,height=28,cursor='hand2',anchor='center', command=self.root.quit, font=('Momcake', 35, 'bold'),
                bg_color='MediumPurple3', fg_color='MediumPurple4', background_corner_colors=['MediumPurple3', 'MediumPurple3', 'MediumPurple3', 'MediumPurple3'])
        
        bt.place(relx=0.11, rely=0.770, relheight=0.1,relwidth=0.330)
        bt2.place(relx=0.17, rely=0.880, relheight=0.1,relwidth=0.180)


if __name__ == "__main__":

    root = Tk()
    app = Interface(root)
    root.mainloop() 
    