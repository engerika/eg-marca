#!/usr/bin/env python3
"""Mantem os previews de componentes alinhados com tokens.css.

Os previews em componentes/ repetem o bloco Preset A inline, para
renderizarem isolados no painel do Design System. Essa duplicacao e
deliberada, mas sem controle ela diverge — e divergiu: em 28/08 dois
previews tinham --eb-hover e um nao.

Este script e o controle.

    python3 sincronizar-tokens.py              # escreve
    python3 sincronizar-tokens.py --verificar  # so checa, sai 1 se divergir

Camada 3 da arquitetura do CLAUDE.md: deterministico, testavel, no lugar
de conferencia manual.
"""

from __future__ import annotations  # anotacoes preguicosas: str | None em Python < 3.10

import re
import sys
from pathlib import Path

RAIZ = Path(__file__).parent
TOKENS = RAIZ / "tokens.css"
PREVIEWS = sorted((RAIZ / "componentes").glob("*.html"))

INICIO = "/* @tokens-preset-a:inicio */"
FIM = "/* @tokens-preset-a:fim */"


def bloco_canonico() -> str:
    """Le o :root do Preset A em tokens.css, entre os marcadores."""
    texto = TOKENS.read_text(encoding="utf-8")
    try:
        corpo = texto.split(INICIO, 1)[1].split(FIM, 1)[0]
    except IndexError:
        sys.exit(f"erro: marcadores nao encontrados em {TOKENS.name}")
    # reindenta para caber dentro do <style> dos previews
    linhas = [ln[2:] if ln.startswith("  ") else ln for ln in corpo.strip().splitlines()]
    return "\n".join("  " + ln if ln.strip() else "" for ln in linhas)


def bloco_atual(texto: str) -> str | None:
    """Extrai o bloco ja presente no preview, se houver marcadores."""
    if INICIO not in texto or FIM not in texto:
        return None
    return texto.split(INICIO, 1)[1].split(FIM, 1)[0].strip("\n")


def aplicar(texto: str, canonico: str) -> str:
    """Substitui o bloco entre marcadores; insere marcadores se faltarem."""
    novo = f"{INICIO}\n{canonico}\n  {FIM}"
    if INICIO in texto and FIM in texto:
        antes = texto.split(INICIO, 1)[0]
        depois = texto.split(FIM, 1)[1]
        return antes + novo + depois
    # primeira passada: troca o :root solto pelo bloco marcado
    padrao = re.compile(r"[ \t]*:root\s*\{.*?\}\n", re.S)
    if not padrao.search(texto):
        sys.exit("erro: nem marcadores nem :root encontrados")
    return padrao.sub("  " + novo + "\n", texto, count=1)


DESIGN = RAIZ / "DESIGN.md"

# Nome no DESIGN.md (formato do Google, chaves em ingles) -> variavel CSS.
# Token novo nos dois arquivos = linha nova aqui; sem ela ele nao e conferido.
PARES = {
    "colors.primary": "--eb-primaria",
    "colors.primary-button": "--eb-primaria-botao",
    "colors.primary-text": "--eb-primaria-texto",
    "colors.on-primary": "--eb-texto-invertido",
    "colors.secondary": "--eb-acento",
    "colors.tertiary": "--eb-hover",
    "colors.background": "--eb-bg",
    "colors.background-light": "--eb-bg-claro",
    "colors.surface": "--eb-card",
    "colors.on-surface": "--eb-texto",
    "colors.on-surface-muted": "--eb-texto-suave",
    "colors.border-subtle": "--eb-borda-sutil",
    "colors.white": "--eb-branco",
    "colors.black": "--eb-preto",
    "rounded.sm": "--eb-radius-sm",
    "rounded.icon": "--eb-radius-icone",
    "rounded.md": "--eb-radius",
    "rounded.lg": "--eb-radius-card",
    "rounded.xl": "--eb-radius-bloco",
    "spacing.card-padding": "--eb-pad-card",
}
PARES.update({f"colors.subtone-{n}": f"--eb-subtom-{n}" for n in (50, 100, 200, 300)})
PARES.update({f"colors.neutral-{n}": f"--eb-cinza-{n}" for n in range(100, 1000, 100)})
PARES["colors.neutral-50"] = "--eb-cinza-50"


def valores_design() -> dict[str, str]:
    """Le os valores simples (chave: valor) do front matter do DESIGN.md.

    Sem PyYAML de proposito (so stdlib): o front matter usa grupos de um
    nivel com valor na mesma linha, e e so isso que este controle precisa.
    """
    texto = DESIGN.read_text(encoding="utf-8")
    frente = texto.split("---", 2)[1]
    valores, grupo = {}, None
    for linha in frente.splitlines():
        if re.match(r"^\S[^:]*:\s*$", linha):
            grupo = linha.split(":")[0]
        elif grupo and (m := re.match(r"^  ([\w-]+):\s*\"?([^\"#\s][^\"]*|#[0-9A-Fa-f]+)\"?\s*$", linha)):
            valores[f"{grupo}.{m.group(1)}"] = m.group(2).strip()
        elif re.match(r"^\S", linha):
            grupo = None
    return valores


def valores_css() -> dict[str, str]:
    corpo = TOKENS.read_text(encoding="utf-8").split(INICIO, 1)[1].split(FIM, 1)[0]
    return dict(re.findall(r"(--eb-[\w-]+):\s*([^;]+);", corpo))


def verificar_design() -> list[str]:
    """Compara DESIGN.md com tokens.css; devolve as divergencias."""
    design, css = valores_design(), valores_css()
    erros = []
    for chave, var in PARES.items():
        a, b = design.get(chave), css.get(var)
        if a is None or b is None:
            erros.append(f"{chave} / {var}: falta em {'DESIGN.md' if a is None else 'tokens.css'}")
        elif a.lower() != b.strip().lower():
            erros.append(f"{chave} = {a}  x  {var} = {b.strip()}")
    return erros


def main() -> int:
    verificar = "--verificar" in sys.argv
    canonico = bloco_canonico()
    divergentes = []

    erros_design = verificar_design()
    for erro in erros_design:
        print(f"  DIVERGE  DESIGN.md  {erro}")
    if not erros_design:
        print(f"  ok       DESIGN.md ({len(PARES)} tokens)")

    for preview in PREVIEWS:
        texto = preview.read_text(encoding="utf-8")
        atual = bloco_atual(texto)
        # compara sem indentacao das pontas: o bloco escrito carrega os
        # espacos que alinham o marcador de fim dentro do <style>
        if atual is not None and atual.strip() == canonico.strip():
            print(f"  ok       {preview.name}")
            continue
        divergentes.append(preview.name)
        if verificar:
            print(f"  DIVERGE  {preview.name}")
        else:
            preview.write_text(aplicar(texto, canonico), encoding="utf-8")
            print(f"  escrito  {preview.name}")

    if verificar and divergentes:
        print(f"\n{len(divergentes)} preview(s) fora de sincronia com tokens.css.")
        print("Rode sem --verificar para corrigir.")
        return 1
    if erros_design:
        print(f"\n{len(erros_design)} token(s) do DESIGN.md diferentes de tokens.css.")
        print("O DESIGN.md e editado a mao: corrija um dos dois.")
        return 1
    print("\nTudo em sincronia com tokens.css.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
