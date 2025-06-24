def adicionar_tarefa(tarefas, nome_tarefa):
  # tarefa: nome da tarefa
  # completada: indicar se essa tarefa ja foi completada ou nao
  tarefa = {"tarefa": nome_tarefa, "completada": False}
  tarefas.append(tarefa)
  print(f"Tarefa {nome_tarefa} foi adicionada com sucesso!")
  return

def ver_tarefas(tarefas):
  print("\nLista de tarefas:")
  for indice, tarefa in enumerate(tarefas, start=1):
    status = "✓" if tarefa["completada"] else " "
    nome_tarefa = tarefa["tarefa"]
    print(f"{indice}. [{status}] {nome_tarefa}")
  return

def atualizar_nome_tarefa(tarefas, indice_tarefa, novo_nome):
    print(f"Tarefa {indice_tarefa + 1} atualizada para '{novo_nome}'")
    # Verifica se o índice da tarefa é válido
    if 0 <= indice_tarefa < len(tarefas):
        tarefas[indice_tarefa]["tarefa"] = novo_nome
        print(f"Tarefa {indice_tarefa + 1} atualizada para '{novo_nome}'")
    else:
        print("Índice inválido. Tarefa não encontrada.")

    return


tarefas = []
while True:
  print("\nMenu do Gerenciador de Lista de tarefas:")
  print("1. Adicionar tarefa")
  print("2. Ver tarefas")
  print("3. Atualizar Tarefas")
  print("4. Completar Tarefas")
  print("5. Deletar tarefas completadas")
  print("6. Sair")

  escolha = input("Digite a sua escolha: ")

  if escolha == "1":
    nome_tarefa = input("Digite o nome da tarefa que deseja adicionar: ")
    adicionar_tarefa(tarefas, nome_tarefa)
  elif escolha == "2":
    ver_tarefas(tarefas)
  elif escolha == "3":
    ver_tarefas(tarefas)
    # Solicita o índice da tarefa a ser atualizada
    indice_tarefa = int(input("Digite o número da tarefa que deseja atualizar: ")) - 1
    novo_nome = input("Digite o novo nome da tarefa: ")
    atualizar_nome_tarefa(tarefas, indice_tarefa, novo_nome)
  elif escolha == "6":
    break

print("Programa finalizado")