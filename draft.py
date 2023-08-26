from inner_project.load_file import Csv

import1 = Csv('example_20_rows.csv')
print(import1.getRows())
print(import1._getIndexOfColumnName('User score'))
print(import1.getValuesOfColumn('Price'))

rows = {}
rows['paid'] = 0
rows['free'] = 0
data = import1.getValuesOfColumn('Price')
for r in data:
  if(float(r) > 0): rows['paid'] = rows['paid'] + 1
  else: rows['free'] = rows['free'] + 1

for k, v in rows.items():
  print(k, ' => %.0f' % int( (v/len(data))*100 ) + '%')