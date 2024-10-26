def imprime_jogo(jogo):
    for linha in jogo:
        print(" ".join(str(num) for num in linha))

def encontra_vazio(jogo):
    for i in range(len(jogo)):
        for j in range(len(jogo[0])):
            if jogo[i][j] == 0:
                return(i,j)
    return None

def posicao_valida(jogo,num,pos):
    for i in range(len(jogo[0])):
        if jogo[pos[0]][i] == num and pos[1] != i:
            return False
        
    for i in range(len(jogo)):
        if jogo[i][pos[1]] == num and pos[0] != i:
            return False
        
    jogo_x = pos[1]//3
    jogo_y = pos[0]//3

    for i in range(jogo_y*3,jogo_y*3 + 3):
        for j in range(jogo_x*3, jogo_x*3 +3):
            if jogo[i][j] == num and (i,j) != pos:
                return False
            
    return True

def resolve(jogo):
    encontra = encontra_vazio(jogo)
    if not encontra:
        return True
    else:
        linha, coluna = encontra

    for i in range(1,10):
        if posicao_valida(jogo,i,(linha,coluna)):
            jogo[linha][coluna] = i

            if resolve(jogo):
                return True
            
            jogo[linha][coluna] = 0

    return False

jogo = [
    [0, 0, 0, 0, 0, 7, 0, 0, 3],
    [0, 0, 0, 9, 1, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 3, 2, 0, 4],
    [0, 8, 0, 1, 0, 0, 0, 7, 0],
    [0, 0, 0, 0, 0, 0, 0, 6, 0],
    [2, 0, 0, 0, 0, 4, 0, 0, 0],
    [0, 0, 6, 8, 0, 0, 0, 0, 0],
    [0, 5, 0, 0, 0, 0, 0, 0, 6],
    [0, 7, 3, 2, 0, 0, 0, 9, 0]
]

resolve(jogo)
print("Tabuleiro Resolvido: ")
imprime_jogo(jogo)