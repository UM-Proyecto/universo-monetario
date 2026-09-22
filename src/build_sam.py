# -*- coding: utf-8 -*-
import sys, pathlib, html
S = pathlib.Path("/tmp/claude-1000/-home-scasus/5cdc479a-ff68-4418-9ad8-f75db02af95d/scratchpad")
sys.path.insert(0, str(S))
from layout2 import (arbol, goal_lin, goal_alto, goal_y, ALTO, ANCHO, COL,
                     PAD, PAD_V, FS, LH, RAMAS)
from mapa_datos import GOAL, GOAL_METRICA, E, ACTORES

def esc(s): return html.escape(str(s), quote=True)
gx, gw = COL["goal"]; ax, aw = COL["actor"]; ix, iw = COL["imp"]; ex, ew = COL["ent"]

def curva(x1, y1, x2, y2):
    dx = (x2 - x1) * 0.5
    return 'M{:.0f},{:.0f} C{:.0f},{:.0f} {:.0f},{:.0f} {:.0f},{:.0f}'.format(
        x1, y1, x1 + dx, y1, x2 - dx, y2, x2, y2)

HEX = {"blue": "#3b82f6", "indigo": "#6366f1", "amber": "#f59e0b", "emerald": "#10b981",
       "rose": "#f43f5e", "violet": "#8b5cf6", "sky": "#0ea5e9"}

paths, nodos = [], []
g_cx, g_cy = gx + gw, goal_y + goal_alto / 2

for a in arbol:
    r, col = a["rama"], HEX[a["rama"]]
    a_cy = a["y"] + a["alto"] / 2
    paths.append('<path class="ln ln-{r}" d="{d}" stroke="{c}"/>'.format(
        r=r, d=curva(g_cx, g_cy, ax, a_cy), c=col))
    for im in a["imps"]:
        i_cy = im["y"] + im["alto"] / 2
        paths.append('<path class="ln ln-{r}" d="{d}" stroke="{c}"/>'.format(
            r=r, d=curva(ax + aw, a_cy, ix, i_cy), c=col))
        for en in im["ents"]:
            e_cy = en["y"] + en["alto"] / 2
            paths.append('<path class="ln ln-thin ln-{r}" d="{d}" stroke="{c}"/>'.format(
                r=r, d=curva(ix + iw, i_cy, ex, e_cy), c=col))

    # ---- nodo actor ----
    nodos.append(
        '<div class="map-node actor-node color-{r} rama-{r}" style="left:{x}px;top:{y:.0f}px;width:{w}px">'
        '<div class="icon-bg"><i data-lucide="{ic}"></i></div>'
        '<div class="an-txt">{n}</div>'
        '<div class="an-meta">{ni} impactos &middot; {sp} SP</div>'
        '<div class="an-desc">{d}</div></div>'.format(
            r=r, x=ax, y=a["y"], w=aw, ic=a["icono"], n=esc(a["nombre"]),
            ni=len(a["imps"]), sp=sum(x[3] for x in E if x[0] == a["clave"]),
            d=esc(a["desc"])))

    for im in a["imps"]:
        nodos.append(
            '<div class="map-node impact-node color-{r} rama-{r}" '
            'style="left:{x}px;top:{y:.0f}px;width:{w}px">'
            '<span class="tag-label">Impacto</span>{t}</div>'.format(
                r=r, x=ix, y=im["y"], w=iw, t=esc(im["texto"])))

        for en in im["ents"]:
            est = en["estado"].replace(" ", "")
            nodos.append(
                '<div class="map-node task-node color-{r} rama-{r} st-{e}" '
                'style="left:{x}px;top:{y:.0f}px;width:{w}px" title="{tt}">'
                '<div class="tn-txt">{t}</div>'
                '<div class="tn-nota">{nt}</div>'
                '<div class="tn-pie"><span class="sp">{sp} SP</span>'
                '<span class="mat">{m}</span>'
                '<span class="est est-{e}">{estado}</span></div></div>'.format(
                    r=r, e=est, x=ex, y=en["y"], w=ew, t=esc(en["texto"]),
                    nt=esc(en["notaFull"]), sp=en["sp"],
                    m=esc("—" if en["materia"] == "—" else en["materia"]),
                    estado=esc(en["estado"]),
                    tt=esc(en["texto"] + " — " + en["estado"])))

goal = (
    '<div class="map-node goal-node" style="left:{x}px;top:{y:.0f}px;width:{w}px">'
    '<div class="icon-bg"><i data-lucide="target"></i></div>'
    '<span class="goal-tag">The Goal · ¿Por qué?</span>'
    '<div class="goal-txt">{t}</div>'
    '<div class="goal-met">{m}</div></div>'.format(
        x=gx, y=goal_y, w=gw, t=esc(GOAL), m=esc(GOAL_METRICA)))

leyenda = "".join(
    '<button class="leg color-{r} rama-{r}" data-r="{r}">'
    '<span class="dot"></span>{n}<em>{sp}&nbsp;SP</em></button>'.format(
        r=a["rama"], n=esc(a["nombre"]), sp=sum(x[3] for x in E if x[0] == a["clave"]))
    for a in arbol)

SP_TOTAL = sum(x[3] for x in E)
N_IMP = sum(len(a[3]) for a in ACTORES)
materias = sorted({x[4] for x in E}, key=lambda m: (m == "—", m))
tarjetas = "".join(
    '<div class="kpi"><b>{sp}</b><span>{m}</span><em>{n} entregables</em></div>'.format(
        sp=sum(x[3] for x in E if x[4] == m), n=sum(1 for x in E if x[4] == m),
        m=esc("Sin materia" if m == "—" else m))
    for m in materias)

TPL = r"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Universo Monetario - Mapa de Impacto</title>
<script src="https://cdn.tailwindcss.com"></script>
<script src="https://unpkg.com/lucide@latest"></script>
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800;900&family=Inter:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">
<script>
tailwind.config = { theme: { extend: { fontFamily: {
  sans: ['Poppins','sans-serif'], inter: ['Inter','sans-serif'] } } } }
</script>
<style>
  body{
    font-family:'Poppins',sans-serif;
    background-color:#f4f6fa;
    background-image:radial-gradient(#cbd5e1 1.5px, transparent 1.5px);
    background-size:24px 24px;
    margin:0; overflow:hidden;
  }
  .custom-scrollbar::-webkit-scrollbar{width:8px;height:8px}
  .custom-scrollbar::-webkit-scrollbar-track{background:transparent}
  .custom-scrollbar::-webkit-scrollbar-thumb{background-color:rgba(148,163,184,.35);border-radius:10px}
  .custom-scrollbar::-webkit-scrollbar-thumb:hover{background-color:rgba(148,163,184,.65)}

  .map-wrapper{
    background:linear-gradient(135deg,#f8fafc 0%,#f1f5f9 100%);
    background-image:url("data:image/svg+xml,%3Csvg width='60' height='60' viewBox='0 0 60 60' xmlns='http://www.w3.org/2000/svg'%3E%3Cg fill='none' fill-rule='evenodd'%3E%3Cg fill='%23cbd5e1' fill-opacity='0.15'%3E%3Cpath d='M36 34v-4h-2v4h-4v2h4v4h2v-4h4v-2h-4zm0-30V0h-2v4h-4v2h4v4h2V6h4V4h-4zM6 34v-4H4v4H0v2h4v4h2v-4h4v-2H6zM6 4V0H4v4H0v2h4v4h2V6h4V4H6z'/%3E%3C/g%3E%3C/g%3E%3C/svg%3E");
  }
  .canvas{position:relative;min-width:max-content}
  /* el mismo origen para el svg y para los nodos: los absolutos se posicionan
     contra el padding box, asi que el margen va en .inner y no en .canvas */
  .inner{position:relative;margin:70px 60px}
  #svg-canvas{position:absolute;top:0;left:0;pointer-events:none;z-index:0;overflow:visible}
  .ln{fill:none;stroke-width:2.5;opacity:.55;
      stroke-dasharray:var(--len);stroke-dashoffset:var(--len);
      animation:draw 1.1s cubic-bezier(.4,0,.2,1) forwards}
  .ln-thin{stroke-width:1.8;opacity:.4}
  @keyframes draw{to{stroke-dashoffset:0}}

  /* ---- nodos, con el lenguaje del MVP: 16px de radio, blur y sombra suave ---- */
  .map-node{
    position:absolute;
    background:rgba(255,255,255,.95);
    backdrop-filter:blur(10px);
    border:1px solid rgba(226,232,240,.8);
    border-radius:16px;
    padding:17px 22px;
    box-shadow:0 10px 25px -5px rgba(0,0,0,.05),0 8px 10px -6px rgba(0,0,0,.01);
    transition:transform .4s cubic-bezier(.175,.885,.32,1.275),box-shadow .4s ease,border-color .3s ease;
    z-index:10;
    opacity:0; animation:fadeInUp .5s cubic-bezier(.16,1,.3,1) forwards;
  }
  @keyframes fadeInUp{0%{opacity:0;transform:translateY(18px)}100%{opacity:1;transform:translateY(0)}}
  .map-node:hover{
    transform:scale(1.04) translateY(-5px);
    box-shadow:0 25px 30px -5px rgba(0,0,0,.1),0 15px 15px -10px var(--branch-color);
    border-color:var(--branch-color);
    z-index:30;
  }

  .color-blue{--branch-color:#3b82f6;--bg-light:#eff6ff;--text-dark:#1e3a8a}
  .color-indigo{--branch-color:#6366f1;--bg-light:#eef2ff;--text-dark:#312e81}
  .color-amber{--branch-color:#f59e0b;--bg-light:#fffbeb;--text-dark:#78350f}
  .color-emerald{--branch-color:#10b981;--bg-light:#ecfdf5;--text-dark:#064e3b}
  .color-rose{--branch-color:#f43f5e;--bg-light:#fff1f2;--text-dark:#881337}
  .color-violet{--branch-color:#8b5cf6;--bg-light:#f5f3ff;--text-dark:#4c1d95}
  .color-sky{--branch-color:#0ea5e9;--bg-light:#f0f9ff;--text-dark:#075985}

  .goal-node{
    background:linear-gradient(145deg,#0f172a,#1e293b);
    color:#fff;border:1px solid #334155;text-align:center;padding:30px;
    box-shadow:0 20px 40px -10px rgba(15,23,42,.5);overflow:hidden;
  }
  .goal-node::before{content:'';position:absolute;top:0;left:0;right:0;height:6px;
    background:linear-gradient(90deg,#3b82f6,#8b5cf6,#f43f5e)}
  .goal-node .icon-bg{background:rgba(255,255,255,.1);color:#fff;margin:8px auto 18px auto;
    backdrop-filter:blur(5px);border:1px solid rgba(255,255,255,.2)}
  .goal-tag{font-size:.65rem;font-weight:900;text-transform:uppercase;letter-spacing:.15em;
    color:#94a3b8;display:block;margin-bottom:10px}
  .goal-txt{font-size:1.05rem;font-weight:600;line-height:1.5}
  .goal-met{font-family:'Inter',sans-serif;font-size:.72rem;font-weight:400;color:#94a3b8;
    line-height:1.6;margin-top:16px;border-top:1px solid rgba(255,255,255,.12);padding-top:14px;
    text-align:left}

  .icon-bg{background:#fff;padding:9px;border-radius:12px;display:inline-flex;
    align-items:center;justify-content:center;color:var(--branch-color);
    box-shadow:0 4px 10px -2px rgba(0,0,0,.1);transition:transform .3s ease}
  .icon-bg i{width:20px;height:20px}
  .map-node:hover .icon-bg{transform:scale(1.1) rotate(5deg)}

  .actor-node{border-top:6px solid var(--branch-color);
    background:linear-gradient(to bottom,var(--bg-light),#fff);
    border-bottom:2px solid rgba(0,0,0,.05)}
  .an-txt{font-weight:800;text-transform:uppercase;font-size:.85rem;color:var(--text-dark);
    line-height:1.4;margin-top:12px;letter-spacing:.01em}
  .an-meta{font-family:'Inter',sans-serif;font-size:.68rem;font-weight:700;
    color:var(--branch-color);margin-top:6px;letter-spacing:.04em}
  .an-desc{font-family:'Inter',sans-serif;font-size:.7rem;font-weight:400;color:#64748b;
    line-height:1.5;margin-top:9px}

  .impact-node{border-left:8px solid var(--branch-color);font-size:.9rem;
    color:var(--text-dark);font-weight:700;line-height:1.45}
  .tag-label{font-size:.65rem;font-weight:900;text-transform:uppercase;letter-spacing:.15em;
    margin-bottom:8px;display:block;color:var(--branch-color)}

  .task-node{border-left:4px solid var(--branch-color);background:#fff}
  .tn-txt{font-size:.8rem;color:#334155;line-height:1.5;font-weight:600}
  .tn-nota{font-family:'Inter',sans-serif;font-size:.7rem;color:#94a3b8;line-height:1.45;
    margin-top:6px;font-weight:400}
  .tn-pie{display:flex;align-items:center;gap:8px;margin-top:11px;flex-wrap:wrap}
  .tn-pie .sp{font-family:'Inter',sans-serif;font-size:.65rem;font-weight:900;
    color:var(--branch-color);background:var(--bg-light);padding:3px 7px;border-radius:6px}
  .tn-pie .mat{font-family:'Inter',sans-serif;font-size:.65rem;font-weight:600;color:#94a3b8}
  .est{font-family:'Inter',sans-serif;font-size:.6rem;font-weight:800;text-transform:uppercase;
    letter-spacing:.08em;padding:3px 7px;border-radius:6px;margin-left:auto}
  .est-hecho,.est-resuelto{background:#dcfce7;color:#15803d}
  .est-encurso,.est-parcial{background:#fef3c7;color:#a16207}
  .est-pendiente{background:#f1f5f9;color:#94a3b8}
  .est-bloqueante{background:#ffe4e6;color:#be123c}
  .task-node.st-bloqueante{border-left-color:#e11d48;box-shadow:0 10px 25px -5px rgba(225,29,72,.18)}

  /* aislar rama */
  .canvas.aislar .map-node:not(.on):not(.goal-node){opacity:.12}
  .canvas.aislar .ln:not(.on){opacity:.05}
  .map-node,.ln{transition:opacity .25s ease}

  .leg{display:inline-flex;align-items:center;gap:8px;padding:7px 13px;border-radius:10px;
    background:#fff;border:1px solid #e2e8f0;font-size:.76rem;font-weight:600;color:#475569;
    cursor:pointer;transition:all .2s ease;box-shadow:0 1px 2px rgba(0,0,0,.04)}
  .leg:hover{border-color:var(--branch-color);color:#0f172a;transform:translateY(-1px)}
  .leg[aria-pressed="true"]{background:var(--bg-light);border-color:var(--branch-color);
    color:var(--text-dark);box-shadow:0 4px 10px -4px var(--branch-color)}
  .leg .dot{width:10px;height:10px;border-radius:50%;background:var(--branch-color);flex:none}
  .leg em{font-family:'Inter',sans-serif;font-style:normal;font-size:.68rem;font-weight:800;
    color:#94a3b8}

  .kpi{background:#fff;border:1px solid #e2e8f0;border-radius:14px;padding:13px 17px;
    box-shadow:0 4px 10px -6px rgba(0,0,0,.1);min-width:132px}
  .kpi b{font-family:'Inter',sans-serif;display:block;font-size:1.5rem;font-weight:900;
    color:#0f172a;line-height:1}
  .kpi span{display:block;font-size:.72rem;font-weight:700;color:#475569;margin-top:4px}
  .kpi em{font-family:'Inter',sans-serif;font-style:normal;display:block;font-size:.65rem;
    color:#94a3b8;font-weight:500;margin-top:2px}

  .zoom-btn{width:34px;height:34px;border-radius:9px;background:#fff;border:1px solid #e2e8f0;
    display:grid;place-items:center;cursor:pointer;color:#475569;transition:all .2s}
  .zoom-btn:hover{border-color:#6366f1;color:#4f46e5}
  .zoom-btn i{width:16px;height:16px}
  @media (prefers-reduced-motion:reduce){*{animation:none!important;transition:none!important}
    .map-node{opacity:1}.ln{stroke-dashoffset:0!important}}
</style>
</head>
<body class="h-screen flex flex-col">

<header class="bg-white border-b border-slate-200 px-6 py-3 flex items-center gap-4 flex-wrap shadow-sm z-40">
  <div class="flex items-center gap-3">
    <div class="w-10 h-10 rounded-xl bg-gradient-to-br from-slate-900 to-slate-700 grid place-items-center text-white shadow-lg">
      <i data-lucide="target" class="w-5 h-5"></i>
    </div>
    <div>
      <h1 class="text-base font-black text-slate-800 tracking-tight leading-none">MAPA DE IMPACTO</h1>
      <p class="text-[11px] text-slate-500 font-medium mt-0.5">Universo Monetario &bull; Univalle Santa Cruz</p>
    </div>
  </div>
  <div class="flex items-center gap-4 ml-auto flex-wrap font-inter">
    <div class="flex items-center gap-4 text-[11px] font-bold text-slate-400 tracking-wide">
      <span><b class="text-slate-800 text-sm">__NACT__</b> ACTORES</span>
      <span><b class="text-slate-800 text-sm">__NIMP__</b> IMPACTOS</span>
      <span><b class="text-slate-800 text-sm">__NENT__</b> ENTREGABLES</span>
      <span><b class="text-indigo-600 text-sm">__SPTOTAL__</b> STORY POINTS</span>
    </div>
    <div class="flex items-center gap-1.5">
      <button class="zoom-btn" id="zout" title="Alejar"><i data-lucide="minus"></i></button>
      <span id="zlabel" class="text-[11px] font-bold text-slate-500 w-10 text-center font-inter">100%</span>
      <button class="zoom-btn" id="zin" title="Acercar"><i data-lucide="plus"></i></button>
      <button class="zoom-btn" id="zfit" title="Ver todo"><i data-lucide="maximize-2"></i></button>
    </div>
  </div>
</header>

<div class="bg-white/70 backdrop-blur border-b border-slate-200 px-6 py-2.5 flex items-center gap-2 flex-wrap z-30">
  <span class="text-[10px] font-black uppercase tracking-[.15em] text-slate-400 mr-1">Ramas</span>
  __LEYENDA__
  <button id="limpiar" class="text-[11px] font-semibold text-slate-400 hover:text-slate-700 ml-2 underline underline-offset-2">ver todas</button>
</div>

<main class="flex-1 overflow-auto map-wrapper custom-scrollbar" id="scroller">
  <div class="canvas" id="canvas" style="width:__W__px;height:__H__px">
    <div class="inner" style="width:__SW__px;height:__SH__px">
      <svg id="svg-canvas" width="__SW__" height="__SH__" viewBox="0 0 __SW__ __SH__">__PATHS__</svg>
      __NODOS__
      __GOAL__
    </div>
  </div>
</main>

<footer class="bg-white border-t border-slate-200 px-6 py-3 flex items-center gap-3 flex-wrap overflow-x-auto custom-scrollbar z-40">
  <span class="text-[10px] font-black uppercase tracking-[.15em] text-slate-400 mr-1 flex-none">Esfuerzo<br>por materia</span>
  __TARJETAS__
</footer>

<script>
lucide.createIcons();

// las lineas se dibujan solas: cada una arranca con su propio largo como dasharray
document.querySelectorAll("#svg-canvas path").forEach((p, i) => {
  const L = p.getTotalLength();
  p.style.setProperty("--len", L);
  p.style.animationDelay = (300 + i * 12) + "ms";
});
document.querySelectorAll(".map-node").forEach((n, i) => {
  n.style.animationDelay = (i * 14) + "ms";
});

// aislar una rama
const canvas = document.getElementById("canvas");
let fijada = null;
function aislar(r){
  document.querySelectorAll(".leg").forEach(b =>
    b.setAttribute("aria-pressed", String(b.dataset.r === r)));
  canvas.querySelectorAll(".map-node,.ln").forEach(el => el.classList.remove("on"));
  if (!r){ canvas.classList.remove("aislar"); fijada = null; return; }
  fijada = r;
  canvas.classList.add("aislar");
  canvas.querySelectorAll(".rama-" + r + ", .ln-" + r).forEach(el => el.classList.add("on"));
}
document.querySelectorAll(".leg").forEach(b =>
  b.addEventListener("click", () => aislar(fijada === b.dataset.r ? null : b.dataset.r)));
document.getElementById("limpiar").addEventListener("click", () => aislar(null));

// zoom
const scroller = document.getElementById("scroller");
const zlabel = document.getElementById("zlabel");
let z = 1;
function aplicar(nuevo){
  z = Math.min(1.4, Math.max(0.2, nuevo));
  canvas.style.transform = "scale(" + z + ")";
  canvas.style.transformOrigin = "0 0";
  canvas.style.width  = (__W__ * z) + "px";
  canvas.style.height = (__H__ * z) + "px";
  zlabel.textContent = Math.round(z * 100) + "%";
}
document.getElementById("zin").addEventListener("click", () => aplicar(z + 0.1));
document.getElementById("zout").addEventListener("click", () => aplicar(z - 0.1));
document.getElementById("zfit").addEventListener("click", () =>
  aplicar(Math.min(scroller.clientWidth / __W__, scroller.clientHeight / __H__)));

// al abrir, el Goal centrado en pantalla
window.addEventListener("load", () => {
  scroller.scrollTop  = __GY__ - scroller.clientHeight / 2 + 160;
  scroller.scrollLeft = 0;
});
</script>
</body>
</html>
"""

W, H = ANCHO + 120, int(ALTO) + 140
out = (TPL.replace("__PATHS__", "".join(paths))
          .replace("__NODOS__", "".join(nodos))
          .replace("__GOAL__", goal)
          .replace("__LEYENDA__", leyenda)
          .replace("__TARJETAS__", tarjetas)
          .replace("__SPTOTAL__", str(SP_TOTAL))
          .replace("__NIMP__", str(N_IMP))
          .replace("__NACT__", str(len(ACTORES)))
          .replace("__NENT__", str(len(E)))
          .replace("__SW__", str(ANCHO)).replace("__SH__", str(int(ALTO)))
          .replace("__W__", str(W)).replace("__H__", str(H))
          .replace("__GY__", str(int(goal_y))))

(S/"MAPA-IMPACTO.html").write_text(out, encoding="utf-8")
faltan = [m for m in ("__NACT__","__NENT__","__PATHS__","__NODOS__","__GOAL__","__LEYENDA__","__TARJETAS__",
                      "__SPTOTAL__","__NIMP__","__SW__","__SH__","__W__","__H__","__GY__") if m in out]
print("bytes:", len(out), "| marcadores sin sustituir:", faltan)
print("nodos:", len(nodos), "| paths:", len(paths), "| lienzo:", W, "x", H)
