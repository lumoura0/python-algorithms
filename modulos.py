print("Exemplo de importação de um módulo padrão!")
import math
print("O valor de pi é:", math.pi)

raiz_quadrada = math.sqrt(16)
print("A raiz quadrada de 16 é:", raiz_quadrada)

# Exemplo de importação de um módulo personalizado
# import meu_modulo
from meu_modulo import saudacao, dobro
print("Exemplo de importação de um módulo personalizado!")
mensagem = saudacao("Shiro")
print(mensagem)

dobro = dobro(5)
print("O dobro de 5 é:", dobro)