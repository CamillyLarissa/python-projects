import cv2
import os
import numpy as np


class Filtro:
    def __init__(self, imagem):
        self.imagem = imagem

    def aplicar(self):
        raise NotImplementedError("Método 'aplicar' não implementado")

    def salvar(self, nome_arquivo):
        resultado = self.aplicar()
        cv2.imwrite(nome_arquivo, resultado)
        print(f'Imagem salva como {nome_arquivo}')

class EscalaCinza(Filtro):
    def aplicar(self):
        imagemCinza = cv2.cvtColor(self.imagem, cv2.COLOR_BGR2GRAY)
        return imagemCinza

class PretoEBranco(Filtro):
    def aplicar(self):
        imagemCinza = cv2.cvtColor(self.imagem, cv2.COLOR_BGR2GRAY)
        _, imagemPretoBranco = cv2.threshold(imagemCinza, 127, 255, cv2.THRESH_BINARY)
        return imagemPretoBranco


class Cartoon(Filtro):
    def aplicar(self):
        imagemBilateral = cv2.bilateralFilter(self.imagem, d=9, sigmaColor=75, sigmaSpace=75)
        imagemCinza = cv2.cvtColor(imagemBilateral, cv2.COLOR_BGR2GRAY)
        imagemCinzaBlurred = cv2.medianBlur(imagemCinza, 7)
        bordas = cv2.adaptiveThreshold(imagemCinzaBlurred, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 10)
        imagemCartoon = cv2.bitwise_and(imagemBilateral, imagemBilateral, mask=bordas)
        return imagemCartoon
    
class Cartoon1(Filtro):
    def aplicar(self):
        imagemBilateral = cv2.bilateralFilter(self.imagem, d=15, sigmaColor=150, sigmaSpace=150)
        imagemCinza = cv2.cvtColor(imagemBilateral, cv2.COLOR_BGR2GRAY)
        imagemCinzaBlurred = cv2.medianBlur(imagemCinza, 9)
        bordas = cv2.adaptiveThreshold(imagemCinzaBlurred, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
        imagemCartoon = cv2.bitwise_and(imagemBilateral, imagemBilateral, mask=bordas)
        return imagemCartoon

class FotoNegativa(Filtro):
    def aplicar(self):
        imagemNegativa = cv2.bitwise_not(self.imagem)
        return imagemNegativa

class Contorno(Filtro):
    def aplicar(self):
        imagemCinza = cv2.cvtColor(self.imagem, cv2.COLOR_BGR2GRAY)
        bordas = cv2.Canny(imagemCinza, 100, 200)
        imagemContorno = cv2.cvtColor(bordas, cv2.COLOR_GRAY2BGR)
        return imagemContorno

class Blurred(Filtro):
    def init(self, imagem):
        super().init(imagem)

    def aplicar(self):
        imagemBlurred = cv2.blur(self.imagem, (20,20))
        return imagemBlurred

    
if __name__ == '__main__':
    imagem_path = 'img\coringa-instagram-fotos-novas-1.jpg'
    imagem = cv2.imread(imagem_path)

    
    filtro = Cartoon1(imagem)
    filtro.salvar('tuuu')


    print('Filtros aplicados com sucesso')