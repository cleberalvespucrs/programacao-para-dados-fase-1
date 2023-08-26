import sys
sys.path.append('../')

from inner_project.load_file import Csv
from inner_project.graphic import Graphic

print("Qual o percentual de jogos gratuitos e pagos na plataforma?")

#leitura do arquivo
# file = Csv('steam_games.csv')
file = Csv('example_20_rows.csv')

#busca os valores da coluna "Price"
data = file.getValuesOfColumn('Price')

#monta objeto para armazenar os dados, instancia com zero e percorre as linhas
rows = {}
rows['paid'] = 0
rows['free'] = 0
for r in data:
  #se o valor é acima de zero, conta pago, senão grátis
  if(float(r) > 0): rows['paid'] = rows['paid'] + 1
  else: rows['free'] = rows['free'] + 1

# percorre as linhas e imprime a resposta
print('Resposta:')
for k, v in rows.items():
  print(k, ' => %.0f' % int( (v/len(data))*100 ) + '%')

print("De um total de " + str(len(data)) + " jogos, encontramos um total de " + str(rows['free']) + ' jogos gratuítos')

# monta os objetos de label e value para utilizar no gráfico
labels = []
values = []
for k, v in rows.items():
  labels.append(k)
  values.append(v)

# renderiza o gráfico do tipo pie
graphic = Graphic(labels, values)
graphic.setTitle('Qual o percentual de jogos gratuitos e pagos na plataforma?')
graphic.show('pie')