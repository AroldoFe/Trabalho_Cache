
def criarCache(config):
	memoriaC = {};
	linha = []

	for i in range(config['Palavras']): # Criando os valores Null's
		linha.append('Null-Null-Null');
	
	if(config['Mapeamento'] != 3):
		for i in range(config['Linhas']):
			memoriaC[i] = linha;
			if(config['Mapeamento'] == 2 and config['Substituicao'] != 1):
				memoriaC[i].append(0);
		return memoriaC;
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

				aux_linha += 1 
					
		return memoriaC;

def mostrarCache(memoriaC, config):
	print("CACHE L1:");
	print("Linha-Bloco-Endereço-Conteúdo");


	if(config['Mapeamento'] == 3):
		for value in memoriaC.values():
			for k,v in value.items():
				for i in range(config['Palavras']):
					if(config['Substituicao']!=1):
						print(str(k)+'-'+str(v[i])+' ....... '+str(v[-1]));
					else:
						print(str(k)+'-'+str(v[i]));
	else:
		for key,value in memoriaC.items():
			for i in range(config['Palavras']):
				if(config['Mapeamento'] != 1 and config['Substituicao'] != 1):
					print(str(key)+'-'+str(value[i])+' ....... '+str(value[-1]));
				else:
					print(str(key)+'-'+str(value[i]));