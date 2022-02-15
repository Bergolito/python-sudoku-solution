from solucao_arvore_geral import Posicao_Possibilidades, Trinca, renorna_lista_trincas, retorna_trincas, imprime_trincas, imprime_saida

# ====================================
def monta_arvore_02_possibs(lista_possibilidades):
    lista_global = [[],[]]

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
# ====================================
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
# ====================================
if __name__ == '__main__':
    p1 = Posicao_Possibilidades(0, 2, [3, 4])
    p2 = Posicao_Possibilidades(1, 3, [5, 8])
    p3 = Posicao_Possibilidades(3, 6, [3, 7])
    lista_possibilidades = [p1, p2, p3]
    imprime_trincas(lista_possibilidades)
    arvore = monta_arvore_02_possibs(lista_possibilidades)
    imprime_saida(arvore)