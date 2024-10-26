from datetime import date
import calendar

# Recebe a data atual
data_atual = date.today()
dia = data_atual.day
mes = data_atual.month
ano = data_atual.year

# Recebe o dia da semana atual
semana = str(input('Qual dia da semana é hoje? ')).lower()
dias_semana = ['segunda', 'terça', 'quarta', 'quinta', 'sexta', 'sabado', 'domingo']

# Verifica se a entrada é válida
if semana not in dias_semana:
    print("Dia da semana inválido.")
    exit()

# Mapeia o dia da semana atual para um índice
indice_semana = dias_semana.index(semana)

# Recebe a data desejada
dia_desejado = int(input('Para qual dia quer ir? '))
mes_desejado = int(input('Para qual mês deseja ir? '))
ano_desejado = int(input('Para qual ano quer ir? '))

# Cria a data desejada
data_desejada = date(ano_desejado, mes_desejado, dia_desejado)

# Calcula a diferença de dias entre as duas datas
diferenca_dias = (data_desejada - data_atual).days

# Calcula o dia da semana para a data desejada
indice_dia_desejado = (indice_semana + diferenca_dias) % 7
dia_da_semana_desejado = dias_semana[indice_dia_desejado]

if ano_desejado > ano:
    print(f"O dia {dia_desejado}/{mes_desejado}/{ano_desejado} será um(a) {dia_da_semana_desejado}.")
if ano_desejado < ano:
    print(f"O dia {dia_desejado}/{mes_desejado}/{ano_desejado} foi um(a) {dia_da_semana_desejado}.")
if ano_desejado == ano:
    if mes_desejado > mes:
        print(f"O dia {dia_desejado}/{mes_desejado}/{ano_desejado} será um(a) {dia_da_semana_desejado}.")
    elif mes_desejado < mes:
        print(f"O dia {dia_desejado}/{mes_desejado}/{ano_desejado} foi um(a) {dia_da_semana_desejado}.")
    else:
        if dia_desejado < dia:
            print(f"O dia {dia_desejado}/{mes_desejado}/{ano_desejado} foi um(a) {dia_da_semana_desejado}.")
        if dia_desejado > dia:
            print(f"O dia {dia_desejado}/{mes_desejado}/{ano_desejado} será um(a) {dia_da_semana_desejado}.")
        else:
            print('É hoje')
        
