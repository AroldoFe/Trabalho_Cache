
def criarCache(config):
	memoriaC = []
	linha = []
	endereco = 0;
	
	for bloco in range( config['Linhas'] ):
		for palavra in range( config['Palavras'] ):
			linha.append(str(bloco)); # linha
			linha.append('0') # bloco
			linha.append('0'); # endereço
			linha.append('0'); # conteudo
			
			if(config['Mapeamento'] == 1 # Direto
				or (config['Mapeamento'] == 3 and config['Conjuntos'] == 1) # Parcialmente asso. com Aleatório
				or (config['Mapeamento'] == 2 and config['Substituicao'] == 1)): # Totalmente associativo com Aleatório
				linha = '-'.join(linha)
			else: # Totalm./parci. assoc. com FIFO, LRU ou LFU
				linha = ['-'.join(linha), 0];
			
			memoriaC.append(linha);
			endereco += 1;
			linha = []; # reseta a linha
	return memoriaC;
	'''elif(config['Mapeamento'] == 2 
		or (config['Mapeamento'] == 3 and config['Conjuntos'] == config['Linhas'])): # Totalmente associativo
		
		if(config['Substituicao'] == 2): # FIFO
			for bloco in range(config['Linhas']):
				for palavra in range(config['Palavras']):
					#aux = []

					linha.append(str(bloco)); # linha
					linha.append('0'); # bloco
					linha.append('0'); # endereço
					linha.append('0'); # conteudo
					linha = ['-'.join(linha), 0];
					#aux.append('-'.join(linha));
					#aux.append('')
					memoriaC.append(linha);
			return memoriaC;
		elif(config['Substituicao'] == 3): # LFU
			for bloco in range(config['Linhas']):
				for palavra in range(config['Palavras']):

					linha.append(str(bloco)); # linha
					linha.append('0'); # bloco
					linha.append('0'); # endereço
					linha.append('0'); # conteudo
					linha = ['-'.join(linha), 0];
					memoriaC.append(linha);
			return memoriaC;
		elif(config['Substituicao'] == 4): # LRU
			for bloco in range(config['Linhas']):
				for palavra in range(config['Palavras']):

					linha.append(str(bloco)); # linha
					linha.append('0'); # bloco
					linha.append('0'); # endereço
					linha.append('0'); # conteudo
					linha = ['-'.join(linha), 0];
					memoriaC.append(linha);
			return memoriaC;
	elif(config['Mapeamento'] == 3): # Parcialmente associativo
		pass
	return memoriaC;'''

def mostrarCache(memoriaC, config):
	print("CACHE L1:");
	print("Linha-Bloco-Endereço-Conteúdo");

	for linha in memoriaC:
		print(linha);