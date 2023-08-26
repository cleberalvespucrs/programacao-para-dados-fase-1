import sys
sys.path.append('../')

from inner_project.load_file import Csv
from inner_project.graphic import Graphic

# file = Csv('steam_games.csv')
file = Csv('example_20_rows.csv')

rows = {}
rows['paid'] = 0
rows['free'] = 0
data = file.getValuesOfColumn('Price')
for r in data:
  if(float(r) > 0): rows['paid'] = rows['paid'] + 1
  else: rows['free'] = rows['free'] + 1

for k, v in rows.items():
  print(k, ' => %.0f' % int( (v/len(data))*100 ) + '%')

labels = []
values = []
for k, v in rows.items():
  labels.append(k)
  values.append(v)

graphic = Graphic(labels, values)
graphic.setTitle('Free Vs Paids')
graphic.show('pie')