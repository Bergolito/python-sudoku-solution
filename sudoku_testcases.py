from unittest import TestCase
from sudoku import *

MATRIZ_ENTRADA_01 = np.array(
    [
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

matriz_valida = np.array([
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

class SudokuTestCases(TestCase):

    def test_pega_elementos_linha(self):
        self.assertEqual(len(pega_elementos_linha(0, MATRIZ_ENTRADA_01)), 1)
        self.assertEqual(len(pega_elementos_linha(1, MATRIZ_ENTRADA_01)), 5)
        self.assertEqual(len(pega_elementos_linha(2, MATRIZ_ENTRADA_01)), 4)
        self.assertEqual(len(pega_elementos_linha(8, MATRIZ_ENTRADA_01)), 1)
        self.assertNotEqual(len(pega_elementos_linha(7, MATRIZ_ENTRADA_01)), 3)
        
    def test_pega_elementos_coluna(self):
        self.assertEqual(len(pega_elementos_coluna(0, MATRIZ_ENTRADA_01)), 1)
        self.assertEqual(len(pega_elementos_coluna(1, MATRIZ_ENTRADA_01)), 5)

    def test_elementos_quadrante_linha_coluna(self):
        self.assertEqual(len(retorna_elementos_quadrante_linha_coluna(1, 1, MATRIZ_ENTRADA_01)), 3)
        self.assertEqual(len(retorna_elementos_quadrante_linha_coluna(7, 7, MATRIZ_ENTRADA_01)), 3)
        self.assertNotEqual(len(retorna_elementos_quadrante_linha_coluna(0, 3, MATRIZ_ENTRADA_01)), 5)

    def test_retorna_qtd_possibs_celula(self):
        self.assertEqual(len(retorna_qtd_possibs_celula(1, 2, MATRIZ_ENTRADA_01)), 2)
        self.assertEqual(len(retorna_qtd_possibs_celula(2, 3, MATRIZ_ENTRADA_01)), 2)
        self.assertNotEqual(len(retorna_qtd_possibs_celula(3, 7, MATRIZ_ENTRADA_01)), 4)
        self.assertNotEqual(len(retorna_qtd_possibs_celula(7, 5, MATRIZ_ENTRADA_01)), 4)
    
    def test_retorna_matriz_completa(self):
        matriz_completa = retorna_matriz_completa(MATRIZ_ENTRADA_01)
        self.assertNotEqual(matriz_completa[3][4], 0)
        self.assertNotEqual(matriz_completa[5][5], 0)
        self.assertNotEqual(matriz_completa[4][1], 0)
        self.assertNotEqual(matriz_completa[7][2], 0)

    def test_existe_valor_repetido(self):
        self.assertTrue(existe_valor_repetido([1,2,3,2,5,3,6]))
        self.assertTrue(existe_valor_repetido([1,2,3,4,1]))
        self.assertFalse(existe_valor_repetido([4,5,6,9]))
        self.assertFalse(existe_valor_repetido([1,2,3,4,7,8]))
    
    def test_retorna_elementos_quadrante(self):
        self.assertEqual(len(retorna_elementos_quadrante(0, MATRIZ_ENTRADA_01)), 3)
        self.assertEqual(len(retorna_elementos_quadrante(2, MATRIZ_ENTRADA_01)), 3)
        self.assertNotEqual(len(retorna_elementos_quadrante(6, MATRIZ_ENTRADA_01)), 5)
    
    def test_verifica_matriz_eh_valida(self):
        matriz_teste1 = matriz_valida.copy()
        self.assertTrue(verifica_matriz_eh_valida(matriz_teste1))
        matriz_teste2 = matriz_valida.copy()
        matriz_teste2[0][8] = 6
        matriz_teste2[8][8] = 2
        self.assertFalse(verifica_matriz_eh_valida(matriz_teste2))
    def test_array_sem_zeros(self):
        array1 = [1,2,0,4,5,7,0]
        self.assertEqual(len(retorna_array_sem_zeros(array1)),5)
        array2 = [0,0,0,4,0,0,0]
        self.assertEqual(len(retorna_array_sem_zeros(array2)),1)
if __name__ == '__main__':
    SudokuTestCases.main()