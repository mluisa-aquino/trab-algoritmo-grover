"""Executa o notebook e grava as saídas (e as figuras em ./figuras)."""
from pathlib import Path

import nbformat
from nbclient import NotebookClient

raiz = Path(__file__).resolve().parent.parent
caminho = raiz / "grover_qiskit.ipynb"

nb = nbformat.read(caminho, as_version=4)
NotebookClient(nb, timeout=1200, kernel_name="python3", resources={"metadata": {"path": str(raiz)}}).execute()
nbformat.write(nb, caminho)
print("Notebook executado:", caminho)
