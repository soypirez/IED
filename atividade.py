import datetime  # Importa o módulo datetime para usar a data e hora atuais

tarefas = []  # Lista principal onde as tarefas são armazenadas
historico = []  # Pilha para armazenar tarefas adicionadas (para desfazer)
fila_execucao = []  # Fila para controlar a ordem de atendimento das tarefas

ARQUIVO_TAREFAS = "tarefas.txt"  # Nome do arquivo onde as tarefas serão salvas

def salvar_em_arquivo(): # Função para salvar as tarefas no arquivo de texto
    with open(ARQUIVO_TAREFAS, "w", encoding="utf-8") as f:  # Abre o arquivo para escrita
        for tarefa in tarefas:  # Para cada tarefa na lista de tarefas
            f.write(f"{tarefa['descricao']} | Prioridade: {tarefa['prioridade']} | Data: {tarefa['data']}\n")  # Escreve a tarefa no arquivo

def adicionar_tarefa(descricao, prioridade): # Função para adicionar uma nova tarefa
    data = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Pega a data e hora atuais no formato desejado
    tarefa = {  # Cria um dicionário com os dados da tarefa
        "descricao": descricao,  # Descrição da tarefa
        "prioridade": prioridade,  # Prioridade da tarefa
        "data": data  # Data e hora de criação da tarefa
    }
    tarefas.append(tarefa)  # Adiciona a tarefa à lista principal
    historico.append(tarefa)  # Adiciona a tarefa ao histórico (pilha)
    fila_execucao.append(tarefa)  # Adiciona a tarefa à fila de execução
    salvar_em_arquivo()  # Salva as tarefas no arquivo
    print(f"Tarefa '{descricao}' adicionada com prioridade {prioridade}!\n")  # Mensagem de confirmação

def desfazer_ultima_tarefa(): # Função para desfazer a última tarefa adicionada
    if historico:  # Verifica se há tarefas no histórico
        ultima = historico.pop()  # Remove a última tarefa adicionada
        tarefas.remove(ultima)  # Remove a tarefa da lista principal
        fila_execucao.remove(ultima)  # Remove a tarefa da fila
        salvar_em_arquivo()  # Salva o novo estado no arquivo
        print(f"Tarefa '{ultima['descricao']}' desfeita!\n")  # Mensagem de confirmação
    else:
        print("Nenhuma tarefa para desfazer.\n")  # Mensagem caso não haja tarefas a desfazer

def atender_tarefa(): # Função para atender (remover) a primeira tarefa da fila
    if fila_execucao:  # Verifica se há tarefas na fila
        feita = fila_execucao.pop(0)  # Remove a primeira tarefa da fila (modo FIFO)
        tarefas.remove(feita)  # Remove a tarefa da lista principal
        salvar_em_arquivo()  # Salva o novo estado no arquivo
        print(f"Tarefa '{feita['descricao']}' atendida!\n")  # Mensagem de confirmação
    else:
        print("Nenhuma tarefa para atender.\n")  # Mensagem caso não haja tarefas na fila

def mostrar_tarefas(): # Função para exibir todas as tarefas cadastradas
    if not tarefas:  # Verifica se a lista de tarefas está vazia
        print("\nNenhuma tarefa registrada.\n")  # Mensagem se não houver tarefas
        return  # Sai da função
    print("\nLista de Tarefas:")  # Título da lista
    for i, t in enumerate(tarefas):  # Percorre todas as tarefas com índice
        print(f"{i + 1}. {t['descricao']} | Prioridade: {t['prioridade']} | Adicionada em: {t['data']}")  # Mostra os dados da tarefa
    print()  # Linha em branco no final da lista

while True: # Loop principal do programa
    print("1. Adicionar Tarefa")  # Opção 1 do menu
    print("2. Desfazer Última Tarefa")  # Opção 2 do menu
    print("3. Atender Tarefa (modo fila)")  # Opção 3 do menu
    print("4. Mostrar Tarefas")  # Opção 4 do menu
    print("5. Sair")  # Opção 5 do menu

    opcao = input("Escolha uma opção: ")  # Pede ao usuário para escolher uma opção

    if opcao == '1':  # Se o usuário escolher adicionar tarefa
        descricao = input("Digite a descrição da tarefa: ")  # Pede a descrição
        prioridade = input("Digite a prioridade (Alta/Média/Baixa): ")  # Pede a prioridade
        adicionar_tarefa(descricao, prioridade.capitalize())  # Adiciona a tarefa, capitalizando a prioridade
    elif opcao == '2':  # Se escolher desfazer
        desfazer_ultima_tarefa()  # Chama a função para desfazer
    elif opcao == '3':  # Se escolher atender
        atender_tarefa()  # Chama a função para atender
    elif opcao == '4':  # Se escolher mostrar tarefas
        mostrar_tarefas()  # Chama a função para mostrar
    elif opcao == '5':  # Se escolher sair
        print("Saindo do programa...")  # Mensagem de saída
        break  # Sai do loop
    else:
        print("Opção inválida!\n")  # Mensagem para entrada inválida
