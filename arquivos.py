##################################################################
##                                                              ##
##      Codigo criado por Alexandre Xavier Ciuffatelli          ##
##      https://www.facebook.com/alexandre.ciuffatelli          ##
##      Todos podem usar este codigo livremente                 ##
##      Não comercialize esse código, grato                     ##
##                                                              ##
##################################################################

import xlrd

def le_excel_linha(arq_xls):#le a linha
    # Abre o arquivo
    xls = xlrd.open_workbook(arq_xls)
    # Pega a primeira planilha do arquivo
    planilha = xls.sheets()[0]

    # Para i de zero ao numero de linhas da planilha
    for i in range(planilha.nrows):
        # Le os valores nas linhas da planilha
        yield planilha.row_values(i)

#for linha in xlread_linha('arquivo.xlsx'):
#    print(linha)

def le_excel_coluna(arq_xls):#le a coluna
    # Abre o arquivo
    xls = xlrd.open_workbook(arq_xls)
    # Pega a primeira planilha do arquivo
    planilha = xls.sheets()[0]

    # Para i de zero ao numero de linhas da planilha
    for i in range(planilha.ncols):
        # Le os valores nas linhas da planilha
        yield planilha.col_values(i)

#for linha in xlread_coluna('arquivo.xlsx'):
#    print(linha)

def le_txt(arq_txt):
    try:
        entrada = open(arq_txt, 'r')
    except IOError:
        print("Nao foi possivel abrir o arquivo %s" % arq_txt)
        exit(1)
        
    linhasEntrada = []
    for linha in entrada:
        linhasEntrada.append(linha.split())

    entrada.close()
    return linhasEntrada

def salva_txt(arq_txt, texto):
    saida = open(arq_txt, 'w')
    saida.write(texto)
    saida.close()

def existe_arq(arquivo):
    try:
        existe = open(arquivo, 'r')
        existe.close()
        return True
    except IOError:
        return False

print(le_txt("rede_pronta.txt"))