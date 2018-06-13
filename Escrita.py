from Leitura import *

def writeCache(memoriaC, memoriaP, config, endereco, conteudo):
	if(int(endereco)>= config['Blocos']*config['Palavras']):
		print('----> Erro: endereço fora do intervalo!');
		return memoriaP;

	memoriaC = read(config, memoriaC, memoriaP, endereco, True);
	if(config['Mapeamento'] == 1 or (config['Mapeamento'] == 3 and (config['Conjuntos'] == 1 or config['Conjuntos'] == config['Linhas']))):

		num_Bloco = int(endereco)//config['Palavras'];
		linha_Cache = num_Bloco%config['Linhas'];
		palavra = int(endereco)%config['Palavras'];

		memoriaC[linha_Cache][palavra] = memoriaC[linha_Cache][palavra].split('-')
		memoriaC[linha_Cache][palavra][-1] = conteudo;
		memoriaC[linha_Cache][palavra] = '-'.join(memoriaC[linha_Cache][palavra])
		
		print("    * novo valor do endereço "+endereco+" é "+conteudo)
		return memoriaC

	elif(config['Mapeamento'] == 2): # Totalmente Associativo
				
		for key, value in memoriaC.items():
			for i in range(config['Palavras']):
				if(value[i].split('-')[1] == str(endereco)):
					copy_linha = value[i].split('-')
					copy_linha[-1] = conteudo;
					copy_linha = '-'.join(copy_linha);
					memoriaC[key][i] = copy_linha;
					print("    * novo valor do endereço "+endereco+" é "+conteudo)
					return memoriaC;

		print("    * novo valor do endereço "+endereco+" é "+conteudo)
		return new_Cache;
	elif(config['Mapeamento'] == 3):
		# Serve para todos: Random, FIFO, LFU e LRU
		bloco_principal = int(endereco)//config['Palavras']; # Qual bloco na memo principal ele está?
		conjunto = bloco_principal%config['Conjuntos']; # Qual conjunto ele deve estar?

		for k,v in memoriaC[conjunto].items():
			for i in range(config['Palavras']):
				if(v[i].split('-')[1] == str(endereco)):
					copy_linha = v[i].split('-')
					copy_linha[-1] = conteudo;
					copy_linha = '-'.join(copy_linha);
					memoriaC[conjunto][k][i] = copy_linha;
					print("    * novo valor do endereço "+endereco+" é "+conteudo)
					return memoriaC;

def writePRIN(memoriaP, endereco, conteudo, palavras):
	bloco = int(endereco)//palavras;
	palavra = int(endereco)%palavras;

	memoriaP[bloco][palavra] = memoriaP[bloco][palavra].split('-');
	memoriaP[bloco][palavra][-1] = conteudo;
	memoriaP[bloco][palavra] = '-'.join(memoriaP[bloco][palavra]);

	return memoriaP;