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