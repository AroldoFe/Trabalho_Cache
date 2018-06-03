
def ler():
	file = open('config.txt');
	config = {}
	# Salvando as configurações do arquivo em config
	for line in file:
		line = line.split(': ')
		config[line[0]] = int(line[1].replace("\n", ""));
	file.close()
	return config;

def lerCache(config, memoriaC, memoriaP, endereco):
	if(config['Mapeamento'] == 1): #Direto
		linha = int(endereco)//config['Linhas'];
		print(linha);
	#elif(config['Mapeamento' == 2]): 