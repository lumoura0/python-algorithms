# Declaração
texto = "Olá, Mundo!"
# Exibição
print(texto)
# Exibição do tipo da variável
print(type(texto))
# Exibição do tamanho da variável
print(len(texto))
# Exibição do primeiro caractere
print(texto[0])
# Exibição do último caractere  
print(texto[-1])
nome = """
Shiro
"""
print(nome)

# Formatação de strings
nome = "Shiro"
sobrenome = "Kuro"
# Exibição com concatenação
print("Meu nome é " + nome + " " + sobrenome)
# Exibição com formatação f-string
print(f"Meu nome é {nome} {sobrenome}")
# Exibição com método format
print("Meu nome é {} {}".format(nome, sobrenome))
# Exibição com método format com índice
print("Meu nome é {0} {1}".format(nome, sobrenome))
# Exibição com método format com nome
print("Meu nome é {n} {s}".format(n=nome, s=sobrenome))

# Declaração
nome_completo = "Shiro Luna"

nome_completo_aspas = """Shiro Luna"""

nome_completo_quebra = "Shiro \ Luna"

nome = "Shiro"
sobrenome = "Luna"

# Formação
print("Nome completo (1a forma):", nome_completo)
print("Nome completo (2a forma):" + nome_completo)
print("Nome completo (3a forma):" + "Gabriel" + "Casemiro")
print("Nome completo (4a forma):" + "Gabriel", "Casemiro")
print("Nome completo (5a forma):", nome_completo_aspas)
print("Nome completo (6a forma):", nome_completo_quebra)
print("Nome completo (7a forma): %s" % nome_completo)
print("Nome completo (8a forma): %s %s" % (nome, sobrenome))
print(f"Nome completo (9a forma): {nome} {sobrenome}")
print("Nome completo (10a forma): {} {}".format(sobrenome, nome))