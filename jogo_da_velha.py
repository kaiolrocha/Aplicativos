print("Jogo da Velha") #Usando apenas Estruturas Condicionais: IF ELSE ELIF. Operadores Lógicos: AND OR NOT Estruturas de Repetição: WHILE FOR
print("-------------")
a = "1"
b = "2"
c = "3"

d = "4"
e = "5"
f = "6"

g = "7"
h = "8"
i = "9"

#\033[4m Para iniciar sublinhado, e \033[0m para finalizar sublinhado.
print(f"\033[4m{a}|{b}|{c}\n{d}|{e}|{f}\n{g}|{h}|{i}\033[0m")
combinacao = False
tentativas = 9

while combinacao == False:

    #Vez do X
    print("-------------")
    valido = False
    while valido == False: # Para validar jogada repetida.
        #Validar o numero de casa jogada e repetir caso for não estiver entre 1 a 9.
        while valido == False:
            jogar = input("X joga, Escolha um casa: ")
            jogar = int(jogar)
            
            if jogar in range(1,10):
                break
            else:
                print("Digite uma casa entre 1 a 9.")

        jogar = str(jogar)
        print("-------------")

        #Numeros 1 a 3
        if jogar == a:
            a = str(a.replace(a, "X"))
            break
        elif jogar == b:
            b = str(b.replace(b, "X"))
            break
        elif jogar == c:
            c = str(c.replace(c, "X"))
            break

        #Numeros 3 a 6
        elif jogar == d:
            d = str(d.replace(d, "X"))
            break
        elif jogar == e:
            e = str(e.replace(e, "X"))
            break
        elif jogar == f:
            f = str(f.replace(f, "X"))
            break

        #Numeros 7 a 9
        elif jogar == g:
            g = str(g.replace(g, "X"))
            break
        elif jogar == h:
            h = str(h.replace(h, "X"))
            break
        elif jogar == i:
            i = str(i.replace(i, "X"))
            break

        else:
            print("Casa ocupada, faça uma nova jogada.")

    #Valor da variavel entre aspas para poder quebrar linha e ficar mais organizado
    combinacao = ( a + b + c == "XXX"or a + b + c == "OOO"
                  or d + e + f == "XXX" or d + e + f == "OOO"
                  or g + h + i == "XXX" or g + h + i == "OOO"
                  or a + d + g == "XXX" or a + d + g == "OOO"
                  or b + e + h == "XXX" or b + e + h == "OOO"
                  or c + f + i == "XXX" or c + f + i == "OOO"
                  or a + e + i == "XXX" or a + e + i == "OOO" 
                  or c + e + g == "XXX" or c + e + g == "OOO"
                  ) 

    print(f"\033[4m{a}|{b}|{c}\n{d}|{e}|{f}\n{g}|{h}|{i}\033[0m")

    if combinacao == True:
        print(f"Primeiro jogador (X) ganhou!")
        break #Do while(combinacao) caso faça uma das combinações.
    
    tentativas = tentativas - 1
    # print(f"\nTentativas restantes: {tentativas}") So pra testar a quantidade de tentativas.
    if tentativas == 0:
        print("Empate")
        break #Do while(combinacao) caso chegue em 0 tentativas.
    
    
    #Segundo jogador - Vez do O
    print("-------------")
    while valido == False: # Para validar jogada repetida.
        #Validar o numero de casa jogada e repetir caso for não estiver entre 1 a 9.
        while valido == False:
            jogar = input("O joga, Escolha um casa: ")
            jogar = int(jogar)
                
            if jogar in range(1,10):
                break #Do while(valido).
            else:
                print("Digite uma casa entre 1 a 9.")
        jogar = str(jogar)
        print("-------------")

        #Numeros 1 a 3
        if jogar == a:
            a = str(a.replace(a, "O"))
            break
        elif jogar == b:
            b = str(b.replace(b, "O"))
            break
        elif jogar == c:
            c = str(c.replace(c, "O"))
            break

        #Numeros 3 a 6
        elif jogar == d:
            d = str(d.replace(d, "O"))
            break
        elif jogar == e:
            e = str(e.replace(e, "O"))
            break
        elif jogar == f:
            f = str(f.replace(f, "O"))
            break

        #Numeros 7 a 9
        elif jogar == g:
            g = str(g.replace(g, "O"))
            break
        elif jogar == h:
            h = str(h.replace(h, "O"))
            break
        elif jogar == i:
            i = str(i.replace(i, "O"))
            break

        else:
            print("Casa ocupada, faça uma nova jogada.")

    print(f"\033[4m{a}|{b}|{c}\n{d}|{e}|{f}\n{g}|{h}|{i}\033[0m")

    combinacao = ( a + b + c == "XXX"or a + b + c == "OOO"
                  or d + e + f == "XXX" or d + e + f == "OOO"
                  or g + h + i == "XXX" or g + h + i == "OOO"
                  or a + d + g == "XXX" or a + d + g == "OOO"
                  or b + e + h == "XXX" or b + e + h == "OOO"
                  or c + f + i == "XXX" or c + f + i == "OOO"
                  or a + e + i == "XXX" or a + e + i == "OOO" 
                  or c + e + g == "XXX" or c + e + g == "OOO"
                  ) 

    tentativas = tentativas - 1
    #print(f"Tentativas restantes: {tentativas}") So pra testar a quantidade de tentativas.
    if tentativas == 0:
        print("Empate")
        break  #Do while(combinacao) caso chegue em 0 tentativas.