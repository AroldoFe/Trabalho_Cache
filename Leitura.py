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
	if(config['Mapeamento'] == 1 or(config['Mapeamento'] == 3 and config['Conjuntos'] == 1)): #Direto ou parcialmente associativo com conjuntos de tamanho 1
		num_Bloco = int(endereco)//config['Palavras'];
		linha_Cache = num_Bloco%config['Linhas'];
		palavra = int(endereco)%config['Palavras'];

		# Preciso saber se o bloco está alocado
		if(memoriaC[linha_Cache*(config['Palavras'])+palavra].split('-')[2] == endereco):
				print('HIT linha ' + str(linha_Cache))
				return memoriaC;
		# Deu MISS

		bloco_Subs = [];
		# Em que bloco o endereço está na memória principal?
		onde = int(endereco)//config['Palavras'];
		for i in memoriaP:
			search = i.split('-');
			if(int(search[0]) == onde):
				bloco_Subs.append('-'.join(search));

		# Escrevendo na cache: 
		aux = 0;
		new_Cache = [];
		for i in memoriaC:
			if(i.split('-')[0] == str(linha_Cache)):
				linha_subs = []
				onde = i.split('-')[1];
				linha_subs.append(i.split('-')[0]);
				linha_subs.append(bloco_Subs[aux]);
				new_Cache.append('-'.join(linha_subs));
				aux += 1;
			else:
				new_Cache.append(i);

		print('MISS -> Alocado na linha ' + str(linha_Cache) + ' bloco ' + str(onde) + ' substituído');
		return new_Cache;

	elif(config['Mapeamento'] == 2 or (config['Mapeamento'] == 3 and config['Conjuntos'] == config['Linhas'])): # Totalmente associativo
		if(config['Substituicao'] == 1): # Aleatório
			for i in memoriaC:
				if(i.split('-')[2] == str(endereco)):
					if(HIT):
						print('HIT -> linha ' + i.split('-')[0]);
					return memoriaC;

			# Não está na cache então devo substituir
			# Bloco da memória principal
			bloco_Subs = [];
			# Em que bloco o endereço está na memória principal?
			onde = int(endereco)//config['Palavras'];
			for i in memoriaP:
				search = i.split('-');
				if(int(search[0]) == onde):
					bloco_Subs.append('-'.join(search));
			# Ja tenho o bloco
			# Onde colocar? random(0, config)
			linha_Cache = str(randint(0, config['Linhas']+1));
			
			aux = 0;
			new_Cache = []
			for i in memoriaC:
				
				if(i.split('-')[0] == linha_Cache):
					onde = i.split('-')[1]
					linha_subs = []
					linha_subs.append(i.split('-')[0]);
					linha_subs.append(bloco_Subs[aux]);
					new_Cache.append('-'.join(linha_subs));
					aux += 1;
				else:
					new_Cache.append(i);

			print('MISS -> Alocado na linha ' + str(linha_Cache) + ' bloco ' + str(onde) + ' substituído');
			
		elif(config['Substituicao'] == 2): # FIFO
			for i in memoriaC:
				if(i[0].split('-')[2] == str(endereco)):
					if(HIT):
						print('HIT -> linha ' + i[0].split('-')[0]);
					return memoriaC;

			# Não está na cache então devo substituir
			# Bloco da memória principal
			bloco_Subs = [];
			# Em que bloco o endereço está na memória principal?
			onde = int(endereco)//config['Palavras'];
			for i in memoriaP:
				search = i.split('-');
				if(int(search[0]) == onde):
					bloco_Subs.append('-'.join(search));
			# Ja tenho o bloco
			# Vou substituir no que tem o menor valor associado
			# Vetor com valores auxiliares
			entradas = [];
			for i in memoriaC:
				entradas.append(i[1]);
			menor = min(entradas);

			aux = 0;
			new_Cache = []
			for i in memoriaC:	
				if(i[1] == menor and aux < 4):
					linha_Cache = i[0].split('-')[0]
					onde = i[0].split('-')[1]
					linha_subs = []
					linha_subs.append(i[0].split('-')[0]); # Linha da cache
					linha_subs.append(bloco_Subs[aux]); # Linha da principal
					linha_subs = ['-'.join(linha_subs), max(entradas)+1]
					#print(linha_subs);
					new_Cache.append(linha_subs);
					aux += 1;
				else:
					new_Cache.append(i);

			print('MISS -> Alocado na linha ' + linha_Cache + ' bloco ' + onde + ' substituído');
			
		elif(config['Substituicao'] == 3): # LFU
			onde = int(endereco)//config['Palavras'];

			for key, value in enumerate(memoriaC):
				if(value[0].split('-')[1] == str(onde)): # Bloco
					memoriaC[key][1] += 1;

			for key, value in enumerate(memoriaC):
				if(value[0].split('-')[2] == str(endereco)):
					if(HIT):
						print('HIT -> linha ' + value[0].split('-')[0]);
					return memoriaC;

			# Não está na cache então devo substituir
			# Bloco da memória principal
			bloco_Subs = [];
			# Em que bloco o endereço está na memória principal?
			onde = int(endereco)//config['Palavras'];
			for i in memoriaP:
				search = i.split('-');
				if(int(search[0]) == onde):
					bloco_Subs.append('-'.join(search));
			# Ja tenho o bloco

			# Vou substituir no que tem o menor valor associado
			# Vetor com valores auxiliares
			entradas = [];
			for i in memoriaC:
				entradas.append(i[1]);
			menor = min(entradas);

			aux = 0;
			new_Cache = []
			for i in memoriaC:	
				if(i[1] == menor and aux < 4):
					linha_Cache = i[0].split('-')[0]
					onde = i[0].split('-')[1]
					linha_subs = []
					linha_subs.append(i[0].split('-')[0]);
					linha_subs.append(bloco_Subs[aux]);
					linha_subs = ['-'.join(linha_subs), 1]
					#print(linha_subs);
					new_Cache.append(linha_subs);
					aux += 1;
				else:
					new_Cache.append(i);

			print('MISS -> Alocado na linha ' + linha_Cache + ' bloco ' + onde + ' substituído');
		
		elif(config['Substituicao'] == 4): # LRU
			onde = int(endereco)//config['Palavras'];

			#Preciso saber qual o próximo ciclo
			entradas = [];
			for i in memoriaC:
				entradas.append(i[1]);
			menor = min(entradas);
			
			for key, value in enumerate(memoriaC):
				if(value[0].split('-')[2] == str(endereco)):
					if(HIT):
						print('HIT -> linha ' + value[0].split('-')[0]);
						for key2, value2 in enumerate(memoriaC):
							if(value2[0].split('-')[1] == str(onde)):
								memoriaC[key2][1] = max(entradas) + 1;
					return memoriaC;

			# Não está na cache então devo substituir
			# Bloco da memória principal
			bloco_Subs = [];
			# Em que bloco o endereço está na memória principal?
			onde = int(endereco)//config['Palavras'];
			for i in memoriaP:
				search = i.split('-');
				if(int(search[0]) == onde):
					bloco_Subs.append('-'.join(search));
			# Ja tenho o bloco

			aux = 0;
			new_Cache = []
			for i in memoriaC:	
				if(i[1] == menor and aux < 4):
					linha_Cache = i[0].split('-')[0]
					onde = i[0].split('-')[1]
					linha_subs = []
					linha_subs.append(i[0].split('-')[0]);
					linha_subs.append(bloco_Subs[aux]);
					linha_subs = ['-'.join(linha_subs), max(entradas)+1]
					new_Cache.append(linha_subs);
					aux += 1;
				else:
					new_Cache.append(i);

			print('MISS -> Alocado na linha ' + linha_Cache + ' bloco ' + onde + ' substituído');

		return new_Cache;
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
		for i in memoriaP:
			search = i.split('-');
			if(int(search[0]) == onde):
				bloco_Subs.append('-'.join(search));
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
		elif(config['Substituicao'] == 2 or config['Substituicao'] == 4): # FIFO ou LRU
			# Não está na cache então devo substituir
			# Vou substituir no que tem o menor valor associado

			for k,v in memoriaC[conjunto].items():
				if(memoriaC[conjunto][k][-1] == menor):
					onde = memoriaC[conjunto][k][0].split('-')[0]
					memoriaC[conjunto][k] = bloco_Subs;
					memoriaC[conjunto][k].append(maior+1);
					print('MISS -> Alocado na linha ' + str(k) + ' bloco ' + str(onde) + ' substituído');
					return memoriaC;
		elif(config['Substituicao'] == 3): # LFU
			# Não está na cache então devo substituir
			# Vou substituir no que tem o menor valor associado

			for k,v in memoriaC[conjunto].items():
				if(memoriaC[conjunto][k][-1] == menor):
					onde = memoriaC[conjunto][k][0].split('-')[0]
					memoriaC[conjunto][k] = bloco_Subs;
					memoriaC[conjunto][k].append(1);
					print('MISS -> Alocado na linha ' + str(k) + ' bloco ' + str(onde) + ' substituído');
					return memoriaC;