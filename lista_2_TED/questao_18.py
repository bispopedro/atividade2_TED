# Questão 18 - Teste de caixa-preta
# (solução complementar)
# Regra: até R$ 100 sem desconto; acima de R$ 100, 10% de desconto.
def valor_final(valor):
    if valor < 0:
        raise ValueError("Valor negativo")
    return valor * 0.9 if valor > 100 else valor


# (entrada, esperado)
casos = [(50, 50), (100, 100), (100.01, 90.009), (200, 180), (0, 0)]
for entrada, esperado in casos:
    obtido = valor_final(entrada)
    print(entrada, esperado, round(obtido, 3),
          "Passou" if abs(obtido - esperado) < 0.001 else "Falhou")

try:
    valor_final(-10)
except ValueError:
    print("-10: entrada inválida tratada corretamente")
