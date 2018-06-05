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

def read(config, memoriaC, memoriaP, endereco):
	if(config['Mapeamento'] == 1 or(config['Mapeamento'] == 3 and config['Conjuntos'] == 1)): #Direto
		num_Bloco = int(endereco)//config['Blocos'];
		linha_Cache = num_Bloco%config['Linhas'];
		# Preciso saber se o bloco está alocado
		if(str(num_Bloco) in memoriaC):
			print('HIT linha ' + str(linha_Cache));
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
			esta = False;
			for i in memoriaC:
				if(i.split('-')[2] == str(endereco)):
					print('HIT linha ' + i.split('-')[0]);
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
			onde = str(randint(0, config['Linhas']+1));
			
			aux = 0;
			new_Cache = []
			for i in memoriaC:
				if(i.split('-')[0] == onde):
					linha_subs = []
					linha_subs.append(i.split('-')[0]);
					linha_subs.append(bloco_Subs[aux]);
					new_Cache.append('-'.join(linha_subs));
					aux += 1;
				else:
					new_Cache.append(i);
			return new_Cache;
		elif(config['Substituicao'] == 2): # FIFO
			return memoriaC;