# DEC-02 — Cómo trata el proyecto el quiebre cambiario del 29 de junio de 2026

**Decidido el 17 de septiembre de 2026.** Cierra TASK-51. La decisión está implementada en
`scripts/regimen.py` y verificada por `scripts/verificar_quiebre.py`, que se corre sin argumentos.

---

## El hecho

El tipo de cambio boliviano flota desde el **29 de junio de 2026**, por la **Resolución Ministerial
245/2026**, emitida el 26 de junio y vigente el 29. Antes de esa fecha el oficial estuvo
administrado y en la práctica congelado durante catorce años: en los 707 días hábiles previos se
movió **uno solo**. En los 80 días posteriores se movió **51**.

La fecha que parte las series es la de **vigencia**, no la de emisión. Entre el 26 y el 28 de junio
seguía rigiendo el régimen anterior, y una serie partida el 26 clasificaría tres días al lado
equivocado.

---

## Por qué hace falta una decisión y no basta con saberlo

Este error **no falla: devuelve un número plausible**. Un promedio de tipo de cambio entre 2025 y
2026 da un valor que existe, que se puede graficar y que no describe ningún momento real del país.
Un desvío estándar calculado sobre los dos regímenes juntos mide la distancia entre dos mundos, no
la volatilidad de ninguno. Una correlación calculada a través del quiebre encuentra relaciones que
son el quiebre mismo disfrazado de asociación.

Y el proyecto ya tiene un caso propio y medido de cuánto cambia la lectura. En el informe de
validación, el rendimiento del dólar a doce meses —**−14,9 % nominal**— parecía un deterioro
gradual. Descompuesto por régimen resulta que **no lo es**:

| Tramo | Desde | Hasta | Variación del paralelo |
|---|---|---|---|
| Régimen fijo | 12,73 (16-sep-2025) | 9,90 (28-jun-2026) | **−22,2 %** |
| Régimen flotante | 9,90 (29-jun-2026) | 10,70 (16-sep-2026) | **+8,0 %** |

La caída ocurrió **entera bajo el régimen viejo**, con el oficial todavía congelado, y después de
la flotación el paralelo se recuperó. La cifra agregada es correcta y la historia que sugiere es
falsa: quien la lea sin descomponer va a proyectar hacia adelante una tendencia que fue un evento
de régimen. Ese es exactamente el error que el informe le señala al enunciado de la IDEA 1, cometido
por nosotros.

---

## La decisión, en tres reglas

1. **Toda serie que cruce el 29-jun-2026 se carga con una columna de régimen** (`fijo` /
   `flotante`). La marca la pone la carga, no el archivo en disco.
2. **Ningún estadístico de resumen** —promedio, desvío, variación, correlación, regresión— se
   calcula sobre un tramo que cruce la fecha sin decirlo explícitamente en el mismo lugar donde se
   publica el número.
3. **Toda cifra que abarque los dos regímenes se publica descompuesta por tramo**, como la tabla de
   arriba. El agregado puede acompañar; no puede ir solo.

**Qué NO se hace, y por qué.** No se parte el histórico en dos archivos y no se descarta el tramo
viejo. El régimen anterior es la mitad del fenómeno que el proyecto estudia —la brecha de 136 % de
mayo de 2025 es un dato, no ruido— y tirarlo dejaría al trabajo con once semanas de historia. No se
"ajusta" ni se empalma ninguna serie con un factor: no hay factor que convierta un precio
racionado en un precio de mercado, y un empalme silencioso es peor que dos tramos declarados.

---

## Por qué la marca no se escribe en los archivos crudos

Los CSV de `datos/crudo/` se dejan **exactamente como llegaron de la fuente**. Agregarles una
columna rompería el hash contra el origen y con eso la posibilidad de demostrar que el archivo es
el que la fuente sirvió. La marca la pone `regimen.cargar_csv()`, que es la puerta de entrada
declarada del proyecto a cualquier serie con fechas.

Consecuencia que hay que saber leer: el verificador lista esos archivos como «cruza sin marca», y
eso **no es un hallazgo pendiente**, es la situación correcta. Lo que el verificador garantiza es
que esa lista sea conocida, corta, y que la carga sí marque —lo cual prueba cargando una de ellas
de verdad y mostrando el resultado.

---

## El huso horario, que es donde esto se rompe sin avisar

Dos de las columnas de fecha del proyecto vienen en **UTC**, y Bolivia es UTC−4. Clasificar por los
primeros diez caracteres de una marca UTC pone del lado equivocado todas las observaciones entre
las 00:00 y las 04:00 UTC del 29 de junio, que en Bolivia todavía eran el 28 y todavía regía el
tipo fijo.

No es hipotético: **medido sobre la serie de tick de dolarbluebolivia, son 16 observaciones** las
que cambian de régimen al corregirlo. Y es el mismo error de huso que este proyecto ya pagó una vez
con la captura P2P, donde se inventó un séptimo día que no existía.

`regimen.py` convierte antes de clasificar para las columnas `ts_utc` y `datetime`, y lo tiene en
sus controles: `regimen_de("2026-06-29 02:00:00", desde_utc=True)` tiene que dar `fijo`.

---

## Inventario: qué series cruzan y cuáles no

Medido el 17-sep-2026 abriendo cada archivo, no leyendo su nombre:

| Serie | Rango | ¿Cruza? |
|---|---|---|
| `dolarblue-all-20260917.csv` (tick, oficial y paralelo) | 21-jul-2024 → 17-sep-2026 | **Sí** |
| `dolarblue-historico-15min.csv` | 21-jul-2024 → 1-sep-2026 | **Sí** |
| `dolarblue-oficial-20260917.csv` | 1-dic-2025 → 17-sep-2026 | **Sí** |
| `dolarblue-oficial-diario.csv` | 1-dic-2025 → 1-sep-2026 | **Sí** |
| `paralelo-bo-historical-20260917.csv` | 6-ago-2024 → 17-sep-2026 | **Sí** (692 fijo / 81 flotante) |
| `datos/p2p/anuncios.csv` (libro propio) | 11-sep-2026 → hoy | No: nace bajo flotación |
| `datos/p2p/resumen.csv` | 9-sep-2026 → hoy | No |

Y las series que todavía no están en `datos/` pero el proyecto usa, con su situación declarada:

- **Tasas pasivas del BCB** (ene-2001 → ago-2026): **cruza**, y de la peor manera, porque además
  está desagregada por moneda y el quiebre cambia el sentido económico de comparar una tasa en
  bolivianos contra una en dólares.
- **IPC del INE**: **cruza**. Y tiene un segundo quiebre propio, el empalme de base del índice, que
  no es el mismo evento y hay que declarar aparte.
- **Base de importaciones del INE** (2023 → jul-2026): **cruza**, y es donde el efecto ya está
  medido: el tipo de cambio implícito de aduana fue exactamente 6,96 durante los 42 meses hasta
  junio de 2026 y saltó a 9,25 en julio. Cualquier serie de costo en bolivianos de esa base que
  cruce julio de 2026 mezcla dos unidades de medida.
- **Boletín del Mercado de Valores de ASFI** (ene-2015 → abr-2026): **no cruza todavía**, porque
  termina dos meses antes. El primer boletín posterior a junio de 2026 la convierte en serie que
  cruza, y ahí hay que aplicarle la regla. Queda anotado para que no pase inadvertido.
- **`datos/universo.csv`** (20 instrumentos internacionales cotizados en dólares): **no cruza en su
  moneda original**, y por eso el verificador lo excluye con motivo escrito. Pero cruza **en el
  momento en que se exprese en bolivianos**, que es lo que el proyecto va a querer hacer para
  compararlo contra las opciones locales. Ese es el uso peligroso y hay que marcarlo ahí.

---

## Cómo se verifica

```
python3 scripts/regimen.py           # controles del módulo, incluido el del huso
python3 scripts/verificar_quiebre.py # recorre datos/, mide rangos, y corre el control positivo
```

El verificador **falla con código 1 si no puede interpretar un archivo**, en lugar de saltearlo. Un
verificador que ignora en silencio lo que no entiende devuelve «cero problemas» sobre un directorio
que no miró, y esa salida es indistinguible de un éxito.

Y termina cargando de verdad una de las series que cruzan, para mostrar el reparto por régimen y
las tres fechas del borde. Sin ese control positivo, todo lo anterior se limitaría a decir que unos
archivos no tienen una columna, que es exactamente lo que diría un verificador roto.
