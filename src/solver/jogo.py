#!/usr/bin/env python
# -*- coding: utf-8 -*-
from dados import *
import copy
import time

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


def primeiro_espaco_vazio(tab):
    '''

    :param tab: Tabuleiro
    :return: Posicao
    '''
    for lin in range(9):
        for col in range(9):
            if not tab[lin][col]:
                return (lin,col)


def novo_tab(tab, p, num):
    '''

    :param tab: Tabuleiro
    :param p: Posicao
    :param num: Numero[1,9]
    :return: Tabuleiro
    '''
    novo = copy.deepcopy(tab)
    novo[p[0]][p[1]] = num
    return novo


def proximas_possiveis_solucoes(tab):
    '''
    :param tab: Tabuleiro
    :return: List[Tabuleiro]
    '''
    primeiro_vazio = primeiro_espaco_vazio(tab)

    #proximas_solucoes = []
    for n in range(1,10):
        tab_novo = novo_tab(tab,primeiro_vazio,n);
        #proximas_solucoes.append(tab_novo)
        yield tab_novo

    #return proximas_solucoes


def eh_invalido(tab):
    '''

    :param tab: Tabuleiro
    :return: Boolean
    '''
    for unidade in UNIDADES:
        valores = [tab[pos[0]][pos[1]] for pos in unidade]
        for valor in valores:
            if valor != None and valores.count(valor) > 1:
                return True
    return False




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


t_inicial = time.time()

print_matriz(resolver_sudoku(TAB_MAIS_DIFICIL_DO_MUNDO))

t_final = time.time()
print "Tempo de execução =", t_final - t_inicial


