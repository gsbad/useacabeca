"""Função que varre todos os indices de um array e retorna seus valores identados"""
def array_ident(lista, ident=False, level=0):
    for indice in lista:
        #Verifica se o argumento inserido é uma lista
        if isinstance(indice, list):
            # Retorna a função recursivamente
            array_ident(indice, ident, level+1)
        else:
            if ident:
                for tab_stop in range(level):
                    print("\t", end='')
            print(indice)

""" 
############ EXEMPLO DE USO ############

movies = ["The holy grail", 1975, "Terry Jones", 91,["Graham Chapman",["Michael","Terry","Joe","Bulba"]]]

"""