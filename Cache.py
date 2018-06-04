
def criarCache(config):
	memoriaC = []
	linha = []
	endereco = 0;

	for bloco in range( config['Linhas'] ):
		for palavra in range( config['Palavras'] ):
			linha.append(str(bloco)); # linha
			linha.append('0') # bloco
			linha.append('0'); # endereço
			linha.append('0'); # conteudo
			memoriaC.append('-'.join(linha)); 
			#memoriaC.append(linha);
			endereco += 1;
			linha = []; # reseta a linha

	return memoriaC;

def mostrarCache(memoriaC):
	print("CACHE L1:");
	print("Linha-Bloco-Endereço-Conteúdo");

	for linha in memoriaC:
		print(linha);
	print('\n');