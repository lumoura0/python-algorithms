# Tuplas
# Tuplas são coleções ordenadas e imutáveis de elementos
# Tuplas são definidas com parênteses   
# Tuplas podem conter elementos de diferentes tipos
tupla = (1, 2, 2, 3, 4, 5)
# Tuplas podem ser acessadas por índice
print(tupla[0])  # Acessa o primeiro elemento
print(tupla[1])  # Acessa o segundo elemento
print(tupla[-1])  # Acessa o último elemento

# Método count() conta quantas vezes um elemento aparece na tupla
print("Quantidade de vezes que aparece:", tupla.count(2))  # Conta quantas vezes o número 2 aparece na tupla

indice = tupla.index(3)  # Encontra o índice do primeiro elemento igual a 3
print("Índice do elemento 3:", indice)  # Imprime o índice do elemento 3