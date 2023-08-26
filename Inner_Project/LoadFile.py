import csv

class Csv:

  def __init__(self, filename, delimiter = ','):
    self.filename = filename
    self.delimiter = delimiter
    self.rows = self._loadFile(self.filename, self.delimiter)

  def getRows(self):
    return self.rows

  def getValuesOfColumn(self, colunmName):
    values = []
    for r in self.rows:
      values.append(r[self._getIndexOfColumnName(colunmName)])
    return values

  def _loadFile(self, filename, delimiter):
    with open(filename) as csv_file:
      lines = csv.reader(csv_file, delimiter = delimiter)
      rows = []
      cols = []
      rowCount = 0
      for line in lines:
        colCount = 0

        # if first row, get columns names
        if rowCount == 0:
          while colCount < len(line):
            cols.append(self._getValueOfColumn(line, colCount))
            colCount += 1
          rowCount += 1
          self.cols = cols
        else:
          # else, get values of rows
          newRow = []
          while colCount < len(line):
            newRow.append(self._getValueOfColumn(line, colCount))
            colCount += 1

          # new row
          rows.append(newRow)

    # return rows
    return rows;

  def _getValueOfColumn(self, row, col):
    try:
      return row[col]
    except ValueError:
      print("Registro não encontrado!")

  def _getIndexOfColumnName(self, colunmName):
    for idx, colunm in enumerate(self.cols):
      if colunm == colunmName: return idx

    raise Exception('Coluna não encontrada!')