from lib.console import solicitar_numero
from lib.juros import calcular_montante, calcular_lucro


valor = solicitar_numero('Digite o valor para investimento: ')

juros_poupanca = 0.005
juros_cdb = 0.007

print('Poupança:')

print('12 meses: R$ ', calcular_montante(valor, juros_poupanca, 12))
print('24 meses: R$ ', calcular_montante(valor, juros_poupanca, 24))
print('36 meses: R$ ', calcular_montante(valor, juros_poupanca, 36))

print('CDB:')

print('12 meses: R$ ', calcular_montante(valor, juros_cdb, 12))
print('24 meses: R$ ', calcular_montante(valor, juros_cdb, 24))
print('36 meses: R$ ', calcular_montante(valor, juros_cdb, 36))
