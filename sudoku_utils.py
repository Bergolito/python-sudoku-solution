import numpy as np
import time
import datetime

from random import choice
from collections import Counter

class Posicao_Possibilidades():
    def __init__(self, l, c, valores):
        self.linha = l
        self.coluna = c
        self.possibilidades = valores
    def __str__(self):
        return '({},{})={}'.format(self.linha, self.coluna,self.possibilidades)
# ====================================
class Trinca():
    def __init__(self, l, c, val):
        self.linha = l
        self.coluna = c
        self.valor = val
    def __str__(self):
        return '({},{},{})'.format(self.linha, self.coluna,self.valor)
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

    numeros = {1, 2, 3, 4, 5, 6, 7, 8, 9}
    return list(numeros.difference(conjunto_b))
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
def retorna_trincas(posicao):
    lista_trincas = []
    num_possibilidades = len(posicao.possibilidades)
    for i in range(0, num_possibilidades):
        trinca = Trinca(posicao.linha, posicao.coluna, posicao.possibilidades[i])
        lista_trincas.append(trinca)
    return lista_trincas
# ====================================
def imprime_trincas(lista_possibilidades):
    print('\nTrincas => [',end='')   
    contador = 0    
    for pp in lista_possibilidades:        
        for tc in retorna_lista_trincas(pp):
            contador += 1
            print(tc,end='')
    print('] Total => {}'.format(contador), end='')
# ====================================
def retorna_lista_trincas(posicao: Posicao_Possibilidades):
    lista_trincas = []
    for k,num in enumerate(posicao.possibilidades):
        trinca = Trinca(posicao.linha, posicao.coluna, posicao.possibilidades[k])
        lista_trincas.append(trinca)

    return lista_trincas
# ====================================
def imprime_saida(lista_global):

    for k, item1 in enumerate(lista_global):
        print("\n[{}] -> ".format(k),end="")
        for item2 in item1:
            print(item2, end="")   
# ====================================

