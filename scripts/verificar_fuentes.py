#!/usr/bin/env python3
"""Comprueba que las fuentes declaradas en fuentes.json siguen en pie.

Lo que este script prueba y lo que no:

    Prueba      que la URL responde y con qué código.
    No prueba   que el archivo que buscás siga ahí, ni que diga lo que creés.

La distinción no es un tecnicismo. Una página institucional puede responder 200
durante años mientras el Excel que colgaba de ella cambió de nombre, de ruta o de
contenido. Por eso el campo `estado` de fuentes.json se llena a mano, cuando
alguien baja el archivo y lo abre, y este script nunca lo modifica.

Uso:
    python3 scripts/verificar_fuentes.py
    python3 scripts/verificar_fuentes.py --json      # salida para otro programa
    python3 scripts/verificar_fuentes.py --timeout 30

Sale con código 1 si alguna fuente declarada no responde, para que sirva en un
cron o en integración continua.

No necesita instalar nada: solo la biblioteca estándar de Python 3.8 o superior.
"""

from __future__ import annotations

import argparse
import json
import ssl
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path
from typing import Any

RAIZ = Path(__file__).resolve().parent.parent
FUENTES = RAIZ / "fuentes.json"

# Algunos sitios institucionales rechazan clientes sin User-Agent.
CABECERAS = {
    "User-Agent": "Mozilla/5.0 (compatible; universo-monetario/1.0; verificacion de fuentes)"
}


def consultar(url: str, timeout: int) -> dict[str, Any]:
    """Pide la URL y devuelve código, tamaño y tiempo. Nunca lanza excepción."""
    inicio = time.monotonic()
    pedido = urllib.request.Request(url, headers=CABECERAS, method="GET")
    contexto = ssl.create_default_context()
    try:
        with urllib.request.urlopen(pedido, timeout=timeout, context=contexto) as r:
            cuerpo = r.read(4096)
            return {
                "codigo": r.status,
                "bytes_leidos": len(cuerpo),
                "segundos": round(time.monotonic() - inicio, 2),
                "error": None,
            }
    except urllib.error.HTTPError as e:
        return {
            "codigo": e.code,
            "bytes_leidos": 0,
            "segundos": round(time.monotonic() - inicio, 2),
            "error": f"HTTP {e.code}",
        }
    except Exception as e:  # red caída, DNS, TLS, timeout
        return {
            "codigo": None,
            "bytes_leidos": 0,
            "segundos": round(time.monotonic() - inicio, 2),
            "error": f"{type(e).__name__}: {e}",
        }


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--timeout", type=int, default=25, help="segundos por fuente (por defecto 25)")
    ap.add_argument("--json", action="store_true", help="imprime el resultado como JSON")
    args = ap.parse_args()

    if not FUENTES.exists():
        print(f"No encuentro {FUENTES}", file=sys.stderr)
        return 2

    catalogo = json.loads(FUENTES.read_text(encoding="utf-8"))
    fuentes = catalogo["fuentes"]
    descartadas = catalogo.get("rutas_descartadas", [])

    resultados = []
    for f in fuentes:
        r = consultar(f["url"], args.timeout)
        resultados.append({**{k: f[k] for k in ("id", "institucion", "url", "estado")}, **r})

    # Control negativo: las rutas que sabemos rotas tienen que seguir fallando.
    # Si alguna empezara a responder 200, el catálogo está desactualizado, y eso
    # también hay que verlo. Sin este control, un script que devuelve "todo bien"
    # se lee igual estando ciego.
    controles = []
    for d in descartadas:
        r = consultar(d["url"], args.timeout)
        controles.append({"url": d["url"], "esperado": d["resultado"], **r})

    if args.json:
        print(json.dumps({"fuentes": resultados, "controles": controles}, ensure_ascii=False, indent=2))
    else:
        print(f"Fuentes declaradas en {FUENTES.name}\n")
        for r in resultados:
            marca = "OK " if r["codigo"] == 200 else "FALLA"
            detalle = r["error"] or f'{r["codigo"]}  {r["bytes_leidos"]} bytes  {r["segundos"]}s'
            print(f'  [{marca:5}] {r["id"]:20} {detalle}')
            print(f'           {r["url"]}')
            print(f'           estado declarado: {r["estado"]}')
        print("\nControl negativo — rutas que deben seguir rotas:")
        for c in controles:
            coincide = str(c["codigo"]) == str(c["esperado"])
            marca = "OK " if coincide else "OJO"
            print(f'  [{marca:5}] esperaba {c["esperado"]}, obtuvo {c["codigo"]}   {c["url"]}')
            if not coincide:
                print("           Esta ruta cambió de comportamiento. Revisá el catálogo.")

    caidas = [r for r in resultados if r["codigo"] != 200]
    print(f'\n{len(resultados) - len(caidas)} de {len(resultados)} fuentes responden.')
    if caidas:
        print("No responden: " + ", ".join(c["id"] for c in caidas))
        return 1

    print("\nRecordatorio: que respondan no significa que el archivo que buscás")
    print("siga ahí. El campo `estado` de fuentes.json se llena abriendo el archivo.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
