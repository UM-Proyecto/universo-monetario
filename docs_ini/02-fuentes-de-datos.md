# Fuentes de datos — qué baja, cómo baja y qué se rompe

> Investigación inicial asistida por agente de IA, 10 de septiembre de 2026. El criterio de esta
> lista es que una fuente entra como **verificada** solo si alguien descargó el archivo y lo
> abrió. Que la página responda no es verificación: el modo de falla dominante de estas fuentes
> no es el error, es devolver algo que se lee bien y contesta otra pregunta.

---

## Series macroeconómicas bolivianas

Todas las de esta tabla se verificaron descargando el archivo y abriéndolo, no solo comprobando
que el sitio responda.

| Serie | Emisor | Cobertura | Formato | Estado |
|---|---|---|---|---|
| Agregados monetarios | BCB | Mensual, 2003–2025 | Excel | Verificada |
| Reservas internacionales netas | BCB | Mensual | Excel | Verificada |
| Tipo de cambio oficial (boletín) | BCB | Mensual | Excel | Verificada |
| Tipo de cambio oficial diario | BCB | 1940–2026 | HTML por año | Requiere raspado |
| IPC empalmado | INE | Mensual | Excel | Verificada |
| PIB anual | INE | 1980–2024 | Excel | Verificada |

### El gotcha que rompe el pipeline a los tres meses

**Los enlaces del Boletín Estadístico del BCB llevan la fecha de publicación dentro de la ruta y
cambian cada trimestre.** Un pipeline que los fije funciona hoy y se rompe solo en tres meses,
sin avisar: la descarga falla o devuelve la versión vieja, y el modelo se entrena con datos
desactualizados sin que nadie lo note.

La solución es resolver la fecha vigente desde la página índice en cada corrida, en lugar de
guardar la URL. Los enlaces del INE, en cambio, son permanentes y se pueden fijar.

---

## Tipo de cambio y conversión a bolivianos

El **tipo de cambio oficial del BCB es la fuente primaria de conversión**. Todo rendimiento y
todo riesgo se expresa en bolivianos, con conmutación opcional a dólares.

Para el paralelo, **`paralelo.bo` está verificada y tiene histórico desde 2024**.
`dolarbluebolivia.click` queda por evaluar como fuente alternativa.

La distinción entre oficial y paralelo importa menos que antes —tras la flotación del 29 de junio
de 2026 la brecha cayó a cerca del 1 %—, pero **el histórico anterior a esa fecha sí la
necesita**: en ese tramo la brecha superaba el 40 %, y una serie convertida solo al oficial
distorsiona todo el período previo.

Consecuencia de modelado, no de ingesta: el 29 de junio de 2026 es un **quiebre estructural con
fecha conocida**. Los datos previos describen un régimen que ya no rige.

---

## Precios de activos

| Clase | Instrumentos | Frecuencia | Fuente prevista | Estado |
|---|---|---|---|---|
| Criptomonedas | 5 | Continua, 24/7 | APIs públicas de exchanges | Por instrumentar |
| Acciones | 8 | Diaria, cinco días hábiles | Proveedor de series históricas | Por definir |
| Divisas | 4 pares | Diaria | BCB + proveedor internacional | Parcialmente verificada |
| Bonos | 3 series | Diaria, cupones trimestrales | BBV + proveedor internacional | Por definir |
| Comercio global | Declarado | Anual, rezago 1–2 años | UN Comtrade, Banco Mundial | Implementación final |

### El problema real de esta capa

No es conseguir los precios: es **integrar frecuencias radicalmente distintas sin crear
artefactos por desincronización temporal**. Cripto opera 24/7, la bolsa cinco días, los bonos
pagan cupones trimestrales. Alinearlas mal produce correlaciones que no existen —el fin de semana
en que solo se mueve cripto se lee como movimiento independiente— y ese artefacto se propaga
hasta el valor en riesgo.

La decisión de diseño es fijar una grilla temporal explícita y documentar la regla de relleno,
antes de calcular la primera correlación.

---

## Datos para la dimensión fiscal

**ASFI y el BCB** publican agregados de operaciones con activos virtuales por entidades
supervisadas. Es la serie de la que salen los 294 millones de dólares del primer semestre de 2025
y las 252.800 personas involucradas. Sirve para acotar **qué porción del volumen pasa por canal
formal**.

La **Aduana Nacional de Bolivia** publica estadísticas de importación por partida, origen y valor.
De ahí sale el denominador del lado de las operaciones que superan el umbral de Bs 50.000 de la
RND 102400000021.

La diferencia entre ambos **no es un dato medido sino una estimación con supuestos**, y es
defendible siempre que los supuestos estén escritos. Escribirlos es parte del entregable, no una
nota al pie.

---

## Datos primarios del equipo

La validación de comprensibilidad se hace con usuarios reales sin formación financiera. El
instrumento lo levanta el equipo. Es el dato que sostiene el objetivo general del proyecto, así
que su diseño no se improvisa: la pregunta tiene que poder devolver un resultado que desmienta la
hipótesis, no solo confirmarla.

---

## Fuentes revisadas y descartadas para modelado macro

Este relevamiento se hizo a raíz de una sugerencia del docente de Business Intelligence II sobre
revisar modelos de equilibrio general, IS-LM o Mundell-Fleming. El resultado, medido:

**Equilibrio general computable: sigue siendo GAMS.** No hay ningún paquete de CGE en Python o R
que se instale normalmente y tenga mantenimiento. `python-cge` tiene un solo commit de 2014;
`PSLmodels/CGE` está congelado desde julio de 2024 y sin releases. Lo único vivo es GAMSPy, que
es GAMS con otra cara y la misma licencia. **Trampa concreta: `pip install pycge` instala un motor
de videojuegos 2D de otro autor.**

**DSGE: hay ecosistema Python vivo, pero no del que sirve para empezar.** `econpizza` es lo más
activo y `pydsge` le sigue, pero apuntan a agentes heterogéneos y no linealidad sobre JAX. Para
un modelo de libro de texto la ruta con menos fricción sigue siendo Dynare sobre GNU Octave, que
es gratis.

**IS-LM: no existe «la librería», y no es un problema.** O se escribe como sistema de ecuaciones
simultáneas —ahí la herramienta viva es `bimets` de R, cuya viñeta replica el modelo FRB/US de la
Reserva Federal, sin equivalente vivo en Python— o se estima un VAR y se le impone estructura
mínima, que es lo que hace la literatura aplicada desde los años ochenta.

**`sequence-jacobian` en PyPI está congelado en 2022** aunque su repositorio siga activo.

La conclusión operativa fue incorporar Mundell-Fleming al marco teórico y ningún modelo de
equilibrio general a la implementación. El límite no es de método sino de aritmética: hay dos
meses de datos bajo el régimen cambiario nuevo y un VAR necesita del orden de veinte a treinta
observaciones.

### Antecedente boliviano, que es mejor de lo esperado

Si el equipo toca el tema, no arranca de cero. Hay tres modelos DSGE del Banco Central de Bolivia
publicados en su Revista de Análisis —Cerezo (2010); Díaz Quevedo y Garrón Vedia (2015/2016);
Vallejos (2016)—, **dos de ellos declarando explícitamente que usaron Dynare**, y el CGE de UDAPE
de Beltrán y Huarachi (1988), que construyó una matriz de contabilidad social de Bolivia de 1987
y dice en sus conclusiones que la resolvió con GAMS.

Sobre matrices de contabilidad social, que son el cuello de botella real del CGE: existe la de
UDAPE de 1987 y existe la «Bolivia Social Accounting Matrix, 2012» de IFPRI, el BID, INESAD y el
Kiel Institute, publicada en 2015 con licencia abierta y DOI propio. El INE no publica ninguna
SAM propia, solo matrices insumo-producto hasta 2014.

Para Mundell-Fleming no existe un trabajo boliviano que calibre o estime formalmente las curvas
IS-LM-BP, pero sí dos artículos de la Revista de Análisis del BCB que usan el marco de forma
explícita: Requena, Mendoza, Lora y Escobar (2001), que invoca la trinidad imposible para
explicar los límites de la política monetaria bajo el crawling-peg de entonces, y Franco
Rodríguez (2016). Y para el episodio de 2026, Luis Carlos Jemio (INESAD) nombró la trinidad
imposible el 24 de julio de 2026 para explicar por qué la flotación le devuelve autonomía
monetaria al BCB —es una nota de webinario, no literatura arbitrada, y hay que citarla como tal.

### Una trampa de citación en esta misma sección

**El PDF del BCB alojado en `.../MECTC/ctcmemodeloequilibrio.pdf` aparece en los buscadores
asociado al trabajo de Cerezo (2010), pero al abrirlo es el de Díaz Quevedo y Garrón Vedia.**
Citarlo por lo que dice el buscador produce una cita falsa que apunta a un documento real, que es
la variante que no se nota.
