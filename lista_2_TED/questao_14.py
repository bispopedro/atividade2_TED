# Questão 14 - Tratamento de dados ausentes
# (solução complementar)
entrada = input("Preço do produto: ")

if entrada.strip() == "":
    print("Erro: o preço não foi informado.")
else:
    try:
        preco = float(entrada.replace(",", "."))
        print(f"Preço com 10% de imposto: R$ {preco * 1.10:.2f}")
    except ValueError:
        print("Erro: informe um número válido.")
