# Algoritmo de Grover em Qiskit

Trabalho da disciplina de Computação Quântica (curso de Sistemas de Informação). O enunciado está em [`trabalho.md`](trabalho.md).

O trabalho estuda o algoritmo de Grover, que busca um item em uma lista sem ordem com cerca de √N consultas, contra cerca de N/2 da busca clássica. Inclui a teoria, a implementação em Qiskit, a validação em simulador e a comparação com a busca clássica.

## Conteúdo

| Arquivo | O que é |
|---|---|
| [`relatorio.pdf`](relatorio.pdf) | Relatório técnico (8 páginas). Fonte em [`relatorio.md`](relatorio.md). |
| [`grover_qiskit.ipynb`](grover_qiskit.ipynb) | Notebook comentado, já executado, com todos os gráficos e tabelas. |
| [`guia_apresentacao.pdf`](guia_apresentacao.pdf) | Guia para a apresentação: analogias, roteiro minuto a minuto e perguntas prováveis. Fonte em [`guia_apresentacao.md`](guia_apresentacao.md). |
| [`plano.md`](plano.md) | Plano do trabalho e pendências do grupo. |
| `figuras/` | Figuras geradas pelo notebook e usadas no relatório. |
| `scripts/` | Scripts que geram o notebook, executam-no e convertem o relatório em PDF. |

## Como reproduzir

Requer Python 3.10 ou superior.

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt

# Executa o notebook e atualiza as figuras
python scripts\run_notebook.py

# Gera os PDFs (requer Microsoft Edge ou Google Chrome instalado)
python scripts\build_pdf.py relatorio guia_apresentacao
```

Para abrir o notebook de forma interativa: `jupyter lab grover_qiskit.ipynb` (instale antes com `pip install jupyterlab`).

Se alterar o conteúdo do notebook, edite `scripts/build_notebook.py`, rode-o para regenerar o `.ipynb` e execute `scripts/run_notebook.py`.

## Execução em hardware IBM Quantum (opcional)

A seção 9 do notebook roda o circuito em um computador quântico real se a variável de ambiente `IBM_QUANTUM_TOKEN` estiver definida. Opcionalmente, defina também `IBM_QUANTUM_INSTANCE` com o CRN da instância.

```powershell
$env:IBM_QUANTUM_TOKEN = "SUA_CHAVE"
```

Nunca escreva o token em arquivos do repositório.

## Observações

- A execução em hardware real ainda não foi feita; a seção 4.7 do relatório está marcada como pendente.
- O modelo de ruído usado nas simulações é sintético e não representa um dispositivo específico.
- O oráculo do exemplo de busca em tabela (seção 4.5) é construído a partir de índices calculados de forma clássica. Serve para demonstrar o fluxo do algoritmo, e não como busca real.
