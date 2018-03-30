"""Função que varre todos os indices de um array e retorna seus valores identados"""

import sys

# O padrao do argumento fh é a saida padrao do print. Se definido, 
# é o apontamento para o arquivc q sera salvo o resultado da funçao

def array_ident(lista, ident=False, level=0, fh=sys.stdout):
    for indice in lista:
        #Verifica se o argumento inserido é uma lista
        if isinstance(indice, list):
            # Retorna a função recursivamente
            array_ident(indice, ident, level+1, fh)
        else:
            if ident:
                for tab_stop in range(level):
                    print("\t", end='', file=fh)
            print(indice, file=fh)

""" 
############ EXEMPLO DE USO ############

movies = ["The holy grail", 1975, "Terry Jones", 91,["Graham Chapman",["Michael","Terry","Joe","Bulba"]]]

"""