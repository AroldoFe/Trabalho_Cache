from Leitura import *

def writeCache(memoriaC, memoriaP, config, endereco, conteudo):
	memoriaC = read(config, memoriaC, memoriaP, endereco, True);
	if(config['Mapeamento'] == 1
		or config['Mapeamento'] == 3 and config['Conjuntos'] == 1
		or config['Mapeamento'] == 2 and config['Substituicao'] == 1):

		num_Bloco = int(endereco)//config['Blocos'];
		linha_Cache = num_Bloco%config['Linhas'];

		# Preciso saber se o bloco está alocado
		for i in range(4):
			if(memoriaC[linha_Cache*4+i].split('-')[2] == endereco):
				linha_subs = memoriaC[linha_Cache*4+i].split('-');
				linha_subs[3] = conteudo;
				memoriaC[linha_Cache*4+i] = '-'.join(linha_subs);
				print("    * novo valor do endereço: "+endereco+"="+conteudo)
				return memoriaC;
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

		print("    * novo valor do endereço: "+endereco+"="+conteudo)
		return new_Cache;

def writePRIN(memoriaP, endereco, conteudo):
	bloco = int(endereco)//4;
	palavra = int(endereco)%4;

	linha_subs = memoriaP[bloco*4+palavra].split('-')
	linha_subs[2] = conteudo
	memoriaP[bloco*4+palavra] = '-'.join(linha_subs);

	return memoriaP;
