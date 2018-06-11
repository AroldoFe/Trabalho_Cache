from Leitura import *

def writeCache(memoriaC, memoriaP, config, endereco, conteudo):
	memoriaC = read(config, memoriaC, memoriaP, endereco, True);
	if(config['Mapeamento'] == 1
		or config['Mapeamento'] == 3 and config['Conjuntos'] == 1
		or config['Mapeamento'] == 2 and config['Substituicao'] == 1):

		num_Bloco = int(endereco)//config['Palavras'];
		linha_Cache = num_Bloco%config['Linhas'];
		palavra = int(endereco)%config['Palavras'];

		if(memoriaC[linha_Cache*config['Palavras']+palavra].split('-')[2] == str(endereco)):
			linha_subs = memoriaC[linha_Cache*config['Palavras']+palavra].split('-');
			linha_subs[3] = conteudo;
			memoriaC[linha_Cache*config['Palavras']+palavra] = '-'.join(linha_subs);
			print("    * novo valor do endereço: "+endereco+" é "+conteudo)
		return memoriaC

	elif(config['Mapeamento'] == 2 or config['Mapeamento'] == 3 and config['Linhas'] == config['Conjuntos']): # Totalmente Associativo
		new_Cache = []
		for i in memoriaC:
			if(i[0].split('-')[2] == endereco):
				linha = i[0].split('-');
				linha[3] = conteudo;
				linha = '-'.join(linha)
				if(config['Substituicao'] == 1): # Random
					new_Cache.append(linha)
				elif(config['Substituicao'] == 2): # FIFO
					new_Cache.append([linha, i[1]])
				else: 								# LFU
					new_Cache.append([linha, i[1]])
			else:
				if(config['Substituicao']!=3): new_Cache.append(i);
				else:
					i[1] += 1
					new_Cache.append(i);

		print("    * novo valor do endereço: "+endereco+" é "+conteudo)
		return new_Cache;

def writePRIN(memoriaP, endereco, conteudo, palavras):
	bloco = int(endereco)//palavras;
	palavra = int(endereco)%palavras;

	linha_subs = memoriaP[bloco*palavras+palavra].split('-')
	linha_subs[2] = conteudo
	memoriaP[bloco*palavras+palavra] = '-'.join(linha_subs);

	return memoriaP;
