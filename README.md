# Trabalho de Implementação de Buscas

O objetivo do trabalho é implementar um agente inteligente que utiliza
algoritmos de busca para encontrar a solução para o jogo Sokoban
(https://en.wikipedia.org/wiki/Sokoban). O agente deve mostrar a
solução encontrada.
Implementar e comparar os seguintes algoritmos de busca:
* largura
* profundidade
* profundidade iterativa
* A* (utilizar ao menos 1 função heurística).

Para implementação, utilize a biblioteca de busca fornecida pelo professor Jomi Hubner (UFSC),
disponível em http://jomi.das.ufsc.br/ia/busca/buscaJava/index.html

O agente deve executar os algoritmos de busca nos 10 levels fornecidos no arquivo.
Para entender o formato dos arquivos, consulte o link:
http://www.sokobano.de/wiki/index.php?title=How_to_play_Sokoban


Para entrega, a equipe deve elaborar um relatório técnico, no formato da SBC, contendo as seções a
seguir, devidamente explicadas. O tamanho máximo do relatório é 6 páginas:

* Resumo
* Introdução
* Representação de estado
  * como a equipe representa um estado? qual estrutura de dados? o que armazena cada
campo/posição? a equipe deve elaborar figuras ilustrativas para explicar.
* Heurística utilizada
    * descrever e explicar a heurística utilizadas pela equipe, justificando por que é admissível.
    * colocar uma figura de um estado do jogo, explicar e exemplificar o cálculo da heurística.
    * um exemplo de heurística pode ser encontrada na Tese de Doutorado de André Grahl
Pereira, disponível no link: https://lume.ufrgs.br/handle/10183/149574
* Ambiente de simulação utilizado
    * qual o hardware da máquina? velocidade da CPU? quantidade de memória? versão do
sistema operacional? versão do Java (ou outro compilador/VM)?
* Resultados
    * detalhar os resultados obtidos para os diferentes algoritmos de busca em cada um dos
10 levels do dataset.
    * apresentar uma tabela para detalhar os resultados, mostrando o tempo (em segundos) e
quantidade de estados visitados para cada caso.
o explicar textualmente os resultados, enfatizando os motivos das diferenças de valores.
* Conclusões
    * apresentar as conclusões da equipe a respeito dos experimentos, explicando qual
algoritmo teve os melhores resultados e por que.

O link a seguir apresenta um exemplo de relatório, para que a equipe possa verificar como se escreve
um relatório técnico: organização do conteúdo, figuras, gráficos, etc. É altamente recomendado que a
equipe leia o exemplo para saber como fazer o seu.
http://www.repositorio.ufop.br/handle/123456789/1624


____

* Como baixar o dataset xsokoban (http://www.cs.cornell.edu/andru/xsokoban.html)

* Baixar o source code do xsokoban, disponível na opção “The source code for various versions”.

* Descompactar o arquivo .tar.gz. Os levels estão no diretório xsokoban/screens.

* Cada level está em um arquivo texto cujo nome segue o padrão “screen.X”, onde X é o level.

* Para entender o formato dos arquivos, consulte o link:
    * http://www.sokobano.de/wiki/index.php?title=How_to_play_Sokoban