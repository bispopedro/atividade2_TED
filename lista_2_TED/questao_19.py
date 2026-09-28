# Questão 19 - Teste de caixa-branca
def verificar_usuario(idade, renda, cadastro):

    if idade < 18:
        return "Usuário menor de idade."

    elif renda < 1500:
        return "Usuário maior de idade, mas possui renda baixa."

    elif cadastro == "inativo":
        return "Usuário maior de idade, renda suficiente, mas cadastro inativo."

    else:
        return "Usuário aprovado."


# Teste 1
print("Teste 1:")
print(verificar_usuario(16, 2000, "ativo"))

# Teste 2
print("\nTeste 2:")
print(verificar_usuario(20, 1000, "ativo"))

# Teste 3
print("\nTeste 3:")
print(verificar_usuario(20, 2000, "inativo"))

# Teste 4
print("\nTeste 4:")
print(verificar_usuario(20, 2000, "ativo"))
