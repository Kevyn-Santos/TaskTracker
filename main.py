import json
from datetime import datetime

def Ler_tarefas():
    try:
        with open('tarefas.json', 'r', encoding='utf-8') as tasks:
            return json.load(tasks)
    except (json.JSONDecodeError, FileNotFoundError):
        print('Não ha tarefas no arquivo ou ele esta corrompido')
        return []

def gravar_tarefas(tasks):

    with open('tarefas.json', 'w', encoding='utf8') as f:
        json.dump(tasks, f, indent=4, ensure_ascii=False)
    return

def Criar_Tarefa():
    tarefas_arquivo = Ler_tarefas()

    descricao = input("\nDescreva Sua Tarefa: ")
    
    JsonString ={
            'id': len(tarefas_arquivo) +1,
            'Descrição': descricao,
            'Status': 'Todo',
            'Data de Criação': datetime.today().strftime('%d/%m/%Y')
            }
    
    tarefas_arquivo.append(JsonString)
    gravar_tarefas(tarefas_arquivo)

    print(f'\nTarefa adicionada com sucesso\n')
    return

def Listar_tarefas():
    tarefasAtuais = Ler_tarefas()

    if tarefasAtuais is None or len(tarefasAtuais) == 0:
        print('Não ha tarefas para listar\n')
    else:
        for i in range(len(tarefasAtuais)):
            print(tarefasAtuais[i])

def Atualizar_tarefa():
    tarefasAtuais = Ler_tarefas()

    for i in range(len(tarefasAtuais)):
        print(tarefasAtuais[i])

    IndiceSelecionado = int(input('\nselecione o ID de uma tarefa: ')) -1
    print(f'\nTarefa selecionada: {tarefasAtuais[IndiceSelecionado]}')
    print(f'Descrição da tarefa selecionada: {tarefasAtuais[IndiceSelecionado]["Descrição"]} \n')

    novaDescricao = input("Coloque a nova descrição: ")

    tarefasAtuais[IndiceSelecionado]['Descrição'] = novaDescricao
    tarefasAtuais[IndiceSelecionado]['Data de Atualização'] = "Atualizado pela ultima vez em: " + datetime.today().strftime('%d/%m/%Y %H:%M:%S')

    gravar_tarefas(tarefasAtuais)
    print(f"Descrição alterada com sucesso para: {novaDescricao}\n")
    return

def Excluir_tarefa():
    tarefas_atuais = Ler_tarefas()

    if tarefas_atuais is None or len(tarefas_atuais) == 0:
        print('Não ha tarefas para excluir')
        return
    else:
        for i in range(len(tarefas_atuais)):
            print(tarefas_atuais[i])

        tarefa_selecionada = int(input('selecione o ID de uma tarefa para excluir: ')) -1

        if input(f'''\nVocê realmente deseja excluir a tarefa: \n{tarefas_atuais[tarefa_selecionada]} ? s/n ''').strip().lower() == 's':

            del tarefas_atuais[tarefa_selecionada]
            for tarefas in tarefas_atuais:
                tarefas['id'] = tarefas['id'] - 1

            gravar_tarefas(tarefas_atuais)
            print('Tarefa excluida com sucesso\n')
        else:
            print('tarefa não excluida\n')
            return

def main():
    while True:
        opcao = input("""Selecione o que deseja fazer:             
        add - Criar uma tarefa
        att - Atualizar uma tarefa
        del - Deletar uma tarefa
        lst - Listar todas as tarefas
        q - Sair\n
        """).strip().lower()
        match opcao:
            case 'add': Criar_Tarefa()
            case 'att': Atualizar_tarefa()
            case 'lst': Listar_tarefas()
            case 'del': Excluir_tarefa()
            case 'q': break
            case '_': print('comando invalido')

if __name__ == '__main__':
    main()