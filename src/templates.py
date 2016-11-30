#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 05/12/2014

@author: helio
'''

'''Template para busca em profundidade com backtracking (retorna uma solucao)'''

'''
def funcao_backtracking(x):
    
   if estah_resolvido(x):
        return x
    else:
        for t in proximas_possiveis_solucoes(x):  #de preferencia retorna um gerador
            if not eh_invalido(t):
                tentativa = funcao_backtracking(t) #testa um proximo / filho
                if tentativa:  #aqui ocorre o backtracking da solução caso encontrada
                    return tentativa     
        return False

        
'''

''' Template para busca em profundidade
    com backtracking (para varias solucoes)'''

'''
def funcao_backtracking_gen(x):
    if estah_resolvido(x):
        yield x
    else:
        for t in proximas_possiveis_solucoes(x):  
            if not eh_invalido(t):
                for tentativa in funcao_backtracking_gen(t): 
                    if tentativa: 
                        yield tentativa 


cont = 1    
for solucao in funcao_backtracking_gen():
    print cont," : ",solucao
    cont+=1
'''

