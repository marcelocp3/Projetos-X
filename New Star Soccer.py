titulos = {
    'Copa América': 0,
    'Copa do Mundo': 0,
    'Bola de Ouro' : 0,
    'Jogador do ano da liga':0,
    'Jogador do clube do ano': 0
    }

while True:
    liga = input('Ganhou qual liga nacional? ')
    copa = input('Ganhou qual copa nacional? ')
    if copa == 'Copa da Liga':
        copa_inglaterra = input('Ganhou outra?')
    continente = input('Ganhou qual copa continental? ')
    copa_america = input('Ganhou a copa américa?')
    copa_mundo = input('Ganhou a copa do mundo?')
    bola_ouro = input('Ganhou a bola de ouro?')
    jogador_clube = input('Ganhou o prêmio de jogador do clube?')
    jogador_ano = input('Ganhou o jogador do ano da liga?')


    # Adicionando liga nacional ao dicionário
    if liga != 'nenhuma':
        if liga:
            if liga in titulos:
                titulos[liga] += 1
            else:
                titulos[liga] = 1

    # Adicionando copa nacional ao dicionário
    if copa != 'nenhuma':
        if copa:
            if copa in titulos:
                titulos[copa] += 1
            else:
                titulos[copa] = 1

    # Adicionando copa da Inglaterra se Copa da Liga foi ganha
    if copa == 'Copa da Liga' and copa_inglaterra:
        if copa_inglaterra in titulos:
            titulos[copa_inglaterra] += 1
        else:
            titulos[copa_inglaterra] = 1

    if continente != 'nenhuma':
        if continente:
            if continente in titulos:
                titulos[continente] += 1
            else:
                titulos[continente] = 1
            
    # Adicionando Títulos por seleção
    if copa_america == 'sim':
        titulos['Copa América'] += 1
    

    if copa_mundo == 'sim':
        titulos['Copa do Mundo'] += 1
    
    # Prêmios individuais
    if bola_ouro == 'sim':
        titulos['Bola de Ouro'] += 1
    if jogador_clube == 'sim':
        titulos['Jogador do clube do ano'] += 1
    if jogador_ano == 'sim':
        titulos['Jogador do ano da liga'] += 1
        
    # Condição para encerrar o loop (pode ser ajustada conforme necessário)
    continuar = input("Deseja continuar?")
    if continuar == 'nao' or continuar == 'n':
        break
    
print(titulos)