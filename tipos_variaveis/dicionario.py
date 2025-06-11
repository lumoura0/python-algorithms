# Um dicionário é uma coleção não ordenada de pares chave-valor. 
# As chaves devem ser únicas e imutáveis, enquanto os valores podem ser de qualquer tipo.
# Dicionários são mutáveis, o que significa que você pode adicionar, remover ou alterar pares chave-valor.
# Exemplo de dicionário 
dicionario = {
    "nome": "Shiro",
    "idade": 30,
    "cidade": "São Paulo"
}
# Acessando valores
print(dicionario["nome"])  # Saída: Shiro
print(dicionario["idade"])  # Saída: 30 
print(dicionario["cidade"])  # Saída: São Paulo
# Adicionando um novo par chave-valor
dicionario["profissao"] = "Engenheiro"
# Acessando o novo valor
print(dicionario["profissao"])  # Saída: Engenheiro

# Removendo um par chave-valor
del dicionario["idade"]

print(dicionario)  # Saída: {'nome': 'Shiro', 'cidade': 'São Paulo', 'profissao': 'Engenheiro'}

# Métodos: keys(), values(), items()
chaves = dicionario.keys()  # Retorna as chaves do dicionário
print(chaves)  # Saída: dict_keys(['nome', 'cidade', 'profissao'])
print(list(chaves))  # Convertendo para lista: ['nome', 'cidade', 'profissao']

# Método values() retorna os valores do dicionário
valores = dicionario.values()  # Retorna os valores do dicionário
print(valores)  # Saída: dict_values(['Shiro', 'São Paulo', 'Engenheiro'])

# Método items() retorna os pares chave-valor do dicionário
itens = list(dicionario.items())  # Retorna os pares chave-valor do dicionário
print("Primeira chave-valor: %s = %s" % (itens[0][0],itens[0][1]))
# Saída: Primeira chave-valor: nome = Shiro
print("Segunda chave-valor: %s = %s" % (itens[1][0],itens[1][1]))
