from Inner_Project.LoadFile import Csv

import1 = Csv('example_20_rows.csv')
print(import1.getRows())
print(import1._getIndexOfColumnName('User score'))
print(import1.getValuesOfColumn('Price'))