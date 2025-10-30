import json
from datetime import datetime


tarefas = []

def Criar_Tarefa():

    descricao = input("\nDescreva Sua Tarefa: ")
    
    JsonString ={
            'id': len(tarefas) +1,
            'Descrição': descricao,
            'Status': 'Todo',
            'Data de Criação': datetime.today().strftime('%d/%m/%Y')
            }
    
    tarefas.append(JsonString)
    
    with open('tarefas.json', 'w', encoding='utf8', newline= '\n') as f:
        json.dump(tarefas, f, indent=4, ensure_ascii=False)

    print(f'\nTarefa adicionada com sucesso\n')

    main()
    return

def Listar_tarefas():

    for i in range(len(tarefas)):
        print(tarefas[i])

    main()
    return

def Atualizar_tarefa():
    print('\nselecione o ID de uma tarefa: ')

    for i in range(len(tarefas)):
        print(tarefas[i])

    IndiceSelecionado = int(input('')) -1
    TarefaSelecionada = tarefas[IndiceSelecionado]
    TarefaSelecionada['Descrição'] = input("Coloque a nova descrição: ")
    TarefaSelecionada['Data de Atualização'] = "Atualizado pela ultima vez em: " + datetime.today().strftime('%d/%m/%Y %H:%M:%S')

    print("\nDescrição alterada com sucesso\n")

    main()
    return

def main():
    opcao = input("""Selecione o que deseja fazer:             
    add - Criar uma tarefa
    att - Atualizar uma tarefa
    del - Deletar uma tarefa
    lst - Listar todas as tarefas\n
    """)
    
    match opcao:
        case 'add': Criar_Tarefa()
        case 'att': Atualizar_tarefa()
        case 'lst': Listar_tarefas()

main()