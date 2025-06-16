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