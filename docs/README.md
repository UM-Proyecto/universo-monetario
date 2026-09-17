# `docs/` — verificación de fuentes y decisiones de datos

Esta carpeta trae el trabajo de verificación que hasta ahora vivía sólo en el servidor, donde el
equipo no lo veía. Cada archivo responde a una pregunta distinta.

## Si vas a usar una fuente, empezá por acá

**[`CATALOGO-FUENTES.md`](CATALOGO-FUENTES.md)** — El catálogo único del proyecto, con fecha de
corte del 17 de septiembre de 2026. Dice, fuente por fuente, si alguien **abrió el archivo** o si
sólo comprobó que la página responde, que no es lo mismo. Trae además las siete trampas que este
proyecto ya pagó, con la medición al lado de cada una.

Hay una distinción que conviene entender antes de leer nada más: **que un sitio devuelva 200 sólo
prueba que el sitio está en pie.** Cuatro de los dominios que usamos devuelven éxito a rutas que no
existen, y uno de ellos —la Gaceta Oficial— llega a descargar un PDF real para cualquier
identificador. Por eso el catálogo distingue «descargada y abierta» de «responde».

**[`fuentes.json`](fuentes.json)** — El mismo catálogo en formato legible por programa, 26 entradas.
Reemplaza al `fuentes.json` de la raíz del repositorio, que tiene 8 entradas y ninguna abierta.

## Decisiones tomadas, con su fundamento

**[`decisiones/DEC-01-fuente-dolar-paralelo.md`](decisiones/DEC-01-fuente-dolar-paralelo.md)** — Qué
fuente del dólar paralelo usa el proyecto y por qué. Compara `paralelo.bo` contra
`dolarbluebolivia.click` sobre los 772 días que tienen en común. El resultado que decide: hoy las
dos casi coinciden (0,25 % de diferencia mediana), pero en mayo de 2025 —cuando la brecha contra el
oficial tocó el 136 %— se separaban hasta un 9,7 %. Se parecen cuando el fenómeno es chico y se
separan cuando es grande.

**[`decisiones/DEC-02-quiebre-cambiario.md`](decisiones/DEC-02-quiebre-cambiario.md)** — Cómo se
trata el quiebre del 29 de junio de 2026, cuando el tipo de cambio pasó a flotar. Toda serie que
cruce esa fecha describe dos regímenes distintos. El caso que muestra por qué importa: el dólar
perdió 14,9 % en doce meses, pero **toda la caída ocurrió antes de la flotación** —−22,2 % bajo el
régimen viejo— y después incluso subió 8 %. La cifra agregada es correcta y la historia que sugiere
es falsa.

## Relevamientos originales

Los dos documentos siguientes son de rondas anteriores. Traen el **procedimiento** de descarga de
cada fuente, que sigue valiendo. Lo que **no** vale de ellos es el estado de cada fuente: para eso
está el catálogo.

**[`FUENTES-formales.md`](FUENTES-formales.md)** — Ronda del 11 de septiembre de 2026 sobre ASFI,
BBV y BCB, hecha con Chromium headless desde el servidor. Es la que consiguió las tres columnas que
no tenían fuente: fondos de inversión SAFI (100 fondos, 382.424 filas diarias desde 2010), tasas
pasivas del BCB (302 de 308 meses desde enero de 2001) y bolsa en renta fija, que no salió de la
BBV —bloquea por IP— sino del Boletín Estadístico de ASFI (135 boletines).

**[`FUENTES.md`](FUENTES.md)** — Fuentes internacionales y dólar paralelo, ronda del 1 de septiembre
de 2026. Explica por qué los bonos van por yfinance y no por FRED, y por qué las divisas van por
Frankfurter y no por open.er-api.

## Alertas y formulación

**[`alertas-asfi.md`](alertas-asfi.md)** — Lo que ASFI publica y qué obliga, para la parte
regulatoria del trabajo.

**[`formulacion-pregunta-objetivo.md`](formulacion-pregunta-objetivo.md)** — El trabajo sobre cómo
está formulada la pregunta de investigación y el objetivo.

## Cómo rehacer cualquier cifra

Ninguna cifra de estos documentos hay que creerla. En el repositorio del servidor:

```
python3 scripts/verificar_fuentes.py   # mide cada fuente con su control negativo
python3 scripts/verificar_quiebre.py   # qué serie cruza el 29-jun-2026 y si está marcada
python3 scripts/comparar_paralelo.py   # las dos fuentes del paralelo, una contra otra
python3 scripts/huecos_p2p.py          # huecos de la captura propia, por hora boliviana
```
