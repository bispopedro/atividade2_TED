# Questão 20 - Projeto final: cadastro de alunos (versão corrigida)
# (solução complementar)
def ler_float(msg, minimo, maximo):
    while True:
        try:
            valor = float(input(msg).replace(",", "."))
            if minimo <= valor <= maximo:
                return valor
            print(f"Digite um valor entre {minimo} e {maximo}.")
        except ValueError:
            print("Entrada inválida! Digite um número.")


def situacao(media):
    if media >= 7:
        return "Aprovado"
    elif media >= 5:
        return "Recuperação"
    return "Reprovado"


alunos = []
while True:
    nome = input("Nome (vazio para sair): ").strip()
    if nome == "":
        break
    idade = int(ler_float("Idade: ", 1, 120))
    notas = [ler_float(f"Nota {i}: ", 0, 10) for i in (1, 2, 3)]
    media = sum(notas) / 3
    alunos.append((nome, idade, media, situacao(media)))

for nome, idade, media, sit in alunos:
    print(f"{nome} ({idade} anos) - média {media:.1f} - {sit}")
