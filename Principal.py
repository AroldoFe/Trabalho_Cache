from random import randint

def criarPrincipal(config):
	memoriaP = [];
	linha = []
	endereco = 0;
	for bloco in range( config['Blocos'] ):
		for palavra in range( config['Palavras'] ):
			linha.append(str(bloco)); # bloco 
			linha.append(str(endereco)); # endereço
			linha.append(str(randint(0,127))); # conteudo
			memoriaP.append('-'.join(linha));
			endereco += 1;
			linha = []; # reseta a linha

	return memoriaP;

def mostrarPrincipal(memoriaP):
	print("\nMEMÓRIA PRINCIPAL:");
	print("Linha-Bloco-Endereço-Conteúdo");

	for linha in memoriaP:
		print(linha);
