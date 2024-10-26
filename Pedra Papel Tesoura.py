import random

placar = {
    'CPU': 0,
    'Você': 0 
}

escolha_cpu = {
    0: "Pedra",
    1: "Papel",
    2: "Tesoura"
}

while True:
    ppt = random.randint(0,2)
    escolha_player = str(input("Pedra papel ou tesoura? "))
    if ppt == 0: #CPU escolheu pedra
        if escolha_player == "pedra" or escolha_player == "Pedra":
            print(escolha_cpu[ppt])
            print("Empate!")
            print(placar)
        if escolha_player == "papel" or escolha_player == "Papel":
            print(escolha_cpu[ppt])
            print("Você ganhou")
            placar['Você'] += 1
            print(placar)
        if escolha_player == "tesoura" or escolha_player == "Tesoura":
            print(escolha_cpu[ppt])
            print("Você perdeu")
            placar['CPU'] += 1
            print (placar)

    if ppt == 1: #CPU escolheu papel
        if escolha_player == "papel" or escolha_player == "Papel":
            print(f"A cpu escolheu {escolha_cpu[ppt]}")
            print("Empate!")
            print(placar)
        if escolha_player == "tesoura" or escolha_player == "Tesoura":
            print(f"A cpu escolheu {escolha_cpu[ppt]}")
            print("Você ganhou")
            placar['Você'] += 1
            print(placar)
        if escolha_player == "pedra" or escolha_player == "Pedra":
            print(f"A cpu escolheu {escolha_cpu[ppt]}")
            print("Você perdeu")
            placar['CPU'] += 1
            print (placar)

    if ppt == 2: #CPU escolheu tesoura
        if escolha_player == "tesoura" or escolha_player == "Tesoura":
            print(f"A cpu escolheu {escolha_cpu[ppt]}")
            print("Empate!")
            print(placar)
        if escolha_player == "pedra" or escolha_player == "Pedra":
            print(f"A cpu escolheu {escolha_cpu[ppt]}")
            print("Você ganhou")
            placar['Você'] += 1
            print(placar)
        if escolha_player == "papel" or escolha_player == "Papel":
            print(f"A cpu escolheu {escolha_cpu[ppt]}")
            print("Você perdeu")
            placar['CPU'] += 1
            print (placar)
    
    if placar['CPU'] == 3:
        print('A CPU GANHOU!!')
        break

    if placar['Você'] == 3:
        print('VOCÊ GANHOU!!')
        break