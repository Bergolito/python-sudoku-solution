import numpy as np
from random import choice
from collections import Counter
from nova_solucao import Posicao_Possibilidades, monta_arvore

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
        print('Total de Possibilidades: {} '.format(retorna_total_possibilidades(matriz_entrada)))
        print('Lista de Posição Possibilidades: \n ')
        for pp in retorna_posicoes_possibilidades(matriz_entrada):
            print(pp)
        teste_matriz_02(matriz_entrada)
        
def retorna_total_possibilidades(matriz):
    total = 1
    for i in range(0, 9):
        for j in range(0, 9):
            if matriz[i][j] == 0:
                lista = retorna_qtd_possibs_celula(i, j, matriz)
                if len(lista) == 2:
                    total = total * len(lista)
    return total

def retorna_posicoes_possibilidades(matriz):
    lista_possibs = []
    for i in range(0, 9):
        for j in range(0, 9):
            if matriz[i][j] == 0:
                lista = retorna_qtd_possibs_celula(i, j, matriz)
                
                if len(lista) == 2:
                    lista_possibs.append(Posicao_Possibilidades(i,j,lista))
    return lista_possibs
                


def validacao(matriz):
    
    for i in range(0,9):
        for j in range(0, 9):
            if matriz[i][j] == 0:
                lista = retorna_qtd_possibs_celula(i, j, matriz)
                '''
                if len(lista) == 2:
                    print('({},{}) => {} => {} '.format(i,j,lista, choice(lista)))
                '''
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
    
    conjuntoB = set(elementos)
    
    return list(CONJUNTO_COMPLETO.difference(conjuntoB))

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
        linha_inicio = 0;
        linha_fim = 2;
        coluna_inicio = 0;
        coluna_fim = 2;
    if quadrante == 1:
        linha_inicio = 0;
        linha_fim = 2;
        coluna_inicio = 3;
        coluna_fim = 5;
    if quadrante == 2:
        linha_inicio = 0;
        linha_fim = 2;
        coluna_inicio = 6;
        coluna_fim = 8;
    if quadrante == 3:
        linha_inicio = 3;
        linha_fim = 5;
        coluna_inicio = 0;
        coluna_fim = 2;
    if quadrante == 4:
        linha_inicio = 3;
        linha_fim = 5;
        coluna_inicio = 3;
        coluna_fim = 5;
    if quadrante == 5:
        linha_inicio = 3;
        linha_fim = 5;
        coluna_inicio = 6;
        coluna_fim = 8;
    if quadrante == 6:
        linha_inicio = 6;
        linha_fim = 8;
        coluna_inicio = 0;
        coluna_fim = 2;
    if quadrante == 7:
        linha_inicio = 6;
        linha_fim = 8;
        coluna_inicio = 3;
        coluna_fim = 5;
    if quadrante == 8:
        linha_inicio = 6;
        linha_fim = 8;
        coluna_inicio = 6;
        coluna_fim = 8;
    
    elementos = []
    for i in range(linha_inicio, linha_fim + 1):
        for j in range(coluna_inicio, coluna_fim + 1):
            if matriz[i][j] != 0:
                elementos.append(matriz[i][j])
    return elementos

def teste_matriz_02(matriz_a_verificar):
    p1 = Posicao_Possibilidades(0, 8,  [9, 2])
    p2 = Posicao_Possibilidades(1, 8,  [1, 2])
    p3 = Posicao_Possibilidades(3, 1,  [2, 5])
    p4 = Posicao_Possibilidades(4, 8,  [9, 2])
    p5 = Posicao_Possibilidades(7, 4,  [1, 5])
    lista_possibilidades = [p1, p2, p3, p4, p5]
    arvore = monta_arvore(lista_possibilidades)

    cont_matrizes_validas = 0
    for k,item_arvore in enumerate(arvore):
        matriz_teste = matriz_a_verificar.copy()
        texto_trincas = ''
        for trinca in item_arvore:
            texto_trincas = texto_trincas + str(trinca)
            matriz_teste[trinca.linha][trinca.coluna] = trinca.valor
        eh_valida = verifica_matriz_incompleta_esta_valida(matriz_teste)
        if eh_valida:
            cont_matrizes_validas +=1
            print('Matriz {} Válida => {} => [{}]'.format(k,eh_valida, texto_trincas))
        '''    
        else:
            print('Matriz {} Válida => {} '.format(k, eh_valida))
        '''
        
    print('Matrizes Válidas => {} '.format(cont_matrizes_validas))
