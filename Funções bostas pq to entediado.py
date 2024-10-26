import random

def calcula_BMI(altura,peso):
    resultado = peso/((altura)**2)
    if resultado <= 18.6:
        frase = 'Você está abaixo do peso!'
    if 18.6 < resultado <= 24.9:
        frase = 'Você está saudável!'
    if 25<= resultado <= 30:
        frase = 'Você está acima do peso!'
    if resultado> 30:
        frase = 'Você está muito acima do peso! Procure um médico'
    print(f'Seu BMI foi de {resultado:.2f}.{frase}')
    return resultado


# import random
# passlen = int(input("enter the length of password"))
# s="abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
# p = "".join(random.sample(s,passlen ))
# print(p)

def soma(a,b)
    resultado = a + b
    return resultado