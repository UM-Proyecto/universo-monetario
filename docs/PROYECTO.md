# Universo Monetario — objetivos, alcance y datos previstos

**Materia:** Business Intelligence II · **Proyecto Integrador**, sexto semestre
**Carrera:** Ingeniería en Ciencia de Datos — Universidad Privada del Valle, Santa Cruz
**Fecha de esta versión:** 10 de septiembre de 2026

> Este documento recoge el enfoque que el equipo consolidó en el tablero «Entendiendo problemas»:
> del planteamiento general sobre la administración del dinero en Bolivia al problema específico
> del importador que paga con dólares digitales y no puede respaldar ese pago. Reemplaza al
> boceto de agosto, cuyo eje era el inversionista minorista.

---

## 1. Planteamiento general

La inflación, el aumento del dólar y la falta de herramientas financieras dificultan que las
personas y las empresas bolivianas administren su dinero. El resultado son tres cosas medibles:
pérdida de poder adquisitivo, gastos imprevistos y decisiones tomadas sin información suficiente.

El problema alcanza a varios grupos a la vez: ahorristas sin formación financiera, personas que
tienen dinero en bolivianos o en dólares, importadores que pagan a proveedores extranjeros,
personal encargado de compras e inventarios, y quienes usan dólares digitales o activos virtuales.

Sobre eso pesan factores sociales y culturales que el proyecto no puede ignorar: la baja educación
financiera, la desconfianza hacia las plataformas digitales, las estafas asociadas a ofertas de
inversión y la costumbre de ahorrar únicamente en efectivo, en bolivianos o en dólares.

### La evidencia de que el problema importa

**Las operaciones con activos virtuales crecieron fuerte.** El volumen operado por entidades
supervisadas pasó de 46,5 millones de dólares en el primer semestre de 2024 a 294 millones en el
primero de 2025, un alza del 630 %. La composición dice para qué se usa: alrededor del 73 % de las
operaciones es USDT y menos del 1 % es bitcóin o éter. No es especulación, es cobertura.

**La infraestructura digital de pagos es masiva.** Hay 7.955.358 billeteras móviles emitidas a
julio de 2026 y 18.925.898 cuentas de depósito a junio del mismo año, con cobertura en 338 de los
339 municipios y el 86 % de las transferencias electrónicas hechas por código QR.

**La participación en el mercado formal de valores es mínima.** Las agencias de bolsa autorizadas
sumaban 2.157 clientes en todo el país en abril de 2026. Son unas 3.688 billeteras móviles por
cada cliente de agencia de bolsa.

La lectura conjunta es la que sostiene el proyecto: **la gente ya usa herramientas digitales, pero
le falta información sencilla para entender los riesgos y respaldar lo que hace.**

### Cómo se replanteó el problema

El equipo arrancó pensando que el problema era la falta de acceso a inversiones. Al medirlo, esa
premisa no se sostuvo: Takenos y Belo entraron a Bolivia en 2026 y resolvieron la entrada; los
fondos administrados por las SAFI tienen 124.867 participantes con montos de apertura desde cien
dólares. Cuando la puerta está abierta, el boliviano entra.

Lo que sí falta es **información consolidada**. Cada plataforma muestra solamente sus propios
productos, y ninguna permite ver todo el patrimonio, los riesgos y los rendimientos en un solo
lugar. La brecha es de consolidación, no de acceso.

---

## 2. Problema específico

El problema se enfoca en los **importadores bolivianos**.

El importador compra mercadería en otro país y paga a su proveedor con dólares digitales. Puede
tener dificultades para obtener un comprobante válido de esa transferencia, y sin un respaldo
documental aceptado corre el riesgo de no poder justificar formalmente la compra ante la
administración tributaria.

La consecuencia concreta es la posible pérdida del **crédito fiscal**: el monto pagado por
concepto de IVA en sus compras, que puede usar para descontar parte del impuesto que debe pagar.
Sin él, asume un costo tributario mayor por una operación que realmente hizo y realmente pagó.

Dicho en una línea: **el importador compra y paga su mercadería, pero si el pago con dólares
digitales no cuenta con documentación aceptada, puede tener dificultades para demostrar ese gasto
y aprovechar su crédito fiscal.**

### La norma, ya identificada y verificada

El tablero del equipo dejó anotado que antes de defender la afirmación de que las compras mayores
a Bs 50.000 «se presumen inexistentes» hacía falta identificar la norma exacta y confirmar que se
aplica a pagos con dólares digitales. Esa verificación está hecha, y **corrige la afirmación**.

La norma es la **Resolución Normativa de Directorio 102400000021, «Respaldo de Transacciones con
Documentos de Pago»**, aprobada el 20 de septiembre de 2024 y vigente desde el 1 de enero de 2025.
Obliga a respaldar toda compraventa de bienes o servicios por un monto total igual o superior a
**Bs 50.000** —al contado, a crédito o en pagos parciales— con un documento de pago emitido o
reconocido por una entidad regulada por ASFI o por el Banco Central: cheque, orden de
transferencia electrónica de fondos, voucher de tarjeta o carta de crédito.

Su **artículo 5** fija los efectos tributarios de no contar con ese respaldo, y el principal para
el comprador es la **pérdida del crédito fiscal IVA**.

**La norma no dice que la compra se presuma inexistente.** Dice que hay consecuencias tributarias,
y la principal es la pérdida del crédito fiscal. La redacción prudente que el equipo se propuso
—«podrían no ser reconocidas fiscalmente si no cumplen los requisitos documentales»— es la
correcta, y ahora tiene la norma detrás.

### La pregunta abierta que decide el tamaño del problema

La **Resolución ASFI 540/2025** obligó a los Proveedores de Servicios de Activos Virtuales y a las
plataformas de pago a obtener autorización formal. El plazo venció el 30 de abril de 2026; más de
176 proveedores y 33 plataformas entraron al proceso. Desde entonces **existen proveedores
regulados por ASFI**, y la RND acepta documentos emitidos o reconocidos por entidad regulada por
ASFI.

De ahí sale la pregunta que hay que contestar antes de la defensa: **¿el comprobante que emite un
proveedor autorizado califica como documento de pago bajo la RND 102400000021?** Se contesta
contrastando la enumeración de documentos admitidos de la norma contra lo que un proveedor
autorizado efectivamente emite.

Sirve en los tres desenlaces. Si no califica, el problema queda confirmado por norma en su punto
más atacable. Si califica, el enunciado se reformula como problema de transición: quien venía
pagando fuera del canal formal tiene que migrar a uno que recién existe, y no sabe cuánto crédito
fiscal dejó en el camino. Y en cualquier caso **el problema no desaparece hacia atrás**: las
operaciones pagadas en dólares digitales entre 2023 y abril de 2026 ya ocurrieron y su crédito
fiscal ya se perdió. Es stock, no flujo, y es cuantificable.

---

## 3. Objetivos

### Objetivo general

Desarrollar un sistema de análisis que consolide y presente de manera ordenada y comprensible las
operaciones de pago con dólares digitales de importadores bolivianos, estimando qué porción de
esas operaciones queda sin respaldo documental válido bajo la normativa tributaria vigente y qué
crédito fiscal está en riesgo por esa causa.

### Objetivos específicos

1. Caracterizar el marco normativo aplicable —RND 102400000021, Resolución ASFI 540/2025 y Decreto
   Supremo 5384— determinando con precisión qué documentos de pago son admitidos y si el
   comprobante de un proveedor autorizado de activos virtuales califica entre ellos.
2. Construir un flujo de ingesta que integre las fuentes públicas que permiten dimensionar el
   fenómeno: estadísticas de importación de la Aduana Nacional, agregados de operaciones con
   activos virtuales de ASFI y el BCB, y series de tipo de cambio e inflación.
3. Estimar, a nivel agregado y por sector importador, el volumen de operaciones que supera el
   umbral de Bs 50.000 y la porción de ese volumen expuesta a quedar sin documento de pago válido,
   dejando escritos todos los supuestos de la estimación.
4. Desarrollar un modelo de clasificación que, sobre operaciones de compra, estime la probabilidad
   de que una operación quede sin respaldo válido a partir de variables observables —monto, forma
   de pago, contraparte y documentación asociada— y evaluarlo contra una línea base ingenua
   mediante exactitud, F1, ROC-AUC y matriz de confusión.
5. Situar el problema en el marco macroeconómico del cambio de régimen cambiario de junio de 2026,
   usando el modelo IS-LM y su extensión Mundell-Fleming como lente interpretativa del contexto en
   que se toman estas decisiones de pago.
6. Implementar un tablero que presente las operaciones consolidadas, el crédito fiscal en riesgo y
   su evolución, y validar su comprensibilidad con usuarios sin formación contable ni financiera.

---

## 4. Alcance

### Delimitación en cinco dimensiones

| Dimensión | Qué comprende |
|---|---|
| **Temática** | Ingeniería de datos, clasificación supervisada y análisis normativo aplicados a operaciones de pago con activos virtuales. No abarca auditoría contable, valuación de mercadería ni análisis aduanero de partidas arancelarias. |
| **Espacial** | Importadores bolivianos y sus operaciones de pago al exterior. El contexto normativo es exclusivamente boliviano. |
| **Temporal** | Desarrollo en el segundo semestre de 2026. La ventana de análisis se ancla en la vigencia de la RND, desde el 1 de enero de 2025, con contexto desde 2023. |
| **Metodológica** | Enfoque cuantitativo, diseño no experimental sobre datos secundarios públicos y, donde se consiga, datos de compras de una empresa real con montos normalizados. Implementación en Python. |
| **Funcional** | El sistema analiza, estima y presenta. No emite dictamen tributario, no presenta declaraciones, no ejecuta pagos y no custodia fondos. |

### Por qué la frontera funcional es ésta y no otra

Las cinco actividades con activos virtuales que exigen licencia de ASFI bajo el Decreto Supremo
5384 son todas transaccionales: intercambio entre criptoactivos y moneda fiduciaria, intercambio
entre criptoactivos, transferencia, custodia o administración, y emisión. Analizar información y
mostrarla no está entre ellas.

Y del lado tributario, el sistema **estima exposición con supuestos escritos**; determinar deuda
tributaria o emitir dictamen es trabajo de profesional habilitado, no de una herramienta de
análisis. Esa distinción va escrita en el tablero, no solo en el documento.

### Qué queda fuera

**No se cubre el inversionista minorista.** El planteamiento anterior del equipo apuntaba a
consolidar el patrimonio disperso de un ahorrista sin formación financiera. Ese eje queda como
antecedente: su evidencia sostiene el planteamiento general de la sección 1, pero el problema
específico es el del importador.

**No se estiman modelos macroeconómicos.** El IS-LM y Mundell-Fleming entran al marco teórico, no
a la implementación. La razón es aritmética y no de método: hay dos meses de datos bajo el régimen
cambiario nuevo y una estimación de ese tipo necesita del orden de veinte a treinta observaciones.
Cualquier tabla de coeficientes «del período flotante» se cae en la primera pregunta sobre grados
de libertad. Lo que sí aguanta es un test de Chow con la fecha de quiebre conocida y un estudio de
evento alrededor del 29 de junio de 2026.

**No se construyen matrices de contabilidad social ni modelos de equilibrio general.** El
relevamiento de herramientas está en `docs/investigacion-inicial/02-fuentes-de-datos.md` y su conclusión es que ese
camino cuesta un trabajo de tesis de maestría, no un semestre.

---

## 5. Datos previstos

### Fuentes públicas que dan el denominador

| Fuente | Qué aporta | Frecuencia | Estado |
|---|---|---|---|
| Aduana Nacional de Bolivia | Estadísticas de importación por partida, origen y valor; permite contar operaciones sobre Bs 50.000 | Periódica | Por instrumentar |
| ASFI y BCB | Agregados de operaciones con activos virtuales por entidades supervisadas; acota la porción por canal formal | Semestral / anual | Identificada |
| ASFI | Registro de proveedores de servicios de activos virtuales autorizados | Continua | Identificada |
| Servicio de Impuestos Nacionales | Texto de la RND 102400000021 y normativa conexa | — | Verificada |

**La diferencia entre el volumen importado que supera el umbral y el volumen que pasa por canal
formal no es un dato medido: es una estimación con supuestos.** Es defendible siempre que los
supuestos estén escritos y se pueda rehacer la cuenta con otros. Escribirlos es parte del
entregable.

### Datos de operaciones para el componente de modelado

El componente de clasificación necesita operaciones individuales, no agregados. Hay disponible un
**conjunto de datos de compras de una empresa de Santa Cruz, con montos normalizados**, apto para
prototipar el modelo con variables reales: monto, forma de pago, contraparte y documentación
asociada.

Sin esas operaciones el proyecto se queda en estimación agregada, que es un resultado válido pero
más pobre. Conseguir y anonimizar ese conjunto es una tarea de la primera etapa, no del final.

### Series de contexto macroeconómico

Todas se verificaron descargando el archivo y abriéndolo, no solo comprobando que la página
responda.

| Serie | Emisor | Cobertura | Formato |
|---|---|---|---|
| Agregados monetarios | BCB | Mensual, 2003–2025 | Excel |
| Reservas internacionales netas | BCB | Mensual | Excel |
| Tipo de cambio oficial | BCB | Mensual (boletín) y diario 1940–2026 (HTML) | Excel / raspado |
| IPC empalmado | INE | Mensual | Excel |
| PIB anual | INE | 1980–2024 | Excel |
| Tipo de cambio paralelo | `paralelo.bo` | Diaria, histórico desde 2024 | Raspado |

**Gotcha registrado:** los enlaces del Boletín Estadístico del BCB llevan la fecha de publicación
dentro de la ruta y cambian cada trimestre. Un pipeline que los fije se rompe solo a los tres
meses, sin avisar. La fecha vigente hay que resolverla desde la página índice en cada corrida. Los
enlaces del INE son permanentes.

### Datos primarios del equipo

La validación de comprensibilidad se hace con usuarios sin formación contable ni financiera,
mediante un instrumento que levanta el equipo. Es el dato que sostiene el sexto objetivo, así que
su diseño no se improvisa: la pregunta tiene que poder devolver un resultado que desmienta la
hipótesis, no solo confirmarla.

---

## 6. Limitaciones declaradas

**Quien paga fuera del canal formal no deja registro público.** No existe un conjunto de datos
directo del fenómeno; el denominador se estima con fuentes públicas y la porción expuesta sale de
supuestos, no de una medición.

**El componente de modelado depende de conseguir operaciones reales.** Si el conjunto de datos de
compras no se consigue o no alcanza en volumen, el proyecto se queda en estimación agregada.

**La pregunta normativa está abierta.** Si el comprobante de un proveedor autorizado califica como
documento de pago, el tamaño del problema en presente se reduce y el enunciado se reformula como
transición. El stock acumulado entre 2023 y abril de 2026 no cambia en ninguno de los dos casos.

**El quiebre estructural del boliviano de junio de 2026** obliga a explicitar el tratamiento del
corte en cualquier serie que cruce esa fecha; los datos previos describen un régimen cambiario que
ya no rige.

**El componente macroeconómico es interpretativo.** No hay observaciones suficientes bajo el
régimen nuevo para estimar formalmente el modelo, y el documento lo dice en lugar de presentar
coeficientes que no se sostienen.

**El estudio no establece causalidad ni constituye asesoramiento tributario ni de inversión.**
