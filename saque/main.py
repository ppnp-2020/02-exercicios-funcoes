from funcoes import autenticar, efetuar_saque


conta = input('Digite o número da conta: ')
senha = input('Digite a senha: ')

if autenticar(conta, senha):
  efetuar_saque()
