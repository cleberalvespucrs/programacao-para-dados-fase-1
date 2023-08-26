import sys
sys.path.append('../')

from inner_project.load_file import Csv
from inner_project.graphic import Graphic

print("Qual o percentual de jogos disponíveis para a plataforma IOS?")

#leitura do arquivo
# file = Csv('steam_games.csv')
file = Csv('example_20_rows.csv')

# total de jogos
total = len(file.getRows())

#monsta um objeto com o valor zero
rows = {}
rows['total'] = 0
rows['mac'] = 0

#busca os valores da coluna "Mac" e percorre as linhas
data = file.getValuesOfColumn('Mac')
for r in data:
  if r == 'True': rows['mac'] = rows['mac'] + 1

# restante
rows['total'] = total-rows['mac']

# percorre as linhas e imprime a resposta
for k, v in rows.items():
  print(k, ' => %.1f' % float( (v/total)*100 ) + '%')

print("De um total de " + str(total) + " jogos, encontramos " + str(rows['mac']) + ' jogos compatíveis com as plataformas IOS')

# monta os objetos de label e value para utilizar no gráfico
labels = []
values = []
for k, v in rows.items():
  labels.append(k)
  values.append(v)

# renderiza o gráfico do tipo pie
graphic = Graphic(labels, values)
graphic.setTitle('Qual o percentual de jogos disponíveis para a plataforma IOS?')
graphic.show('pie')