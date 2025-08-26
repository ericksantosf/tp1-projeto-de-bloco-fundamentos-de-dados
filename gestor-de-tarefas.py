import datetime

tarefas = [
    {
        'id': 1,
        'descricao': 'Estudar Python',
        'data_criacao': datetime.date(2025, 8, 20),
        'status': 'Pendente',
        'prazo_final': datetime.date(2025, 8, 25),
        'urgencia': 'Alta'
    },
    {
        'id': 2,
        'descricao': 'Estudar banco de dados',
        'data_criacao': datetime.date(2025, 8, 24),
        'status': 'Pendente',
        'prazo_final': datetime.date(2025, 8, 25),
        'urgencia': 'Media'
    },
    {
        'id': 3,
        'descricao': 'Estudar lógica de programação',
        'data_criacao': datetime.date(2025, 8, 22),
        'status': 'Concluída',
        'prazo_final': datetime.date(2025, 8, 23),
        'urgencia': 'Baixa'
    }
]

def adicionar_tarefa(lista_tarefas: list, descricao: str, prazo_final: datetime.date = None, urgencia: str = 'Baixa'):
    """
    Adiciona uma nova tarefa à lista de tarefas.

    Gera um novo ID, define a data de criação e o status inicial.

    Args:
        lista_tarefas (list): A lista de dicionários onde as tarefas são armazenadas.
        descricao (str): A descrição da nova tarefa.
        prazo_final (datetime.date, optional): A data limite para a conclusão da tarefa. Padrão para None.
        urgencia (str, optional): O nível de urgência da tarefa ('Baixa', 'Media', 'Alta'). Padrão para 'Baixa'.

    Returns:
        dict: O dicionário da tarefa recém-adicionada.
    """
    novo_id = 1
    if lista_tarefas:
        novo_id = max(tarefa['id'] for tarefa in lista_tarefas) + 1

    nova_tarefa = {
        'id': novo_id,
        'descricao': descricao,
        'data_criacao': datetime.date.today(),
        'status': 'Pendente',
        'prazo_final': prazo_final,
        'urgencia': urgencia
    }
    lista_tarefas.append(nova_tarefa)
    return nova_tarefa

def listar_tarefas(lista_tarefas: list):
    """
    Exibe todas as tarefas da lista de forma formatada.

    Mostra detalhes como ID, descrição, status, prazo e urgência.

    Args:
        lista_tarefas (list): A lista de dicionários onde as tarefas estão armazenadas.
    """
    print("-" * 50)
    if not lista_tarefas:
        print("Nenhuma tarefa encontrada.")
        return

    print(f"{'ID':<4} | {'Status':<12} | {'Descrição':<40} | {'Prazo':<12} | {'Urgência':<10}")
    print("-" * 105)
    for tarefa in lista_tarefas:
        status_formatado = f"[{'X' if tarefa['status'] == 'Concluída' else ' '}] {tarefa['status']}"
        prazo_formatado = str(tarefa['prazo_final']) if tarefa['prazo_final'] else 'Não definido'
        print(f"{tarefa['id']:<4} | {status_formatado:<12} | {tarefa['descricao']:<40} | {prazo_formatado:<12} | {tarefa['urgencia']:<10}")
    print("-" * 105)

def marcar_como_concluida(lista_tarefas: list, tarefa_id: int):
    """
    Atualiza o status de uma tarefa para 'Concluída'.

    Args:
        lista_tarefas (list): A lista de dicionários onde as tarefas estão armazenadas.
        tarefa_id (int): O ID da tarefa a ser marcada como concluída.

    Returns:
        bool: True se a tarefa foi encontrada e atualizada, False caso contrário.
    """
    for tarefa in lista_tarefas:
        if tarefa['id'] == tarefa_id:
            if tarefa['status'] == 'Concluída':
                print(f"A tarefa com ID {tarefa_id} já está concluída.")
                return False
            tarefa['status'] = 'Concluída'
            return True
    return False

def remover_tarefa(lista_tarefas: list, tarefa_id: int):
    """
    Remove uma tarefa da lista.

    Args:
        lista_tarefas (list): A lista de dicionários onde as tarefas estão armazenadas.
        tarefa_id (int): O ID da tarefa a ser removida.

    Returns:
        bool: True se a tarefa foi encontrada e removida, False caso contrário.
    """
    for i, tarefa in enumerate(lista_tarefas):
        if tarefa['id'] == tarefa_id:
            del lista_tarefas[i]
            return True
    return False

def exibir_menu():
    """Exibe o menu de opções para o usuário."""
    print("\n--- Sistema de Gestão de Tarefas ---")
    print("1. Adicionar Tarefa")
    print("2. Listar Tarefas")
    print("3. Marcar Tarefa como Concluída")
    print("4. Remover Tarefa")
    print("5. Sair")
    print("-" * 37)

def main():
    """
    Função principal que gerencia o fluxo do programa.
    
    Apresenta o menu de opções em um loop e chama as funções apropriadas
    com base na escolha do usuário.
    """
    while True:
        exibir_menu()
        try:
            opcao = int(input("Escolha uma opção: "))

            if opcao == 1:
                descricao = input("Digite a descrição da nova tarefa: ")
                prazo_str = input("Digite o prazo final (AAAA-MM-DD), ou deixe em branco: ")
                urgencia = input("Digite a urgência (Baixa, Media, Alta), ou deixe em branco: ").capitalize()

                prazo_final = None
                if prazo_str:
                    try:
                        prazo_final = datetime.datetime.strptime(prazo_str, "%Y-%m-%d").date()
                    except ValueError:
                        print("Formato de data inválido. Prazo final não será definido.")

                adicionada = adicionar_tarefa(tarefas, descricao, prazo_final, urgencia if urgencia in ['Baixa', 'Media', 'Alta'] else 'Baixa')
                print(f"Tarefa '{adicionada['descricao']}' adicionada com sucesso! (ID: {adicionada['id']})")
            
            elif opcao == 2:
                listar_tarefas(tarefas)
            
            elif opcao == 3:
                try:
                    tarefa_id = int(input("Digite o ID da tarefa para marcar como concluída: "))
                    if marcar_como_concluida(tarefas, tarefa_id):
                        print(f"Tarefa com ID {tarefa_id} marcada como concluída!")
                    else:
                        print(f"Erro: Tarefa com ID {tarefa_id} não encontrada.")
                except ValueError:
                    print("Entrada inválida. Por favor, digite um número inteiro.")

            elif opcao == 4:
                try:
                    tarefa_id = int(input("Digite o ID da tarefa para remover: "))
                    if remover_tarefa(tarefas, tarefa_id):
                        print(f"Tarefa com ID {tarefa_id} removida com sucesso!")
                    else:
                        print(f"Erro: Tarefa com ID {tarefa_id} não encontrada.")
                except ValueError:
                    print("Entrada inválida. Por favor, digite um número inteiro.")

            elif opcao == 5:
                print("Saindo do sistema. Até mais!")
                break
            
            else:
                print("Opção inválida. Por favor, escolha uma opção de 1 a 5.")

        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")

if __name__ == "__main__":
    main()
    