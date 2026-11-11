# Plano do trabalho: Algoritmo de Grover

Disciplina de Computação Quântica, Sistemas de Informação. Algoritmo escolhido: **Grover**. Ferramenta: **Qiskit** (simulador `qiskit-aer`, hardware IBM Quantum opcional).

## 1. Mapa dos requisitos do enunciado

| # | Requisito (trabalho.md) | Entregável | Onde está |
|---|---|---|---|
| 1 | Fundamentação teórica, 5 a 8 páginas | Relatório técnico em PDF | `relatorio.md` → `relatorio.pdf` (seção 2) |
| 2 | Implementação em Qiskit/Cirq, simulador e, se possível, hardware | Notebook comentado | `grover_qiskit.ipynb` (seções 1 a 6, 8, 9) |
| 3 | Comparação com abordagem clássica | Tabelas e gráficos | Notebook seção 7; relatório seção 5 |
| 4 | Apresentação de 15 min (10 + 5) na Semana 19 | Slides (a fazer pelo grupo) | `guia_apresentacao.md` |

## 2. Estrutura do relatório (5 a 8 páginas)

1. Introdução: problema de busca, motivação em Sistemas de Informação, objetivos.
2. Fundamentação teórica: qubits e superposição, oráculo de fase, algoritmo, análise geométrica, número ótimo de iterações, complexidade e otimalidade, limitações.
3. Implementação em Qiskit: oráculo, difusor, circuito, custo em portas.
4. Resultados: validação, probabilidade × iterações, escalabilidade, múltiplos alvos, aplicação em tabela, ruído, hardware.
5. Comparação com a busca clássica: consultas e tempo de relógio.
6. Conclusão.
7. Referências.

## 3. Estrutura do notebook

1. Funções: `oraculo`, `difusor`, `grover`, `iteracoes_otimas`, `prob_teorica`.
2. Exemplo com n = 3.
3. Probabilidade × iterações (efeito de passar do ponto ótimo).
4. Escalabilidade (n = 2 a 10): iterações, profundidade, portas CX.
5. Vários itens marcados.
6. Aplicação em SI: busca de pedidos em tabela de 32 linhas.
7. Comparação com a busca clássica: consultas e tempo.
8. Ruído sintético.
9. Hardware IBM (opcional, exige token).
10. Conclusões.

## 4. Apresentação

O roteiro minuto a minuto, as analogias, o exemplo de quadro com 4 itens, as respostas às perguntas da banca e a lista do que evitar dizer estão em `guia_apresentacao.md` (e `guia_apresentacao.pdf`). Foi escrito para uma turma que nunca viu computação quântica.

## 5. Pendências do grupo

- [ ] Preencher nomes, disciplina e data na capa do relatório.
- [ ] Rodar a seção de hardware com o token IBM e colar o resultado na seção 4.7 do relatório.
- [ ] Montar os slides com base no `guia_apresentacao.md`.
- [ ] Conferir se o professor exige norma de formatação (ABNT).
