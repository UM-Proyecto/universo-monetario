# -*- coding: utf-8 -*-
"""Layout del arbol con las medidas del estilo de Sam: nodos anchos, gaps generosos.
Las posiciones se calculan aca y los nodos se colocan absolutos, en vez de medir el
DOM despues del render: con ramas irregulares (de 1 a 3 entregables por impacto) un
flex centrado no alinea el impacto con sus hijos."""
import sys, pathlib
S = pathlib.Path("/tmp/claude-1000/-home-scasus/5cdc479a-ff68-4418-9ad8-f75db02af95d/scratchpad")
sys.path.insert(0, str(S))
from mapa_datos import GOAL, ACTORES, E

# columnas (x, ancho) con el gap de 160 que usa el original
COL = {"goal": (0, 420), "actor": (580, 300), "imp": (1040, 300), "ent": (1500, 330)}
GAP_ENT, GAP_IMP, GAP_ACT = 18, 40, 70
PAD = 22          # padding lateral del nodo
PAD_V = 17        # padding vertical
CH = 0.52         # ancho medio de caracter en Poppins

FS  = {"goal": 19, "actor": 13.6, "imp": 14.4, "ent": 12.8, "nota": 11.5}
LH  = {"goal": 27, "actor": 19,   "imp": 21,   "ent": 19.2, "nota": 16}

ICONOS = {"ahorrista": "piggy-bank", "importador": "ship", "contador": "calculator",
          "mercado": "candlestick-chart", "fuentes": "database", "regulador": "landmark",
          "tribunal": "graduation-cap"}
RAMAS = ["blue", "indigo", "amber", "emerald", "rose", "violet", "sky"]


def envolver(texto, ancho_px, fs, mayus=False):
    t = texto.upper() if mayus else texto
    max_ch = max(8, int(ancho_px / (fs * (CH + (0.06 if mayus else 0)))))
    palabras, lineas, act = t.split(), [], ""
    for p in palabras:
        cand = (act + " " + p).strip()
        if len(cand) <= max_ch:
            act = cand
        else:
            if act:
                lineas.append(act)
            act = p
    if act:
        lineas.append(act)
    return lineas


arbol = []
w_act = COL["actor"][1] - 2 * PAD
w_imp = COL["imp"][1] - 2 * PAD - 8      # el borde izquierdo de 8px come ancho
w_ent = COL["ent"][1] - 2 * PAD - 4

for k, (clave, nombre, desc, impactos) in enumerate(ACTORES):
    imps = []
    for ii, imp in enumerate(impactos):
        ents = []
        for x in E:
            if x[0] == clave and x[1] == ii:
                lin = envolver(x[2], w_ent, FS["ent"])
                nota = envolver(x[6], w_ent, FS["nota"])[:3]
                # titulo + nota + fila de badges (24px)
                alto = PAD_V * 2 + len(lin) * LH["ent"] + 6 + len(nota) * LH["nota"] + 26
                ents.append({"lin": lin, "nota": nota, "alto": alto, "sp": x[3],
                             "materia": x[4], "estado": x[5], "texto": x[2], "notaFull": x[6]})
        lin_i = envolver(imp, w_imp, FS["imp"])
        imps.append({"texto": imp, "lin": lin_i, "ents": ents,
                     "alto": PAD_V * 2 + 20 + len(lin_i) * LH["imp"]})   # +20 del tag-label
    lin_a = envolver(nombre, w_act, FS["actor"], mayus=True)
    arbol.append({"clave": clave, "nombre": nombre, "desc": desc, "rama": RAMAS[k],
                  "icono": ICONOS[clave], "lin": lin_a, "imps": imps,
                  "alto": PAD_V * 2 + 46 + len(lin_a) * LH["actor"] + 20})  # icono + meta

y = 0
for a in arbol:
    a_top = y
    for im in a["imps"]:
        im_top = y
        for en in im["ents"]:
            en["y"] = y
            y += en["alto"] + GAP_ENT
        bloque = y - GAP_ENT - im_top
        im["y"] = im_top + max(0, (bloque - im["alto"]) / 2)
        y += GAP_IMP - GAP_ENT
    y -= GAP_IMP - GAP_ENT
    bloque = y - a_top
    a["y"] = a_top + max(0, (bloque - a["alto"]) / 2)
    y += GAP_ACT

ALTO = y - GAP_ACT
goal_lin = envolver(GOAL, COL["goal"][1] - 60, FS["goal"])
goal_alto = 30 * 2 + 74 + len(goal_lin) * LH["goal"] + 24
goal_y = max(0, (ALTO - goal_alto) / 2)
ANCHO = COL["ent"][0] + COL["ent"][1]

if __name__ == "__main__":
    print("lienzo:", ANCHO, "x", round(ALTO))
    print("goal:", len(goal_lin), "lineas, alto", goal_alto, "y", round(goal_y))
    cajas = [(en["y"], en["y"] + en["alto"]) for a in arbol for im in a["imps"] for en in im["ents"]]
    print("entregables:", len(cajas), "| solapes:", sum(1 for p, q in zip(cajas, cajas[1:]) if q[0] < p[1]))
    for a in arbol:
        ents = [en for im in a["imps"] for en in im["ents"]]
        print("  {:<32} rama={:<8} y={:<5} imps={} ents={}".format(
            a["nombre"][:31], a["rama"], round(a["y"]), len(a["imps"]), len(ents)))
