import numpy as np
from random import choice
from solucao_arvore_duas_possibs import Posicao_Possibilidades, monta_arvore_02_possibs
from solucao_arvore_tres_possibs import Trinca
from solucao_arvore_geral import imprime_saida
from collections import Counter
import time

CONJUNTO_COMPLETO = {1, 2, 3, 4, 5, 6, 7, 8, 9}

MATRIZ_ENTRADA_01 = np.array([
        [0, 0, 3, 0, 0, 0, 0, 0, 0],
        [0, 8, 0, 0, 1, 7, 3, 6, 0],
        [0, 2, 0, 0, 9, 3, 0, 0, 8],
        [0, 5, 2, 0, 0, 0, 0, 0, 0],
        [0, 6, 4, 0, 0, 0, 1, 3, 0],
        [0, 0, 0, 0, 0, 0, 5, 4, 0],
        [1, 0, 0, 5, 7, 0, 0, 8, 0],
        [0, 7, 6, 1, 4, 0, 0, 2, 0],
        [0, 0, 0, 0, 0, 0, 7, 0, 0]
])

MATRIZ_ENTRADA_02 = np.array([
        [6, 1, 8,  0, 0, 0,  4, 0, 0],
        [0, 0, 0,  0, 9, 6,  0, 0, 0],
        [0, 0, 0,  8, 0, 0,  0, 0, 7],
        [0, 0, 0,  6, 8, 9,  0, 0, 3],
        [4, 0, 0,  1, 0, 0,  0, 0, 0],
        [9, 0, 0,  0, 4, 0,  0, 0, 8],
        [0, 0, 0,  0, 0, 0,  7, 0, 0],
        [0, 7, 0,  0, 0, 3,  0, 0, 6],
        [0, 4, 0,  2, 0, 0,  0, 0, 5]
    ])
MATRIZ_ENTRADA_02_RESOLVIDA = np.array([
        [6, 1, 8,  7, 2, 5,  4, 3, 9],
        [7, 5, 4,  3, 9, 6,  2, 8, 1],
        [3, 9, 2,  8, 1, 4,  6, 5, 7],
        [1, 2, 7,  6, 8, 9,  5, 4, 3],
        [4, 8, 5,  1, 3, 7,  9, 6, 2],
        [9, 6, 3,  5, 4, 2,  1, 7, 8],
        [5, 3, 1,  9, 6, 8,  7, 2, 4],
        [2, 7, 9,  4, 5, 3,  8, 1, 6],
        [8, 4, 6,  2, 7, 1,  3, 9, 5]
    ])

#MATRIZ_ENTRADA_02[][] = MATRIZ_ENTRADA_02_RESOLVIDA[][]
# 1 Lote
'''
MATRIZ_ENTRADA_02[0][8] = MATRIZ_ENTRADA_02_RESOLVIDA[0][8]
MATRIZ_ENTRADA_02[1][8] = MATRIZ_ENTRADA_02_RESOLVIDA[1][8]
MATRIZ_ENTRADA_02[3][1] = MATRIZ_ENTRADA_02_RESOLVIDA[3][1]
MATRIZ_ENTRADA_02[4][8] = MATRIZ_ENTRADA_02_RESOLVIDA[4][8]
MATRIZ_ENTRADA_02[7][4] = MATRIZ_ENTRADA_02_RESOLVIDA[7][4]
'''
# 2 Lote
'''
MATRIZ_ENTRADA_02[1][1] = MATRIZ_ENTRADA_02_RESOLVIDA[1][1]
MATRIZ_ENTRADA_02[3][6] = MATRIZ_ENTRADA_02_RESOLVIDA[3][6]
MATRIZ_ENTRADA_02[4][4] = MATRIZ_ENTRADA_02_RESOLVIDA[4][4]
MATRIZ_ENTRADA_02[4][5] = MATRIZ_ENTRADA_02_RESOLVIDA[4][5]
MATRIZ_ENTRADA_02[6][4] = MATRIZ_ENTRADA_02_RESOLVIDA[6][4]
#MATRIZ_ENTRADA_02[6][5] = MATRIZ_ENTRADA_02_RESOLVIDA[6][5]


MATRIZ_ENTRADA_01_RESOLVIDA = np.array([
        [6, 9, 3, 8, 5, 4, 2, 7, 1],
        [4, 8, 5, 2, 1, 7, 3, 6, 9],
        [7, 2, 1, 6, 9, 3, 4, 5, 8],
        [3, 5, 2, 4, 6, 1, 8, 9, 7],
        [9, 6, 4, 7, 8, 5, 1, 3, 2],
        [8, 1, 7, 3, 2, 9, 5, 4, 6],
        [1, 3, 9, 5, 7, 2, 6, 8, 4],
        [5, 7, 6, 1, 4, 8, 9, 2, 3],
        [2, 4, 8, 9, 3, 6, 7, 1, 5]
    ])
'''


def inicio():
    start = time.time()
    achou_solucao = False
    LOOPS = 1000
    for i in range(LOOPS):
        matriz_entrada = MATRIZ_ENTRADA_02
        mat, eh_valida = validacao(matriz_entrada)
        if eh_valida:
            achou_solucao = True
            print('===========================================')
            print(' Achou uma matriz válida na {}ª interação: '.format(i+1))
            print(mat)
            print('===========================================')
            break
            
    if not achou_solucao:
        print('===========================================')
        print('Em {} interações, não achou a solução: '.format(LOOPS))
        print('===========================================')

        lista_mat_validas_02_possibs = verifica_matriz_celulas_02_possibs(matriz_entrada)
        lista_trincas_inferencia_02_possibs = mostra_estatisticas(lista_mat_validas_02_possibs)
        seta_valores_inferidos(matriz_entrada, lista_trincas_inferencia_02_possibs)

        lista_mat_validas_03_possibs = verifica_matriz_celulas_03_possibs(matriz_entrada)
        lista_trincas_inferencia_03_possibs = mostra_estatisticas(lista_mat_validas_03_possibs)
        seta_valores_inferidos(matriz_entrada, lista_trincas_inferencia_03_possibs)

        print(' Qtd total de listas : {} * {} = {}'.format(
            len(lista_mat_validas_02_possibs),
            len(lista_mat_validas_03_possibs),
            (len(lista_mat_validas_02_possibs)*len(lista_mat_validas_03_possibs)))
        )
        lista_matrizes_combinada_02e03_possibs = []
        for it_lista1 in lista_mat_validas_02_possibs:
            for it_lista2 in lista_mat_validas_03_possibs:
                lista_matrizes_combinada_02e03_possibs.append(it_lista1 + it_lista2)

    matrizes_combinadas_validas = []
    contador_matrizes_combinadas_validas = 0
    for k, item_lista in enumerate(lista_matrizes_combinada_02e03_possibs):
        matriz_teste = matriz_entrada.copy()

        if k >= 1000 and k // 1000 == 0:
            print('{} .'.format(k))

        for trinca in item_lista:
            matriz_teste[trinca.linha][trinca.coluna] = trinca.valor

        eh_valida = verifica_matriz_incompleta_esta_valida(matriz_teste)
        if eh_valida:
            matrizes_combinadas_validas.append(item_lista)
            contador_matrizes_combinadas_validas += 1

    print(' Qtd matrizes combinadas validas => {}'.format(contador_matrizes_combinadas_validas))
    imprime_matriz_matrizes_validas(matrizes_combinadas_validas)

    verifica_matriz_celulas_04_possibs(matriz_entrada, matrizes_combinadas_validas)

    end = time.time()
    hours, rem = divmod(end - start, 3600)
    minutes, seconds = divmod(rem, 60)
    print(" Tempo Total (HH:mm:ss) = {:0>2}:{:0>2}:{:05.2f}".format(int(hours), int(minutes), seconds))

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

def retorna_total_possibilidades(matriz):
    total = 1
    for i in range(0, 9):
        for j in range(0, 9):
            if matriz[i][j] == 0:
                lista = retorna_qtd_possibs_celula(i, j, matriz)
                if len(lista) == 2:
                    total = total * len(lista)
    return total

def retorna_posicoes_possibilidades(matriz, num_possibs):
    lista_possibs = []
    for i in range(0, 9):
        for j in range(0, 9):
            if matriz[i][j] == 0:
                lista = retorna_qtd_possibs_celula(i, j, matriz)
                
                if len(lista) == num_possibs:
                    lista_possibs.append(Posicao_Possibilidades(i,j,lista))
    return lista_possibs

def retorna_posicoes_02_possibilidades(matriz):
    return retorna_posicoes_possibilidades(matriz, 2)

def retorna_posicoes_03_possibilidades(matriz):
    return retorna_posicoes_possibilidades(matriz, 3)

def retorna_posicoes_04_possibilidades(matriz):
    return retorna_posicoes_possibilidades(matriz, 4)

def validacao(matriz):
    
    for i in range(0,9):
        for j in range(0, 9):
            if matriz[i][j] == 0:
                lista = retorna_qtd_possibs_celula(i, j, matriz)
                if len(lista) == 1:
                    matriz[i][j] = lista[0]
    
    matriz_completa = retorna_matriz_completa(matriz)
    return matriz_completa,verifica_matriz_eh_valida(matriz_completa)

def existe_valor_repetido(array):
    lista = [item for item, count in Counter(array).items() if count > 1]
    return (len(lista) > 0)

def retorna_array_sem_zeros(array):
    saida = []
    for item in array:
        if item != 0:
            saida.append(item)
    return saida

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

def retorna_matriz_completa(matriz):
    matriz.copy()
    matriz_inicial = matriz.copy()
    for i in range(0, 9):
        for j in range(0, 9):
            if matriz_inicial[i][j] == 0:
                matriz_inicial[i][j] = choice(retorna_qtd_possibs_celula(i, j, matriz))
    return matriz_inicial


def retorna_qtd_possibs_celula(linha, coluna, matriz):
    elementos = []
    elementos.extend(pega_elementos_linha(linha, matriz))
    elementos.extend(pega_elementos_coluna(coluna, matriz))
    elementos.extend(retorna_elementos_quadrante_linha_coluna(linha, coluna, matriz))
    conjunto_b = set(elementos)
    return list(CONJUNTO_COMPLETO.difference(conjunto_b))

def pega_elementos_linha(linha, matriz):
    elementos = []
    for num in matriz[linha]:
        if num != 0:
            elementos.append(num)
    return elementos

def pega_elementos_coluna(coluna, matriz):
    elementos = []
    for num in matriz[:, coluna]:
        if num != 0:
            elementos.append(num)
    return elementos

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

def verifica_matriz_celulas_02_possibs(matriz_a_verificar):
    print('Lista de Posição 02 Possibilidades: \n ')
    posicoes = retorna_posicoes_02_possibilidades(matriz_a_verificar)
    for pp in posicoes:
        print(pp)

    lista_possibilidades = []
    for pos in posicoes:
        lista_possibilidades.append(pos)
    arvore = monta_arvore_02_possibs(lista_possibilidades)

    cont_matrizes_validas = 0

    matriz_matrizes_validas = []
    for k,item_arvore in enumerate(arvore):
        matriz_teste = matriz_a_verificar.copy()
        lista_trincas = []

        for trinca in item_arvore:
            lista_trincas.append(trinca)
            matriz_teste[trinca.linha][trinca.coluna] = trinca.valor
        eh_valida = verifica_matriz_incompleta_esta_valida(matriz_teste)
        if eh_valida:
            matriz_matrizes_validas.append(lista_trincas)
            cont_matrizes_validas +=1

    print('Matrizes Válidas => {} '.format(cont_matrizes_validas))

    imprime_matriz_matrizes_validas(matriz_matrizes_validas)

    return matriz_matrizes_validas

def verifica_matriz_celulas_03_possibs(matriz_a_verificar):
    print('Lista de Posição 03 Possibilidades: \n ')
    posicoes = retorna_posicoes_03_possibilidades(matriz_a_verificar)
    for pp in posicoes:
        print(pp)

    lista_possibilidades = []
    for pos in posicoes:
        lista_possibilidades.append(pos)
    arvore = monta_arvore_03_possibs(lista_possibilidades)

    cont_matrizes_validas = 0

    matriz_matrizes_validas = []
    for k,item_arvore in enumerate(arvore):
        matriz_teste = matriz_a_verificar.copy()
        lista_trincas = []

        if k >= 1000 and k // 1000 == 0:
            print('{} .'.format(k))

        for trinca in item_arvore:
            lista_trincas.append(trinca)
            matriz_teste[trinca.linha][trinca.coluna] = trinca.valor
        eh_valida = verifica_matriz_incompleta_esta_valida(matriz_teste)
        if eh_valida:
            matriz_matrizes_validas.append(lista_trincas)
            cont_matrizes_validas +=1

    print('Matrizes Válidas => {} '.format(cont_matrizes_validas))

    imprime_matriz_matrizes_validas(matriz_matrizes_validas)
    #mostra_estatisticas(matriz_matrizes_validas)

    return matriz_matrizes_validas


def verifica_matriz_celulas_04_possibs(matriz_a_verificar, matrizes_combinadas_validas):
    print('Lista de Posição 04 Possibilidades: \n ')
    posicoes = retorna_posicoes_04_possibilidades(matriz_a_verificar)
    for pp in posicoes:
        print(pp)

    
    lista_possibilidades = []
    for pos in posicoes:
        lista_possibilidades.append(pos)
    arvore = monta_arvore_04_possibs(lista_possibilidades)
    imprime_saida(arvore)
    
    '''
    cont_matrizes_validas = 0

    matriz_matrizes_validas = []
    for k,item_arvore in enumerate(arvore):
        matriz_teste = matriz_a_verificar.copy()
        lista_trincas = []

        if k >= 1000 and k // 1000 == 0:
            print('{} .'.format(k))

        for trinca in item_arvore:
            lista_trincas.append(trinca)
            matriz_teste[trinca.linha][trinca.coluna] = trinca.valor
        eh_valida = verifica_matriz_incompleta_esta_valida(matriz_teste)
        if eh_valida:
            matriz_matrizes_validas.append(lista_trincas)
            cont_matrizes_validas +=1

    print('Matrizes Válidas => {} '.format(cont_matrizes_validas))

    imprime_matriz_matrizes_validas(matriz_matrizes_validas)

    return matriz_matrizes_validas
    '''

def imprime_matriz_matrizes_validas(matriz_matrizes_validas):
    for k,list in enumerate(matriz_matrizes_validas):
        print('{}-> ['.format(k), end='')
        for it in list:
            print('{},'.format(it),end='')
        print(']')

def mostra_elementos_diferentes_lista(lista_trincas):
    lista = []
    for trinca in lista_trincas:
        lista.append(str(trinca))
    return list(set(lista))


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


def retorna_coluna_matriz(matrix, column_index):
    return [row[column_index] for row in matrix]

def monta_arvore_03_possibs(lista_possibilidades):
    lista_global = [[], [], []]

    trincas = renorna_lista_trincas(lista_possibilidades[0])
    lista_global[0].append(trincas[0])
    lista_global[1].append(trincas[1])
    lista_global[2].append(trincas[2])

    for k, pp in enumerate(lista_possibilidades):
        if (k == 0):
            continue
        elif k > 0:
            lista_trincas_arg = renorna_lista_trincas(pp)
            lista_global = triplica_lista_trincas(lista_global, lista_trincas_arg)

    return lista_global

def monta_arvore_04_possibs(lista_possibilidades):
    lista_global = [[], [], [], []]

    trincas = renorna_lista_trincas(lista_possibilidades[0])
    lista_global[0].append(trincas[0])
    lista_global[1].append(trincas[1])
    lista_global[2].append(trincas[2])
    lista_global[3].append(trincas[3])

    for k, pp in enumerate(lista_possibilidades):
        if k == 0:
            continue
        elif k > 0:
            lista_trincas_arg = renorna_lista_trincas(pp)
            lista_global = quadruplica_lista_trincas(lista_global, lista_trincas_arg)

    return lista_global

def triplica_lista_trincas(lista_global, nova_lista_trincas):
    nova_lista_retornada = [[]]
    lista = []
    if len(lista_global) == 0:
        nova_lista_retornada = [[] for i in range(len(nova_lista_trincas))]
        for k,item in enumerate(nova_lista_trincas):
            lista = [item]
            nova_lista_retornada[k].extend(lista)
    else:
        nova_lista_retornada = [[] for i in range(3 * len(lista_global))]
        for (k,item) in enumerate(lista_global):
            if k == 1:
                k += 2
            elif k >= 2:
                k *= 3
            nova_lista_retornada[k].extend(item)
            nova_lista_retornada[k].append(nova_lista_trincas[0])
            nova_lista_retornada[k+1].extend(item)
            nova_lista_retornada[k+1].append(nova_lista_trincas[1])
            nova_lista_retornada[k+2].extend(item)
            nova_lista_retornada[k+2].append(nova_lista_trincas[2])

    return nova_lista_retornada

def quadruplica_lista_trincas(lista_global, nova_lista_trincas):
    nova_lista_retornada = [[]]
    lista = []
    if len(lista_global) == 0:
        nova_lista_retornada = [[] for i in range(len(nova_lista_trincas))]
        for k,item in enumerate(nova_lista_trincas):
            lista = [item]
            nova_lista_retornada[k].extend(lista)
    else:
        nova_lista_retornada = [[] for i in range(4 * len(lista_global))]
        for (k,item) in enumerate(lista_global):
            if k == 1:
                k += 3
            elif k >= 2:
                k *= 4
            nova_lista_retornada[k].extend(item)
            nova_lista_retornada[k].append(nova_lista_trincas[0])
            nova_lista_retornada[k+1].extend(item)
            nova_lista_retornada[k+1].append(nova_lista_trincas[1])
            nova_lista_retornada[k+2].extend(item)
            nova_lista_retornada[k+2].append(nova_lista_trincas[2])
            nova_lista_retornada[k+3].extend(item)
            nova_lista_retornada[k+3].append(nova_lista_trincas[3])

    return nova_lista_retornada

def renorna_lista_trincas(posicao: Posicao_Possibilidades):
    lista_trincas = []
    for k,num in enumerate(posicao.possibilidades):
        trinca = Trinca(posicao.linha, posicao.coluna, posicao.possibilidades[k])
        lista_trincas.append(trinca)
    return lista_trincas
