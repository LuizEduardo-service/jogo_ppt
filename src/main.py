import tkinter
from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
from random import randint

class Cores():
    # cores --------------------------------
    co0 = "#FFFFFF"  # white / branca
    co1 = "#333333"  # black / preta
    co2 = "#fcc058"  # orange / laranja
    co3 = "#fff873"  # yellow / amarela
    co4 = "#34eb3d"   # green / verde
    co5 = "#e85151"   # red / vermelha
    fundo = "#3b3b3b"

class JogoDaVelha(Cores):

    def __init__(self):
        # configuração de self.janela
        self.janela = Tk()
        self.janela.title('Jogo da Velha')
        self.janela.geometry('260x280')
        self.janela.configure(background=Cores.fundo)
        self.pontos_vencedor: int = 0
        self.carregar_imagens()
        self.frames_tela()
        self.config_frame_placar()
        self.config_frame_resultados()
        self.config_frame_escolha()
        self.janela.mainloop()
    
    def frames_tela(self):
        #frames da self.janela

        self.frame_placar = Frame(self.janela, width=260, height=100, bg=Cores.co1,relief='raised')
        self.frame_placar.grid(row=0,column=0,sticky=NW)

        self.frame_resultado = Frame(self.janela, width=260, height=70, bg=Cores.co0,relief='flat')
        self.frame_resultado.grid(row=1,column=0,sticky=NW)

        self.frame_escolha = Frame(self.janela, width=260, height=180, bg=Cores.co0,relief='flat')
        self.frame_escolha.grid(row=2,column=0,sticky=NW)


        estilo = ttk.Style(self.janela)
        estilo.theme_use('clam')
    
    def carregar_imagens(self):
        self.image_pedra = Image.open(r'image\pedra.png') # type: ignore
        self.image_pedra = self.image_pedra.resize((50,50), Image.LANCZOS)
        self.image_pedra = ImageTk.PhotoImage(self.image_pedra)

        self.image_papel = Image.open(r'image\papel.png')
        self.image_papel = self.image_papel.resize((50,50), Image.LANCZOS)
        self.image_papel = ImageTk.PhotoImage(self.image_papel)

        self.image_tesoura = Image.open(r'image\tesoura.png')
        self.image_tesoura = self.image_tesoura.resize((50,50), Image.LANCZOS)
        self.image_tesoura = ImageTk.PhotoImage(self.image_tesoura)
    
    def config_frame_placar(self):
        # configuração de frame placar
        self.pontos_jogador = IntVar()
        self.pontos_pc = IntVar()
        self.pontos_jogador.set(0)
        self.pontos_pc.set(0)
        jogador = Label(self.frame_placar, text='Você', height=1, anchor='center', font=('Ivy 10 bold'), bg=Cores.co1,fg=Cores.co0)
        jogador.place(x=40,y=70)
        computer = Label(self.frame_placar, text='PC', height=1, anchor='center', font=('Ivy 10 bold'), bg=Cores.co1,fg=Cores.co0)
        computer.place(x=190,y=70)

        # placar
        placar_jogador = Label(self.frame_placar,textvariable=self.pontos_jogador, height=1, anchor='center',font=('Ivy 30 bold'), bg=Cores.co1,fg=Cores.co0)
        separador = Label(self.frame_placar, text=':', height=1, anchor='center',font=('Ivy 30 bold'), bg=Cores.co1,fg=Cores.co0)
        placar_PC = Label(self.frame_placar, textvariable=self.pontos_pc, height=1, anchor='center',font=('Ivy 30 bold'), bg=Cores.co1,fg=Cores.co0)

        placar_jogador.place(x=40, y=10)
        separador.place(x=125, y=10)
        placar_PC.place(x=190, y=10)

    def config_frame_resultados(self):
    #configurando frame de resultados
        self.result_jogador = Label(self.frame_resultado, image='', anchor='center',font=('Ivy 10 bold'), bg=Cores.co0,fg=Cores.co1)
        separador = Label(self.frame_resultado, text='X', height=1, anchor='center',font=('Ivy 30 bold'), bg=Cores.co0,fg=Cores.co1)
        self.result_PC = Label(self.frame_resultado, image='', anchor='center',font=('Ivy 10 bold'), bg=Cores.co0,fg=Cores.co1)

        self.result_jogador.place(x=30, y=10,width=50, height=50)
        separador.place(x=120, y=10)
        self.result_PC.place(x=185, y=10, width=50, height=50)

    def config_frame_escolha(self):
        #configurando frame de escolhas
        self.btn_pedra = Button(self.frame_escolha,
                           width=50,
                           height=50,
                           image=self.image_pedra,
                           compound=CENTER,
                           bg=Cores.co0,
                           fg=Cores.co0,
                           cursor='hand2',
                           font=('Ivy 10 bold'),
                           anchor=CENTER, 
                           relief='flat',
                           command=lambda:self.escolha_jogador('Pedra'))
        self.btn_pedra.place(x=40,y=20)


        self.btn_papel = Button(self.frame_escolha,
                           width=50,
                           height=50,
                           image=self.image_papel,
                           compound=CENTER,
                           bg=Cores.co0,
                           fg=Cores.co0,
                           cursor='hand2',
                           font=('Ivy 10 bold'),
                           anchor=CENTER, 
                           relief='flat',
                           command=lambda:self.escolha_jogador('Papel'))
        self.btn_papel.place(x=110,y=20)


        self.btn_tesoura = Button(self.frame_escolha,
                           width=50,
                           height=50,
                           image=self.image_tesoura,
                           compound=CENTER,
                           bg=Cores.co0,
                           fg=Cores.co0,
                           cursor='hand2',
                           font=('Ivy 10 bold'),
                           anchor=CENTER, 
                           relief='flat',
                           command=lambda:self.escolha_jogador('Tesoura'))
        self.btn_tesoura.place(x=170,y=20)

        self.btn_papel.configure(state='disabled')
        self.btn_tesoura.configure(state='disabled')
        self.btn_pedra.configure(state='disabled')

        #botão de inicio
        self.btn_iniciar = Button(self.frame_escolha,
                                  text='Iniciar!',
                                  compound=CENTER, 
                                  bg=Cores.co1, 
                                  fg=Cores.co0, 
                                  cursor='hand2',
                                  font=('Ivy 10 bold'), 
                                  anchor=CENTER, 
                                  relief='flat',
                                  command=self.reiniciar_jogo)
        
        self.btn_iniciar.place(x=80,y=80, width=110, height=20)

    def escolha_computer(self):
        opc = randint(1,3)

        if opc == 1:
            return self.image_pedra, 'Pedra'
        elif opc == 2:
            return self.image_papel, 'Papel'
        else:
            return self.image_tesoura, 'Tesoura'

    def pontuacao(self, vencedor, qtde_pontos_vencedor: int = 5):
        jogador = self.pontos_jogador.get()
        pc = self.pontos_pc.get()

        if vencedor == 1:
            jogador += 1
            self.pontos_jogador.set(jogador)
        elif vencedor == 2:
            pc += 1
            self.pontos_pc.set(pc)

        if jogador == qtde_pontos_vencedor:
            messagebox.showinfo('Resultado','Jogador Venceu!')
            self.btn_papel.configure(state='disabled')
            self.btn_tesoura.configure(state='disabled')
            self.btn_pedra.configure(state='disabled')
            self.btn_iniciar.configure(text='Jogar Novamente!')
            self.btn_iniciar.configure(state='normal')

        elif pc == qtde_pontos_vencedor:
            messagebox.showinfo('Resultado','Computador Venceu!')
            self.btn_papel.configure(state='disabled')
            self.btn_tesoura.configure(state='disabled')
            self.btn_pedra.configure(state='disabled')
            self.btn_iniciar.configure(text='Jogar Novamente!')
            self.btn_iniciar.configure(state='normal')

    def escolha_jogador(self, escolha: str =''):

        if escolha == 'Pedra':
             image_player, opc_player = self.image_pedra, 'Pedra'
        elif escolha == 'Papel':
             image_player, opc_player = self.image_papel, 'Papel'
        else:
             image_player, opc_player = self.image_tesoura, 'Tesoura'
        
        image_pc, opc_pc = self.escolha_computer()

        vencedor = self.definir_vencedor(str(opc_player), str(opc_pc))

        self.result_jogador.configure(image=image_player)        
        self.result_PC.configure(image=image_pc) 
        self.pontuacao(vencedor)

    def reiniciar_jogo(self):

        self.pontos_jogador.set(0)
        self.pontos_pc.set(0)
        self.btn_papel.configure(state='normal')
        self.btn_tesoura.configure(state='normal')
        self.btn_pedra.configure(state='normal')
        self.result_jogador.configure(image='')
        self.result_PC.configure(image='')
        self.btn_iniciar.configure(state='disabled')

    def definir_vencedor(self, jogador: str, pc: str):
        print('='*30)
        print(f'Jogador: {jogador} PC: {pc}')
        print('='*30)

        if jogador == 'Pedra' and pc == 'Tesoura':
            print(f'Jogador Venceu')
            return 1
        elif jogador == 'Tesoura' and pc == 'Papel':
            print(f'Jogador Venceu')
            return 1
        elif jogador == 'Papel' and pc == 'Pedra':
            print(f'Jogador Venceu')
            return 1
        elif jogador == pc:
            print(f'Empate')
            return 0
        else:
            print(f'Computador Venceu')
            return 2


if __name__ == '__main__':
    JogoDaVelha()
    