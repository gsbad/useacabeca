import array_ident 
import pickle; # O pickle dump gera um arquivo de dump binário

''' Cria duas listas '''
man = []
otherman = []

''' Executa os comandos em try, o except filtra o erro '''
try:
	arquivo = 'sketch.txt'

	data = open(arquivo)
	# Cria um laço iterando linha a linha do arquivo aberto
	for linha in data:
	    # Tenta quebrar essa string de linha com o dois-pontos como separador e atribui a variaveis
	    try:
		    (dono, fala) = linha.split(':',1) # o atributo maxsplit esta definido como 1
		    fala = fala.strip() # Corta os espaços em branco
		    if dono == 'Man':
		    	man.append(fala) # Usa o identificador man, q é uma lista, para chamar a funçao append e adicionar a fala à lista
		    elif dono == 'Other Man':
		    	otherman.append(fala)		    	
	    except ValueError:
		    pass

except IOError as err:
	print('O arquivo solicitado não foi encontrado. Erro: ', err)

# O finally é executado de qualquer forma
finally:
	#mas antes testa a instancia data, q pode n ter sido criada
	if 'data' in locals():
		data.close()

''' Utiliza os dois arrays criados para salvar em arquivos separados  '''
try:
	# Abre os arquivos em modo gravação 'w', p usar c array_ident, 'wb' para uso c pickes
	with open('man_data.txt', 'wb') as man_file: #o with garante a abertura da instancia, e remove a necessidade do finally
		#array_ident.array_ident(man, fh=man_file)
		pickle.dump(man, man_file)

	with open('other_data.txt', 'wb') as otherman_file:
		#array_ident.array_ident(otherman, fh=otherman_file)	
		pickle.dump(otherman, otherman_file)

	# Imprime o conteudo de man e otherman refereciando as instancias de arquivos
	
except IOError as err:
	print('Erro no salvamento do arquivo: ', str(err))

# Except padrao do pickle
except pickle.PickleError as perr:
	print('Pickling error: ' + str(perr))


''' Lê os arquivos gerados em modos pickes com load '''

new_man = []
new_otherman = []

try:
	# With Duplo, separado por virgulas
	with open('man_data.txt','rb') as pickle_man, open('other_data.txt','rb') as pickle_otherman:
		new_man = pickle.load(pickle_man)
		new_otherman = pickle.load(pickle_otherman)	

except IOError as err:
	print('Erro no salvamento do arquivo: ', str(err))

# Except padrao do pickle
except pickle.PickleError as perr:
	print('Pickling error: ' + str(perr))


# Exibe os arquivos
array_ident.array_ident(new_man)
array_ident.array_ident(new_otherman)
