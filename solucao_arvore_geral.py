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
        return '({},{},{})'.format(self.linha, self.coluna,self.valor)
# ====================================
def retorna_lista_trincas(posicao: Posicao_Possibilidades):
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
    print('Trincas => [',end='')   
    contador = 0    
    for pp in lista_possibilidades:        
        for tc in retorna_lista_trincas(pp):
            contador += 1
            print(tc,end='')
    print('] Total => {}'.format(contador), end='')
# ====================================
def imprime_saida(lista_global):

    for k, item1 in enumerate(lista_global):
        print("\n[{}] -> ".format(k),end="")
        for item2 in item1:
            print(item2, end="")   
# ====================================
def imprime_saida_retorna_tam_lista(lista_global):
    if(len(lista_global) > 200):
        print('\nImpressao de árvore suprimida pois eh maior que 200')

    if(len(lista_global) <= 200):
        for k, item1 in enumerate(lista_global):
            print("\n[{}] -> ".format(k),end="")
            for item2 in item1:
                print(item2, end="")
    return (len(lista_global))        
# ====================================

