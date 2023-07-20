#Fazer um jogo de jokenpo contra a máquina do random, mostrar textos de jo-ken-po e deixar imersivo
from random import randint
from time import sleep

placar_maquina=0
placar_player=0
items=['PEDRA','PAPEL','TESOURA']
while True:
    print("=======ESSE É UM JOGO DE JOKENPO CONTRA A IA=======")
    print("ESCOLHA UMA DAS OPÇÕES: | [0]PEDRA | [1]PAPEL | [2]TESOURA | ")
    jogador=int(input("QUAL VOCÊ ESCOLHE: "))

    if jogador<0 or jogador>2:
        print("COLOQUE ALGO VÁLIDO")
        continue

    maquina=randint(0,2)
    print("JO")
    sleep(1)
    print("KEN")
    sleep(1)
    print("PO")
    sleep(2)
    print(f"A Máquina jogou: {items[maquina]}")
    print(f"Você jogou: {items[jogador]}")

    if maquina==jogador:
        print("EMPATE UHUUUUU")
        
    elif maquina==0 and jogador==1 or maquina==1 and jogador==2 or maquina==2 and jogador==0:
        print("VOCÊ GANHOU MDS")
        placar_player+=1

    else:
        print("PERDEU KKKKKKKKKKKKKKKK")
        placar_maquina+=1

    print("PLACAR--MÁQUINA:{} VOCÊ:{}".format(placar_maquina,placar_player))
    denovo=str(input("Deseja jogar novamente S/N: ")).upper().strip()

    if denovo!='S':
        break

