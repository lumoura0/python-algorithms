# Exceções Try catch
def divisao(a, b):
    try:
        resultado = a / b
    except ZeroDivisionError:
        print("Erro: Divisão por zero não é permitida.")
        return None
    except TypeError:
        print("Erro: Tipos de dados inválidos para divisão.")
        return None
    else:
        return resultado

# Exemplo de uso
if __name__ == "__main__":
    print(divisao(10, 2))  # Saída: 5.0
    print(divisao(10, 0))  # Saída: Erro: Divisão por zero não é permitida.
    print(divisao(10, "a"))  # Saída: Erro: Tipos de dados inválidos para divisão.
    print(divisao("10", 2))  # Saída: Erro: Tipos de dados inválidos para divisão.
    print(divisao(10, 5))  # Saída: 2.


print("Exemplo de captura de exceção")
try:
    numero = int(input("Digite um número: "))
    resultado = 10 / numero
    print(f"Resultado: {resultado}")
except ValueError as e:
    print(f"Erro de value error: {e}")
except Exception as e:
    print(f"Erro: {e}")
else:
    print("Divisão realizada com sucesso!")
finally:
    print("Fim do bloco try-except.")