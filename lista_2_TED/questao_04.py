# Questão 4 - Conversão de texto para número
# (solução complementar)
texto = input("Digite o preço do produto: ").strip().replace(",", ".")
try:
    preco = float(texto)
    if preco < 0:
        print("O preço não pode ser negativo.")
    else:
        qtd = int(input("Digite a quantidade: "))
        print(f"Total da compra: R$ {preco * qtd:.2f}")
except ValueError:
    print("Entrada inválida! Digite apenas números (ex: 10 ou 10.50).")
