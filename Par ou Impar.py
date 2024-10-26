import random

placar = {
    'CPU': 0,
    'Você': 0 
}

while True:
    pergunta = str(input('Par ou Ímpar? '))
    mao_cpu = random.randint(0,10)
    mao_player = int(input('Número jogado: '))
    resultado = mao_cpu + mao_player
    print(resultado)
    if pergunta == 'par' or pergunta == 'Par':
        if resultado%2 == 0:
            print('Você ganhou!')
            placar['Você'] += 1
            print(placar)
        else:
            print('Você perdeu!')
            placar['CPU'] += 1
            print(placar)
    if pergunta == 'impar' or pergunta == 'Impar':
        if resultado%2 != 0:
            print('Você ganhou!')
            placar['Você'] += 1
            print(placar)
        else:
            print('Você perdeu!')
            placar['CPU'] += 1
            print(placar)
    
    if placar['CPU'] == 3:
        print('A CPU GANHOU!!')
        break
    if placar['Você'] == 3:
        print("Parabéns, você ganhou!!")
        break

