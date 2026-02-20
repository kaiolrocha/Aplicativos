
#No caso da interface CustomTkinter
import customtkinter as ctk
ctk.set_appearance_mode('system')

#Criação da janela
calculadora = ctk.CTk()
calculadora.title('Calculadora')
calculadora.geometry('320x500')

total_colunas = 4
total_linhas = 8

for col in range(total_colunas):
    calculadora.grid_columnconfigure(col, weight=1)

#Menu
calculadora.grid_rowconfigure(0, weight=0, minsize=35)
#Visor
calculadora.grid_rowconfigure(1, weight=3)
#Botãozinhos
calculadora.grid_rowconfigure(2, weight=0)
#Botões principais
for row in range(3, 9):
    calculadora.grid_rowconfigure(row, weight=2)

#Criação das funções de funcinalidades

#Frame do Menu
primeira_linha = ctk.CTkFrame(calculadora, fg_color='transparent', height=35)
primeira_linha.grid(row=0, column=0, columnspan=4, pady=1, sticky='nsew')
primeira_linha.grid_propagate(False) #Com isso aqui consegui deixar pequeno mesmo sem nenhum conteudo, importante.

primeira_linha.grid_columnconfigure(0, weight=0)
primeira_linha.grid_columnconfigure(1, weight=0)
primeira_linha.grid_columnconfigure(2, weight=0)
primeira_linha.grid_columnconfigure(3, weight=1)
primeira_linha.grid_columnconfigure(4, weight=0)

botao_menu = ctk.CTkButton(primeira_linha,text='|||',width=20, text_color='black', fg_color='transparent')
botao_menu.grid(row=0, column=0, padx=2, pady=2)

modelo = ctk.CTkLabel(primeira_linha,text='Padrão', font=ctk.CTkFont(size=20, weight='bold'))
modelo.grid(row=0, column=1, padx=2, pady=2)


botao_subir = ctk.CTkButton(primeira_linha, text='SU', width=20, text_color='black', fg_color='transparent')
botao_subir.grid(row=0, column=2, padx=2, pady=2)

#Coluna 3 vazia, so para criar espaço

botao_historico = ctk.CTkButton(primeira_linha, text='HI', width=20, text_color='black', fg_color='transparent')
botao_historico.grid(row=0, column=4, padx=2, pady=2)

#Frame do Visor
local_do_calculo = ctk.CTkFrame(calculadora, fg_color='transparent')
local_do_calculo.grid(row=1, column=0, columnspan=4, pady=1, sticky='nsew')
local_do_calculo.grid_columnconfigure(0, weight=1)
local_do_calculo.grid_rowconfigure(0, weight=1)

campo_usuario = ctk.CTkEntry(local_do_calculo,placeholder_text='0', justify='right', font=ctk.CTkFont(size=50))
campo_usuario.grid(row=0, column=0, padx=2, pady=2, sticky='nsew')

#Frame dos Botãozinhos
botoes_pequenos = ctk.CTkFrame(calculadora, fg_color='transparent')
botoes_pequenos.grid(row=2, column=0, columnspan=4, pady=1, sticky='nsew') #Ajuda do chat com collunspan e sticky

for colframe2 in range(6):
    botoes_pequenos.grid_columnconfigure(colframe2, weight=1)

botao_mc = ctk.CTkButton(botoes_pequenos,text='MC',width=20, text_color='black', fg_color='transparent')
botao_mc.grid(row=0, column=0, padx=2, pady=2)

botao_mr = ctk.CTkButton(botoes_pequenos,text='MR',width=20, text_color='black', fg_color='transparent')
botao_mr.grid(row=0, column=1, padx=2, pady=2)

botao_Mmais = ctk.CTkButton(botoes_pequenos,text='M+',width=20, text_color='black', fg_color='transparent')
botao_Mmais.grid(row=0, column=2, padx=2, pady=2)

botao_Mmenos = ctk.CTkButton(botoes_pequenos,text='M-',width=20, text_color='black', fg_color='transparent')
botao_Mmenos.grid(row=0, column=3, padx=2, pady=2)

botao_Ms = ctk.CTkButton(botoes_pequenos,text='M-',width=20, text_color='black', fg_color='transparent')
botao_Ms.grid(row=0, column=4, padx=2, pady=2)

botao_Msetinha = ctk.CTkButton(botoes_pequenos,text='M+',width=20, text_color='black', fg_color='transparent')
botao_Msetinha.grid(row=0, column=5, padx=2, pady=2)

#Botões Linha 3
# caramba antes estava com width=75, height=55 em todos os botões, invés de sticky='nsew', quando abria tela cheia o tamanho dos botoes não acompanhava...
botao_excluir = ctk.CTkButton(calculadora,text='◅')
botao_excluir.grid(row=3, column=3, padx=2, pady=2, sticky='nsew')

botao_porcentagem = ctk.CTkButton(calculadora,text='%')
botao_porcentagem.grid(row=3, column=0, padx=2, pady=2, sticky='nsew')

botao_limparCE = ctk.CTkButton(calculadora,text='CE')
botao_limparCE.grid(row=3, column=1, padx=2, pady=2, sticky='nsew')

botao_limparC = ctk.CTkButton(calculadora,text='C')
botao_limparC.grid(row=3, column=2, padx=2, pady=2, sticky='nsew')

#Botões Linha 4
botao_excluir = ctk.CTkButton(calculadora,text='¹/x')
botao_excluir.grid(row=4, column=0, padx=2, pady=2, sticky='nsew')

botao_x2 = ctk.CTkButton(calculadora,text='x²')
botao_x2.grid(row=4, column=1, padx=2, pady=2, sticky='nsew')

botao_raizquadrada = ctk.CTkButton(calculadora,text='√x')
botao_raizquadrada.grid(row=4, column=2, padx=2, pady=2, sticky='nsew')

botao_dividir = ctk.CTkButton(calculadora,text='÷')
botao_dividir.grid(row=4, column=3, padx=2, pady=2, sticky='nsew')

#Botões Linha 5
botao_7 = ctk.CTkButton(calculadora,text='7')
botao_7.grid(row=5, column=0, padx=2, pady=2, sticky='nsew')

botao_8 = ctk.CTkButton(calculadora,text='8')
botao_8.grid(row=5, column=1, padx=2, pady=2, sticky='nsew')

botao_9 = ctk.CTkButton(calculadora,text='9')
botao_9.grid(row=5, column=2, padx=2, pady=2, sticky='nsew')

botao_x = ctk.CTkButton(calculadora,text='x')
botao_x.grid(row=5, column=3, padx=2, pady=2, sticky='nsew')

#Botões Linha 6
botao_4 = ctk.CTkButton(calculadora,text='4')
botao_4.grid(row=6, column=0, padx=2, pady=2, sticky='nsew')

botao_5 = ctk.CTkButton(calculadora,text='5')
botao_5.grid(row=6, column=1, padx=2, pady=2, sticky='nsew')

botao_6 = ctk.CTkButton(calculadora,text='6')
botao_6.grid(row=6, column=2, padx=2, pady=2, sticky='nsew')

botao_menos = ctk.CTkButton(calculadora,text='-')
botao_menos.grid(row=6, column=3, padx=2, pady=2, sticky='nsew')

#Botões Linha 7
botao_1 = ctk.CTkButton(calculadora,text='1')
botao_1.grid(row=7, column=0, padx=2, pady=2, sticky='nsew')

botao_2 = ctk.CTkButton(calculadora,text='2')
botao_2.grid(row=7, column=1, padx=2, pady=2, sticky='nsew')

botao_3 = ctk.CTkButton(calculadora,text='3')
botao_3.grid(row=7, column=2, padx=2, pady=2, sticky='nsew')

botao_mais = ctk.CTkButton(calculadora,text='+')
botao_mais.grid(row=7, column=3, padx=2, pady=2, sticky='nsew')

#Botões Linha 8
botao_mais_e_menos = ctk.CTkButton(calculadora,text='+/-')
botao_mais_e_menos.grid(row=8, column=0, padx=2, pady=2, sticky='nsew')

botao_0 = ctk.CTkButton(calculadora,text='0')
botao_0.grid(row=8, column=1, padx=2, pady=2, sticky='nsew')

botao_virgula = ctk.CTkButton(calculadora,text=',')
botao_virgula.grid(row=8, column=2, padx=2, pady=2, sticky='nsew')

botao_igual = ctk.CTkButton(calculadora,text='=', fg_color='blue',font=ctk.CTkFont(size=20))
botao_igual.grid(row=8, column=3, padx=2, pady=2, sticky='nsew')

#Inicia o loop da aplicação, sem isso nem abre
calculadora.mainloop()