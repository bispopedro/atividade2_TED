# Questão 8 - Erro de lógica em média
# Problema identificado: A fórmula da média está incorreta, provavelmente por
# erro na ordem das operações (ex.: nota1 + nota2 + nota3 / 3).
# Algoritmo/estratégia: Somar as três notas primeiro e depois dividir por 3.
nota1 = float(input("Nota 1: "))
nota2 = float(input("Nota 2: "))
nota3 = float(input("Nota 3: "))

media = (nota1 + nota2 + nota3) / 3
print("Média:", media)
