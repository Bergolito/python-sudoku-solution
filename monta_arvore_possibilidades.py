# ====================================
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
        return '({},{},{})'.format(self.linha, self.coluna, self.valor)
# ====================================

def renorna_lista_trincas(posicao: Posicao_Possibilidades):
    lista_trincas = []
    for k,num in enumerate(posicao.possibilidades):
        trinca = Trinca(posicao.linha, posicao.coluna, posicao.possibilidades[k])
        lista_trincas.append(trinca)
    return lista_trincas


def monta_arvore_02_possibilidades(lista_possibilidades):
    lista_global = [[], []]

    trincas = renorna_lista_trincas(lista_possibilidades[0])
    lista_global[0].append(trincas[0])
    lista_global[1].append(trincas[1])

    for k, pp in enumerate(lista_possibilidades):
        if (k == 0):
            continue
        elif k > 0:
            lista_trincas_arg = renorna_lista_trincas(pp)
            lista_global = duplica_lista_trincas(lista_global, lista_trincas_arg)

    return lista_global

def monta_arvore_03_possibilidades(lista_possibilidades):
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


def retorna_trincas(posicao):
    lista_trincas = []
    num_possibilidades = len(posicao.possibilidades)
    for i in range(0, num_possibilidades):
        trinca = Trinca(posicao.linha, posicao.coluna, posicao.possibilidades[i])
        lista_trincas.append(trinca)
    return lista_trincas

'''
    # duplica a lista
    # copia os valores
    # insere as novas trincas
'''
def duplica_lista_trincas(lista_global, nova_lista_trincas):
    nova_lista_retornada = [[]]
    lista = []
    if len(lista_global) == 0:
        nova_lista_retornada = [[] for i in range(len(nova_lista_trincas))]
        for k,item in enumerate(nova_lista_trincas):
            lista = [item]
            nova_lista_retornada[k].extend(lista)
    else:
        nova_lista_retornada = [[] for i in range(2*len(lista_global))]
        for (k,item) in enumerate(lista_global):
            if k == 1:
                k += 1
            elif k >= 2:
                k *= 2
            nova_lista_retornada[k].extend(item)
            nova_lista_retornada[k].append(nova_lista_trincas[0])
            nova_lista_retornada[k+1].extend(item)
            nova_lista_retornada[k+1].append(nova_lista_trincas[1])
    return nova_lista_retornada

'''
    # triplica a lista
    # copia os valores
    # insere as novas trincas
'''
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

def imprime_trincas(lista_possibilidades):
    print('\nTrincas => ')
    cont = 0
    for pp in lista_possibilidades:
        for tc in renorna_lista_trincas(pp):
            cont +=1
            print(tc,end='')
    print('\nTotal => {}'.format(cont))
    
    
def imprime_saida(lista_global):

    for k, item1 in enumerate(lista_global):
        print("\n[{}] -> ".format(k),end="")
        for item2 in item1:
            print(item2, end="")

if __name__ == '__main__':
    p1 = Posicao_Possibilidades(0, 2, [3, 4])
    p2 = Posicao_Possibilidades(1, 3, [5, 8])
    p3 = Posicao_Possibilidades(3, 6, [3, 7])
    #p4 = Posicao_Possibilidades(4, 5, [2, 9])
    #p5 = Posicao_Possibilidades(5, 1, [4, 7])
    #lista_possibilidades = [p1, p2, p3, p4, p5]
    lista_possibilidades = [p1, p2, p3]
    imprime_trincas(lista_possibilidades)
    arvore = monta_arvore_02_possibilidades(lista_possibilidades)
    imprime_saida(arvore)

    p11 = Posicao_Possibilidades(0, 2, [3, 4, 5])
    p22 = Posicao_Possibilidades(1, 3, [1, 5, 8])
    p33 = Posicao_Possibilidades(3, 6, [3, 5, 7])
    p44 = Posicao_Possibilidades(4, 5, [2, 6, 9])
    #p5 = Posicao_Possibilidades(5, 1, [1, 4, 7])
    #lista_possibilidades = [p1, p2, p3, p4, p5]
    #lista_possibilidades = [p1, p2, p3]
    lista_possibilidades2 = [p11, p22, p33, p44]
    imprime_trincas(lista_possibilidades2)
    arvore2 = monta_arvore_03_possibilidades(lista_possibilidades2)
    imprime_saida(arvore2)



    