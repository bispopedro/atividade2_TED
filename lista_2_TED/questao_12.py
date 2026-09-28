# Questão 12 - Lista com dados duplicados
nomes = ["Ana", "João", "Maria", "Ana", "Pedro", "João"]

duplicados = []

for nome in nomes:
    if nomes.count(nome) > 1 and nome not in duplicados:
        duplicados.append(nome)

if len(duplicados) > 0:
    print("Nomes repetidos:")
    for nome in duplicados:
        print(nome)
else:
    print("Não existem nomes repetidos.")
