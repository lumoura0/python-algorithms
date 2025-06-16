lista = [1,2,3,4,5,6,7,8,9,10]
for i in lista:
    if i % 2 == 0:
        print(f"{i} é par")
    else:
        print(f"{i} é ímpar")
print("\nFim da lista")


pessoa = {
    "nome": "Luís",
    "idade": 18,
    "altura": 1.75
}
for chave, valor in pessoa.items():
    print(f"{chave}: {valor}")

# range() é uma função que gera uma sequência de números
print("\nUsando a função range() para números de 1 a 10:")
for i in range(1, 11):
    if i % 2 == 0:
        print(f"{i} é par")
    else:
        print(f"{i} é ímpar")

# range() com len() para iterar sobre uma lista
print("\nUsando range() com len() para iterar sobre uma lista:")
lista_nomes = [1, 2, 3, 4, 5]   
for i in range(0, len(lista_nomes)):
    print(f"Índice {i}: {lista_nomes[i]}")

# enumerate() para obter índice e valor
print("\nUsando enumerate() para obter índice e valor:")
for i, valor in enumerate(lista_nomes):
    print(f"Índice {i}: {valor}")