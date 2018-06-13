from random import randint

def ler():
	file = open('config.txt');
	config = {}
	# Salvando as configurações do arquivo em config
	for line in file:
		line = line.split(': ')
		config[line[0]] = int(line[1].replace("\n", ""));
	file.close()
	return config;

def read(config, memoriaC, memoriaP, endereco, HIT):
	if(int(endereco)>= config['Blocos']*config['Palavras']):
		print('----> Erro: endereço fora do intervalo!');
		return memoriaC;
	# ------------------------------------ Direto ------------------------------------

	if(config['Mapeamento'] == 1 or (config['Mapeamento'] == 3 and config['Conjuntos'] == 1)): # Direto
		num_Bloco = int(endereco)//config['Palavras'];
		linha_Cache = num_Bloco%config['Linhas'];
		palavra = int(endereco)%config['Palavras'];

		# Preciso saber se o bloco está alocado
		if(memoriaC[linha_Cache][palavra].split('-')[1] == endereco):
			print('HIT -> linha ' + str(linha_Cache))
			return memoriaC;
		# Deu MISS
		# Bloco da memória principal na memoria cache
		onde = memoriaC[linha_Cache][0].split('-')[0];
		memoriaC[linha_Cache] = memoriaP[num_Bloco];

		print('MISS -> Alocado na linha ' + str(linha_Cache) + ' bloco ' + str(onde) + ' substituído');
		return memoriaC;

	# ------------------------------------ Totalmente Associativo ------------------------------------

	elif(config['Mapeamento'] == 2 or (config['Mapeamento'] == 3 and config['Conjuntos'] == config['Linhas'])): # Totalmente associativo
		# Não está na cache então devo substituir
		# Em que bloco o endereço está na memória principal?
		onde = int(endereco)//config['Palavras'];
		bloco_Subs = memoriaP[onde];
		# Ja tenho o bloco da principal [Otimização de código]

		# Para os casos de LRU, FIFO e LFU
		if(config['Substituicao'] != 1):
			entradas = [];
			for value in memoriaC.values():
				entradas.append(value[-1]);
			#print(entradas);
			menor = min(entradas);
			maior = max(entradas);

		# Procurando por toda a cache
		for key, value in memoriaC.items():
			for i in range(config['Palavras']):
				if(value[i].split('-')[1] == str(endereco)):
					print('HIT -> linha ' + str(key));
					if(config['Substituicao'] == 3): # LFU
						memoriaC[key][-1] += 1
					elif(config['Substituicao'] == 4): # LRU
						memoriaC[key][-1] += maior+1
					return memoriaC;


		if(config['Substituicao'] == 1): # Aleatória
			# Se tiver lugar, coloca
			for key, value in memoriaC.items():
				if(value[0] == 'Null-Null-Null'):
					memoriaC[key] = bloco_Subs
					print('MISS -> Alocado na linha ' + str(key) + ' bloco Null substituído');
					return memoriaC;

			# Se não estiver cheia
			# Onde colocar? random(0, config['Linhas'])
			linha_Cache = randint(0, config['Linhas']-1);
			memoriaC[linha_Cache] = bloco_Subs
			print('MISS -> Alocado na linha ' + str(linha_Cache) + ' bloco ' + str(onde) + ' substituído');
			return memoriaC;

		elif(config['Substituicao'] != 1):
			for k,v in memoriaC.items():
				if(memoriaC[k][-1] == menor):
					onde = memoriaC[k][0].split('-')[0]
					memoriaC[k] = bloco_Subs;

					if(config['Substituicao'] == 2 or config['Substituicao'] == 4): # FIFO ou LRU
						memoriaC[k].append(maior+1);

					elif(config['Substituicao'] == 3): # LFU
						memoriaC[k].append(1);

					print('MISS -> Alocado na linha ' + str(k) + ' bloco ' + str(onde) + ' substituído');
					return memoriaC;
		
	# ------------------------------------ Parcialmente Associativo ------------------------------------

	elif(config['Mapeamento'] == 3):
		# Serve para todos: Random, FIFO, LFU e LRU
		bloco_principal = int(endereco)//config['Palavras']; # Qual bloco na memo principal ele está?
		conjunto = bloco_principal%config['Conjuntos']; # Qual conjunto ele deve estar?

		# Para os casos de LRU, FIFO e LFU
		if(config['Substituicao'] != 1):
			entradas = [];
			for i in memoriaC[conjunto].values():
				entradas.append(i[-1]);
			#print(entradas);
			menor = min(entradas);
			maior = max(entradas);

		# Caso não esteja na cache já tenho o bloco que devo substituir [Otimização de código]
		# Bloco da memória principal
		bloco_Subs = [];
		# Em que bloco o endereço está na memória principal?
		onde = int(endereco)//config['Palavras'];
		# Pegue esse bloco
		bloco_Subs = memoriaP[onde]
		# Ja tenho o bloco

		# Verificando se está na Cache
		for k,v in memoriaC[conjunto].items():
			for i in range(config['Palavras']):
				if(v[i].split('-')[1] == str(endereco)):
					print('HIT -> linha ' + str(k));
					if(config['Substituicao'] == 3): # LFU
						memoriaC[conjunto][k][-1] += 1
					elif(config['Substituicao'] == 4): # LRU
						memoriaC[conjunto][k][-1] += maior+1
					return memoriaC;

		if(config['Substituicao'] == 1): # Aleatório
			# Onde colocar depois de cheia? random(0, config)
			# Não estando cheia

			for k,v in memoriaC[conjunto].items():
				if(v[0] == 'Null-Null-Null'):
					memoriaC[conjunto][k] = bloco_Subs;
					print('MISS -> Alocado na linha ' + str(k) + ' bloco NULL substituído');
					return memoriaC;
					
			# Estando cheia
			
			linha_Cache = randint(0,len(memoriaC[conjunto].keys())-1); # é inclusive, então poderia dar falha de segmentação
			linha_Cache = list(memoriaC[conjunto].keys())[linha_Cache] # Agora eu tenho a linha que quero susbtituir
			onde = memoriaC[conjunto][linha_Cache][0].split('-')[0] # Pegando o bloco que foi substituído
			memoriaC[conjunto][linha_Cache] = bloco_Subs 
			
			print('MISS -> Alocado na linha ' + str(linha_Cache) + ' bloco ' + str(onde) + ' substituído');

			return memoriaC
		elif(config['Substituicao'] != 1): # FIFO, LRU ou LFU
			# Não está na cache então devo substituir
			# Vou substituir no que tem o menor valor associado

			for k,v in memoriaC[conjunto].items():
				if(memoriaC[conjunto][k][-1] == menor):
					onde = memoriaC[conjunto][k][0].split('-')[0]
					memoriaC[conjunto][k] = bloco_Subs;

					if(config['Substituicao'] == 2 or config['Substituicao'] == 4): # FIFO ou LRU
						memoriaC[conjunto][k].append(maior+1);

					elif(config['Substituicao'] == 3): # LFU
						memoriaC[conjunto][k].append(1);

					print('MISS -> Alocado na linha ' + str(k) + ' bloco ' + str(onde) + ' substituído');
					return memoriaC;