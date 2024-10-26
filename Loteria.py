import random


def loteria(escolhidos):
    numeros = []
    i = 0
    premio = 0
    while i < 6:
        num = random.randint(1, 60)
        if num not in numeros:
            numeros.append(num)
            i += 1
    
    numeros.sort()


    j = 0
    while j < len(escolhidos):
        if escolhidos[j] in numeros:
            premio += 500000
        else:
            j += 1

    print(f'Os números sorteados foram: {numeros}')
    print(f'Você acertou {premio/3000000} números.')
    return premio


loteria([6,12,18,24,30,36])