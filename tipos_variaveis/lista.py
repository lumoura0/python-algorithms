# Declaração

minha_lista = [1, 2, 3, 4, 5, "texto", True, 3.14]
# Acesso
print(minha_lista[0])  # Acessa o primeiro elemento

# Modificação
minha_lista[0] = 10  # Modifica o primeiro elemento
print(minha_lista)  # Exibe a lista modificada  
# Adição
minha_lista.append(6)  # Adiciona um novo elemento ao final da lista
print(minha_lista)  # Exibe a lista após a adição
print(minha_lista[-1])
print(minha_lista[1:3])  # Exibe os elementos do índice 1 ao 2 (exclusivo)
print(minha_lista[:6])  # Exibe os elementos do índice 1 até o final

# Métodos de listas
# Método append
minha_lista.append("novo elemento")  # Adiciona um novo elemento ao final da lista      
print(minha_lista)  # Exibe a lista após a adição

# Método index
indice = minha_lista.index(3.14)  # Encontra o índice do elemento 3.14
print(f"O índice do elemento 3.14 é: {indice}")  # Exibe o índice encontrado

# Método insert: insere um elemento em uma posição específica
minha_lista.insert(2, "inserido")  # Insere "inserido" no índice 2 
print(minha_lista)  # Exibe a lista após a inserção

# Método pop: remove e retorna o último elemento da lista
ultimo_elemento = minha_lista.pop()  # Remove o último elemento 
print(f"Último elemento removido: {ultimo_elemento}")  # Exibe o último elemento removido
# Exibe a lista após a remoção
print(minha_lista)  # Exibe a lista após a remoção

# Método remove: remove a primeira ocorrência de um elemento específico
minha_lista.remove("inserido")  # Remove o elemento "inserido"
print(minha_lista)  # Exibe a lista após a remoção do elemento "inserido"

# Método sort: ordena os elementos da lista
minha_lista_numerica = [5, 2, 9, 1, 5, 6]
minha_lista_numerica.sort()  # Ordena a lista numerica
print(minha_lista_numerica)  # Exibe a lista ordenada