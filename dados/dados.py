def sanitize(time_string):
	if '-' in time_string:
		separador = '-'
	elif ':' in time_string:
		separador = ':'
	else:
		return(time_string)	

	(mins, secs) = time_string.split(separador)

	return (mins + '.' + secs)

def pega_lista_tempo(arquivo):
	try:
		with open(arquivo) as arq:
			data = arq.readline()
		return(data.strip().split(','))

	except IOError as ioerr:
		print("File error: " + str(ioerr))
		return(None)	

james = pega_lista_tempo('james.txt')
julie = pega_lista_tempo('julie.txt')
mikey = pega_lista_tempo('mikey.txt')
sarah = pega_lista_tempo('sarah.txt')


# Método 'compreensão da lista' - Sem necessidade do método append
james = [sanitize(linha) for linha in james]

# Método 'compreensão da lista' - Sem necessidade do método append
julie = [sanitize(linha) for linha in julie]

# Método 'compreensão da lista' - Sem necessidade do método append
mikey = [sanitize(linha) for linha in mikey]

# Método 'compreensão da lista'
sarah = [sanitize(linha) for linha in sarah]

james_unica = sorted(set(james))
julie_unica = sorted(set(julie))
mikey_unica = sorted(set(mikey))
sarah_unica = sorted(set(sarah))


print(james_unica[0:3])

print(julie_unica[0:3])

print(mikey_unica[0:3])

print(sarah_unica[0:3])
