import sys
sys.path.append('../')

from inner_project.load_file import Csv
from inner_project.graphic import Graphic

# file = Csv('steam_games.csv')
file = Csv('example_20_rows.csv')

rows = {}
rows['windows'] = 0
rows['mac'] = 0
rows['linux'] = 0

data = file.getValuesOfColumn('Windows')
for r in data:
  if r == 'True': rows['windows'] = rows['windows'] + 1

data = file.getValuesOfColumn('Mac')
for r in data:
  if r == 'True': rows['mac'] = rows['mac'] + 1

data = file.getValuesOfColumn('Linux')
for r in data:
  if r == 'True': rows['linux'] = rows['linux'] + 1

for k, v in rows.items():
  print(k, ' => %.0f' % int( (v/len(file.getRows()))*100 ) + '%')

labels = []
values = []
for k, v in rows.items():
  labels.append(k)
  values.append(v)

graphic = Graphic(labels, values)
graphic.setTitle('Plataformas')
graphic.show('pie')