from Leitura import *

def writeCache(memoriaC, memoriaP, config, endereco, conteudo):
	memoriaC = read(config, memoriaC, memoriaP, endereco, True);
	if(config['Mapeamento'] == 1
		or config['Mapeamento'] == 3 and config['Conjuntos'] == 1
		or config['Mapeamento'] == 2 and config['Substituicao'] == 1):
		new_Cache = []
		for i in memoriaC:
			if(i.split('-')[2] == endereco):
				i = i.split('-');
				#velho_conteudo == i[3];
				i[3] = conteudo;
				new_Cache.append('-'.join(i))
			else:
				new_Cache.append(i);
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
	new_RAM = []
	for i in memoriaP:
		if(i.split('-')[1] == endereco):
			i = i.split('-');
			i[2] = conteudo;
			new_RAM.append('-'.join(i))
		else:
			new_RAM.append(i);

	return new_RAM;
