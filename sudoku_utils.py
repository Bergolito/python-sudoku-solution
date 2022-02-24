import numpy as np
import time
import datetime

from random import choice
from collections import Counter

from solucao_arvore_geral import Posicao_Possibilidades, Trinca, imprime_trincas, imprime_saida, imprime_saida_retorna_tam_lista
from solucao_arvore_02_possibs import monta_arvore_02_possibilidades
from solucao_arvore_03_possibs import monta_arvore_03_possibilidades
from solucao_arvore_04_possibs import monta_arvore_04_possibilidades
from solucao_arvore_05_possibs import monta_arvore_05_possibilidades
from solucao_arvore_06_possibs import monta_arvore_06_possibilidades
from solucao_arvore_07_possibs import monta_arvore_07_possibilidades

CONJUNTO_COMPLETO = {1, 2, 3, 4, 5, 6, 7, 8, 9}

# ====================================
def retorna_date_time_string():
    x = datetime.datetime.now()
    date_str = str(x.strftime("%Y"))+str(x.strftime("%m"))+str(x.strftime("%d"))+'_'+str(x.strftime("%f"))
    return date_str
# ====================================
def exibe_tempo_processamento(start, end):
    hours, rem = divmod(end - start, 3600)
    minutes, seconds = divmod(rem, 60)
    print("\nTempo Total (HH:mm:ss) = {:0>2}:{:0>2}:{:05.2f}".format(int(hours), int(minutes), seconds))
# ====================================
def seta_valores_inferidos(matriz_entrada, lista_trincas_inferencia):

    # inferir valores com 100% de certeza 
    for item_str in lista_trincas_inferencia:
        trinca_formatada = item_str.replace('(','')
        trinca_formatada = trinca_formatada.replace(')','')
        tokens_trinca = trinca_formatada.split(',')

        linha = int(tokens_trinca[0])
        coluna = int(tokens_trinca[1])
        valor = int(tokens_trinca[2])
        matriz_entrada[linha][coluna] = valor
        print('\n\n SETOU o valor {} na linha {} e na coluna {} \n\n'.format(valor, linha, coluna))
# ====================================
def validacao(matriz):
    
    for i in range(0,9):
        for j in range(0, 9):
            if matriz[i][j] == 0:
                lista = retorna_qtd_possibs_celula(i, j, matriz)
                if len(lista) == 1:
                    matriz[i][j] = lista[0]
    
    matriz_completa = retorna_matriz_completa(matriz)
    return matriz_completa,verifica_matriz_eh_valida(matriz_completa)
# ====================================
def existe_valor_repetido(array):
    lista = [item for item, count in Counter(array).items() if count > 1]
    return (len(lista) > 0)
# ====================================
def retorna_array_sem_zeros(array):
    saida = []
    for item in array:
        if item != 0:
            saida.append(item)
    return saida
# ====================================
def verifica_matriz_eh_valida(matriz):
    # verifica nas linhas
    for i in range(0,9):
        linha_com_duplicacao = existe_valor_repetido(matriz[i])
        if linha_com_duplicacao:
            return False
    # verifica nas colunas
    for j in range(0, 9):
        coluna_com_duplicacao = existe_valor_repetido(matriz[:, j])
        if coluna_com_duplicacao:
            return False

    quad_0 = retorna_elementos_quadrante(0, matriz)
    quad_1 = retorna_elementos_quadrante(1, matriz)
    quad_2 = retorna_elementos_quadrante(2, matriz)
    quad_3 = retorna_elementos_quadrante(3, matriz)
    quad_4 = retorna_elementos_quadrante(4, matriz)
    quad_5 = retorna_elementos_quadrante(5, matriz)
    quad_6 = retorna_elementos_quadrante(6, matriz)
    quad_7 = retorna_elementos_quadrante(7, matriz)
    quad_8 = retorna_elementos_quadrante(8, matriz)

    if existe_valor_repetido(quad_0) or existe_valor_repetido(quad_1) or existe_valor_repetido(quad_2):
        return False
    if existe_valor_repetido(quad_3) or existe_valor_repetido(quad_4) or existe_valor_repetido(quad_5):
        return False
    if existe_valor_repetido(quad_6) or existe_valor_repetido(quad_7) or existe_valor_repetido(quad_8):
        return False
    return True
# ==================================== 
def verifica_matriz_incompleta_esta_valida(matriz):
    # verifica nas linhas
    for i in range(0,9):
        linha_com_duplicacao = existe_valor_repetido(retorna_array_sem_zeros(matriz[i]))
        if linha_com_duplicacao:
            return False
    # verifica nas colunas
    for j in range(0, 9):
        coluna_com_duplicacao = existe_valor_repetido(retorna_array_sem_zeros(matriz[:, j]))
        if coluna_com_duplicacao:
            return False

    quad_0 = retorna_array_sem_zeros(retorna_elementos_quadrante(0, matriz))
    quad_1 = retorna_array_sem_zeros(retorna_elementos_quadrante(1, matriz))
    quad_2 = retorna_array_sem_zeros(retorna_elementos_quadrante(2, matriz))
    quad_3 = retorna_array_sem_zeros(retorna_elementos_quadrante(3, matriz))
    quad_4 = retorna_array_sem_zeros(retorna_elementos_quadrante(4, matriz))
    quad_5 = retorna_array_sem_zeros(retorna_elementos_quadrante(5, matriz))
    quad_6 = retorna_array_sem_zeros(retorna_elementos_quadrante(6, matriz))
    quad_7 = retorna_array_sem_zeros(retorna_elementos_quadrante(7, matriz))
    quad_8 = retorna_array_sem_zeros(retorna_elementos_quadrante(8, matriz))

    if existe_valor_repetido(quad_0) or existe_valor_repetido(quad_1) or existe_valor_repetido(quad_2):
        return False
    if existe_valor_repetido(quad_3) or existe_valor_repetido(quad_4) or existe_valor_repetido(quad_5):
        return False
    if existe_valor_repetido(quad_6) or existe_valor_repetido(quad_7) or existe_valor_repetido(quad_8):
        return False
    return True
# ====================================
def retorna_matriz_completa(matriz):
    matriz.copy()
    matriz_inicial = matriz.copy()
    for i in range(0, 9):
        for j in range(0, 9):
            if matriz_inicial[i][j] == 0:
                matriz_inicial[i][j] = choice(retorna_qtd_possibs_celula(i, j, matriz))
    return matriz_inicial
# ====================================
def retorna_qtd_possibs_celula(linha, coluna, matriz):
    elementos = []
    elementos.extend(pega_elementos_linha(linha, matriz))
    elementos.extend(pega_elementos_coluna(coluna, matriz))
    elementos.extend(retorna_elementos_quadrante_linha_coluna(linha, coluna, matriz))
    conjunto_b = set(elementos)
    return list(CONJUNTO_COMPLETO.difference(conjunto_b))
# ====================================
def pega_elementos_linha(linha, matriz):
    elementos = []
    for num in matriz[linha]:
        if num != 0:
            elementos.append(num)
    return elementos
# ====================================
def pega_elementos_coluna(coluna, matriz):
    elementos = []
    for num in matriz[:, coluna]:
        if num != 0:
            elementos.append(num)
    return elementos
# ====================================
def retorna_elementos_quadrante_linha_coluna(linha, coluna, matriz):
    linha_inicio = -1
    linha_fim = -1
    coluna_inicio = -1
    coluna_fim = -1
    
    if linha >= 0 and linha <= 2:
        if coluna >= 0 and coluna <= 2:
            linha_inicio = 0;linha_fim = 2;coluna_inicio = 0;coluna_fim = 2;
        if coluna >= 3 and coluna <= 5:
            linha_inicio = 0;linha_fim = 2;coluna_inicio = 3;coluna_fim = 5;
        if coluna >= 6 and coluna <= 8:
            linha_inicio = 0;linha_fim = 2;coluna_inicio = 6;coluna_fim = 8;
    
    if linha >= 3 and linha <= 5:
        if coluna >= 0 and coluna <= 2:
            linha_inicio = 3;linha_fim = 5;coluna_inicio = 0;coluna_fim = 2;
        if coluna >= 3 and coluna <= 5:
            linha_inicio = 3;linha_fim = 5;coluna_inicio = 3;coluna_fim = 5;
        if coluna >= 6 and coluna <= 8:
            linha_inicio = 3;linha_fim = 5;coluna_inicio = 6;coluna_fim = 8;
    
    if linha >= 6 and linha <= 8:
        if coluna >= 0 and coluna <= 2:
            linha_inicio = 6;linha_fim = 8;coluna_inicio = 0;coluna_fim = 2;
        if coluna >= 3 and coluna <= 5:
            linha_inicio = 6;linha_fim = 8;coluna_inicio = 3;coluna_fim = 5;
        if coluna >= 6 and coluna <= 8:
            linha_inicio = 6;linha_fim = 8;coluna_inicio = 6;coluna_fim = 8;
    
    elementos = []
    for i in range(linha_inicio, linha_fim + 1):
        for j in range(coluna_inicio, coluna_fim + 1):
            if matriz[i][j] != 0:
                elementos.append(matriz[i][j])
    return elementos
# ====================================
def retorna_elementos_quadrante(quadrante, matriz):
    linha_inicio = -1;linha_fim = -1;coluna_inicio = -1;coluna_fim = -1;
    
    if quadrante == 0:
        linha_inicio = 0;linha_fim = 2;coluna_inicio = 0;coluna_fim = 2;
    if quadrante == 1:
        linha_inicio = 0;linha_fim = 2;coluna_inicio = 3;coluna_fim = 5;
    if quadrante == 2:
        linha_inicio = 0;linha_fim = 2;coluna_inicio = 6;coluna_fim = 8;
    if quadrante == 3:
        linha_inicio = 3;linha_fim = 5;coluna_inicio = 0;coluna_fim = 2;
    if quadrante == 4:
        linha_inicio = 3;linha_fim = 5;coluna_inicio = 3;coluna_fim = 5;
    if quadrante == 5:
        linha_inicio = 3;linha_fim = 5;coluna_inicio = 6;coluna_fim = 8;
    if quadrante == 6:
        linha_inicio = 6;linha_fim = 8;coluna_inicio = 0;coluna_fim = 2;
    if quadrante == 7:
        linha_inicio = 6;linha_fim = 8;coluna_inicio = 3;coluna_fim = 5;
    if quadrante == 8:
        linha_inicio = 6;linha_fim = 8;coluna_inicio = 6;coluna_fim = 8;
    
    elementos = []
    for i in range(linha_inicio, linha_fim + 1):
        for j in range(coluna_inicio, coluna_fim + 1):
            if matriz[i][j] != 0:
                elementos.append(matriz[i][j])
    return elementos
# ====================================
def imprime_matriz_matrizes_validas(matriz_matrizes_validas):
    if len(matriz_matrizes_validas) > 500:
        print('Impressao de matriz suprimida pois é maior que 500...')

    if len(matriz_matrizes_validas) <= 500:
        for k,list in enumerate(matriz_matrizes_validas):
            print('[{}] -> ['.format(k), end='')
            for it in list:
                print('{}'.format(it),end='')
            print(']')
# ====================================
def mostra_elementos_diferentes_lista(lista_trincas):
    lista = []
    for trinca in lista_trincas:
        lista.append(str(trinca))
    return list(set(lista))
# ====================================
def mostra_estatisticas(matriz_matrizes_validas):

    lista_trincas_inferencia = []

    for indice_coluna in range(len(matriz_matrizes_validas[0])):
        elementos_coluna = retorna_coluna_matriz(matriz_matrizes_validas, indice_coluna)
        total_elementos = len(elementos_coluna)
        trinca1 = ''
        trinca2 = ''
        trinca3 = ''
        trinca4 = ''
        cont_trinca1 = 0
        cont_trinca2 = 0
        cont_trinca3 = 0
        cont_trinca4 = 0
        for k,item in enumerate(elementos_coluna):

            if k == 0:
                trinca1 = str(elementos_coluna[0])
                cont_trinca1 += 1

            if k > 0:
                if str(item) == trinca1:
                    cont_trinca1 += 1

                if str(item) != trinca1 and trinca2 == '' and trinca3 == '' and trinca4 == '':
                    trinca2 = str(item)
                    cont_trinca2 += 1

                elif str(item) != trinca1 and trinca2 != '' and str(item) == trinca2:
                    trinca2 = str(item)
                    cont_trinca2 += 1

                elif str(item) != trinca1 and trinca2 != '' and str(item) != trinca2:
                    trinca3 = str(item)
                    cont_trinca3 += 1

                elif str(item) != trinca1 and trinca2 != '' and str(item) != trinca2 and trinca3 != '' and str(item) != trinca3:
                    trinca4 = str(item)
                    cont_trinca4 += 1

        percent_trinca1 = (cont_trinca1/total_elementos)
        percent_trinca2 = (cont_trinca2/total_elementos)
        percent_trinca3 = (cont_trinca3/total_elementos)
        percent_trinca4 = (cont_trinca4/total_elementos)

        if percent_trinca1 == 1.0:
            lista_trincas_inferencia.append(trinca1)
        elif percent_trinca2 == 1.0:
            lista_trincas_inferencia.append(trinca2)
        elif percent_trinca3 == 1.0:
            lista_trincas_inferencia.append(trinca3)
        elif percent_trinca4 == 1.0:
            lista_trincas_inferencia.append(trinca4)

        #print(percent_trinca1, percent_trinca2, percent_trinca3, percent_trinca4)

        print(' ================================ ', end='\n')
        print(' Coluna {}'.format(indice_coluna),end='\n')
        print(' Trinca 1 ({}) => {}%'.format(trinca1, percent_trinca1 * 100))
        print(' Trinca 2 ({}) => {}%'.format(trinca2, percent_trinca2 * 100 ))
        print(' Trinca 3 ({}) => {}%'.format(trinca3, percent_trinca3 * 100))
        print(' Trinca 4 ({}) => {}%'.format(trinca4, percent_trinca4 * 100))
    print(' ================================ ', end='\n')

    return lista_trincas_inferencia  
# ====================================
def retorna_coluna_matriz(matrix, column_index):
    return [row[column_index] for row in matrix]
# ====================================
def renorna_lista_trincas(posicao: Posicao_Possibilidades):
    lista_trincas = []
    for k,num in enumerate(posicao.possibilidades):
        trinca = Trinca(posicao.linha, posicao.coluna, posicao.possibilidades[k])
        lista_trincas.append(trinca)
    return lista_trincas
# ====================================