
def adicionar_tarefa(tarefas, nome_tarefa):
    tarefa = {
        'tarefa': nome_tarefa,
        'completada': False
    }
    tarefas.append(tarefa)
    print(f"Tarefa '{nome_tarefa}' adicionada com sucesso!")
    return

tarefas = []
while True:
    print("\nMenu do Gerenciador de Lista de Tarefas:")
    print("1. Adicionar Tarefa")
    print("2. Ver Tarefas")
    print("3. Atualizar Tarefa")
    print("4. Completar Tarefa")
    print("5. Sair")
    tarefas = []

    escolha = input("Escolha uma opção (1-5): ")

    if escolha == '1':
        nome_tarefa = input("Digite o nome da tarefa: ")
        adicionar_tarefa(tarefas, nome_tarefa)
    elif escolha == '5':
        print("Saindo do programa...")
        break

print("Programa encerrado.")