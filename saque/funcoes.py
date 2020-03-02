saldo = 1000
numero_conta = '1234-5'
senha_conta = '112233'


def efetuar_saque():
  valor = input('Digite o valor desejado: ')

  if not valor.isnumeric():
    print('O valor digitado é inválido')
    return

  valor = float(valor)

  if valor <= saldo:
    print('Saque efetuado')
  else:
    print('Saldo insuficiente')


def autenticar(conta_informada, senha_informada):
  if numero_conta == conta_informada or senha_conta == senha_informada:
    print('Acessando a conta...')
    return True
  else:
    print('Crendenciais inválidas')
    return False




