"""Converte arquivos .md em PDF: pandoc -> HTML com MathML -> Edge/Chrome headless.

Uso: python scripts/build_pdf.py [relatorio] [guia_apresentacao]
Sem argumentos, gera apenas relatorio.pdf.
"""
import subprocess
import sys
from pathlib import Path

import pypandoc

raiz = Path(__file__).resolve().parent.parent
css = raiz / "scripts" / "relatorio.css"
nomes = sys.argv[1:] or ["relatorio"]

candidatos = [
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
]
nav = next((c for c in candidatos if Path(c).exists()), None)
if nav is None:
    raise SystemExit("Edge/Chrome não encontrado.")

for nome in nomes:
    html = raiz / f"{nome}.html"
    pdf = raiz / f"{nome}.pdf"
    pypandoc.convert_file(
        str(raiz / f"{nome}.md"), "html5", outputfile=str(html),
        extra_args=["--standalone", "--embed-resources", "--mathml", f"--css={css}",
                    f"--metadata=title:{nome}", "--metadata=lang:pt-BR",
                    f"--metadata=pagetitle:{nome}", f"--resource-path={raiz}"],
    )
    subprocess.run([nav, "--headless=new", "--disable-gpu", "--no-pdf-header-footer",
                    f"--print-to-pdf={pdf}", html.as_uri()], check=True, timeout=120)
    html.unlink()
    print("PDF gerado:", pdf)
