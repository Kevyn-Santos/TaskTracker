obj = {
    'nome': 'teste',
    'Descrição': 'OWO'
}

print(obj)

obj['Descrição'] = 'AWA'
print(obj)

chave = 2
if chave == 2:
    obj['Descrição'] = 'BOB'
print(obj)

{'id': 1,
        'Descrição': 'teste',
        'Status': 'Todo',
        'Data de Criação': datetime.today().strftime('%d/%m/%Y')}