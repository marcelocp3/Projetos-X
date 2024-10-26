print('Nesse programa, é possível descobrir quais números primos estão entre x valor e y valor e se um número específico é primo!')
escolha = int(input('Gostaria de saber um número específico(1) ou algum intervalo(2)? '))
if escolha == 1:
    print('Indique o número que deseja descobrir: ')
    num_unico = int(input(''))
    k = num_unico - 1
    f = 0
    while k >= 1:
        if k != 1:
            if num_unico%k == 0:
                f += 1
                break
            k -= 1
        else:
            if k == 1:
                f -= 1
            k -= 1
    if f > 0:
        print(f'O número {num_unico} não é primo')
    else:
        print(f'O número {num_unico} é primo')


if escolha == 2:
    print('Primeiramente, indique o valor x: ')
    num_inicial = int(input(''))
    print('Agora, indique o valor y: ')
    num = int(input(''))
    i = num_inicial
    if i == 0 or i == 1:
        lista_primos  = [1]
    else:
        lista_primos = []
    while i in range(num +1):
        j = i - 1
        while j >= 1:
            if j != 1:
                if i%j == 0:
                    break
                j -= 1
            else:
                if j == 1:
                    lista_primos.append(i)
                j -= 1
        i += 1

    print(lista_primos)
    print(f'Tem {len(lista_primos)} número(s) primo(s) entre {num_inicial} e {num}')






