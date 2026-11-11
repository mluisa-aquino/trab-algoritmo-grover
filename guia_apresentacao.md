::: {.capa}
# Guia de apresentação: Algoritmo de Grover

Para o grupo explicar o trabalho a uma turma que nunca viu computação quântica

*Tempo: 15 minutos (10 de exposição + 5 de perguntas)*
:::

## 1. A ideia central em 30 segundos

> Uma lista de 1 milhão de nomes embaralhados. Para achar um nome, o computador comum olha um por um: **500 mil olhadas em média**. O algoritmo de Grover, num computador quântico, acha o mesmo nome com cerca de **785 olhadas**.

Se a turma guardar só uma coisa, que seja esta: **Grover é um jeito de achar algo numa lista sem ordem com muito menos tentativas. O ganho é a raiz quadrada do tamanho da lista.**

## 2. Glossário (decore estes oito termos)

| Termo | Explicação para a turma |
|---|---|
| **Bit** | Unidade de informação do computador comum: 0 ou 1. |
| **Qubit** | Unidade do computador quântico: pode ser 0, 1 ou uma mistura dos dois. |
| **Superposição** | A mistura. É como uma moeda girando no ar: ainda não é "cara" nem "coroa". |
| **Amplitude** | A "nota" de cada possibilidade. Quanto maior a nota, maior a chance daquela possibilidade sair. |
| **Medida** | O momento de olhar o resultado: a moeda cai e vira cara ou coroa. A chance de cada uma é a nota ao quadrado. |
| **Circuito / porta** | O programa quântico: uma sequência de operações (portas) sobre os qubits. |
| **Oráculo** | A parte do circuito que reconhece a resposta certa e marca ela (inverte a nota). Ele não diz qual é, só marca. |
| **Consulta** | Cada vez que se pergunta ao oráculo "esse item é o certo?". É a unidade para comparar com o computador comum. |

## 3. Três analogias para escolher

**A) O balanço (para explicar "parar na hora certa").** O algoritmo é como empurrar um balanço: cada empurrão aumenta a altura. Se empurrar no ritmo certo, chega ao topo (resposta quase certa). Se continuar empurrando depois do topo, o balanço desce de novo. Por isso o número de repetições precisa ser calculado.

**B) As barras de nota (para explicar "marcar e amplificar").** Imagine 8 barras do mesmo tamanho, cada uma representando uma posição da lista. Passo 1: a barra da resposta certa vira de ponta-cabeça (nota negativa). Passo 2: esticamos tudo "espelhando" as barras em volta da média. A barra de ponta-cabeça, que estava longe da média, vai lá para cima; as outras encolhem um pouco. Repetindo, a barra certa fica enorme e as outras ficam quase zero. É exatamente a Figura 1 do relatório.

**C) A moeda girando (para explicar superposição e medida).** Uma moeda girando no ar tem "um pouco de cara e um pouco de coroa". Só ao pegar a moeda (medir) ela vira um resultado único. Grover é um jeito de "viciar" a moeda girando para que, ao pegar, saia quase sempre a resposta certa.

## 4. Exemplo para fazer no quadro (4 itens, uma repetição)

Mostre que o algoritmo funciona com contas que todos acompanham. Alvo na posição 3, quatro posições.

| Etapa | Pos. 0 | Pos. 1 | Pos. 2 | Pos. 3 (alvo) | Média |
|---|--:|--:|--:|--:|--:|
| Início | 0,5 | 0,5 | 0,5 | 0,5 | 0,5 |
| Oráculo (inverte o alvo) | 0,5 | 0,5 | 0,5 | $-0{,}5$ | 0,25 |
| Difusor (nova nota = 2 × média − nota) | 0 | 0 | 0 | 1 | 0,25 |

Conta de exemplo: para a posição 0, $2 \times 0{,}25 - 0{,}5 = 0$. Para o alvo, $2 \times 0{,}25 - (-0{,}5) = 1$.
A chance é a nota ao quadrado: o alvo passou de $0{,}5^2 = 25\%$ para $1^2 = 100\%$ em **uma** repetição.

Em listas maiores, uma repetição não basta, mas a lógica é a mesma. Para 8 itens são 2 repetições (94,5% de chance), como mostra o gráfico do relatório e do notebook.

## 5. Roteiro de fala (10 minutos)

A coluna "Dizer" é uma sugestão em linguagem simples. Adapte ao jeito de cada apresentador.

| Min | Slide | Dizer | Mostrar |
|---|---|---|---|
| 0:00 a 1:00 | **O problema** | "Imagine achar um nome numa lista de 1 milhão sem ordem nenhuma. O computador comum olha um por um: em média 500 mil vezes." | Lista embaralhada, número 500 mil |
| 1:00 a 2:30 | **Computação quântica em 1 minuto** | "Em vez de bits, qubits. Um qubit pode ser 0, 1 ou uma mistura, como uma moeda girando. Cada possibilidade tem uma nota. Ao olhar, sai uma só, com chance proporcional à nota ao quadrado." | Moeda girando, glossário (qubit, superposição, medida) |
| 2:30 | **Cuidado: não é mágica** | "Não dá para testar tudo de graça e ler a resposta. Se olhássemos logo, sairia um resultado aleatório. O truque é mexer nas notas antes de olhar." | Frase em destaque |
| 3:00 a 5:00 | **Como o Grover funciona** | "Dois passos repetidos: marcar a resposta certa (inverter a nota) e amplificar (espelhar em torno da média). A nota certa sobe, as outras descem." | Tabela de 4 itens no quadro e gráfico das barras (Figura 1) |
| 5:00 a 5:45 | **Quantas repetições** | "Como o balanço: tem uma hora certa de parar. São cerca de 0,8 vezes a raiz do tamanho da lista." | Gráfico de probabilidade × iterações |
| 5:45 a 7:15 | **Na prática: o código** | "Fizemos em Qiskit, a biblioteca da IBM. Rodamos num simulador. Com 3 qubits, o resultado certo saiu em 94% das vezes." | Circuito de 3 qubits, histograma |
| 7:15 a 8:45 | **Quântico × comum** | "Com 4096 itens, o comum faz 2057 consultas em média; o Grover faz 50. Com 1 bilhão de itens, seriam meio bilhão contra uns 25 mil." | Gráfico de consultas (Figura 7) |
| 8:45 a 9:30 | **Os limites** | "Hoje os computadores quânticos erram muito: com 6 qubits o resultado já parece chute. E num banco de dados com índice, o computador comum já é rapidíssimo." | Gráfico de ruído |
| 9:30 a 10:00 | **Conclusão** | "Grover reduz as tentativas de N para raiz de N. É um ganho real e provado, mas ainda depende de hardware melhor." | Frase de fechamento do relatório |

**Divisão sugerida entre apresentadores** (ajuste ao número de integrantes): um fala do problema e da base quântica (min 0 a 3), outro do algoritmo (3 a 5:45), outro do código e dos resultados (5:45 a 10).

## 6. Demonstração ao vivo (opcional)

Se houver computador na sala, abra `grover_qiskit.ipynb` já executado (as saídas já estão salvas, não precisa rodar tudo). Mostre só:

1. A célula do **circuito de 3 qubits** e o **histograma**: "o 101 saiu 94% das vezes".
2. O **gráfico passo a passo** (seção 2.1 do notebook).
3. O **gráfico de consultas** (seção 7.1).

Tenha também um backup em PDF ou em imagem, para o caso de o notebook não abrir.

## 7. Perguntas prováveis e respostas curtas

**Isso é exponencialmente mais rápido?**
Não. É quadrático: de N para raiz de N. Para 1 milhão de itens, de 500 mil para uns 785. Já foi provado que não dá para ser melhor em buscas sem ordem.

**Por que não repetir mais vezes para ter 100% de certeza?**
Porque passa do ponto, como o balanço que passa do topo e começa a descer. Depois do número ideal de repetições, a chance cai.

**O computador quântico testa todas as respostas ao mesmo tempo?**
Em certo sentido ele *representa* todas ao mesmo tempo, mas só se consegue ler uma. Por isso é preciso o algoritmo: ele aumenta a chance da certa antes da leitura.

**Dá para usar no banco de dados da empresa?**
Hoje não. Primeiro porque os computadores quânticos ainda erram muito. Segundo porque bancos de dados têm índices e já buscam rapidíssimo. Terceiro porque levar os dados para o computador quântico custa tanto quanto a busca clássica.

**Como o computador sabe qual é a resposta certa (oráculo)?**
O oráculo não diz qual é: ele só reconhece uma resposta quando recebe ela, como um cadeado que diz "abriu" quando a chave certa é testada. Na prática, é um circuito que verifica a condição do problema.

**E se houver mais de uma resposta certa?**
Funciona e fica até mais rápido: com 4 respostas certas em 16, uma repetição basta. Mas é preciso saber (ou estimar) quantas são.

**Por que o simulador não é mais rápido que o computador comum?**
O simulador é um programa em um computador comum imitando o quântico, e imitar n qubits custa cerca de 2ⁿ. O ganho do Grover só existe em um computador quântico de verdade.

**Vocês rodaram num computador quântico de verdade?**
*[Responder conforme o resultado da seção 4.7 do relatório. Se não rodaram: "Rodamos em simulador. A execução em hardware está descrita no notebook e pode ser feita com um token da IBM."]*

**Quanto esse ruído atrapalha?**
Com os erros típicos de hoje, em 6 qubits o resultado é tão ruim quanto chutar. Por isso os testes em hardware real usam 2 ou 3 qubits.

## 8. O que evitar dizer

- "O computador quântico testa todas as possibilidades ao mesmo tempo e dá a resposta." Não é verdade: só se lê um resultado, e o algoritmo existe para tornar o certo provável.
- "É exponencialmente mais rápido." É quadrático.
- "Vai acabar com as senhas." Grover reduz pela metade os bits de segurança de uma chave (256 bits viram o equivalente a 128). Dobrar o tamanho da chave resolve.
- "Os resultados no simulador mostram o ganho de tempo." Mostram a lógica correta, não o ganho de tempo.

## 9. Lista de verificação antes de apresentar

- [ ] Todos sabem explicar o exemplo do quadro (4 itens) sem olhar.
- [ ] Nomes na capa do relatório, e resultado de hardware preenchido (ou frase de explicação pronta).
- [ ] Notebook aberto com saídas visíveis e backup em imagens.
- [ ] Cronometrar um ensaio completo: o limite é 10 minutos de fala.
- [ ] Cada integrante sabe responder pelo menos duas perguntas da seção 7.
