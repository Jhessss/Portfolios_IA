# Portfólio - Parte 2

Parte 2 do portfólio da matéria Inteligência Artificial a respeito dos tópicos: Agente de soluções de problemas, Problemas de malha aberta e de malha fechada, 
Algoritmos de busca(busca cega, busca informada), Funções heurísticas, Busca em ambientes complexos e Algoritmos genéticos.

## Impressões iniciais

Nessa parte dois do portfólio, começamos a ver na prática os tipos de algoritmos que são fundamentais para a compreensão da Inteligência Artificial. Inicialmente, o nome dos conteúdos e a variedade de abordagens algorítmicas podem parecer desafiadoras. No entanto, à medida que exploramos agentes de soluções de problemas, problemas de malha aberta e de malha fechada, algoritmos de busca, funções heurísticas, busca em ambientes complexos e algoritmos genéticos, fica evidente a fascinante interseção entre a lógica computacional e a resolução de problemas do mundo real. 

## Apresentação do Conteúdo

🔵 Agente de Soluções de Problemas.

Um agente de soluções de problemas, no contexto da Inteligência Artificial, é um sistema que busca ativamente resolver questões ou desafios por meio de ações e tomada de decisões [1]. Esses agentes são essenciais para lidar com problemas complexos e dinâmicos. Eles podem ser classificados em agentes de malha aberta e agentes de malha fechada.

🔵 Problemas de Malha Aberta e de Malha Fechada.

Agentes de Malha Aberta: São agentes que tomam decisões com base em informações limitadas e não têm uma visão completa do ambiente. Eles dependem de estratégias de ação pré-definidas. Um exemplo disso é um programa de xadrez que usa um conjunto de regras para decidir os movimentos das peças sem considerar a estratégia global do jogo.

Agentes de Malha Fechada: São mais sofisticados e tomam decisões com base em informações contínuas do ambiente. Eles usam retroalimentação constante para ajustar suas ações. Um exemplo é um veículo autônomo que usa sensores para perceber o ambiente e tomar decisões em tempo real, como ajustar a velocidade ou a direção com base no tráfego e nas condições da estrada.

A inteligência artificial emprega agentes de soluções de problemas em várias aplicações. Por exemplo:

Sistemas de Recomendação: Agentes de malha fechada são usados em sistemas de recomendação, como o algoritmo da Netflix, que sugere filmes com base no histórico de visualizações do usuário.

Robótica: Robôs autônomos usam agentes de malha fechada para navegar em ambientes desconhecidos, evitar obstáculos e cumprir tarefas específicas.

Jogos de Estratégia: Agentes de malha aberta e fechada são usados em jogos como xadrez e Go, onde devem avaliar diferentes jogadas e planejar estratégias.

Sistemas de Controle Industrial: Agentes de malha fechada são aplicados em sistemas de controle para otimizar processos de fabricação, como a automação de uma linha de produção.

Esses exemplos demonstram como os agentes de soluções de problemas desempenham um papel fundamental na IA, capacitando sistemas para tomar decisões, aprender com experiências passadas e se adaptar a ambientes variados. Eles são uma parte vital no avanço das capacidades da Inteligência Artificial em resolver problemas do mundo real.

🔵 Algoritmos de Busca(busca cega, busca informada)

Busca Cega (ou Busca Não Informada) Os algoritmos de busca cega, também chamados de busca sem informação, são os mais simples, pois não possuem nenhuma informação adicional além de sua definição . Eles não contêm informações sobre seu domínio e a única coisa que esses algoritmos podem fazer é distinguir entre um estado não objetivo e um estado objetivo. Existem basicamente duas estratégias cegas para a construção e pesquisa em uma árvore de busca: Busca em Largura e Busca em Profundidade. Esses algoritmos são utilizados para ambientes com as seguintes dimensões: Busca em extensão [2].

Por exemplo, considere o problema do quebra-cabeça das 8 peças. A solução pode ser encontrada através de uma busca cega, onde o algoritmo explora todas as possíveis configurações das peças até encontrar a configuração objetivo.

Busca Informada (ou Busca Heurística) A busca informada, por outro lado, utiliza conhecimento extra sobre o problema para guiar o processo de busca. Uma função heurística é usada para estimar o custo ou a distância até o objetivo a partir de um determinado estado. Isso permite que o algoritmo priorize certos caminhos em detrimento de outros, potencialmente encontrando a solução de maneira mais eficiente.

Ambos os tipos de algoritmos têm suas vantagens e desvantagens, e a escolha entre eles depende das características específicas do problema a ser resolvido. Em geral, a busca cega é mais simples e pode ser garantida para encontrar uma solução se ela existir, mas pode ser ineficiente. A busca informada pode ser muito mais eficiente, mas a qualidade da solução encontrada pode depender da qualidade da função heurística utilizada.

🔵 Funções Heurísticas.

As funções heurísticas são uma parte essencial da inteligência artificial, especialmente quando se trata de algoritmos de busca informada1. Uma função heurística é uma técnica projetada para resolver um problema mais rapidamente quando os métodos clássicos são muito lentos, ou para encontrar uma solução aproximada quando os métodos clássicos não conseguem encontrar uma solução exata2.

A função heurística é usada para estimar o custo ou a distância até o objetivo a partir de um determinado estado1. Isso permite que o algoritmo priorize certos caminhos em detrimento de outros, potencialmente encontrando a solução de maneira mais eficiente [3].

Por exemplo, no algoritmo A*, uma função heurística é usada para estimar a distância até o objetivo e priorizar os caminhos que parecem levar mais diretamente ao objetivo [3]. A função heurística guia os algoritmos baseados em busca pela melhor escolha na direção mais promissora, sugerindo que caminho seguir [4].

Em resumo, as funções heurísticas são uma ferramenta poderosa na inteligência artificial, permitindo que os algoritmos de busca encontrem soluções de maneira mais eficiente ao fornecer informações adicionais sobre o problema em questão.

🔵 Busca em Ambientes Complexos

A busca em ambientes complexos é um aspecto crucial da inteligência artificial (IA). Ela se refere ao processo de encontrar soluções em espaços de problema que são grandes, dinâmicos ou difíceis de entender completamente [5].

Em muitos casos, os ambientes nos quais a IA precisa operar são complexos e incertos. Por exemplo, um robô que navega em um ambiente desconhecido precisa ser capaz de lidar com uma variedade de desafios, como obstáculos inesperados, mudanças no ambiente e limitações em sua capacidade de percepção.

Existem muitos algoritmos de busca diferentes, cada um com suas próprias forças e fraquezas, e a escolha do algoritmo certo depende das características específicas do ambiente e do problema. Por exemplo, a busca em profundidade pode ser eficaz em ambientes onde o caminho para o objetivo é longo e sinuoso, enquanto a busca em largura pode ser melhor quando existem muitas soluções possíveis que estão próximas ao estado inicial.

Em resumo, a busca em ambientes complexos é um desafio importante na IA, mas também uma área de intensa pesquisa e inovação. Com o desenvolvimento contínuo de novos algoritmos e técnicas, a capacidade da IA de operar efetivamente em ambientes complexos está sempre melhorando.

🔵 Algoritmos Genéticos

Os Algoritmos Genéticos (AGs) são uma técnica de busca utilizada na ciência da computação para encontrar soluções aproximadas em problemas de otimização e busca. Eles são baseados nos princípios de genética e seleção natural, e foram desenvolvidos por John Holland, David E. Goldberg e seus alunos e colegas da Universidade de Michigan.[6]

Os AGs começam com uma população de possíveis soluções para o problema dado. Essas soluções são submetidas a recombinação e mutação (como na genética natural), produzindo novas gerações de soluções. O processo é repetido por várias gerações. Cada indivíduo (ou solução) recebe um valor de aptidão (com base no valor da função objetiva). Os indivíduos mais aptos têm maior chance de se acasalar.[6]

Os AGs são frequentemente usados para resolver problemas de otimização, pesquisa e aprendizado automático. Eles são particularmente úteis quando o espaço de pesquisa é muito grande e há uma grande quantidade de parâmetros envolvidos.[6]

No entanto, os AGs têm suas limitações. Eles podem não ser adequados para todos os problemas, especialmente problemas que são simples e para os quais informações derivativas estão disponíveis. Além disso, sendo estocásticos, não há garantias sobre a otimização ou a qualidade da solução.[6]

Em resumo, os Algoritmos Genéticos são uma ferramenta poderosa na inteligência artificial, permitindo que os sistemas encontrem soluções eficientes para problemas complexos através da imitação dos processos naturais de evolução e seleção.

## Discussões

🔵 Algoritmos de procura

Os algoritmos de procura têm aplicações amplas, não se limitando apenas a quebra-cabeças ou jogos. Eles são usados em planejamento automatizado, roteamento de veículos, design de circuitos e muito mais.
Os algoritmos de procura têm aplicações práticas em muitas áreas. Por exemplo, eles podem ser usados para buscar um aluno dado sua matrícula, buscar um cliente dado o seu CPF, ou buscar uma pessoa dado o seu RG2. Além disso, eles são essenciais para a navegação em ambientes desconhecidos e dinâmicos na robótica. A busca em ambientes complexos é crucial para permitir que sistemas de IA tomem decisões eficazes em cenários desafiadores.[7]

🔵 Expansão do Uso de Algoritmos de Procura

Os algoritmos de procura têm aplicações amplas em diferentes áreas.
Planejamento automatizado: Os algoritmos de procura são usados para encontrar a melhor sequência de ações que atingem um objetivo desejado, dadas certas condições. Eles são usados em uma variedade de aplicações, incluindo planejamento de rotas, agendamento de tarefas e controle de robôs.[8][9]

Roteamento de veículos: Os algoritmos de procura são usados para encontrar a rota mais eficiente entre vários locais. Isso é particularmente útil em logística e transporte, onde o objetivo é minimizar o tempo de viagem ou o custo do combustível.[9]

Design de circuitos: No design de circuitos, os algoritmos de procura são usados para encontrar a melhor disposição dos componentes para minimizar o uso do espaço e maximizar a eficiência. Eles também podem ser usados para encontrar o caminho mais curto através de um circuito, o que é útil para minimizar o atraso do sinal.[10]

🔵 Expansão sobre Algoritmos Genéticos

Os Algoritmos Genéticos (AGs) são uma classe de algoritmos de otimização inspirados na evolução natural e genética. Eles operam através de um processo iterativo de seleção, cruzamento (recombinação) e mutação para evoluir uma população de soluções potenciais para um problema.[11]
Os AGs têm uma ampla gama de aplicações práticas. Por exemplo, eles são frequentemente usados na otimização de parâmetros de redes neurais. Nesse contexto, os AGs podem ajustar os pesos e vieses das redes neurais para minimizar uma função de custo, melhorando assim o desempenho da rede.[11]
Na engenharia, os AGs são usados para otimizar o design de sistemas complexos. Por exemplo, eles podem ser usados para encontrar a melhor disposição de componentes em um circuito eletrônico para minimizar o uso do espaço e maximizar a eficiência.[11]

Os AGs também são eficazes na solução de quebra-cabeças complexos. Eles podem explorar um grande espaço de soluções potenciais de maneira eficiente, encontrando soluções que seriam difíceis ou impossíveis de encontrar através de métodos de busca exaustiva.

A eficácia dos AGs é fortemente influenciada pela escolha dos parâmetros do algoritmo, como a taxa de mutação e a probabilidade de cruzamento. A taxa de mutação controla a frequência com que as alterações aleatórias são introduzidas nas soluções, enquanto a probabilidade de cruzamento determina a frequência com que as soluções são combinadas para criar novas soluções. Ajustar esses parâmetros corretamente é crucial para garantir que o AG explore efetivamente o espaço da solução e converja para uma solução ótima.

🔵 Uso de Algoritmos de busca em IA

Além de discutir como os algoritmos de busca são aplicados em IA, é relevante considerar como essas técnicas evoluem com os avanços na área. Por exemplo, o aprendizado de máquina e as redes neurais têm impactado significativamente o uso de algoritmos de busca em tarefas como processamento de linguagem natural e visão computacional. Sistemas híbridos que combinam busca com outras técnicas de IA são fundamentais para abordar problemas complexos e de grande escala.

Em resumo, essas discussões e contribuições ampliam o entendimento e a aplicação dos conceitos de busca, algoritmos genéticos e sua relevância na Inteligência Artificial. A IA continua evoluindo, e a compreensão desses tópicos desempenha um papel fundamental na solução de problemas do mundo real.

## Referências

[1] PROBLEM SOLVING AGENTS PROBLEM-SOLVING APPROACH IN ARTIFICIAL INTELLIGENCE PROBLEMS. Disponível em <https://medium.com/geekculture/artificial-intelligence-series-problem-solving-agents-2ee405ddf4d0> <br><br>
[2] NETO, ROSALVO. RESOLUÇÃO DE PROBLEMAS POR MEIO DE BUSCA. UNIVASF. Disponível em <http://univasf.edu.br/~rosalvo.oliveira/Disciplinas/AULAS/IA/AULA04.pdf>
<br><br>
[3] SILVA, JOSÉ. INTELIGENCIA ARTIFICIAL. AULA 5 - BUSCA INFORMADA, HEURÍSTICA. USP. Disponível em <https://edisciplinas.usp.br/pluginfile.php/7205133/mod_resource/content/4/Aula5.pdf>
<br><br>
[4] SIMÕES, ALEXANDRE. AULA 05 - BUSCA COM INFORMAÇÃO. UNESP. Disponível em <http://www2.gasi.sorocaba.unesp.br/assimoes/lectures/iac/downloads/busca_heuristica.pdf>
<br><br>
[5] RUSSELL, Stuart; NORVIG, Peter. Inteligência Artificial: Uma Abordagem Moderna. 4. ed. Rio de Janeiro: GEN LTC, 2022. 
<br><br>
[6] Kerschbaumer, Ricardo. TÓPICOS EM INTELIGÊNCIA ARTIFICIAL - ALGORÍTMOS GENÉTICOS. Instituto Federal Catarinense. Disponível em <https://professor.luzerna.ifc.edu.br/ricardo-kerschbaumer/wp-content/uploads/sites/43/2018/03/5-Algoritmos-Gen%C3%A9ticos.pdf>
<br><br>
[7] Dias, Zanoni. MC102 – Aula 11 - Algoritmos de Busca. Unicamp. Disponível em <https://www.ic.unicamp.br/~mc102/aulas/aula11.pdf>
<br><br>
[8] Botelho, Luís. Inteligência Artificial Apontamentos para as aulas. Instituto Superior de Ciências do Trabalho e da Empresa. 2017. Disponível em <http://home.iscte-iul.pt/~luis/aulas/ia/Algoritmos%20de%20procura.pdf><br><br>
[9] Codificação de problemas de procura em espaços de estados. Disponível em <https://ia.ssdi.di.fct.unl.pt/guiao1.html><br><br>
[10] Carvalho, Paulo. ALgoritmos em Grafos. Disponível em <https://impa.br/wp-content/uploads/2021/07/PAPMEM_Julho_2021_Paulo-Cezar_Algoritmos-em-grafos.pdf><br><br>
[11] Pacheco, M. A. C. (Ano).ALGORITMOS GENÉTICOS: PRINCÍPIOS E APLICAÇÕES. Pontifícia Universidade Católica do Rio de Janeiro, Departamento de Engenharia Elétrica. Rua Marques de São Vicente 225, Gávea, CEP 22453-900, Rio de Janeiro, RJ, Brasil. Disponível em <http://www.inf.ufsc.br/~mauro.roisenberg/ine5377/Cursos-ICA/CE-intro_apost.pdf><br><br>
[12] Repositório com códigos requisitados: <https://github.com/Jhessss/Portfolios_IA/tree/main/Portf%C3%B3lio_2>

