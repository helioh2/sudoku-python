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