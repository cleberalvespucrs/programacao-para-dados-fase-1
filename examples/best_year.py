import sys
sys.path.append('../')

from inner_project.load_file import Csv
from inner_project.graphic import Graphic

# file = Csv('steam_games.csv')
file = Csv('example_20_rows.csv')

rows = {}
data = file.getValuesOfColumn('Release date')

for r in data:
  year = r[len(r)-4: len(r)]

  if year not in rows:
    rows[year] = 0

  rows[year] = rows[year] + 1

# sort
rows = dict(sorted(rows.items()))

print(rows)

bigger = 0
for k, v in rows.items():
  if int(v) > bigger:
    bigger = int(v)

years = []
for k, r in rows.items():
  if int(r) == bigger:
    years.append(k)


graphic = Graphic()
graphic.setItems(rows.items())
graphic.setTitle('Best Years')
graphic.show('bar')