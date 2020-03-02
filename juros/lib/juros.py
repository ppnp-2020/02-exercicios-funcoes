def calcular_montante(capital, taxa, tempo):
  return capital * (1 + taxa) ** tempo

def calcular_lucro(capital, taxa, tempo):
  return calcular_montante(capital, taxa, tempo) - capital

