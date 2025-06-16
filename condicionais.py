# Condição
# if, else, elif
idade = 19
if idade < 18:
    print("Menor de idade") 
elif idade == 18:
    print("Tem 18 anos")
else:
    print("Maior de idade")

if idade <= 18:
    print("Menor de idade")

mensagem = "Menor de idade" if idade < 18 else "Maior de idade"     
print(mensagem)
# Operadores lógicos    
# and, or, not
idade = 19
if idade < 18 and idade > 0:
    print("Menor de idade") 
if idade < 18 or idade > 60:
    print("Menor de idade ou maior de 60 anos") 
if not idade < 18:
    print("Maior de idade")


mens = int(input("Digite um número: "))
if mens % 2 == 0:
    print("O número é par")
else:
    print("O número é ímpar")