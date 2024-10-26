def romano_para_inteiro(s):
    numeros_romanos = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    total = 0
    valor_ant = 0

    for char in reversed(s):
        valor = numeros_romanos[char]
        if valor < valor_ant:
            total -= valor
        else:
            total += valor
        valor_ant = valor

    return total

def inteiro_para_romano(num):
    valores_int = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4,
        1
    ]
    simbolos_rom = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV",
        "I"
    ]
    algarismo = ''
    i = 0
    while num > 0:
        for _ in range(num // valores_int[i]):
            algarismo += simbolos_rom[i]
            num -= valores_int[i]
        i += 1
    return algarismo

def main():
    while True:
        print("Escolha uma opção:")
        print("1. Converter número romano para inteiro")
        print("2. Converter inteiro para número romano")
        print("3. Sair")
        escolha = input("Digite sua escolha (1/2/3): ")

        if escolha == '1':
            numero_romano = input("Digite um número romano: ").upper()
            print(f"Resultado: {romano_para_inteiro(numero_romano)}\n")
        elif escolha == '2':
            numero_inteiro = int(input("Digite um número inteiro: "))
            print(f"Resultado: {inteiro_para_romano(numero_inteiro)}\n")
        elif escolha == '3':
            break
        else:
            print("Escolha inválida. Tente novamente.\n")

if __name__ == "__main__":
    main()
