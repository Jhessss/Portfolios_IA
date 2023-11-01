# Portfólio - Parte 2

Parte 2 do portfólio da matéria Inteligência Artificial a respeito dos tópicos: Agente de soluções de problemas, Problemas de malha aberta e de malha fechada, 
Algoritmos de busca(busca cega, busca informada), Funções heurísticas, Busca em ambientes complexos e Algoritmos genéticos.

## Impressões iniciais

Nessa parte dois do portfólio, começamos a ver na prática os tipos de algoritmos que são fundamentais para a compreensão da Inteligência Artificial. Inicialmente, o nome dos conteúdos e a variedade de abordagens algorítmicas podem parecer desafiadoras. No entanto, à medida que exploramos agentes de soluções de problemas, problemas de malha aberta e de malha fechada, algoritmos de busca, funções heurísticas, busca em ambientes complexos e algoritmos genéticos, fica evidente a fascinante interseção entre a lógica computacional e a resolução de problemas do mundo real. 

## Apresentação do Conteúdo

🔵 Agente de soluções de problemas.

Um agente de soluções de problemas, no contexto da Inteligência Artificial, é um sistema que busca ativamente resolver questões ou desafios por meio de ações e tomada de decisões [1]. Esses agentes são essenciais para lidar com problemas complexos e dinâmicos. Eles podem ser classificados em agentes de malha aberta e agentes de malha fechada.

🔵 Problemas de malha aberta e de malha fechada.

Agentes de Malha Aberta: São agentes que tomam decisões com base em informações limitadas e não têm uma visão completa do ambiente. Eles dependem de estratégias de ação pré-definidas. Um exemplo disso é um programa de xadrez que usa um conjunto de regras para decidir os movimentos das peças sem considerar a estratégia global do jogo.

Agentes de Malha Fechada: São mais sofisticados e tomam decisões com base em informações contínuas do ambiente. Eles usam retroalimentação constante para ajustar suas ações. Um exemplo é um veículo autônomo que usa sensores para perceber o ambiente e tomar decisões em tempo real, como ajustar a velocidade ou a direção com base no tráfego e nas condições da estrada.

A inteligência artificial emprega agentes de soluções de problemas em várias aplicações. Por exemplo:

Sistemas de Recomendação: Agentes de malha fechada são usados em sistemas de recomendação, como o algoritmo da Netflix, que sugere filmes com base no histórico de visualizações do usuário.

Robótica: Robôs autônomos usam agentes de malha fechada para navegar em ambientes desconhecidos, evitar obstáculos e cumprir tarefas específicas.

Jogos de Estratégia: Agentes de malha aberta e fechada são usados em jogos como xadrez e Go, onde devem avaliar diferentes jogadas e planejar estratégias.

Sistemas de Controle Industrial: Agentes de malha fechada são aplicados em sistemas de controle para otimizar processos de fabricação, como a automação de uma linha de produção.

Esses exemplos demonstram como os agentes de soluções de problemas desempenham um papel fundamental na IA, capacitando sistemas para tomar decisões, aprender com experiências passadas e se adaptar a ambientes variados. Eles são uma parte vital no avanço das capacidades da Inteligência Artificial em resolver problemas do mundo real.

🔵 Algoritmos de busca(busca cega, busca informada)

Busca Cega (ou Busca Não Informada) Os algoritmos de busca cega, também chamados de busca sem informação, são os mais simples, pois não possuem nenhuma informação adicional além de sua definição . Eles não contêm informações sobre seu domínio e a única coisa que esses algoritmos podem fazer é distinguir entre um estado não objetivo e um estado objetivo. Existem basicamente duas estratégias cegas para a construção e pesquisa em uma árvore de busca: Busca em Largura e Busca em Profundidade. Esses algoritmos são utilizados para ambientes com as seguintes dimensões: Busca em extensão [2].

Por exemplo, considere o problema do quebra-cabeça das 8 peças. A solução pode ser encontrada através de uma busca cega, onde o algoritmo explora todas as possíveis configurações das peças até encontrar a configuração objetivo.

Busca Informada (ou Busca Heurística) A busca informada, por outro lado, utiliza conhecimento extra sobre o problema para guiar o processo de busca. Uma função heurística é usada para estimar o custo ou a distância até o objetivo a partir de um determinado estado. Isso permite que o algoritmo priorize certos caminhos em detrimento de outros, potencialmente encontrando a solução de maneira mais eficiente.

Ambos os tipos de algoritmos têm suas vantagens e desvantagens, e a escolha entre eles depende das características específicas do problema a ser resolvido. Em geral, a busca cega é mais simples e pode ser garantida para encontrar uma solução se ela existir, mas pode ser ineficiente. A busca informada pode ser muito mais eficiente, mas a qualidade da solução encontrada pode depender da qualidade da função heurística utilizada.

🔵 Funções Heurísticas.

As funções heurísticas são uma parte essencial da inteligência artificial, especialmente quando se trata de algoritmos de busca informada1. Uma função heurística é uma técnica projetada para resolver um problema mais rapidamente quando os métodos clássicos são muito lentos, ou para encontrar uma solução aproximada quando os métodos clássicos não conseguem encontrar uma solução exata2.

A função heurística é usada para estimar o custo ou a distância até o objetivo a partir de um determinado estado1. Isso permite que o algoritmo priorize certos caminhos em detrimento de outros, potencialmente encontrando a solução de maneira mais eficiente [3].

Por exemplo, no algoritmo A*, uma função heurística é usada para estimar a distância até o objetivo e priorizar os caminhos que parecem levar mais diretamente ao objetivo3. A função heurística guia os algoritmos baseados em busca pela melhor escolha na direção mais promissora, sugerindo que caminho seguir4.

Em resumo, as funções heurísticas são uma ferramenta poderosa na inteligência artificial, permitindo que os algoritmos de busca encontrem soluções de maneira mais eficiente ao fornecer informações adicionais sobre o problema em questão.


## Referências

[1] PROBLEM SOLVING AGENTS PROBLEM-SOLVING APPROACH IN ARTIFICIAL INTELLIGENCE PROBLEMS. Disponível em <https://medium.com/geekculture/artificial-intelligence-series-problem-solving-agents-2ee405ddf4d0>. <br><br>
[2] NETO, ROSALVO. RESOLUÇÃO DE PROBLEMAS POR MEIO DE BUSCA. UNIVASF. Disponível em <http://univasf.edu.br/~rosalvo.oliveira/Disciplinas/AULAS/IA/AULA04.pdf>
<br><br>
[3] SILVA, JOSÉ. INTELIGENCIA ARTIFICIAL. AULA 5 - BUSCA INFORMADA, HEURÍSTICA. Disponível em <https://edisciplinas.usp.br/pluginfile.php/7205133/mod_resource/content/4/Aula5.pdf>
