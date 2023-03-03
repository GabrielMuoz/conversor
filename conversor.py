

#Conversor de pies a metros 

from tkinter import *
from tkinter import ttk

class Conversor:
    def __init__(self,raiz):
        raiz.title("Pies a Metros")

        self.pies = StringVar()
        self.metros=StringVar()

        mainFrame = ttk.Frame(raiz)
        mainFrame.grid(column=0, row=0)

        piesEntry = ttk.Entry(mainFrame, textvariable=self.pies)
        piesEntry.grid(column=1, row=0)
        ttk.Label(mainFrame, text="pies").grid(column=2, row=0)
        ttk.Label(mainFrame, text="son equivalentes a").grid(column=0, row=1)
        ttk.Label(mainFrame, textvariable=self.metros).grid(column=1, row=1)
        ttk.Label(mainFrame, text="metros").grid(column=2, row=1)
        ttk.Button(mainFrame, text="calcular", command=self.calcular).grid(column=2, row=2) 

        raiz.bind("<Return>", self.calcular)

    def calcular(self, *args):
        print("boton precionado")
        pieUsuario = self.pies.get()
        piesFlotante=float(pieUsuario)
        metros= piesFlotante*.3048
        print("pies ingresaos: ",pieUsuario)
        print("metros: ", metros)
        self.metros.set(metros)


if __name__=="main_":
    print("Este es el archivo principal.")
    print("Nada mas se mostrara esto si es el prinipal.")