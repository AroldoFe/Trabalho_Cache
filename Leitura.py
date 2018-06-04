
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
	if(config['Mapeamento'] == 1): #Direto
		num_Bloco = int(endereco)//config['Blocos'];
		linha_Cache = num_Bloco%config['Linhas'];
		# Preciso saber se o bloco está alocado
		if(str(num_Bloco) in memoriaC):
			print('HIT linha ' + linha_Cache);
		
		else:
			bloco_Subs = [];
			# Em que bloco o endereço está na memória principal?
			where = int(endereco)//config['Palavras'];
			for i in memoriaP:
				search = i.split('-');
				if(int(search[0]) == where):
					bloco_Subs.append('-'.join(search));
			# Imprime o bloco que vai ser jogado na cache
			print('Bloco que vou substituir')
			print('\n'.join(bloco_Subs))
			# Preciso substituir na cache
			#print((bloco_Subs[0]).split('-')[0])
			bloco_Subs_Cache = []
			for i in memoriaC:
				search = i.split('-');
				# Se estiver na configuração inicial, não escrever na memória
				if(search[1] == 0 and search[2] == 0 and search[3] == 0):
					pass;
				elif(i[0] == linha_Cache):
					bloco_Subs_Cache.append('-'.join(search));
			
			if(len(bloco_Subs_Cache) != 0):
				print('Bloco que devo salvar na RAM');
				print('\n'.join(bloco_Subs_Cache));
				where = (bloco_Subs_Cache[0]).split('-')[0];

				aux = 0;
				for i in memoriaP:
					if(i.split('-')[0] == where):
						i.split('-')[2] == bloco_Subs_Cache[aux].split('-')[3];
						aux += 1;

			# Escrevendo na cache: 
			aux = 0;
			linha_subs = []
			for key, value in enumerate(memoriaC):
				if(memoriaC[key].split('-')[0] == linha_Cache):
					where = value.split('-')[1];
					linha_subs.append(value.split('-')[0]);
					linha_subs.append(bloco_Subs[aux]);
					'-'.join(linha_subs);
					memoriaC[key] = linha_subs;
					aux += 1;
			print('MISS -> Alocado na linha ' + str(linha_Cache) + ' bloco ' + str(where) + ' substituído');
	#elif(config['Mapeamento' == 2]): 