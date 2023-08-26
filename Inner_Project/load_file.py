import csv

class Csv:

  """
  Classe que disponibiliza métodos para extração de dados de um CSV
  """

  def __init__(self, filename, delimiter = ','):
    self.filename = filename
    self.delimiter = delimiter
    self.rows = self._loadFile(self.filename, self.delimiter)

  def getRows(self):
    """
    Method: getRows
    Description: retorna todas as linhas extraídas do arquivo

    Examples
    --------
    >>> file = Csv('../examples/example_20_rows.csv')
    >>> len(file.getRows()) > 0
    True
    """
    return self.rows

  def getValuesOfColumn(self, colunmName):
    """
    Method: getValuesOfColumn
    Description: retorna apenas os valores da coluna passado por parâmetro

    Examples
    --------
    >>> file = Csv('../examples/example_20_rows.csv')
    >>> len(file.getValuesOfColumn('Windows')) > 0
    True
    """

    values = []
    for r in self.rows:
      values.append(r[self._getIndexOfColumnName(colunmName)])
    return values

  def _loadFile(self, filename, delimiter):
    """
    Method: _loadFile
    Description: método que faz a leitura do arquivo e retorna as linhas extraídas

    Examples
    --------
    >>> file = Csv('../examples/example_20_rows.csv')
    >>> len(file.getRows()) > 0
    True
    """

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
    return rows

  def _getValueOfColumn(self, row, col):
    """
    Method: _getValueOfColumn
    Description: retorna apenas o valor do index passado por parâmetro

    Examples
    --------
    >>> file = Csv('../examples/example_20_rows.csv')
    >>> file._getValueOfColumn(file.getRows()[0], 0) != ""
    True
    """

    try:
      return row[col]
    except ValueError:
      print("Registro não encontrado!")

  def _getIndexOfColumnName(self, colunmName):
    """
    Method: _getIndexOfColumnName
    Description: retorna o indice de uma coluna passado por parâmetro

    Examples
    --------
    >>> file = Csv('../examples/example_20_rows.csv')
    >>> file._getIndexOfColumnName('AppID') == 0
    True
    """

    for idx, colunm in enumerate(self.cols):
      if colunm == colunmName: return idx

    raise Exception('Coluna não encontrada!')
  
if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)