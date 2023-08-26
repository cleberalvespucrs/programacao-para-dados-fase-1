import sys
sys.path.append('../')

from inner_project.load_file import Csv
from inner_project.graphic import Graphic

print("Qual o ano com o maior número de novos jogos? Em caso de empate, retorne uma lista com os anos empatados.")

#leitura do arquivo
# file = Csv('steam_games.csv')
file = Csv('example_20_rows.csv')

#busca os valores da coluna "Release date"
data = file.getValuesOfColumn('Release date')

#monta objeto para armazenar os dados e percorre as linhas
rows = {}
for r in data:
    #pega apena 4 últimos digítos, referente ao ano
    year = r[len(r)-4: len(r)]

    #se não tiver um indice com esse ano, cria com zero
    if year not in rows:
        rows[year] = 0

    #contador do ano
    rows[year] = rows[year] + 1

#ordeno os itens pelo indíce, para deixar o mapa em ordem de ano
rows = dict(sorted(rows.items()))

#verifica qual é o maior valor entre os anos
bigger = 0
for k, v in rows.items():
  if int(v) > bigger:
    bigger = int(v)

#varre os anos e armazena os que tiverem maior lançamento
years = []
for k, r in rows.items():
  if int(r) == bigger:
    years.append(k)

# print(years)

if(len(years) > 1):
    print("Resposta: Com um total de " + str(bigger) + " jogos lançados, anos com maiores números de lançamentos foram:", end= ' ')
    print(' - '.join(years))
else:
    print("Resposta: Com um total de " + str(bigger) + " jogos lançados, o ano com o maior número de lançamentos foi:", end= ' ')
    print(' - '.join(years))

graphic = Graphic()
graphic.setItems(rows.items())
graphic.setTitle('Qual o ano com o maior número de novos jogos?')
graphic.show('bar')