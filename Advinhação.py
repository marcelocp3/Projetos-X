import random


print('Vamos escolher um número aleatório entre 1 e 100, e você deve acertar em menos de 10 tentativas!')
numero = random.randint(1,100)
palpite = int(input('Qual o seu palpite? '))
tentativas = 1
while palpite != numero or tentativas <= 10:
    if 1 <= abs(numero - palpite) <= 10:
        print('Muito quente!')
    if 10 < abs(numero - palpite) <= 30:
        print('Esquentando')
    if 30 < abs(numero - palpite) <= 50:
        print('Morno')
    if 50 < abs(numero - palpite) <= 70:
        print('Frio')
    if 70 < abs(numero - palpite) < 100:
        print('Muito frio')
    if palpite == numero:
        break
    tentativas += 1
    palpite = int(input('Qual o seu palpite? '))

if palpite == numero:
    print(f'Você acertou em {tentativas} tentativas!')
    print(f'O número era {numero}')

if palpite != numero and tentativas > 10:
    print('Você perdeu')
    print(f'O número era {numero}')
