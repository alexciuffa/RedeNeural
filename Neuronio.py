import random

def cria_neuronio_aleatorio(num_pesos, id_neuronio, funcao_ativacao=1):
    lista_pesos = []
    for i in range(0, num_pesos+1): # +1 pq Bias
        lista_pesos.append(random.uniform(-1.0, 1.0))
    return Neuronio(id_neuronio, funcao_ativacao, lista_pesos)

class Neuronio():

    def __init__(self, id_neuronio, tipo_funcao_ativacao, lista_pesos=[]):
        if len(lista_pesos) == 0:
        	self.lista_pesos = self.set_pesos_iniciais()
        else:
            self.lista_pesos = lista_pesos
        self.tipo_funcao_ativacao = tipo_funcao_ativacao
        self.id_neuronio = id_neuronio
        self.saida = 0
        self.derivada_funcao_ativacao = 0
        self.gradiente = 0

    def __str__(self):
        texto = " Neuronio " + str(self.id_neuronio)
        texto += "\n lista_Pesos:"
        for i in range(0, len(self.lista_pesos)):
                texto+= str((self.lista_pesos[i])) + ";"
                #texto+= "%5.2f "%(self.lista_pesos[i])
        texto += "\n funcao_ativacao: " + str(self.tipo_funcao_ativacao)
        return texto

    def set_pesos_iniciais(self):
        return[2,2,2]

    def calcula_somatoria(self, lista_entradas):
        somatoria = 0
        for i in range (0, len(lista_entradas)):
            somatoria += lista_entradas[i] * self.lista_pesos[i]
        return somatoria

    def funcao_ativacao(self, somatoria):
        if self.tipo_funcao_ativacao == 1:
            return (1/(1+2.718281**(-somatoria)))#1/[1+e^(-somatoria)]
        else:
            print("##### DEU RUIM #####")
            return 0

    def derivada_funcao_ativacao(self, somatoria):
        if self.tipo_funcao_ativacao == 1:
            return self.funcao_ativacao(somatoria)*(1 - self.funcao_ativacao(somatoria))
        else:
            print("##### DEU RUIM 22222 ###")
            return 0

    def calcula_saida(self, lista_entradas):
        somatoria = self.calcula_somatoria(lista_entradas)
        saida = self.funcao_ativacao(somatoria)
        self.saida = saida
        self.derivada_funcao_ativacao = self.derivada_funcao_ativacao(somatoria)
        return saida

    def calcula_gradiente(self, rede, saida_esperada):
        '''
        Sob Análise

    # Somatoria(gradiente_da_frente * W) * F'
        somatoria = 0
        if (self.id[0] == len(rede)-1):# eh a ultima camada
            return (rede[self.id[0]][self.id[1]] - saida_esperada) * self.derivada_funcao_ativacao
        #else:
        for i in range(0, len(rede[self.id[0]+1])):
            somatoria += rede[self.id[0]+1][i].lista_pesos[self.id[1]] * rede[self.id[0]+1][i].gradiente
        return somatoria * self.derivada_funcao_ativacao
        '''
        pass

print(Neuronio(0, 1))