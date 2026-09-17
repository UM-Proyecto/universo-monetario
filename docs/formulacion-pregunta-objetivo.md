# Pregunta de investigación y objetivo general: revisión de la formulación

Revisión del 1 de septiembre de 2026 sobre el borrador que Fiorella hizo circular. El borrador
es defendible en su intención y tiene tres problemas concretos, uno de los cuales lo desarma
ante la primera pregunta técnica del tribunal. Los tres se arreglan sin cambiar el tema.

---

## Antes que nada: esta formulación no es la del anteproyecto

El borrador propone predecir la inflación a partir de agregados monetarios y tipo de cambio, con
un tablero de monitoreo. Eso es el proyecto **macroeconómico** que describe la diapositiva del
docente de Business Intelligence II, no el Proyecto Integrador que el equipo tiene escrito.

El anteproyecto plantea otra cosa: la cartera de una persona sin formación financiera, con datos
diarios, veinte instrumentos, clasificación de dirección del rendimiento y valor en riesgo, y
nueve decisiones cerradas alrededor de eso. Cambiar la variable objetivo a la inflación mensual
no es un ajuste de redacción: invalida D3 (horizonte de siete días), D4 (clasificación y valor en
riesgo), D5 (veinte instrumentos) y D9 (presentación del riesgo).

Es la pregunta abierta que ya está registrada como TASK-31 y que decide todo lo demás. Mientras
no se confirme con el docente si BI2 y el Integrador son la misma entrega, lo prudente es tratar
esta formulación como la de **BI2**, y no tocar el objetivo del Integrador.

El resto de este documento asume eso. Al final está lo que habría que hacer si resultan ser la
misma entrega.

---

## Los tres problemas del borrador

### 1. Dice «explicar y predecir», y son dos afirmaciones distintas

«Explicar» exige identificación causal: sostener que un movimiento de M1 *causa* un movimiento
de precios. Con agregados monetarios, tipo de cambio e inflación —tres variables que se
determinan simultáneamente— eso pide un diseño que el proyecto no tiene y que no cabe en un
semestre.

«Predecir» no lo exige. Un modelo puede pronosticar bien sin explicar nada, y eso es un
resultado legítimo y defendible.

Es la primera palabra que un tribunal va a atacar, y sale gratis quitarla. La formulación debe
decir **pronosticar**, y punto.

### 2. No es medible: falta contra qué se compara

«Analizar y predecir el comportamiento de la inflación» no tiene forma de darse por cumplido. No
hay métrica, no hay umbral y, sobre todo, no hay línea base.

Esto importa más de lo que parece con la inflación, porque **la inflación es muy persistente**:
el mejor predictor de la inflación del mes que viene suele ser la de este mes. Un modelo que
acierte «bastante» no dice nada si un modelo ingenuo que repite el último dato acierta igual. Sin
la línea base, el número que se reporte no es interpretable, y el tribunal lo sabe.

La línea base va **antes** de entrenar el primer modelo, no después: es la vara, no el
comentario final.

### 3. El tipo de cambio es una constante en casi todo el período disponible — medido

Este es el que desarma el borrador, y no es una opinión.

Se descargaron las cotizaciones oficiales del BCB año por año y se contaron los valores distintos
de cada año:

| Año | Valores distintos de la cotización oficial |
|---|---|
| 2003 | 37 valores, de 7,48 a 7,84 |
| 2005 | 10 valores, de 8,00 a 8,10 |
| 2008 | 50 valores, de 6,97 a 7,67 |
| 2011 | 18 valores, de 6,86 a 7,04 |
| 2012 | **2** — 6,86 y 6,96 |
| 2015 | **2** — 6,86 y 6,96 |
| 2020 | **2** — 6,86 y 6,96 |
| 2025 | **2** — 6,86 y 6,96 |
| 2026 | 75 valores, de 6,86 a 12,25 |

Los dos valores de 2012 a 2025 son la compra y la venta del mismo tipo de cambio. Es decir: **la
cotización oficial no se movió ni un centavo durante catorce años seguidos.**

La consecuencia es directa. La serie de agregados monetarios del BCB —la tabla 1.06 del Boletín
Estadístico, que es la fuente del borrador— cubre **2003 a 2025**, unas 276 observaciones
mensuales. En esa ventana, el tipo de cambio es una constante durante aproximadamente los dos
tercios finales. Una variable sin varianza no puede explicar ni predecir nada: el modelo le
asignará un coeficiente sin sentido o la descartará sola.

Y el movimiento que sí importa —la flotación del 29 de junio de 2026, de 6,96 a más de 12— **está
fuera del archivo**, que termina en 2025. Cuando entre, aportará dos o tres observaciones
mensuales de un régimen distinto: suficiente para describirlo, no para estimar nada sobre él.

Nada de esto invalida el tema. Obliga a decir dos cosas en el documento: que el tipo de cambio
entra como variable **con su régimen declarado**, y que el período posterior a la flotación se
trata como quiebre estructural conocido y no como más datos de lo mismo.

---

## La formulación propuesta

### Pregunta de investigación

> ¿Con qué precisión permiten los agregados monetarios, el tipo de cambio oficial y las reservas
> internacionales netas pronosticar la variación mensual del índice de precios al consumidor de
> Bolivia a horizontes de uno, tres y seis meses, y en cuánto superan a un modelo ingenuo de
> persistencia?

La segunda mitad es la que la vuelve investigable. Sin ella, cualquier resultado se puede
presentar como éxito.

### Objetivo general

> Desarrollar y evaluar, entre septiembre y diciembre de 2026, un modelo de aprendizaje
> automático que pronostique la variación mensual del índice de precios al consumidor de Bolivia
> a horizontes de uno, tres y seis meses, a partir de la serie mensual de agregados monetarios
> del Banco Central de Bolivia (2003–2025), el tipo de cambio oficial y las reservas
> internacionales netas; midiendo su desempeño con el error absoluto medio frente a una línea
> base de persistencia, y presentando los resultados en un tablero de monitoreo que declare de
> forma explícita el quiebre de régimen cambiario del 29 de junio de 2026.

### Cómo cumple SMART

| Criterio | Dónde está |
|---|---|
| **Específico** | Nombra la variable a pronosticar (variación mensual del IPC), el país, las tres fuentes, la frecuencia y los tres horizontes. No dice «analizar el comportamiento», dice qué número se produce |
| **Medible** | Error absoluto medio contra una línea base de persistencia, por horizonte. El criterio de éxito es un número comparado con otro número, no una impresión |
| **Alcanzable** | Las tres series están verificadas como descargables en Excel real. Con unas 276 observaciones mensuales alcanza para modelos lineales, regularizados y de árboles; **no** alcanza para redes neuronales, y eso se declara como limitación en vez de esperar que no lo pregunten |
| **Relevante** | La inflación de 2025 cerró en 20,40 %, la más alta en treinta y seis años, y en junio de 2026 se abandonó quince años de tipo de cambio fijo. Es el problema económico del país en este momento |
| **Temporal** | Septiembre a diciembre de 2026, con los tres horizontes de pronóstico declarados |

### Objetivos específicos

1. **Construir la base mensual empalmada** con el IPC del INE, los agregados monetarios del BCB y
   el tipo de cambio oficial, dejando escrito el recorte temporal y el tratamiento del quiebre
   del 29 de junio de 2026.
   *Cierre:* una tabla única, con el número de observaciones declarado y el conteo por variable.

2. **Establecer la línea base de persistencia** —pronosticar que la inflación del próximo mes
   será la de este mes— y reportar su error por horizonte **antes** de entrenar cualquier modelo.
   *Cierre:* tabla con el error de la línea base disponible antes del primer entrenamiento.

3. **Entrenar al menos tres modelos** con partición estrictamente cronológica.
   *Cierre:* una prueba automática que falle si alguien usa validación cruzada aleatoria. Sobre
   series de tiempo eso filtra el futuro hacia el pasado y es el error que arrastra buena parte
   de la literatura optimista del campo.

4. **Comparar contra la línea base** en los tres horizontes y **reportar explícitamente aquellos
   donde el modelo no la supera**.
   *Cierre:* tabla comparativa, con los casos negativos incluidos y no escondidos.

5. **Publicar el tablero** con la serie observada, el pronóstico y su margen de error, y una nota
   visible de que los datos anteriores a julio de 2026 corresponden a un régimen cambiario que ya
   no rige.

---

## Sobre las variables del borrador

El borrador lista seis variables independientes y propone «primero analizar y luego seleccionar
las que tengan mayor utilidad». Conviene ajustar dos cosas.

**Elegir variables mirando el resultado es exactamente lo que produce un modelo que funciona en
el papel y no funciona nunca más.** Con 276 observaciones y seis candidatas, probar todas y
quedarse con las que mejor salen garantiza encontrar relaciones que no existen. La selección
tiene que hacerse dentro de la partición de entrenamiento y nunca mirando el conjunto de prueba,
y eso se declara en la metodología.

**La variable de criptomonedas hay que sacarla o justificarla.** El borrador dice «solo si
realmente aportan al modelo», que es la definición de buscar hasta encontrar. Si se incluye, va
como hipótesis declarada de antemano —por ejemplo, que el volumen de operaciones con activos
virtuales anticipa presiones cambiarias— con su prueba escrita antes de correrla. Si no hay
hipótesis, es mejor no incluirla: agregar una variable para que el nombre del proyecto siga
teniendo sentido es la clase de decisión que un tribunal detecta.

Sugerencia de conjunto final, ordenado por lo que se puede defender:

| Variable | Estado |
|---|---|
| Agregados monetarios M1 y M2 | Verificado descargable, mensual 2003–2025 |
| Tipo de cambio oficial | Verificado, **con el régimen declarado**: constante de 2012 a 2025 |
| Reservas internacionales netas | Verificado descargable |
| Tasas de interés pasivas | **No verificado todavía**: las URLs están listadas pero nadie descargó el archivo |
| Rezagos de la propia inflación | Es la variable más predictiva y suele quedar fuera por olvido |

---

## Si BI2 y el Integrador resultan ser la misma entrega

En ese caso no alcanza con reescribir el objetivo: hay que rehacer el anteproyecto, porque las
nueve decisiones cerradas describen un sistema distinto. Antes de aceptarlo conviene tener a mano
el argumento que ya usó el equipo para retirar la optimización de cartera del alcance: **dos
cosas bien hechas superan a tres a medias**. Sostener a la vez un pronóstico de inflación
macroeconómico y una herramienta de riesgo de cartera para el inversionista minorista es
precisamente hacer tres a medias.

La salida intermedia, si el docente quiere ver el marco macro, ya está decidida y registrada como
TASK-30: **Mundell-Fleming y el trilema entran al marco teórico y no al alcance de
implementación**. El trilema explica por qué la flotación del 29 de junio trasladó el riesgo
cambiario a los hogares, que es justamente la justificación económica del proyecto original. Eso
responde a la sugerencia del docente sin desarmar catorce semanas de trabajo.
