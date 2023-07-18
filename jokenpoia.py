#Fazer um jogo de jokenpo contra a máquina do random, mostrar textos de jo-ken-po e deixar imersivo
from random import randint
from time import sleep
maquina=randint(0,2)
items=["PEDRA", "PAPEL", "TESOURA"]
print("ESSE É UM JOGO DE JOKENPO CONTRA A IA")
print("ESCOLHA UMA DAS OPÇÕES: [0]PEDRA [1]PAPEL [2]TESOURA ")
jogador=int(input("QUAL VOCÊ ESCOLHE: "))

print("JO")
sleep(1)
print("KEN")
sleep(1)
print("PO")
sleep(2)
print(f"Maquina jogou:  {items[maquina]}")
print(f"Você jogou:  {items[jogador]}")

if maquina==0:
    if jogador==0:
        print("EMPATOU AAAA")
elif jogador==1:
    print("VOCÊ VENCEU")
elif jogador==2:
    print("VOCÊ PERDEU KKKKKKK")

if maquina==1:
    if jogador==1:
        print("EMPATOU AAAA")
elif jogador==2:
    print("VOCÊ VENCEU")
elif jogador==0:
    print("VOCÊ PERDEU KKKKKKK")

    if jogador==2:
        print("EMPATOU AAAA")
elif jogador==0:
    print("VOCÊ VENCEU")
elif jogador==1:
    print("VOCÊ PERDEU KKKKKKK")
else:
    print("ESCOLHE DIREITO")
