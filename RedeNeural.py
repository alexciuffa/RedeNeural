import random
import Neuronio
import arquivos as Dados
import sys
from math import sqrt
debugg = False

class RedeNeuralArtificial():

    def __init__(self, num_entradas, num_camadas, num_neuronios_por_camada):
        self.num_entradas = num_entradas
        self.num_camadas = num_camadas
        self.num_neuronios_por_camada = num_neuronios_por_camada 
        self.num_saidas = num_neuronios_por_camada[-1]

def feedfoward(entrada, rede):
    entrada_prox_camada = entrada
    for i in range(0, len(rede)):
        entrada = entrada_prox_camada
        entrada.append(1) # bias
        #print(entrada)
        #print(entrada_prox_camada)
        entrada_prox_camada = []
        for j in range(0, len(rede[i])):
            if (debugg == True):
                print("pesos: ", rede[i][j].pesos)
                print("entrada: ", entrada)
            print()
            somatoria = rede[i][j].calcula_saida(entrada)
            entrada_prox_camada.append(rede[i][j].saida)

    if (debugg == True):
        print("saida C1: ", rede[1][0].saida)
        print("saida C2: ", rede[1][1].saida)


def backpropagation(rede, lista_entradas, lista_saidas_esperadas):
    pass

'''
def backpropagation_camada_saida(esperado, saida_output_layer, saida_hidden_layer, rede, taxa_aprendizado):
    #A partir do erro (saida esperada - saida obtida), corrige os pesos da rede, quase como W = W - N * E,         ###### tem que diferenciar o erro relativo da derivada do erro (geralmente chamam de delta)
    #ou seja, peso = peso - taxa_de_aprendizado * erro
    #esperado = [target1, target2]
    #saida_output_layer = [output1, output2] ou [saida_neuronio_10, saida_neuronio_11]                                   ###### a operação que a função faz parece correta, mas eu acho que os nomes não estão precisos
    #saida_hidden_layer = [saida_neuronio_00, saida_neuronio_01, 1]

    for i in range (2,4):
        for j in range(0,2):
            Erro_Relativo = (saida_output_layer[i-2] - esperado[i-2]) * saida_output_layer[i-2]*(1-saida_output_layer[i-2]) * saida_hidden_layer[j]             ###### aqui é um calculo de delta
            rede[i][j] = rede[i][j] - taxa_aprendizado * Erro_Relativo
    return rede

def backpropagation_camada_escondida(esperado, saida_output_layer, saida_hidden_layer, rede, entrada, taxa_aprendizado):       ###### sugiro quebrar a função em funções menores e chamar as coisas aos poucos pra analisar por pedaços
    #A partir do erro (saida esperada - saida obtida), corrige os pesos da rede, quase como W = W - N * P_E,
    #ou seja, peso = peso - taxa_de_aprendizado * propagação do erro
    for i in range (0,2):
        for j in range(0,2):#len(entrada)
            Erro_Relativo = ((saida_output_layer[0]-esperado[0])*saida_output_layer[0]*(1-saida_output_layer[0])*rede[2][i] + (saida_output_layer[1]-esperado[1])*saida_output_layer[1]*(1-saida_output_layer[1])*rede[3][i]) * saida_hidden_layer[i]*(1-saida_hidden_layer[i]) * entrada[j]
            rede[i][j] = rede[i][j] - taxa_aprendizado * Erro_Relativo
    return rede

def backpropagation(esperado, saida_output_layer, saida_hidden_layer, rede , entrada, taxa_aprendizado):
    rede = backpropagation_camada_escondida(esperado, saida_output_layer, saida_hidden_layer, rede, entrada, taxa_aprendizado)
    rede = backpropagation_camada_saida(esperado, saida_output_layer, saida_hidden_layer, rede, taxa_aprendizado)
    return rede
'''

def cria_nova_rede(num_entradas, num_camadas, num_neuronios_por_camada):
    rede = []
    for i in range (0, num_camadas):
        camada = []
        for j in range (0, num_neuronios_por_camada[i]):
            id_neuronio = [i,j]
            if i == 0:#primeira camada
                camada.append(Neuronio.cria_neuronio_aleatorio(num_entradas, id_neuronio))
            else:
                camada.append(Neuronio.cria_neuronio_aleatorio(num_neuronios_por_camada[i-1], id_neuronio))
        rede.append(camada)
    return rede

def carrega_rede(arquivo):
    matrizEntrada = Dados.le_txt(arquivo)
    if (debugg == True):
        print("############\nLe Dados")
        print(matrizEntrada)
    rede = []

    num_entradas = int(matrizEntrada[0][0])
    num_camadas = int(matrizEntrada[0][1])
    num_neuronios_por_camada = []
    for i in range (2, num_camadas+2):
        num_neuronios_por_camada.append(int(matrizEntrada[0][i]))

    for i in range (0, num_camadas):
        camada = []
        for j in range (0, num_neuronios_por_camada[i]):
            lista_pesos = matrizEntrada[i+1][j].split(";")
            if (debugg == True):
                print("lista de pesos: ", lista_pesos)
            id_neuronio = [i,j]

            if(i==0): # primeira camada
                camada.append(Neuronio.Neuronio(num_entradas+1, lista_pesos, id_neuronio)) #+1 pq bias
            else:
                camada.append(Neuronio.Neuronio(num_neuronios_por_camada[i-1]+1, lista_pesos, id_neuronio))
        rede.append(camada)

    if (debugg == True):
        print("Le Dados\n############")
    return rede

def salva_rede(arquivo, rede):
    texto = ""
    texto += str(2) + " " + str(2) #self.num_entradas ; self.num_camadas
    for i in range(0, 2): #(0, len(num_neuronios_por_camada))
        texto += " " + str(2) #self.num_neuronios_por_camada
    texto += "\n"
    for i in range(0, len(rede)):
        for j in range(0, len(rede[i])):
            for k in range(0, len(rede[i][j].pesos)):
                texto += str(rede[i][j].pesos[k]) + ";"
            texto += " "
        texto += "\n"
    Dados.salva_txt(arquivo, texto)

def Erro(esperado, saida_output_layer):
    return (esperado[0]-saida_output_layer[0])**2 + (esperado[1]-saida_output_layer[1])**2

rede = carrega_rede("rede_pronta.txt")
print(rede)