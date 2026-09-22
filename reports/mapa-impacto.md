# Mapa de impacto — Universo Monetario

Proyecto Integrador · Business Intelligence II · Universidad Privada del Valle, Santa Cruz de la Sierra.
Equipo: Sabrina Adrián Zelaya, Fiorella Michelle Sandoval Castro, Samuel Roberto Castillo Cornejo y Carlos Andrés Méndez Cadario.

Generado el 2026-09-22 desde `docs/mapa_datos.py`, que es la fuente única del mapa. La versión navegable está en `docs/mapa-impacto.html` y la imprimible en `docs/mapa-impacto.pdf`.

## Objetivo

**Determinar qué opciones disponibles para un boliviano protegieron el valor de su dinero frente a la inflación y al tipo de cambio entre 2023 y 2026, a qué costo de entrada, con qué liquidez y con qué respaldo documental.**

Objetivo de Investigación Enfocado del proyecto, corregido el 17-sep-2026: el verbo era «explicar» y las herramientas financieras no explican la inflación, reaccionan a ella. Las cuatro dimensiones del enunciado son las del cuadro comparativo. Corrige la formulación; el alcance queda abierto hasta que el equipo ratifique el eje.

## Estructura

Cuatro actores, cuatro impactos por actor y dos entregables por impacto: treinta y dos entregables en total. 
Quedaron fuera del mapa el tribunal y los docentes, que deciden sobre el trabajo y no sobre el problema, 
y los reguladores, cuyo efecto entra por los impactos del contador y del importador.

| Métrica | Valor |
|---|---|
| Actores | 4 |
| Impactos | 16 |
| Entregables | 32 |
| Puntos de historia | 209 |
| Entregables hecho | 4 |
| Entregables en curso | 1 |
| Entregables parcial | 2 |
| Entregables pendiente | 25 |

## Por qué estos cuatro actores

| Actor | Quién es | Puntos |
|---|---|---|
| **Ahorrista sin formación financiera** | Decide entre bolivianos, dólares y banco sin herramientas para comparar. | 55 |
| **Importador que paga al exterior** | Compra mercadería y paga con dólares digitales porque es el canal al que llega. | 44 |
| **Contador de la empresa** | Descubre la pérdida de crédito fiscal cuando ya no se puede corregir. | 70 |
| **Proveedores de datos** | BCB, INE, ASFI, BBV y Binance. Sin ellos no hay columna que llenar. | 40 |

## 1. Ahorrista sin formación financiera

Decide entre bolivianos, dólares y banco sin herramientas para comparar.

### 1.1 Impacto — Compara opciones en la misma vara y no por costumbre

| Entregable | Puntos | Materia | Estado |
|---|---|---|---|
| Tablero comparativo: seis opciones en cuatro dimensiones | 13 | BI II | pendiente |
| Normalizar las seis opciones a una unidad común por cada Bs 1.000 | 5 | BI II | pendiente |

- **Tablero comparativo: seis opciones en cuatro dimensiones** — Es el entregable central de la materia y el que ve el tribunal.
- **Normalizar las seis opciones a una unidad común por cada Bs 1.000** — Sin unidad común no hay comparación, sólo seis fichas de producto. Los fondos ya traen valor cuota diario.

### 1.2 Impacto — Ve cuánto le cuesta quedarse en efectivo

| Entregable | Puntos | Materia | Estado |
|---|---|---|---|
| Serie de rendimiento real contra el IPC empalmado del INE | 8 | BI II | pendiente |
| Línea base del efectivo en bolivianos como referencia | 3 | BI II | pendiente |

- **Serie de rendimiento real contra el IPC empalmado del INE** — Nominal menos inflación. El IPC ya está descargado y abierto.
- **Línea base del efectivo en bolivianos como referencia** — Es el costo de no hacer nada, y la vara contra la que se miden las otras cinco.

### 1.3 Impacto — Lee el riesgo como cifra y no como adjetivo

| Entregable | Puntos | Materia | Estado |
|---|---|---|---|
| Volatilidad por opción, con la escala derivada de la cifra | 8 | BI II | pendiente |
| Presentación del riesgo: escala visual y monto en bolivianos | 5 | BI II | pendiente |

- **Volatilidad por opción, con la escala derivada de la cifra** — De once productos de la región, ninguno publica desviación estándar.
- **Presentación del riesgo: escala visual y monto en bolivianos** — La escala se deriva de la cifra, nunca se calculan por separado.

### 1.4 Impacto — Entiende lo que lee sin formación contable

| Entregable | Puntos | Materia | Estado |
|---|---|---|---|
| Lenguaje sin jerga en toda la interfaz | 5 | BI II | pendiente |
| Validación de comprensibilidad con usuarios reales | 8 | BI II | pendiente |

- **Lenguaje sin jerga en toda la interfaz** — TASK-21 del tablero.
- **Validación de comprensibilidad con usuarios reales** — TASK-22. El instrumento tiene que poder devolver un resultado que desmienta.

## 2. Importador que paga al exterior

Compra mercadería y paga con dólares digitales porque es el canal al que llega.

### 2.1 Impacto — Elige el canal de pago sabiendo qué respaldo le deja

| Entregable | Puntos | Materia | Estado |
|---|---|---|---|
| Columna de respaldo documental con la cita normativa | 5 | BI II | parcial |
| Semáforo de admisibilidad del documento por canal de pago | 5 | BI II | pendiente |

- **Columna de respaldo documental con la cita normativa** — La RND 102400000021 ya está leída y guardada en el repositorio.
- **Semáforo de admisibilidad del documento por canal de pago** — Traduce la enumeración del artículo 3 a una respuesta por canal.

### 2.2 Impacto — Conoce el sobrecosto real de conseguir dólares digitales

| Entregable | Puntos | Materia | Estado |
|---|---|---|---|
| Captura horaria del libro P2P completo, una fila por anuncio | 5 | — | hecho |
| Brecha del precio P2P contra el tipo de cambio oficial, por hora | 5 | BI II | hecho |

- **Captura horaria del libro P2P completo, una fila por anuncio** — Corregida el 11-sep: antes tomaba 20 de ~180 y sesgaba la mediana 2,3 %.
- **Brecha del precio P2P contra el tipo de cambio oficial, por hora** — Sale de resumen.csv; la serie corre desde el 9 de septiembre.

### 2.3 Impacto — Dimensiona su exposición sobre el umbral de la norma

| Entregable | Puntos | Materia | Estado |
|---|---|---|---|
| Conteo de anuncios y volumen por tramo contra el umbral de Bs 50.000 | 3 | Minería | hecho |
| Estimación del volumen importado expuesto, con supuestos escritos | 8 | BI II | pendiente |

- **Conteo de anuncios y volumen por tramo contra el umbral de Bs 50.000** — Medido el 11-sep: 53 de 178 anuncios de compra operan sobre el umbral.
- **Estimación del volumen importado expuesto, con supuestos escritos** — TASK-38. Necesita las estadísticas de la Aduana Nacional.

### 2.4 Impacto — Cuantifica el crédito fiscal que ya perdió

| Entregable | Puntos | Materia | Estado |
|---|---|---|---|
| Estimador de crédito fiscal en riesgo por operación y período | 8 | Minería | pendiente |
| Serie del stock acumulado entre 2023 y abril de 2026 | 5 | BI II | pendiente |

- **Estimador de crédito fiscal en riesgo por operación y período** — El artículo 5 tiene tres efectos: IVA, IUE y RC-IVA.
- **Serie del stock acumulado entre 2023 y abril de 2026** — Es stock, no flujo: ya ocurrió y no cambia con lo que decida el regulador.

## 3. Contador de la empresa

Descubre la pérdida de crédito fiscal cuando ya no se puede corregir.

### 3.1 Impacto — Detecta antes de declarar qué compras quedan sin respaldo

| Entregable | Puntos | Materia | Estado |
|---|---|---|---|
| Detección de anomalías sobre operaciones fuera del patrón documental | 13 | Minería | pendiente |
| Alerta por operación sobre el umbral sin documento admitido | 5 | Minería | pendiente |

- **Detección de anomalías sobre operaciones fuera del patrón documental** — Aporte natural de Minería de Datos y no necesita etiquetas.
- **Alerta por operación sobre el umbral sin documento admitido** — Antes de la declaración, que es cuando todavía se puede corregir.

### 3.2 Impacto — Entiende qué formas de pago concentran el riesgo

| Entregable | Puntos | Materia | Estado |
|---|---|---|---|
| Reglas de asociación: método de pago × tramo × tipo de contraparte | 8 | Minería | pendiente |
| Segmentación no supervisada del panel de anunciantes: K-means y PCA | 13 | IA y ML II | pendiente |

- **Reglas de asociación: método de pago × tramo × tipo de contraparte** — Los métodos se concentran en seis bancos, así que las reglas tienen soporte.
- **Segmentación no supervisada del panel de anunciantes: K-means y PCA** — No supervisado, que es lo que la materia pide y lo que el dato admite.

### 3.3 Impacto — Trabaja con los tres efectos del artículo 5, no sólo el IVA

| Entregable | Puntos | Materia | Estado |
|---|---|---|---|
| Cálculo separado de IVA, IUE y RC-IVA por operación | 8 | BI II | pendiente |
| Verificar si el comprobante de un proveedor autorizado califica | 5 | — | en curso |

- **Cálculo separado de IVA, IUE y RC-IVA por operación** — El enunciado del equipo sólo mencionaba el crédito fiscal; el costo es mayor.
- **Verificar si el comprobante de un proveedor autorizado califica** — TASK-36. Decide si el problema sigue abierto en presente.

### 3.4 Impacto — Ve dónde está el desperdicio del proceso de pago

| Entregable | Puntos | Materia | Estado |
|---|---|---|---|
| Simulación de eventos discretos del flujo de compra y sus ramas | 13 | Optimización III | pendiente |
| Lectura Lean: cuello de botella aparente contra causal | 5 | Dir. Operaciones | pendiente |

- **Simulación de eventos discretos del flujo de compra y sus ramas** — Los parámetros salen del libro: tiempos de pago, disponibilidad, montos.
- **Lectura Lean: cuello de botella aparente contra causal** — El cuello de botella parece el pago; el causal es la documentación.

## 4. Proveedores de datos

BCB, INE, ASFI, BBV y Binance. Sin ellos no hay columna que llenar.

### 4.1 Impacto — Sus datos entran al sistema sin intervención manual

| Entregable | Puntos | Materia | Estado |
|---|---|---|---|
| Ingesta automática de las fuentes ya verificadas | 8 | BI II | pendiente |
| Catálogo de fuentes con evidencia de descarga y fecha de corte | 3 | — | parcial |

- **Ingesta automática de las fuentes ya verificadas** — Las seis columnas tienen su fuente descargada y abierta.
- **Catálogo de fuentes con evidencia de descarga y fecha de corte** — Verificar es abrir el archivo, no comprobar que la página responda.

### 4.2 Impacto — Sus cambios no rompen el sistema en silencio

| Entregable | Puntos | Materia | Estado |
|---|---|---|---|
| Caché en base de datos para operar sin red | 8 | — | pendiente |
| Resolver la fecha del Boletín del BCB en cada corrida | 3 | — | pendiente |

- **Caché en base de datos para operar sin red** — TASK-3. La BBV bloquea por IP ante pedidos concurrentes: la demo no puede depender de ella.
- **Resolver la fecha del Boletín del BCB en cada corrida** — Los enlaces llevan la fecha adentro y cambian cada trimestre, sin avisar.

### 4.3 Impacto — Se sabe qué columna del cuadro puede construirse

| Entregable | Puntos | Materia | Estado |
|---|---|---|---|
| Relevar qué publica cada fuente formal, y con qué profundidad | 5 | — | hecho |
| Decidir en qué dos columnas va la profundidad | 3 | — | pendiente |

- **Relevar qué publica cada fuente formal, y con qué profundidad** — Cerrada el 11-sep: las tres columnas formales tienen fuente gratis y descargada.
- **Decidir en qué dos columnas va la profundidad** — Ninguna queda fuera por datos: las seis tienen fuente. Es decisión de alcance.

### 4.4 Impacto — Las series cruzan el cambio de régimen sin mentir

| Entregable | Puntos | Materia | Estado |
|---|---|---|---|
| Manejo declarado del quiebre estructural del 29 de junio de 2026 | 5 | BI II | pendiente |
| Conversión a bolivianos con opción de dólar y su fecha de corte | 5 | BI II | pendiente |

- **Manejo declarado del quiebre estructural del 29 de junio de 2026** — TASK-15. Los datos previos describen un régimen cambiario que ya no rige.
- **Conversión a bolivianos con opción de dólar y su fecha de corte** — TASK-16. Una cifra en dólares sin su tipo de cambio envejece en una semana.

## Todos los entregables en una tabla

| # | Actor | Impacto | Entregable | Puntos | Materia | Estado |
|---|---|---|---|---|---|---|
| 1 | Ahorrista sin formación financiera | Compara opciones en la misma vara y no por costumbre | Tablero comparativo: seis opciones en cuatro dimensiones | 13 | BI II | pendiente |
| 2 | Ahorrista sin formación financiera | Compara opciones en la misma vara y no por costumbre | Normalizar las seis opciones a una unidad común por cada Bs 1.000 | 5 | BI II | pendiente |
| 3 | Ahorrista sin formación financiera | Ve cuánto le cuesta quedarse en efectivo | Serie de rendimiento real contra el IPC empalmado del INE | 8 | BI II | pendiente |
| 4 | Ahorrista sin formación financiera | Ve cuánto le cuesta quedarse en efectivo | Línea base del efectivo en bolivianos como referencia | 3 | BI II | pendiente |
| 5 | Ahorrista sin formación financiera | Lee el riesgo como cifra y no como adjetivo | Volatilidad por opción, con la escala derivada de la cifra | 8 | BI II | pendiente |
| 6 | Ahorrista sin formación financiera | Lee el riesgo como cifra y no como adjetivo | Presentación del riesgo: escala visual y monto en bolivianos | 5 | BI II | pendiente |
| 7 | Ahorrista sin formación financiera | Entiende lo que lee sin formación contable | Lenguaje sin jerga en toda la interfaz | 5 | BI II | pendiente |
| 8 | Ahorrista sin formación financiera | Entiende lo que lee sin formación contable | Validación de comprensibilidad con usuarios reales | 8 | BI II | pendiente |
| 9 | Importador que paga al exterior | Elige el canal de pago sabiendo qué respaldo le deja | Columna de respaldo documental con la cita normativa | 5 | BI II | parcial |
| 10 | Importador que paga al exterior | Elige el canal de pago sabiendo qué respaldo le deja | Semáforo de admisibilidad del documento por canal de pago | 5 | BI II | pendiente |
| 11 | Importador que paga al exterior | Conoce el sobrecosto real de conseguir dólares digitales | Captura horaria del libro P2P completo, una fila por anuncio | 5 | — | hecho |
| 12 | Importador que paga al exterior | Conoce el sobrecosto real de conseguir dólares digitales | Brecha del precio P2P contra el tipo de cambio oficial, por hora | 5 | BI II | hecho |
| 13 | Importador que paga al exterior | Dimensiona su exposición sobre el umbral de la norma | Conteo de anuncios y volumen por tramo contra el umbral de Bs 50.000 | 3 | Minería | hecho |
| 14 | Importador que paga al exterior | Dimensiona su exposición sobre el umbral de la norma | Estimación del volumen importado expuesto, con supuestos escritos | 8 | BI II | pendiente |
| 15 | Importador que paga al exterior | Cuantifica el crédito fiscal que ya perdió | Estimador de crédito fiscal en riesgo por operación y período | 8 | Minería | pendiente |
| 16 | Importador que paga al exterior | Cuantifica el crédito fiscal que ya perdió | Serie del stock acumulado entre 2023 y abril de 2026 | 5 | BI II | pendiente |
| 17 | Contador de la empresa | Detecta antes de declarar qué compras quedan sin respaldo | Detección de anomalías sobre operaciones fuera del patrón documental | 13 | Minería | pendiente |
| 18 | Contador de la empresa | Detecta antes de declarar qué compras quedan sin respaldo | Alerta por operación sobre el umbral sin documento admitido | 5 | Minería | pendiente |
| 19 | Contador de la empresa | Entiende qué formas de pago concentran el riesgo | Reglas de asociación: método de pago × tramo × tipo de contraparte | 8 | Minería | pendiente |
| 20 | Contador de la empresa | Entiende qué formas de pago concentran el riesgo | Segmentación no supervisada del panel de anunciantes: K-means y PCA | 13 | IA y ML II | pendiente |
| 21 | Contador de la empresa | Trabaja con los tres efectos del artículo 5, no sólo el IVA | Cálculo separado de IVA, IUE y RC-IVA por operación | 8 | BI II | pendiente |
| 22 | Contador de la empresa | Trabaja con los tres efectos del artículo 5, no sólo el IVA | Verificar si el comprobante de un proveedor autorizado califica | 5 | — | en curso |
| 23 | Contador de la empresa | Ve dónde está el desperdicio del proceso de pago | Simulación de eventos discretos del flujo de compra y sus ramas | 13 | Optimización III | pendiente |
| 24 | Contador de la empresa | Ve dónde está el desperdicio del proceso de pago | Lectura Lean: cuello de botella aparente contra causal | 5 | Dir. Operaciones | pendiente |
| 25 | Proveedores de datos | Sus datos entran al sistema sin intervención manual | Ingesta automática de las fuentes ya verificadas | 8 | BI II | pendiente |
| 26 | Proveedores de datos | Sus datos entran al sistema sin intervención manual | Catálogo de fuentes con evidencia de descarga y fecha de corte | 3 | — | parcial |
| 27 | Proveedores de datos | Sus cambios no rompen el sistema en silencio | Caché en base de datos para operar sin red | 8 | — | pendiente |
| 28 | Proveedores de datos | Sus cambios no rompen el sistema en silencio | Resolver la fecha del Boletín del BCB en cada corrida | 3 | — | pendiente |
| 29 | Proveedores de datos | Se sabe qué columna del cuadro puede construirse | Relevar qué publica cada fuente formal, y con qué profundidad | 5 | — | hecho |
| 30 | Proveedores de datos | Se sabe qué columna del cuadro puede construirse | Decidir en qué dos columnas va la profundidad | 3 | — | pendiente |
| 31 | Proveedores de datos | Las series cruzan el cambio de régimen sin mentir | Manejo declarado del quiebre estructural del 29 de junio de 2026 | 5 | BI II | pendiente |
| 32 | Proveedores de datos | Las series cruzan el cambio de régimen sin mentir | Conversión a bolivianos con opción de dólar y su fecha de corte | 5 | BI II | pendiente |

## Reparto por materia

| Materia | Entregables | Puntos |
|---|---|---|
| BI II | 17 | 109 |
| Minería | 5 | 37 |
| Transversal (sin materia) | 7 | 32 |
| IA y ML II | 1 | 13 |
| Optimización III | 1 | 13 |
| Dir. Operaciones | 1 | 5 |

La columna «Transversal» agrupa el trabajo de infraestructura y verificación que ninguna materia 
evalúa por separado pero del que dependen las demás.

