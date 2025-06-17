# Funções - Bloco de código reutilizável
# Def - Definição de uma função
# Funções são blocos de código reutilizáveis que podem ser chamados em diferentes partes do programa.

# Exemplo
def saudacao(nome):
    """Função que imprime uma saudação personalizada."""
    print(f"Olá, {nome}! Bem-vindo ao Python Rocket.")

# Chamada da função
saudacao("Luís")

# Exemplo de função com retorno
def quadrado(numero):
    """Função que retorna o quadrado de um número."""
    return numero ** 2
# Chamada da função e impressão do resultado
resultado = quadrado(5)
print(f"O quadrado de 5 é {resultado}.")

# Exemplo de função com parâmetros padrão
def saudacao_personalizada(nome, saudacao="Olá"):
    """Função que imprime uma saudação personalizada com um parâmetro padrão."""
    print(f"{saudacao}, {nome}! Bem-vindo ao Python Rocket.")

# Chamada da função com e sem o parâmetro padrão
saudacao_personalizada("Luís")  
saudacao_personalizada("Luís", "Bom dia")

# Exemplo de função com múltiplos parâmetros
def soma(a, b):
    """Função que retorna a soma de dois números."""
    return a + b
# Chamada da função e impressão do resultado
resultado_soma = soma(3, 4)