
def criarCache(config):
	memoriaC = []
	linha = []
	endereco = 0;
	
	for bloco in range( config['Linhas'] ):
		contConjunto = 0;
		auxConjunto = 0;
		contLinhas = 0;
		for palavra in range( config['Palavras'] ):

			linha.append(str(bloco)); # linha
			linha.append('0') # bloco
			linha.append('0'); # endereço
			linha.append('0'); # conteudo
			
			if(config['Mapeamento'] == 1 # Direto
				or (config['Mapeamento'] == 3 and config['Conjuntos'] == 1) # Parcialmente asso. com Aleatório
				or (config['Mapeamento'] == 2 and config['Substituicao'] == 1)): # Totalmente associativo com Aleatório
				linha = '-'.join(linha)
			elif(config['Mapeamento'] == 2 or (config['Mapeamento'] == 3 and config['Linhas'] == config['Conjuntos'])): # Totalmente assoc. com FIFO, LRU ou LFU
				linha = ['-'.join(linha), 0];

			memoriaC.append(linha);
			endereco += 1;
			linha = []; # reseta a linha
	return memoriaC;

def mostrarCache(memoriaC, config):
	print("CACHE L1:");
	print("Linha-Bloco-Endereço-Conteúdo");

	for linha in memoriaC:
		if(config['Mapeamento'] == 1
			or (config['Mapeamento'] == 3 and config['Conjuntos'] == 1)
			or (config['Mapeamento'] == 2 and config['Substituicao'] == 1)): print(linha);
		else: print(linha[0]);