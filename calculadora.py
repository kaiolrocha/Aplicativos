cd C:\Python\projeto_calculadora
#No caso da interface CustomTkinter
import customtkinter as ctk
ctk.set_appearance_mode('system')

#Criação da janela
calculadora = ctk.CTk()
calculadora.title('Calculadora')
calculadora.geometry('320x500')

total_colunas = 4
total_linhas = 9

for col in range(total_colunas):
    calculadora.grid_columnconfigure(col, weight=1)

for row in range(total_linhas):
    calculadora.grid_rowconfigure(row, weight=1)

#Criação das funções de funcinalidades
#tese

#Criação dos botões

#Criação do Frames
#Frame da primeira linha
'''
primeira_linha = ctk.CTkFrame(calculadora, fg_color='transparent')
primeira_linha.grid(row=0, column=0, columnspan=4, pady=1)

for colframe0 in range(6):
    primeira_linha.grid_columnconfigure(colframe0, weight=1)
for rowframe0 in range(1):
    primeira_linha.grid_rowconfigure(rowframe0, weight=1)    
'''
#Frame do lugar do calculo
local_do_calculo = ctk.CTkFrame(calculadora, fg_color='transparent')
local_do_calculo.grid(row=2, column=0, columnspan=4, pady=1, sticky='nsew')

campo_usuario = ctk.CTkEntry(local_do_calculo,placeholder_text='0', width=320, height=100, justify='right', font=ctk.CTkFont(size=50))
campo_usuario.grid(row=2, column=0, padx=2, pady=2)

for colframe1 in range(6):
    local_do_calculo.grid_columnconfigure(colframe1, weight=1)
for rowframe1 in range(1):
    local_do_calculo.grid_rowconfigure(rowframe1, weight=1)

#Frame dos botãozinhos
botoes_pequenos = ctk.CTkFrame(calculadora, fg_color='transparent')
botoes_pequenos.grid(row=3, column=0, columnspan=4, pady=1, sticky='nsew') #Ajuda do chat com collunspan e sticky

for colframe2 in range(6):
    botoes_pequenos.grid_columnconfigure(colframe2, weight=1)

for rowframe2 in range(1):
    botoes_pequenos.grid_rowconfigure(rowframe2, weight=1)

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

#Frame termina aqui

botao_excluir = ctk.CTkButton(calculadora,text='◅',width=75, height=55)
botao_excluir.grid(row=4, column=3, padx=2, pady=2)

botao_porcentagem = ctk.CTkButton(calculadora,text='%',width=75, height=55)
botao_porcentagem.grid(row=4, column=0, padx=2, pady=2)

botao_limparCE = ctk.CTkButton(calculadora,text='CE',width=75, height=55)
botao_limparCE.grid(row=4, column=1, padx=2, pady=2)

botao_limparC = ctk.CTkButton(calculadora,text='C',width=75, height=55)
botao_limparC.grid(row=4, column=2, padx=2, pady=2)

botao_excluir = ctk.CTkButton(calculadora,text='¹/x',width=75, height=55)
botao_excluir.grid(row=5, column=0, padx=2, pady=2)

botao_x2 = ctk.CTkButton(calculadora,text='x²',width=75, height=55)
botao_x2.grid(row=5, column=1, padx=2, pady=2)

botao_raizquadrada = ctk.CTkButton(calculadora,text='√x',width=75, height=55)
botao_raizquadrada.grid(row=5, column=2, padx=2, pady=2)

botao_dividir = ctk.CTkButton(calculadora,text='÷',width=75, height=55)
botao_dividir.grid(row=5, column=3, padx=2, pady=2)

botao_7 = ctk.CTkButton(calculadora,text='7',width=75, height=55)
botao_7.grid(row=6, column=0, padx=2, pady=2)

botao_8 = ctk.CTkButton(calculadora,text='8',width=75, height=55)
botao_8.grid(row=6, column=1, padx=2, pady=2)

botao_9 = ctk.CTkButton(calculadora,text='9',width=75, height=55)
botao_9.grid(row=6, column=2, padx=2, pady=2)

botao_x = ctk.CTkButton(calculadora,text='x',width=75, height=55)
botao_x.grid(row=6, column=3, padx=2, pady=2)

botao_4 = ctk.CTkButton(calculadora,text='4',width=75, height=55)
botao_4.grid(row=7, column=0, padx=2, pady=2)

botao_5 = ctk.CTkButton(calculadora,text='5',width=75, height=55)
botao_5.grid(row=7, column=1, padx=2, pady=2)

botao_6 = ctk.CTkButton(calculadora,text='6',width=75, height=55)
botao_6.grid(row=7, column=2, padx=2, pady=2)

botao_menos = ctk.CTkButton(calculadora,text='-',width=75, height=55)
botao_menos.grid(row=7, column=3, padx=2, pady=2)

botao_1 = ctk.CTkButton(calculadora,text='1',width=75, height=55)
botao_1.grid(row=8, column=0, padx=2, pady=2)

botao_2 = ctk.CTkButton(calculadora,text='2',width=75, height=55)
botao_2.grid(row=8, column=1, padx=2, pady=2)

botao_3 = ctk.CTkButton(calculadora,text='3',width=75, height=55)
botao_3.grid(row=8, column=2, padx=2, pady=2)

botao_mais = ctk.CTkButton(calculadora,text='+',width=75, height=55)
botao_mais.grid(row=8, column=3, padx=2, pady=2)

botao_mais_e_menos = ctk.CTkButton(calculadora,text='+/-',width=75, height=55)
botao_mais_e_menos.grid(row=9, column=0, padx=2, pady=2)

botao_0 = ctk.CTkButton(calculadora,text='0',width=75, height=55)
botao_0.grid(row=9, column=1, padx=2, pady=2)

botao_virgula = ctk.CTkButton(calculadora,text=',',width=75, height=55)
botao_virgula.grid(row=9, column=2, padx=2, pady=2)

botao_igual = ctk.CTkButton(calculadora,text='=',width=75, height=55, fg_color='blue',font=ctk.CTkFont(size=20))
botao_igual.grid(row=9, column=3, padx=2, pady=2)

#Inicia o loop da aplicação, sem isso nem abre
calculadora.mainloop()