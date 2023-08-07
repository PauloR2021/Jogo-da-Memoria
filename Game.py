import tkinter as tk
from tkinter import messagebox
import random

#Definindo as Configurações do Jogo
NUM_LINHAS =4
NUM_COLUNAS =4
CARTAO_SIZE_W = 10
CARTAO_SIZE_H = 5
CORES_CARTAO = ['red','blue','green','yellow', 'purple','orange','cyan','magenta']
COR_FUNDO = "#343a40"
COR_LETRA = "white"
FONT_STYLE =('Arial',12,'bold')
MAX_TENTATIVAS = 25

#Criando Função das Grades Aletórias de Cores para as Cartas

def create_card_grid():
    cores = CORES_CARTAO *2
    random.shuffle(cores)

    grid = []

    for _ in range(NUM_LINHAS):
        linha = []
        for _ in range(NUM_COLUNAS):
            cor = cores.pop()
            linha.append(cor)
        grid.append(linha)

    return grid

#Função para o Clique das Cartas
def card_clicked(linha,coluna):
    cartao = cartoes[linha][coluna]
    cor = cartao['bg']

    if cor == 'black':
        cartao['bg']= grid[linha][coluna]
        cartao_revelado.append(cartao)
        if len(cartao_revelado) == 2:
            check_match()

#Verificar se os Cartões são Iguais
def check_match():
    cartao1,cartao2 = cartao_revelado

    if cartao1['bg'] == cartao2['bg']:
        cartao1.after(1000,cartao1.destroy)
        cartao2.after(1000, cartao2.destroy)
        cartao_correspondentes.extend([cartao1,cartao2])

        check_win()
    else:
        cartao1.after(1000,lambda :cartao1.config(bg='black'))
        cartao2.after(1000, lambda: cartao2.config(bg='black'))
    cartao_revelado.clear()

    update_score()

#Verificando se o Jogador Ganhou o Jogo

def check_win():

    if len(cartao_correspondentes) == NUM_LINHAS * NUM_COLUNAS:
        messagebox.showinfo("Parabéns!","Você ganhou o JOGO!")
        janela.quit()

#Atualizar a Pontuação e Verificar se o Jogador Perdeu o Jogo

def update_score():
    global numero_tentativas
    numero_tentativas +=1
    label_tentativas.config(text="Tentativas: {}/{}".format(numero_tentativas,MAX_TENTATIVAS))

    if numero_tentativas >= MAX_TENTATIVAS:
        messagebox.showinfo("Fim de Jogo", "Você perdeu o Jogo!")
        janela.quit()

janela = tk.Tk()
janela.title('')
janela.configure(bg=COR_FUNDO)

#Criando a Grade de Cartas

grid = create_card_grid()
cartoes = []
cartao_revelado = []
cartao_correspondentes =[]
numero_tentativas = 0

for linha in range(NUM_LINHAS):
    linha_de_cartoes = []

    for col in range(NUM_COLUNAS):
        cartao = tk.Button(janela,command=lambda r=linha,c=col:card_clicked(r,c),width=CARTAO_SIZE_W,height=CARTAO_SIZE_H,bg='black',relief=tk.RAISED,bd=3 )
        cartao.grid(row=linha, column=col,padx=5 , pady=5)
        linha_de_cartoes.append(cartao)
    cartoes.append(linha_de_cartoes)



#Criando a Interface do jogo



#Personalizando a Carta

button_style = {'activebackground':'#f8f9fa','font':FONT_STYLE,'fg':COR_LETRA}

janela.option_add('*Button',button_style)

#Criando Texto para Mostrar as Tentativas

label_tentativas = tk.Label(janela,text="Tentativas: {}/{}".format(numero_tentativas,MAX_TENTATIVAS),fg=COR_LETRA,bg=COR_FUNDO,font=FONT_STYLE)
label_tentativas.grid(row=NUM_LINHAS,columnspan=NUM_COLUNAS,padx=10,pady=10)

janela.mainloop()
