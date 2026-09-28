# Questão 10 - Laço de repetição que não termina
n = int(input("informe um numero: "))
while n != 0:
    print(n)
    n = int(input("informe um numero: "))

# O problema identificado é que, após pôr o sistema para mostrar o valor
# digitado, não há um comando para pedir outro número para dar continuidade
# ao loop, levando a variável a guardar apenas o primeiro valor, o que faz o
# sistema entrar em outro loop.
