"""Função que varre todos os indices de um array e retorna seus valores identados"""
def array_ident(lista):
    for indice in lista:
        #Verifica se o argumento inserido é uma lista
        if isinstance(indice, list):
            # Retorna a função recursivamente
            array_ident(indice)
        else:
            # Imprime o item
            print(indice)
print("importado!")
