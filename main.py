import json
from datetime import datetime

def Ler_tarefas():
    try:
        with open('tarefas.json', 'r', encoding='utf-8') as tasks:
            tarefasAtuais = json.load(tasks)
            
            for i in range(len(tarefasAtuais)):
                print(tarefasAtuais[i])
        return tarefasAtuais
    except: 
        print('Não ha tarefas no arquivo')
        return


def Criar_Tarefa():
    tarefas_arquivo = Ler_tarefas()

    if tarefas_arquivo == None:
        # tarefas_arquivo = 0
        tarefas = []
        print(f'Existem estas tarefas na lista vazia: {tarefas}')
    else:
        # print(f'a função Ler_tarefas() retorna -> {tarefas_arquivo}')
        print(f'Existem {len(tarefas_arquivo)} tarefas no arquivo')
        tarefas = list(tarefas_arquivo)
        print(f'Existem estas tarefas na lista: {tarefas}')
        

    descricao = input("\nDescreva Sua Tarefa: ")
    
    JsonString ={
            'id': len(tarefas) +1,
            'Descrição': descricao,
            'Status': 'Todo',
            'Data de Criação': datetime.today().strftime('%d/%m/%Y')
            }
    
    tarefas.append(JsonString)
    
    with open('tarefas.json', 'w', encoding='utf8') as tasks:
        json.dump(tarefas, tasks, indent=4, ensure_ascii=False)

    print(f'\nTarefa adicionada com sucesso\n')

    main()
    return

def Listar_tarefas():

    with open('tarefas.json', 'r', encoding='utf-8') as tasks:
        tarefasAtuais = json.load(tasks)
        
        for i in range(len(tarefasAtuais)):
            print(tarefasAtuais[i])

    main()

def Atualizar_tarefa():
    print('\nselecione o ID de uma tarefa: ')

    with open('tarefas.json', 'r', encoding='utf-8') as tasks:
        tarefasAtuais = json.load(tasks)
        
        for i in range(len(tarefasAtuais)):
            print(tarefasAtuais[i])

        IndiceSelecionado = int(input('')) -1

        print(f'\nTarefa selecionada: {tarefasAtuais[IndiceSelecionado]}')
        print(f'Descrição da tarefa selecionada: {tarefasAtuais[IndiceSelecionado]["Descrição"]} \n')

        novaDescricao = input("Coloque a nova descrição: ")
        
        tarefasAtuais[IndiceSelecionado]['Descrição'] = novaDescricao
        tarefasAtuais[IndiceSelecionado]['Data de Atualização'] = "Atualizado pela ultima vez em: " + datetime.today().strftime('%d/%m/%Y %H:%M:%S')

        print(f'\nNova descrição: {novaDescricao}')
        print(f'{tarefasAtuais[IndiceSelecionado]["Data de Atualização"]}\n')

    with open('tarefas.json', 'w', encoding='utf-8') as tasks:
        json.dump(tarefasAtuais, tasks, indent=4, ensure_ascii=False)
    
    print(f"\nDescrição alterada com sucesso para: {novaDescricao}\n")

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