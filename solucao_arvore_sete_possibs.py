from solucao_arvore_geral import Posicao_Possibilidades, Trinca, renorna_lista_trincas, retorna_trincas, imprime_trincas, imprime_saida

# ====================================
def monta_arvore_07_possibilidades(lista_possibilidades):
    lista_global = [[], [], [], [], [], [], []]

    trincas = renorna_lista_trincas(lista_possibilidades[0])
    lista_global[0].append(trincas[0])
    lista_global[1].append(trincas[1])
    lista_global[2].append(trincas[2])
    lista_global[3].append(trincas[3])
    lista_global[4].append(trincas[4])
    lista_global[5].append(trincas[5])
    lista_global[6].append(trincas[6])

    for k, pp in enumerate(lista_possibilidades):
        if k == 0:
            continue
        elif k > 0:
            lista_trincas_arg = renorna_lista_trincas(pp)
            lista_global = heptatuplica_lista_trincas(lista_global, lista_trincas_arg)
    
    return lista_global
# ====================================
'''
    # heptatuplica a lista
    # copia os valores
    # insere as novas trincas
'''
def heptatuplica_lista_trincas(lista_global, nova_lista_trincas):
    nova_lista_retornada = [[]]
    lista = []
    if len(lista_global) == 0:
        nova_lista_retornada = [[] for i in range(len(nova_lista_trincas))]
        for k,item in enumerate(nova_lista_trincas):
            lista = [item]
            nova_lista_retornada[k].extend(lista)
    else:
        nova_lista_retornada = [[] for i in range(7 * len(lista_global))]
        for (k,item) in enumerate(lista_global):
            if k == 1:
                k += 6
            elif k >= 2:
                k *= 7
            nova_lista_retornada[k].extend(item)
            nova_lista_retornada[k].append(nova_lista_trincas[0])
            nova_lista_retornada[k+1].extend(item)
            nova_lista_retornada[k+1].append(nova_lista_trincas[1])
            nova_lista_retornada[k+2].extend(item)
            nova_lista_retornada[k+2].append(nova_lista_trincas[2])
            nova_lista_retornada[k+3].extend(item)
            nova_lista_retornada[k+3].append(nova_lista_trincas[3])
            nova_lista_retornada[k+4].extend(item)
            nova_lista_retornada[k+4].append(nova_lista_trincas[4])
            nova_lista_retornada[k+5].extend(item)
            nova_lista_retornada[k+5].append(nova_lista_trincas[5])
            nova_lista_retornada[k+6].extend(item)
            nova_lista_retornada[k+6].append(nova_lista_trincas[6])

    return nova_lista_retornada
# ====================================
if __name__ == '__main__':
    p1 = Posicao_Possibilidades(0, 2, [1, 2, 3, 4, 5, 6, 8])
    p2 = Posicao_Possibilidades(1, 3, [1, 2, 3, 5, 5, 8, 9])
    p3 = Posicao_Possibilidades(3, 6, [1, 3, 4, 6, 5, 6, 7])
    lista_possibilidades = [p1, p2, p3]
    imprime_trincas(lista_possibilidades)
    arvore = monta_arvore_07_possibilidades(lista_possibilidades)
    imprime_saida(arvore)



    