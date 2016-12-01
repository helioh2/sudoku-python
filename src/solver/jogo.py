#!/usr/bin/env python
# -*- coding: utf-8 -*-


def estah_resolvido(tab):
    '''
    :param tab: Tabuleiro
    :return: Boolean
    '''
    for lin in range(9):
        for col in range(9):
            if not tab[lin][col]:
                return False
    return True

def proximas_possiveis_solucoes(tab):
    '''

    :param tab: Tabuleiro
    :return: List[Tabuleiro]
    '''
    return []

def eh_invalido(tab):
    '''

    :param tab: Tabuleiro
    :return: Boolean
    '''
    pass



def resolver_sudoku(tab):
    '''
    Tabuleiro -> Tabuleiro
    :return: Tabuleiro
    '''
    if estah_resolvido(tab):
        return tab
    else:
        for t in proximas_possiveis_solucoes(tab):  # de preferencia retorna um gerador
            if not eh_invalido(t):
                tentativa = resolver_sudoku(t)  # testa um proximo / filho
                if tentativa:  # aqui ocorre o backtracking da solução caso encontrada
                    return tentativa
        return False





