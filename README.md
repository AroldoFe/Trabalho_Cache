<h1>Trabalho sobre Cache</h1>

<h2>Autor</h2>
Aroldo Felix Pereira Júnior

<h2>Descrição</h2>
<p>Neste tópico são abordadas características sobre o trabalho.</p>

<h3>Geral</h3>
<p>Projeto desenvolvido na liguagem Python 3 que simula o comportamento da memória Cache L1 e a principal. <br>
<ul>
  <li>Mapeamentos:
    <ol type="a">
      <li> Direto 
      <li> Totalmente Associativo
      <li> Parcialmente Associativo
    </ol>
  <li>Substituições:
    <ol>
      <li> Aleatória
      <li> First In First Out (FIFO)
      <li> Least Frequently Used (LFU)
    </ol>
</ul>
<p> Não foi possível concluir o mapeamento Parcialmente Associativo além de quando a quantidade de conjuntos é 
igual a 1 (usa-se mapeamento direto)  ou igual à quantidade de linhas da cache (usa-se mapeamento totalmente associativo).
<p>Sobre a coerência de dados entre Cache e Principal, foi-se decidido utilizar o método write-through, devido a simples implementação e para evitar a substituição do bloco que está para sair da cache na memória principal, já que estão sincronizados.
  
<h3> Bibliotecas Externas</h3>
<p> Foi usada a biblioteca Random para geração de números aleatórios tanto para
criação da cache quanto para o método de substituição de bloco aleatório.

<h3>Bibliotecas Internas</h3>
Aqui são explicadas as funções externas ao programa main criadas pelo autor do trabalho.
<p>Cache: arquivo onde as funções criarCache e mostrarCache são implementadas, nomes autoexplicativos.
<p>Escrita: arquivo onde as funções writeCache e writePRIN são implementadas, writeCache é a função
que escreve na cache, de maneira análoga, writePRIN na memória Principal.
<p>Leitura: arquivo onde as funções ler e read são implementadas. 
A função ler é para leitura do arquivo de configuração "config.txt". 
A função read é para leitura na cache para dar HIT ou MISS.
<p>Principal: arquivo onde as funções criarPrincipal e mostrarPrincipal são implementadas, 
imilarmente a ao arquivo Cache, porém em relação a memória Principal.
<p>Show: arquivo cuja função show é implementada, ela chama mostrarCache e mostrarPrincipal.

<h2> Compilação</h2>
<p> Para compilar basta digitar no terminal: (Se python 3 for o padrão, se não for)<br>
<ul>
  <li>Se python 3 for a versão padrão: $ python main.py
  <li>Se python 2 for a versão padrao: $ python3 main.py
</ul>

<h2>Execução</h2>
Na execução, quatro códigos são possíveis: read, write, show e quit.
<ul>
  <li>A opção READ tem o seguinte formato: "read A", tal que A é um endereço da memória principal, e tem saída "HIT->Linha X" 
  quando se encontra na X-ésima linha da Cache L1, ou "MISS -> Alocado na linha X, bloco Y substituído", quando não se 
  encontra na cache e então é buscado na memória o bloco em que se encontra. Quando Alocado na cache mostra em que linha se 
  encontra (X) e qual bloco estava lá anteriormente (Y).
  <li>A opção WRITE tem o seguinte formato: "write A B", tal que A é um endereço da memória principal e B  o conteúdo que 
  será guardado no endereço A. Primeiramente, dá-se um "read A" na cache para saber se o endereço está lá ou deve ser colocado,
  se precisar, já é colocado e mostra onde foi colocado. Enfim, é mostrado como saída "novo valor do endereço A=B".
  <li>A opção SHOW não possui argumento, então é executada assim "show" e tem como saída o estado da memória Cache e da Principal.
  <li>A opção QUIT não possui argumento, então é executada assim "quit" e serve para a finalização do loop e encerramento do programa.
</ul>
<h2>Link para o repositório no Github</h2>
https://github.com/AroldoFe/Trabalho_Cache
