from datetime import datetime, timedelta

pessoa = {
    ' dia ': '',
}

for chave in pessoa:
    pessoa[chave] = int(input('Digite o' +chave))
    print(f'{chave}: {pessoa[chave]}')

print(pessoa)

data_nascimento = timedelta(days=pessoa['dia'])
data_hoje = datetime.now()
delta_data_hoje = timedelta(days=data_hoje.day)

difer 