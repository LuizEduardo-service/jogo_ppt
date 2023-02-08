import tkinter
from tkinter import *
from tkinter import ttk

# cores --------------------------------
co0 = "#FFFFFF"  # white / branca
co1 = "#333333"  # black / preta
co2 = "#fcc058"  # orange / laranja
co3 = "#fff873"  # yellow / amarela
co4 = "#34eb3d"   # green / verde
co5 = "#e85151"   # red / vermelha

fundo = "#3b3b3b"
# configuração de janela
janela = Tk()
janela.title('Jogo da Velha')
janela.geometry('260x280')
janela.configure(background=fundo)

#frames da janela

frame_placar = Frame(janela, width=260, height=100, bg=co1,relief='raised')
frame_placar.grid(row=0,column=0,sticky=NW)

frame_escolha = Frame(janela, width=260, height=180, bg=co0,relief='flat')
frame_escolha.grid(row=1,column=0,sticky=NW)

estilo = ttk.Style(janela)
estilo.theme_use('clam')


# configuração de frame placar
jogador = Label(frame_placar, text='Você', height=1, anchor='center', font=('Ivy 10 bold'), bg=co1,fg=co0)
jogador.place(x=40,y=70)
computer = Label(frame_placar, text='PC', height=1, anchor='center', font=('Ivy 10 bold'), bg=co1,fg=co0)
computer.place(x=190,y=70)

# placar
placar_jogador = Label(frame_placar, text='0', height=1, anchor='center',font=('Ivy 30 bold'), bg=co1,fg=co0)
separador = Label(frame_placar, text=':', height=1, anchor='center',font=('Ivy 30 bold'), bg=co1,fg=co0)
placar_PC = Label(frame_placar, text='0', height=1, anchor='center',font=('Ivy 30 bold'), bg=co1,fg=co0)

placar_jogador.place(x=40, y=10)
separador.place(x=125, y=10)
placar_PC.place(x=190, y=10)


janela.mainloop()