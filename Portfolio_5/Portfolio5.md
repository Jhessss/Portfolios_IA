# Portfólio - Parte 5

Parte 5 do portfólio da matéria Inteligência Artificial a respeito dos tópicos: incerteza; Utilidade; Teoria de Decisão; Notação básica de probabilidade; Independência e independência condicional; Regra de Bayes, aplicações e modelo ingênuo; Redes Bayesianas; Inferência; Tempo e incerteza; Estados e observações; Modelo de transição e modelos de sensores; Inferência em modelos temporais: i. Filtragem; ii. Predição; iii. Suavização; iv. Explicação mais provável; v. Aprendizado; Modelo Oculto de Markov; Filtros de Kalman.

## Apresentação do Conteúdo

🔵 Incerteza

A incerteza é uma característica inerente à realidade. Ela pode ser encontrada em diversos contextos, como no mundo natural, nas relações humanas e nas decisões tomadas pelos indivíduos. A Inteligência Artificial (IA) não está imune à incerteza. Na verdade, ela é uma das principais barreiras ao desenvolvimento de sistemas inteligentes capazes de lidar com situações complexas e imprevisíveis.

Tratamento da incerteza na IA

Existem diversas técnicas para o tratamento da incerteza na IA. Algumas das mais comuns são:

Regras de inferência: são regras que permitem tirar conclusões a partir de informações incompletas.
Probabilidade: é uma ferramenta matemática que permite quantificar a incerteza.
Fuzzy logic: é uma lógica que permite lidar com incertezas imprecisas.
Aplicações da incerteza na IA

A incerteza é um desafio para a IA, mas também é uma oportunidade. Sistemas inteligentes capazes de lidar com a incerteza podem ser aplicados em diversas áreas, como:

Robótica: sistemas de robótica precisam ser capazes de lidar com situações imprevisíveis, como obstáculos inesperados ou mudanças no ambiente.
Reconhecimento de padrões: sistemas de reconhecimento de padrões precisam ser capazes de lidar com dados incompletos ou ruidosos.
Tomadas de decisão: sistemas de tomada de decisão precisam ser capazes de lidar com informações incompletas ou conflitantes.


🔵 Utilidade

A teoria da utilidade desempenha um papel fundamental na modelagem de preferências e na escolha de ações em ambientes incertos. Ela oferece um arcabouço matemático para representar e otimizar as decisões em situações onde os resultados são incertos.

Na inteligência artificial, a teoria da utilidade é empregada em várias aplicações, como:

Aprendizado por Reforço: Agentes de IA aprendem ações que maximizam a utilidade ao longo do tempo, considerando recompensas e penalidades associadas a diferentes estados.

Sistemas de Recomendação: Recomendações são personalizadas com base nas preferências do usuário, modeladas por funções de utilidade.

Tomada de Decisão em Ambientes Incertos: Ao enfrentar a incerteza, a utilidade guia a escolha de ações que otimizam o valor esperado para o agente.

🔵 Teoria de Decisão

A teoria de decisão é uma área crucial em inteligência artificial (IA) que se concentra em desenvolver modelos formais para a tomada de decisões sob incerteza. Ela oferece estruturas matemáticas e conceituais para ajudar os agentes de IA a fazerem escolhas racionais e informadas. Vamos explorar os principais aspectos da teoria de decisão em IA:

1. Modelagem de Decisões:
A teoria de decisão em IA envolve a modelagem de situações em que um agente deve escolher entre diferentes ações, cada uma levando a resultados possíveis. Esses modelos incorporam a incerteza, refletindo a realidade de muitos ambientes em que os resultados futuros são desconhecidos.

2. Componentes Principais:
Espaço de Estados: Representa todos os estados possíveis do ambiente em que a IA pode tomar decisões.

Conjunto de Ações: Refere-se às opções disponíveis para a IA em um determinado estado.

Função de Transição: Descreve como o ambiente evolui de um estado para outro após a execução de uma ação.

Função de Utilidade: Atribui um valor de utilidade a cada resultado possível, representando as preferências do agente.

3. Critérios de Decisão:
A teoria de decisão oferece critérios para avaliar e comparar diferentes estratégias de decisão:

Maximização da Utilidade Esperada: Escolhe a ação que maximiza a utilidade ponderada pelos resultados possíveis e suas probabilidades.

Minimização do Risco: Aborda a aversão ao risco, priorizando a minimização do impacto negativo dos resultados desfavoráveis.

Teoria da Utilidade Multiobjetivo: Lida com situações em que há múltiplos objetivos, e as decisões precisam otimizar vários critérios simultaneamente.

4. Decisões Sob Incerteza:
Árvores de Decisão: Representam graficamente as escolhas disponíveis, as probabilidades associadas e as consequências, ajudando na visualização e análise.

Teoria de Jogos: Explora a tomada de decisões em cenários onde os resultados dependem das escolhas de outros agentes.


🔵 Notação Básica de Probabilidade

A notação básica de probabilidade é fundamental para expressar e calcular incertezas em sistemas de inteligência artificial. Essa notação fornece uma linguagem formal para descrever eventos e suas relações probabilísticas. Vamos explorar os principais elementos da notação de probabilidade em IA:

1. Eventos:
Um evento é uma ocorrência ou resultado específico em um experimento ou sistema. É representado por uma letra, geralmente em maiúsculas, como A, B, ou C.

2. Espaço Amostral:
O espaço amostral (S) é o conjunto de todos os resultados possíveis de um experimento. Cada elemento do espaço amostral é um evento.

3. Probabilidade de um Evento:
A probabilidade de um evento P(A) é uma medida numérica que expressa a chance de o evento ocorrer. A probabilidade está no intervalo de 0 a 1, onde 0 indica impossibilidade e 1 indica certeza.

4. Operações Básicas:
União (A∪B): Representa a ocorrência de pelo menos um dos eventos A ou B.

Interseção (A∩B): Representa a ocorrência simultânea dos eventos A e B.

Complemento (A´ ou ˉA): Representa o evento oposto ou complementar a A, ou seja, todos os eventos em S que não são A.

🔵 Independência e Independência Condicional

A noção de independência entre eventos é essencial. A independência condicional é particularmente relevante em contextos onde a ocorrência de um evento afeta a probabilidade de outro.

🔵 Regra de Bayes, Aplicações e Modelo Ingênuo

A Regra de Bayes é uma ferramenta poderosa para atualizar crenças com base em novas evidências. Aplicações incluem diagnósticos médicos, reconhecimento de padrões e aprendizado de máquina. O modelo ingênuo de Bayes é uma simplificação eficaz que assume independência entre variáveis.

🔵 Redes Bayesianas

Redes Bayesianas oferecem uma representação gráfica poderosa para modelar relações probabilísticas entre variáveis. São usadas em diagnósticos, previsões e tomada de decisões.

🔵 Inferência

A inferência envolve derivar conclusões a partir de evidências. Em IA, métodos de inferência são aplicados para atualizar crenças e realizar predições em ambientes incertos.

🔵 Tempo e Incerteza

Integrar o tempo na modelagem é essencial em muitas aplicações. Lida-se com a incerteza temporal ao prever eventos futuros e tomar decisões ao longo do tempo.

🔵 Estados e Observações

Em modelos temporais, distinguir entre estados (variáveis ocultas) e observações (variáveis visíveis) é crucial para representar adequadamente o ambiente.

🔵 Modelo de Transição e Modelos de Sensores

Os modelos de transição descrevem como o sistema evolui ao longo do tempo. Modelos de sensores representam como as observações são geradas a partir dos estados.

🔵 Inferência em Modelos Temporais

Filtragem: Estimar o estado atual com base em observações passadas.
Predição: Antecipar o estado futuro com base no conhecimento atual.
Suavização: Refinar estimativas passadas com informações futuras.
Explicação Mais Provável: Identificar a sequência mais provável de eventos.
Aprendizado: Adaptar o modelo com base em novas observações

🔵 Modelo Oculto de Markov

Os Modelos Ocultos de Markov são amplamente utilizados para modelar sistemas dinâmicos com estados não observáveis. Aplicações incluem reconhecimento de padrões e processamento de linguagem natural.

🔵 Filtros de Kalman

Os Filtros de Kalman são essenciais para estimar estados em sistemas dinâmicos sujeitos a ruído. Aplicações abrangem desde rastreamento de objetos até navegação.

## Discussões

Na interseção fascinante da Inteligência Artificial, dois conceitos notáveis emergem como protagonistas na gestão de incerteza e dinâmicas temporais: Redes Bayesianas e Modelos Temporais. Vamos mergulhar em fatos intrigantes e aplicações cativantes desses tópicos emocionantes:

Redes Bayesianas:
Fundamentos Probabilísticos: As Redes Bayesianas, baseadas em princípios probabilísticos, oferecem um meio eficaz de representar e lidar com incerteza em sistemas complexos.

Aplicações em Diagnóstico Médico: Destacam-se em diagnóstico médico, onde a incerteza é inerente. Essas redes permitem a modelagem de relações entre sintomas e condições de saúde, melhorando a precisão do diagnóstico.

Sistemas de Recomendação Personalizados: Utilizadas em sistemas de recomendação, as Redes Bayesianas adaptam suas inferências para fornecer sugestões personalizadas, levando em consideração preferências individuais e padrões de comportamento.

Análise de Risco e Tomada de Decisão: São ferramentas valiosas na análise de risco e na tomada de decisões sob incerteza, sendo aplicadas em setores como finanças, seguros e logística.

Modelos Temporais:
Gestão de Sequências Temporais: Modelos Temporais são projetados para lidar com dados que evoluem ao longo do tempo, como séries temporais e eventos dinâmicos.

Previsão de Séries Temporais: Aplicam-se extensivamente na previsão, sendo cruciais em áreas como meteorologia, finanças e manufatura, onde a capacidade de antecipar eventos futuros é de suma importância.

Controle de Processos Dinâmicos: São empregados no controle de processos dinâmicos, garantindo estabilidade e eficiência em sistemas que evoluem com o tempo.

Aprendizado em Ambientes Dinâmicos: Possibilitam o aprendizado em ambientes que mudam constantemente, permitindo a adaptação de modelos a novos padrões e cenários.

Aplicações Conjuntas e Sinergia:
Previsões Incorporando Incerteza: A combinação de Redes Bayesianas e Modelos Temporais permite previsões mais robustas, incorporando tanto a incerteza inerente aos eventos quanto a dinâmica temporal das variáveis.

Sistemas de Monitoramento Inteligente: Em sistemas de monitoramento inteligente, essa sinergia é evidente, fornecendo não apenas previsões precisas, mas também avaliando a confiabilidade dessas previsões em um contexto temporal.

Aprimoramento de Sistemas de Saúde: Em saúde pública, a aplicação conjunta desses conceitos pode melhorar a previsão de surtos de doenças, considerando a incerteza nas condições ambientais e nos comportamentos de propagação.

Otimização de Redes Logísticas: Nas cadeias de suprimentos, essa abordagem combinada pode otimizar o gerenciamento de inventário, considerando não apenas padrões temporais, mas também a incerteza nas demandas e nas condições do mercado.

Ao explorar esses tópicos, emergem narrativas emocionantes sobre como Redes Bayesianas e Modelos Temporais não apenas abordam desafios intrincados, mas também colaboram para proporcionar soluções mais abrangentes e robustas em um cenário de Inteligência Artificial em constante evolução.

## Projetos e problemas

Como parte do meu envolvimento prático com Redes Bayesianas e Filtros de Kalman, abaixo segue uma implementação em Python, indo além dos exemplos discutidos em sala de aula. 

1. Projeto: Sistema de Rastreamento com Filtro de Kalman:
Objetivo: Desenvolver um sistema de rastreamento de objetos em movimento utilizando um Filtro de Kalman para prever a posição futura do objeto com base em observações.

Implementação em Python:

```python
import numpy as np
import matplotlib.pyplot as plt

# Função que implementa o Filtro de Kalman
def kalman_filter(observed_data, initial_estimate, initial_error, process_noise, measurement_noise):
    # Inicialização das variáveis do Filtro de Kalman
    state_estimate = initial_estimate
    error_estimate = initial_error

    estimates = []  # Lista para armazenar as estimativas ao longo do tempo

    # Iteração sobre as observações
    for measurement in observed_data:
        # Predição do próximo estado
        prediction = state_estimate
        # Erro associado à predição
        prediction_error = error_estimate + process_noise

        # Cálculo do ganho de Kalman
        kalman_gain = prediction_error / (prediction_error + measurement_noise)

        # Atualização da estimativa do estado com base na observação
        state_estimate = prediction + kalman_gain * (measurement - prediction)

        # Atualização do erro associado à estimativa
        error_estimate = (1 - kalman_gain) * prediction_error

        # Armazenamento da estimativa atual na lista
        estimates.append(state_estimate)

    return estimates

# Exemplo de uso
observed_data = [1.2, 1.8, 2.4, 3.2, 3.8]
initial_estimate = 1.0
initial_error = 1.0
process_noise = 0.1
measurement_noise = 0.2

# Chamada da função do Filtro de Kalman
filtered_estimates = kalman_filter(observed_data, initial_estimate, initial_error, process_noise, measurement_noise)

# Visualização dos resultados
plt.plot(range(1, len(observed_data) + 1), observed_data, label='Observações')
plt.plot(range(1, len(filtered_estimates) + 1), filtered_estimates, label='Estimativas do Filtro de Kalman')
plt.legend()
plt.title('Rastreamento com Filtro de Kalman')
plt.xlabel('Tempo')
plt.ylabel('Posição')
plt.show()

```
Utilidade e Aplicações:

* Rastreamento Suavizado: O Filtro de Kalman é eficaz para suavizar estimativas, tornando-as mais robustas em relação a flutuações e ruídos nas observações.
  
* Previsão de Posição: Através da combinação de previsões e observações, o filtro prevê a posição futura do objeto de forma mais precisa.
  
* Adaptação Dinâmica: O Filtro de Kalman ajusta automaticamente a confiança nas previsões e observações com base na variabilidade do processo e nas incertezas das medições.
  
Essa implementação é útil em diversas situações práticas, como rastreamento de objetos em sistemas de visão computacional, sistemas de navegação, e outras aplicações onde é crucial estimar e prever o estado de um sistema dinâmico em tempo real.

## Referências 

[1] Russell, S., & Norvig, P. (2010). Artificial Intelligence: A Modern Approach. Prentice Hall.<br>
[2] Murphy, K. P. (2012). Machine Learning: A Probabilistic Perspective. MIT Press.<br>
[3] Bishop, C. M. (2006). Pattern Recognition and Machine Learning. Springer.<br>
[4]Koller, D., & Friedman, N. (2009). Probabilistic Graphical Models: Principles and Techniques. MIT Press. <br>
