from Cache import *
from Principal import *
from Show import *
from Leitura import *

def main():
	# Lendo o arquivo de configuração
	config = ler();
	# Criando a Memória Cache
	memoriaC = criarCache(config);
	# Criando a Memória Principal
	memoriaP = criarPrincipal(config);
	# Escolhendo o que se deseja fazer
	resposta = input("Digite o comando ou digite SAIR para sair: ")
	resposta = resposta.lower()
	
	while(resposta != 'sair'):
		resposta = resposta.split(" ");
		#mostrando as memórias
		if(resposta[0] == "show"):
			show(memoriaC, memoriaP, config);
		elif(resposta[0] == "read"):
			memoriaC = read(config, memoriaC, memoriaP, resposta[1]);
		elif(resposta[0] == "write"):
			break;
		else:
			print("Erro: opção inválida!");
		
		resposta = input("Digite o comando ou digite SAIR para sair: ")
		resposta = resposta.lower()


main();