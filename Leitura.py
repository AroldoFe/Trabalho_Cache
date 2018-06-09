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
		num_Bloco = int(endereco)//config['Blocos'];
		linha_Cache = num_Bloco%config['Linhas'];

		# Preciso saber se o bloco está alocado
		for i in memoriaC:
			if(endereco == i.split('-')[2]):
				if(HIT):
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

			#for i in bloco_Subs:
			#	print(i);

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
			for key, value in enumerate(memoriaC):
				if(value[0].split('-')[2] == str(endereco)):
					if(HIT):
						print('HIT -> linha ' + value[0].split('-')[0]);
					memoriaC[key][1] += 1;
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
					linha_subs = ['-'.join(linha_subs), max(entradas)+1]
					#print(linha_subs);
					new_Cache.append(linha_subs);
					aux += 1;
				else:
					new_Cache.append(i);

			print('MISS -> Alocado na linha ' + linha_Cache + ' bloco ' + onde + ' substituído');
		
		return new_Cache;
