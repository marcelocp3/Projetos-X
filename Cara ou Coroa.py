import random



cara = "cara"
coroa = "coroa"

sorteio = random.randint(0,1)

if sorteio == 0:
    resultado = cara
else:
    resultado = coroa

print(f'O resultado foi {resultado}')
