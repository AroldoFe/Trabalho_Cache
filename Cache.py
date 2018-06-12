
def criarCache(config):
	if(config['Mapeamento'] != 3 and config['Conjuntos'] != 1 and config['Conjuntos'] != config['Linhas']):
		memoriaC = []
	else:
		memoriaC = {};
	
	linha = []
	endereco = 0;
	
	auxConjunto = 0;
	if(memoriaC == []):
		for bloco in range( config['Linhas'] ):
			contConjunto = 0;
			contLinhas = 0;
			for palavra in range( config['Palavras'] ):

				linha.append(str(bloco)); # linha
				linha.append('Null-Null-Null') # bloco
				
				if(config['Mapeamento'] == 1 # Direto
					or (config['Mapeamento'] == 3 and config['Conjuntos'] == 1) # Parcialmente asso. com Aleatório
					or (config['Mapeamento'] == 2 and config['Substituicao'] == 1)): # Totalmente associativo com Aleatório
					linha = '-'.join(linha)
				elif(config['Mapeamento'] == 2 or (config['Mapeamento'] == 3 and config['Linhas'] == config['Conjuntos'])): # Totalmente assoc. com FIFO, LRU ou LFU
					linha = ['-'.join(linha), 0];

				memoriaC.append(linha);
				
				endereco += 1;
				linha = []; # reseta a linha

	else:
		aux_linha = 0;

		for i in range(config['Linhas']//config['Conjuntos']):
			# Tenho o número do bloco
			memoriaC[i] = {}
			for j in range(aux_linha, aux_linha+config['Conjuntos']):
				# Tenho linhas por bloco
				memoriaC[i][j] = []
				for w in range(config['Palavras']):
					memoriaC[i][j].append('Null-Null-Null')
				
				if(config['Substituicao'] != 1): # FIFO ou LFU ou LRU
					memoriaC[i][j].append(0);

				aux_linha +=1 
					
	return memoriaC;

def mostrarCache(memoriaC, config):
	print("CACHE L1:");
	print("Linha-Bloco-Endereço-Conteúdo");


	if(config['Mapeamento'] == 3 and config['Conjuntos'] != config['Linhas'] or config['Conjuntos'] != 1):
		for value in memoriaC.values():
			for k,v in value.items():
				for i in range(config['Palavras']):
					if(config['Substituicao']!=1):
						print(str(k)+'-'+str(v[i])+' '+str(v[-1]));
					else:
						print(str(k)+'-'+str(v[i]));
	else:
		for linha in memoriaC:
			if(config['Mapeamento'] == 1
				or (config['Mapeamento'] == 3 and config['Conjuntos'] == 1)
				or (config['Mapeamento'] == 2 and config['Substituicao'] == 1)): print(linha);
			else: print(linha[0], linha[1]);