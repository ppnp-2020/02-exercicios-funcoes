from lib.console import solicitar_numero
from lib.juros import calcular_montante, calcular_lucro


valor = solicitar_numero('Digite o valor para investimento: ')
juros = solicitar_numero('Digite a taxa de juros (%): ')
meses = solicitar_numero('Digite a quantidade de meses: ')

juros = juros / 100

montante = calcular_montante(valor, juros, meses)
lucro = calcular_lucro(valor, juros, meses)

print(f'O valor ao final do período será de R$ {montante}')
print(f'O lucro obtido será R$ {lucro}')
