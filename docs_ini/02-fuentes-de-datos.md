# Fuentes de datos — qué baja, cómo baja y qué se rompe

> Investigación inicial asistida por agente de IA (Claude Code, modelo Opus 5), 10 de septiembre
> de 2026. El criterio de esta lista es que una fuente entra como **verificada** solo si alguien
> descargó el archivo y lo abrió. Que la página responda no es verificación: el modo de falla
> dominante de estas fuentes no es el error, es devolver algo que se lee bien y contesta otra
> pregunta.

---

## El hueco real del enfoque, y por qué tiene salida

El enunciado del importador no traía datos, y sin datos no hay proyecto de ciencia de datos. Esa
es la objeción más seria que se le puede hacer, y la respuesta no es conseguir un conjunto de
datos del fenómeno —no existe, porque quien paga fuera del canal formal no deja registro
público— sino **construir el denominador con fuentes públicas y estimar la porción expuesta con
supuestos escritos**.

Son tres fuentes las que sostienen esa estimación, más un conjunto de datos privado para el
componente de modelado.

---

## Fuentes que dan el denominador

| Fuente | Qué aporta | Frecuencia | Estado |
|---|---|---|---|
| Aduana Nacional de Bolivia | Estadísticas de importación por partida, origen y valor. De ahí sale cuántas operaciones superan los Bs 50.000 y qué volumen representan. | Periódica | Por instrumentar |
| ASFI y BCB | Agregados de operaciones con activos virtuales por entidades supervisadas. Es la serie de la que salen los 294 millones de dólares del primer semestre de 2025. Acota la porción que pasa por canal formal. | Semestral / anual | Identificada |
| ASFI | Registro de proveedores de servicios de activos virtuales autorizados bajo la Resolución 540/2025. | Continua | Identificada |
| Servicio de Impuestos Nacionales | Texto de la RND 102400000021 y normativa conexa. | — | Verificada |

**La diferencia entre el volumen importado que supera el umbral y el que pasa por canal formal no
es un dato medido: es una estimación.** Es defendible siempre que los supuestos estén escritos y
la cuenta se pueda rehacer con otros valores. Un lector tiene que poder cambiar un supuesto y ver
cómo se mueve el resultado; si no puede, la estimación es una afirmación disfrazada de cálculo.

---

## Datos para el componente de modelado

El componente de clasificación necesita operaciones individuales, no agregados. Hay disponible un
**conjunto de datos de compras de una empresa de Santa Cruz, con montos normalizados**, apto para
prototipar con variables reales: monto, forma de pago, contraparte y documentación asociada.

Con eso el problema se vuelve de clasificación —estimar la probabilidad de que una operación quede
sin respaldo válido— y deja de ser puramente descriptivo. Conseguirlo y anonimizarlo es tarea de
la primera etapa. Si no se consigue, el proyecto se queda en estimación agregada, que es un
resultado válido pero más pobre, y conviene decirlo antes y no descubrirlo en la semana doce.

---

## Series macroeconómicas de contexto

Todas se verificaron descargando el archivo y abriéndolo, no solo comprobando que el sitio
responda.

| Serie | Emisor | Cobertura | Formato | Estado |
|---|---|---|---|---|
| Agregados monetarios | BCB | Mensual, 2003–2025 | Excel | Verificada |
| Reservas internacionales netas | BCB | Mensual | Excel | Verificada |
| Tipo de cambio oficial (boletín) | BCB | Mensual | Excel | Verificada |
| Tipo de cambio oficial diario | BCB | 1940–2026 | HTML por año | Requiere raspado |
| IPC empalmado | INE | Mensual | Excel | Verificada |
| PIB anual | INE | 1980–2024 | Excel | Verificada |
| Tipo de cambio paralelo | `paralelo.bo` | Diaria, histórico desde 2024 | Raspado | Probada |

### El gotcha que rompe el pipeline a los tres meses

**Los enlaces del Boletín Estadístico del BCB llevan la fecha de publicación dentro de la ruta y
cambian cada trimestre.** Un pipeline que los fije funciona hoy y se rompe solo en tres meses, sin
avisar: la descarga falla o devuelve la versión vieja, y el análisis corre con datos
desactualizados sin que nadie lo note.

La solución es resolver la fecha vigente desde la página índice en cada corrida, en lugar de
guardar la URL. Los enlaces del INE, en cambio, son permanentes y se pueden fijar.

### El quiebre de serie del 29 de junio de 2026

Tras la flotación, la brecha entre el oficial y el paralelo cayó de más del 40 % a entre uno y tres
por ciento, según rastreadores privados: **ninguna fuente oficial publica el paralelo**, y eso hay
que decirlo al citarlo.

Los datos previos a esa fecha describen un régimen cambiario que ya no rige. Cualquier serie que
cruce el corte tiene que declarar cómo lo trata, y lo que la cantidad de observaciones permite hoy
es un test de Chow con la fecha conocida y un estudio de evento alrededor de ella.

---

## Herramientas de modelado macroeconómico: qué existe de verdad

Este relevamiento salió de la sugerencia del docente de Business Intelligence II sobre revisar
modelos de equilibrio general, IS-LM o Mundell-Fleming. El resultado, medido:

**En equilibrio general computable, la intuición del docente describe el presente y no el pasado:
sigue siendo GAMS.** No hay ningún paquete de CGE en Python o R que se instale normalmente y tenga
mantenimiento. `python-cge` tiene un solo commit de 2014; `PSLmodels/CGE` está congelado desde
julio de 2024 y sin releases. Lo único vivo es GAMSPy, que es GAMS con otra cara y la misma
licencia. **Trampa concreta: `pip install pycge` instala un motor de videojuegos 2D de otro
autor.**

**En DSGE hay ecosistema Python vivo, pero no del que sirve para empezar.** `econpizza` es lo más
activo del relevamiento y `pydsge` le sigue, pero apuntan a agentes heterogéneos y no linealidad
sobre JAX. Para un modelo de libro de texto la ruta con menos fricción sigue siendo Dynare sobre
GNU Octave, que es gratis.

**Para IS-LM no existe «la librería», y no es un problema: no es así como se trabaja.** O se
escribe como sistema de ecuaciones simultáneas —y ahí la herramienta viva es `bimets` de R, cuya
viñeta replica el modelo FRB/US de la Reserva Federal, sin equivalente vivo en Python— o se estima
un VAR y se le impone estructura mínima, que es lo que hace la literatura aplicada desde los años
ochenta y está vivo en los dos lenguajes.

**`sequence-jacobian` en PyPI está congelado en 2022** aunque su repositorio siga activo.

### El límite es de aritmética, no de método

Mundell-Fleming describe exactamente lo que le pasó al país: el trilema dice que no se puede
sostener a la vez tipo de cambio fijo, movilidad de capitales y política monetaria autónoma, y que
al pasar a flotación la política monetaria gana tracción y la fiscal la pierde. Es difícil imaginar
un marco más pertinente para un proyecto cuya justificación es la flotación del 29 de junio de
2026.

Pero **estimarlo para Bolivia hoy es imposible: hay dos meses de datos bajo el nuevo régimen**, no
dos trimestres, y un VAR necesita del orden de veinte a treinta observaciones. Cualquier tabla con
coeficientes «del período flotante» se cae en la primera pregunta sobre grados de libertad.

La recomendación operativa es incorporar el marco al capítulo teórico y ningún modelo de equilibrio
general a la implementación.

### El antecedente boliviano es mejor de lo esperado

Si el equipo toca el tema, no arranca de cero. Hay tres modelos DSGE del Banco Central de Bolivia
publicados en su Revista de Análisis —Cerezo (2010); Díaz Quevedo y Garrón Vedia (2015/2016);
Vallejos (2016)—, **dos de ellos declarando explícitamente que usaron Dynare**, y el modelo de
equilibrio general computable de UDAPE de Beltrán y Huarachi (1988), que construyó una matriz de
contabilidad social de Bolivia de 1987 y dice en sus conclusiones que la resolvió con GAMS.

Sobre matrices de contabilidad social, que son el cuello de botella real del CGE: existe la de
UDAPE de 1987 y existe la «Bolivia Social Accounting Matrix, 2012» de IFPRI, el BID, INESAD y el
Kiel Institute, publicada en 2015 con licencia abierta y DOI propio. El INE no publica ninguna
matriz de contabilidad social propia, solo matrices insumo-producto hasta 2014. Construir una desde
cero es trabajo de tesis de maestría.

Para Mundell-Fleming no existe un trabajo boliviano que calibre o estime formalmente las curvas
IS-LM-BP, pero sí dos artículos de la Revista de Análisis del BCB que usan el marco de forma
explícita: Requena, Mendoza, Lora y Escobar (2001), que invoca la trinidad imposible para explicar
los límites de la política monetaria boliviana bajo el crawling-peg de entonces, y Franco Rodríguez
(2016). Y para el episodio de 2026, Luis Carlos Jemio (INESAD) nombró la trinidad imposible el 24
de julio de 2026 para explicar por qué la flotación le devuelve autonomía monetaria al BCB: es una
nota de webinario, no literatura arbitrada, y hay que citarla como tal.

**Ahí hay una contribución original disponible y barata.** Existe literatura boliviana empírica
sobre régimen cambiario que no nombra el modelo —De Sousa Vargas y Zeballos Coria (2015) sobre
política cambiaria y traspaso a precios, Aguilar Pacajes (2012/13) sobre bolivianización y eficacia
monetaria, Gutiérrez (2009) sobre política cambiaria e inflación—. Tomar esos resultados y leerlos
a través del trilema, mostrando que la pérdida de efectividad monetaria bajo ancla fija es
exactamente lo que el modelo predice, es aporte de escritura y no de implementación.

### Una trampa de citación en esta misma sección

**El PDF del BCB alojado en `.../MECTC/ctcmemodeloequilibrio.pdf` aparece en los buscadores
asociado al trabajo de Cerezo (2010), pero al abrirlo es el de Díaz Quevedo y Garrón Vedia.**
Citarlo por lo que dice el buscador produce una cita falsa que apunta a un documento real, que es
la variante que no se nota.
