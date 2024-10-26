import random
import time

placar = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]]
turno = 0
rodadas_sem_remocao = 0

while True:
    dado_1 = random.randint(1, 6)
    dado_2 = random.randint(1, 6)
    soma_dados = dado_1 + dado_2
    numero_removido = False

    if turno == 0:
        print('Vez do jogador')
        print(placar[turno])
        time.sleep(1)
        print(f'Os dados escolheram {dado_1} e {dado_2} e a soma dos dados foi {soma_dados}')
        if dado_1 in placar[turno] and dado_2 in placar[turno]:
            if dado_1 == dado_2:
                placar[turno].remove(dado_1)
                print(f'Removendo o número {dado_1}')
                numero_removido = True
            else:
                placar[turno].remove(dado_1)
                placar[turno].remove(dado_2)
                print(f'Removendo os números {dado_1} e {dado_2}')
                numero_removido = True
        else:
            if dado_1 not in placar[turno] and dado_2 not in placar[turno]:
                if soma_dados in placar[turno]:
                    placar[turno].remove(soma_dados)
                    print(f'Removendo o número {soma_dados}')
                    numero_removido = True
                else:
                    print('Não foi possível remover nenhum número, portanto estamos passando a vez para a CPU')
                    print(f'Faltam {len(placar[0])} número(s) para você ganhar e {len(placar[1])} número(s) para a CPU ganhar')
                    time.sleep(1)
                    turno += 1
            else:
                if dado_1 not in placar[turno] and dado_2 in placar[turno]:
                    placar[turno].remove(dado_2)
                    print(f'Removendo o número {dado_2}')
                    numero_removido = True
                elif dado_1 in placar[turno] and dado_2 not in placar[turno]:
                    placar[turno].remove(dado_1)
                    print(f'Removendo o número {dado_1}')
                    numero_removido = True
                else:
                    print('Não foi possível remover nenhum número, portanto estamos passando a vez para a CPU')
                    print(f'Faltam {len(placar[0])} número(s) para você ganhar e {len(placar[1])} número(s) para a CPU ganhar')
                    time.sleep(1)
                    turno += 1

        if len(placar[turno]) == 0:
            print('Você venceu!!')
            break
    if turno == 1:
        print('Vez da CPU')
        print(placar[turno])
        time.sleep(1)
        print(f'Os dados escolheram {dado_1} e {dado_2} e a soma dos dados foi {soma_dados}')
        if dado_1 in placar[turno] and dado_2 in placar[turno]:
            if dado_1 == dado_2:
                placar[turno].remove(dado_1)
                print(f'Removendo o número {dado_1}')
                numero_removido = True
            else:
                placar[turno].remove(dado_1)
                placar[turno].remove(dado_2)
                print(f'Removendo os números {dado_1} e {dado_2}')
                numero_removido = True
        else:
            if dado_1 not in placar[turno] and dado_2 not in placar[turno]:
                if soma_dados in placar[turno]:
                    placar[turno].remove(soma_dados)
                    print(f'Removendo o número {soma_dados}')
                    numero_removido = True
                else:
                    print('Não foi possível remover nenhum número, portanto estamos passando a vez de volta para o player')
                    print(f'Faltam {len(placar[1])} número(s) para a CPU ganhar e {len(placar[0])} número(s) para você ganhar')
                    time.sleep(1)
                    turno -= 1
            else:
                if dado_1 not in placar[turno] and dado_2 in placar[turno]:
                    placar[turno].remove(dado_2)
                    print(f'Removendo o número {dado_2}')
                    numero_removido = True
                elif dado_1 in placar[turno] and dado_2 not in placar[turno]:
                    placar[turno].remove(dado_1)
                    print(f'Removendo o número {dado_1}')
                    numero_removido = True
                else:
                    print('Não foi possível remover nenhum número, portanto estamos passando a vez de volta para o player')
                    print(f'Faltam {len(placar[1])} número(s) para a CPU ganhar e {len(placar[0])} número(s) para você ganhar')
                    time.sleep(1)
                    turno -= 1

        if len(placar[turno]) == 0:
            print('A CPU venceu!!')
            break

    if numero_removido:
        rodadas_sem_remocao = 0
    else:
        rodadas_sem_remocao += 1

    if rodadas_sem_remocao >= 10:
        if len(placar[0]) < len(placar[1]):
            print('Devido a 10 rodadas seguidas sem remoção, você venceu com menos números restantes!')
        elif len(placar[0]) > len(placar[1]):
            print('Devido a 10 rodadas seguidas sem remoção, a CPU venceu com menos números restantes!')
        else:
            print('Devido a 10 rodadas seguidas sem remoção, houve um empate!')
        break
