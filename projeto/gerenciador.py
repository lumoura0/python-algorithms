while True:
    print("\nMenu do Gerenciador de Lista de Tarefas:")
    print("1. Adicionar Tarefa")
    print("2. Ver Tarefas")
    print("3. Atualizar Tarefa")
    print("4. Completar Tarefa")
    print("5. Sair")
    tarefas = []

    escolha = input("Escolha uma opção (1-5): ")

    if escolha == '6':
        print("Saindo do programa...")
        break

print("Programa encerrado.")