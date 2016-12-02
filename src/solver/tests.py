#!/usr/bin/env python
# -*- coding: utf-8 -*-


import unittest
from jogo import *
from dados import *

class Test(unittest.TestCase):


    def testResolveSudoku(self):
        self.assertEqual(resolver_sudoku(TAB_FACIL),\
                         TAB_FACIL_SOLUCAO )

    def testEstahResolvido(self):
        self.assertFalse(estah_resolvido(TAB_FACIL))
        self.assertTrue(estah_resolvido(TAB_FACIL_SOLUCAO))

    def testPrimeiroEspaco(self):
        self.assertEqual(primeiro_espaco_vazio(TAB_FACIL), (0,3))

    def testEhInvalido(self):
        TAB_FACIL[0][3] = 2
        self.assertTrue(eh_invalido(TAB_FACIL))
        TAB_FACIL[0][3] = B
        self.assertFalse(eh_invalido(TAB_FACIL))