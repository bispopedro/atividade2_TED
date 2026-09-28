# Questão 16 - Arquivo inexistente
# (solução complementar)
try:
    with open("alunos.txt", "r", encoding="utf-8") as arquivo:
        print(arquivo.read())
except FileNotFoundError:
    print("Erro: o arquivo 'alunos.txt' não foi encontrado.")
    print("Crie o arquivo na mesma pasta do programa e tente novamente.")
