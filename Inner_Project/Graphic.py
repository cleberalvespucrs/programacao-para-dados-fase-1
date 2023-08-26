import matplotlib.pyplot as plt

class Graphic:

    def __init__(self, labels = [], values = []):
        self.values = values
        self.labels = labels
        self.title = ''

    def setItems(self, items):
        for v, k in items:
            self.labels.append(k)
            self.values.append(v)
    
    def setTitle(self, title):
        self.title = title

    def show(self, type = 'bar'):
        if len(self.labels) == 0: raise Exception('O objeto labels não pode ser vazio')
        if len(self.values) == 0: raise Exception('O objeto values não pode ser vazio')
         
        if type ==  'bar': self.createBar()
        elif type == 'pie': self.createPie()
        else: raise Exception('Tipo de gráfico inválido')
    
    def createBar(self):
        plt.bar(self.values,self.labels)
        plt.xticks(self.values)
        plt.title(self.title)
        plt.margins(0)
        plt.show()

    def createPie(self):
        plt.pie(self.values, labels = self.labels, autopct ='%1.1f%%')
        plt.title(self.title)
        plt.margins(0)
        plt.show()