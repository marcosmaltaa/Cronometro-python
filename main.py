from tkinter import *
import tkinter
import time

preto = "#292929"
branco = "#ebe6e6"
azul = "#548af0"

janela= Tk()
janela.title("Cronometro")
janela.geometry("300x180")
janela.configure(bg=preto)
janela.resizable(width=False, height=False)

l_tempo = Label(janela, text="Tempo")
l_tempo.grid(row=0, column=0)
tempo = Entry(janela, width=30)
tempo.grid(row=0, column=1)

def botao():
    nova = Toplevel(janela)
    nova.title("Nova Janela")
    nova.geometry("300x200")
    
    global temp
    temp = tempo.get()

b = Button(janela,text="enviar",bg=azul,command=botao)
b.grid(row=2, column=0)


janela.mainloop()
    