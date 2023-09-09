import random

palavrasAleatorias=['BOLSONARO','ROBERTINHO','CASA','CACHORRO','POLTRONA','PARALELEPIPEDO']
escolha=random.choice(palavrasAleatorias)
letra_correta=[]
letra_errada=[]
tentativas=6
def palavraOculta(palavra,letra_correta,letra_errada):
    palavra_oculta=""
    for letra in palavra:
        if letra in letra_correta:
            palavra_oculta+=letra
        else:
            palavra_oculta+="_"
    return palavra_oculta
while True:
    palavra_oculta=palavraOculta(escolha,letra_correta,letra_errada)
    print(palavra_oculta)
    letra=str(input("COLOQUE UMA LETRA: ")).upper()
    if letra in letra_correta or letra in letra_errada:
        print("VOCÊ JÁ TENTOU ESSA LETRA")
        continue
    if letra in escolha:
        letra_correta.append(letra)
        if escolha==palavra_oculta:
            print("VOCÊ VENCEUU")
            break
    else:
        letra_errada.append(letra)
        tentativas-=1
        print(f"LETRA ERRADA: {','.join(letra_errada)}")
        print(f"TENTATIVAS: {tentativas}")
    if tentativas==0:
        print("VOCÊ PERDEU")
        print(f"A PALAVRA ERA {palavra_oculta}")
        break