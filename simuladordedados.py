import random

while True:
    pergunta=int(input("QUAL DADO DESEJA ROLAR [1]D4 [2]D6 [3]D20 [4]D100: "))
    qntd_dados=int(input("QUANTOS DADOS QUER ROLAR: "))
    soma=0

    if pergunta==1:
        result=[random.randint(1,4) for _ in range(qntd_dados)]
        for x in result:
            soma+=x
        print(f"NO DADO DE 4 LADOS VOCÊ TIROU: {result}")
        print(f"A SOMA DE TOODOS É: {soma}")
        
    elif pergunta==2:
        result=[random.randint(1,6) for _ in range(qntd_dados)]
        for x in result:
            soma+=x
        print(f"NO DADO DE 6 LADOS VOCÊ TIROU: {result}")
        print(f"A SOMA DE TODOS É: {soma}")

    elif pergunta==3:
        result=[random.randint(1,20) for _ in range(qntd_dados)]
        for x in result:
            soma+=x
        print(f"NO DADO DE 20 LADOS VOCÊ TIROU: {result}")
        print(f"A SOMA DE TODOS É: {soma}")

    elif pergunta==4:
        result=[random.randint(1,100) for _ in range(qntd_dados)]
        for x in result:
            soma+=x
        print(f"NO DADO DE 100 LADOS VOCÊ TIROU: {result}")
        print(f"A SOMA DE TODOS É: {soma}")
    else:
        print("COLOQUE VALORES OPÇÕES REAIS")

    sair=str(input("DESEJA SAIR S/N: ")).upper()
    if sair=='S':
        break