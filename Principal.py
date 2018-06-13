from random import randint

def criarPrincipal(config):
	memoriaP = {};
	linha = []
	endereco = 0;
	for bloco in range( config['Blocos'] ):
		memoriaP[bloco] = [];
		for palavra in range( config['Palavras'] ):
			linha.append(str(bloco)); # bloco 
			linha.append(str(endereco)); # endereço
			linha.append(str(randint(1,127))); # conteudo
			memoriaP[bloco].append('-'.join(linha));
			endereco += 1;
			linha = []; # reseta a linha

	return memoriaP;

def mostrarPrincipal(memoriaP, config):
	print("\nMEMÓRIA PRINCIPAL:");
	print("Bloco-Endereço-Conteúdo");

	for value in memoriaP.values():
		for i in range(config['Palavras']):
			print(str(value[i]));