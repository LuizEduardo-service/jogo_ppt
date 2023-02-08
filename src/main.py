import tkinter
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

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

frame_resultado = Frame(janela, width=260, height=70, bg='red',relief='flat')
frame_resultado.grid(row=1,column=0,sticky=NW)

frame_escolha = Frame(janela, width=260, height=180, bg=co0,relief='flat')
frame_escolha.grid(row=2,column=0,sticky=NW)


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

#configurando frame de resultados
# placar
image_pedra = Image.open(r'image\pedra.png')
image_pedra = image_pedra.resize((50,50), Image.LANCZOS)
image_pedra = ImageTk.PhotoImage(image_pedra)

result_jogador = Label(frame_resultado, image=image_pedra, anchor='center',font=('Ivy 10 bold'), bg=co0,fg=co1)
separador = Label(frame_resultado, text='X', height=1, anchor='center',font=('Ivy 30 bold'), bg=co0,fg=co1)
result_PC = Label(frame_resultado, image=image_pedra, anchor='center',font=('Ivy 10 bold'), bg=co0,fg=co1)

result_jogador.place(x=40, y=10,width=50, height=50)
separador.place(x=125, y=10)
result_PC.place(x=190, y=10)

#configurando frame de escolhas
#imagens
# image_pedra = Image.open(r'image\pedra.png')
# image_pedra = image_pedra.resize((50,50), Image.ANTIALIAS)
# image_pedra = ImageTk.PhotoImage(image_pedra)
btn_pedra = Button(frame_escolha,width=50, height=50, image=image_pedra,compound=CENTER, bg=co0, fg=co0, cursor='hand2',font=('Ivy 10 bold'), anchor=CENTER, relief='flat')
btn_pedra.place(x=40,y=20)

image_papel = Image.open(r'image\papel.png')
image_papel = image_papel.resize((50,50), Image.ANTIALIAS)
image_papel = ImageTk.PhotoImage(image_papel)
btn_papel = Button(frame_escolha,width=50, height=50, image=image_papel,compound=CENTER, bg=co0, fg=co0, cursor='hand2',font=('Ivy 10 bold'), anchor=CENTER, relief='flat')
btn_papel.place(x=110,y=20)

image_tesoura = Image.open(r'image\tesoura.png')
image_tesoura = image_tesoura.resize((50,50), Image.ANTIALIAS)
image_tesoura = ImageTk.PhotoImage(image_tesoura)
btn_tesoura = Button(frame_escolha,width=50, height=50, image=image_tesoura,compound=CENTER, bg=co0, fg=co0, cursor='hand2',font=('Ivy 10 bold'), anchor=CENTER, relief='flat')
btn_tesoura.place(x=170,y=20)

#botão de inicio
btn_iniciar = Button(frame_escolha,text='Iniciar!',compound=CENTER, bg=co1, fg=co0, cursor='hand2',font=('Ivy 10 bold'), anchor=CENTER, relief='flat')
btn_iniciar.place(x=100,y=85, width=70, height=20)


janela.mainloop()