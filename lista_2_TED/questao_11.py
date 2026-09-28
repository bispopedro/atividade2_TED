# Questão 11 - Contagem incorreta em um laço
# (solução complementar)
n = int(input("Informe N: "))
contador = 0
for i in range(1, n + 1):   # inclui o N
    if i % 2 == 0:
        contador += 1
print(f"Existem {contador} números pares entre 1 e {n}.")
