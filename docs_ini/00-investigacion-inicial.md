# Investigación inicial — el mercado que el proyecto quiere atender

> **Cómo se produjo este documento.** Lo escribió un agente de IA (Claude Code, modelo Opus 5)
> corriendo en la terminal del equipo, a partir de la base de conocimiento del proyecto y de una
> ronda previa de verificación de fuentes. Fecha de redacción: 10 de septiembre de 2026. Las
> cifras llevan su fecha de corte porque varias envejecen rápido, y al final hay una sección de
> advertencias de citación que registra los errores que ya se cometieron una vez con este mismo
> material. No es un documento de opinión: cada afirmación que sostiene el planteamiento tiene
> una fuente identificable, y las que quedaron sin verificar están marcadas como tales.

---

## Lo que la evidencia dice del canal formal

El punto de partida del proyecto es una asimetría medida. Al 30 de abril de 2026 las diez
agencias de bolsa autorizadas de Bolivia sumaban **2.157 clientes en todo el país**, con una
cartera de **Bs 35.512 millones**. La división da un ticket promedio de unos Bs 16,5 millones
por cliente. En dólares eso son 2,4 millones al tipo de cambio oficial de 6,96 vigente en abril
de 2026, y 1,4 millones al oficial de agosto. La cifra en bolivianos es la que no envejece; la
de dólares va siempre con su tipo de cambio y su fecha.

La conclusión que se sigue no es que haya un canal minorista mal aprovechado, sino que **el
canal es mayorista**.

Del otro lado, la infraestructura de pagos del país es masiva: **7.955.358 billeteras móviles
emitidas**, 18,9 millones de cuentas de depósito, cobertura en 338 de los 339 municipios, 229
pagos electrónicos por habitante al año, con el 86 % de las transferencias hechas por código QR
y el 52 % de esos pagos por debajo de cincuenta bolivianos. La relación entre ambos números es
de **3.688 billeteras móviles por cada persona con cuenta en una agencia de bolsa**.

## La barrera es económica, no normativa

Este punto conviene tenerlo claro porque es el primero que un tribunal va a atacar. Ni la Bolsa
Boliviana de Valores ni ninguna agencia publica un monto mínimo de apertura de cuenta. Lo que sí
está publicado es el tarifario, y ahí aparece el mínimo real: una **tarifa mínima de cincuenta
dólares por operación de renta fija** convierte una inversión de quinientos dólares en una
operación que cuesta 10 % solo en entrar. El mínimo formal no existe; el mínimo económico está
publicado y ronda los cinco mil dólares por operación.

El contraejemplo dentro del mismo país cierra el argumento: los fondos de inversión
administrados por las SAFI tienen **124.867 participantes**, con montos de apertura publicados
**desde cien dólares**. Cuando la puerta está abierta y el precio está escrito, el boliviano
entra.

## El cuello de botella es conocimiento

La inflación de 2025 cerró en **20,40 %**, la más alta en casi cuatro décadas. Los depósitos en
dólares quedaron retenidos y el Ministerio de Economía anunció su devolución **total** —unos 933
millones de dólares correspondientes a personas naturales— mediante un cronograma por tramos de
saldo a lo largo de un año: de 1.001 a 3.000 desde el 15 de julio de 2026, de 3.001 a 5.000
desde mediados de agosto, y así sucesivamente.

Durante ese episodio, ninguna de las dos opciones tradicionales del ahorrista boliviano protegió
el valor. La población reaccionó buscando cobertura: el volumen operado con activos virtuales
por entidades supervisadas pasó de **46,5 millones de dólares en el primer semestre de 2024 a
294 millones en el primero de 2025**, un alza del 630 %, con unas **252.800 personas**
involucradas. Y la composición dice para qué se usa: **73 % de las operaciones es USDT y menos
del 1 % es bitcóin o éter**. Es cobertura, no especulación.

Pero la capacidad de decidir no acompañó al volumen. La medición internacional disponible ubica
a Bolivia en **24 % de adultos financieramente alfabetizados**, contra 33 % del promedio
mundial, por debajo de Uruguay, Chile, Brasil y Argentina. Solo el **6,3 %** declara haber
ahorrado para la vejez.

## Qué cambió el 29 de junio de 2026

La Resolución Ministerial 245/2026, anunciada el 26 de junio de 2026 y vigente desde el 29,
terminó con quince años de tipo de cambio fijo en Bs 6,96 por dólar. El oficial abrió en 9,73 y
llegó a 11,54 en agosto. La brecha con el paralelo cayó de más del 40 % a cerca del 1 %.

Esto tiene dos consecuencias para el proyecto, y las dos son de método.

La primera es que **un enunciado apoyado en una fricción regulatoria puede cerrarse solo mientras
se lo piensa**. El planteamiento original del proyecto medía la brecha cambiaria; la flotación lo
dejó sin objeto en el mismo mes en que se estaba escribiendo. La lección transferible es fechar
el enunciado contra la norma vigente antes de trabajarlo, no después.

La segunda es que **hay un quiebre estructural de serie con fecha conocida**. Los datos previos
al 29 de junio de 2026 describen un régimen cambiario que ya no rige. Cualquier modelo entrenado
sobre la serie completa tiene que tratar ese quiebre de forma explícita, y lo que la
disponibilidad de datos permite hoy es un test de Chow con la fecha conocida y un estudio de
evento alrededor de esa fecha, no una estimación de coeficientes «del período flotante»: hay dos
meses de observaciones bajo el régimen nuevo.

Un dato que corrige el encuadre de urgencia: al 5 de septiembre de 2026 la **inflación acumulada
del año va en 3 %**, contra 18 % en el mismo tramo de 2025. Un argumento construido sobre «la
inflación es el problema» en presente se cae con ese dato. El que aguanta es el de **pérdida
acumulada de poder adquisitivo**: una canasta de quince productos básicos pasó de Bs 189 en 2021
a Bs 301 en 2026, y Bs 1.000 que alcanzaban para poco más de cinco canastas hoy cubren poco más
de tres.

## Qué existe ya en el mercado, y qué no

La premisa de que no hay nada para el inversionista boliviano es falsa. **Takenos** abrió oficina
comercial en Bolivia en 2026 con representante local y alianza con Tether; **Belo** entró el
mismo año. Los dos resolvieron el problema de la entrada: abrir cuenta y poner un dólar.

Lo que ninguno hace —ni ellos, ni los bancos, ni las agencias de bolsa— es **leer lo que el
usuario ya tiene disperso y mostrárselo junto**: stablecoins compradas entre pares, depósito a
plazo fijo, dólares físicos, saldo en billeteras. Cada proveedor enseña su porción porque
monetiza su vertical. El hueco es de consolidación, no de entrada.

Hay además un hallazgo lateral que vale para cualquier producto financiero de la región: de
**once productos revisados, ninguno muestra desviación estándar**. Fintual le pone nombres de
celebridades a sus niveles de riesgo, tyba arranca por la meta del usuario, Takenos traduce
riesgo a quién custodia los fondos. Todos sustituyen la medida de riesgo por otra cosa; ninguno
la cuantifica de forma comparable entre alternativas. Ahí hay espacio para diferenciarse sin
inventar nada: mostrar la cifra.

## Por qué se descartaron dos técnicas que el planteamiento original traía

**Redes LSTM para predicción de precios.** En predicción a un paso el modelo tiende a aprender la
martingala: predice aproximadamente el último precio con retraso. En pruebas sobre el S&P 500 la
estrategia de martingala rindió el doble que el LSTM. Buena parte de la literatura optimista
arrastra fuga de datos documentada (Kapoor y Narayanan, *Patterns*, 2023). Implementar un LSTM
en Keras toma tres días; implementarlo con validez metodológica consume el semestre.

**Optimización de cartera de Markowitz.** DeMiguel, Garlappi y Uppal (2009) probaron catorce
modelos de optimización sobre siete conjuntos de datos y ninguno superó consistentemente a
repartir el capital en partes iguales. Estimaron que harían falta unos 3.000 meses de historia
con 25 activos para que la optimización le gane a la ingenua. Con series desde 2020 no hay
historia suficiente.

Las dos exclusiones son un resultado del trabajo, no una renuncia: el caso de clase que dio
origen al tema proponía ambas técnicas, y la investigación las contradice con literatura.

## La dimensión fiscal, que es el hallazgo más reciente

El 9 de septiembre de 2026 apareció un enunciado que corre el eje hacia el importador boliviano
que paga a su proveedor en dólares digitales y pierde el crédito fiscal por no poder respaldar
esa transferencia. La decisión del equipo fue **conservarlo como dimensión y no como eje**: el
importador que paga en USDT y el ahorrista que se cubre en USDT son el mismo fenómeno, y el
sistema puede sumar la pregunta «cuánto de lo que tengo no puedo respaldar ante el fisco» sin
tirar la evidencia acumulada sobre el inversionista minorista.

El razonamiento que llevó a esa decisión está en `01-marco-normativo.md`, junto con la norma que
lo sostiene y la pregunta abierta que decide su tamaño.

---

## Advertencias de citación

Esta lista existe porque una ronda de verificación cerrada el 28 de agosto de 2026 obligó a
corregir **doce afirmaciones** del anteproyecto. Cuatro cambiaban el sentido de lo que el
documento decía. Se deja escrita porque el modo de falla se repite.

**El «tope de tres mil dólares por ahorrista» no existe.** La nota del Ministerio de Economía
anuncia devolución total, con tramos de saldo escalonados en el tiempo. Los tres mil eran el
techo del primer tramo, no un límite por persona. La fuente oficial desmentía la afirmación que
el documento le atribuía.

**El 73 % de USDT no es una cifra del BCB.** Se abrieron y descartaron una veintena de documentos
del banco y dos de ASFI: no está en ninguno. Viene de reportes de entidades financieras
difundidos por la prensa en agosto de 2025. Citarlo como «según el BCB» es falso.

**La Resolución de Directorio 082/2024 es del 25 de junio, no del 26.** El 26 es la fecha del
comunicado que la anunció. Se verificó leyendo la resolución firmada, que hubo que extraer como
imagen incrustada porque el PDF es un escaneo sin capa de texto. La búsqueda web devolvía «26 de
junio» de forma consistente en varias fuentes secundarias, incluido material jurídico. Ninguna
cantidad de fuentes secundarias coincidentes reemplaza al documento firmado.

**El ticket promedio en dólares depende del tipo de cambio que se use.** Al oficial de abril de
2026 son 2,4 millones; al de agosto, 1,4 millones. El monto se cita en bolivianos y el
equivalente en dólares va con su tipo de cambio y su fecha.

**No mezclar la cifra de Chainalysis con la del BCB.** Los 14.800 millones de dólares de valor
on-chain recibido y los 430 millones acumulados del BCB miden cosas distintas y difieren en tres
órdenes de magnitud.

**Las alertas de ASFI son doce, sobre siete plataformas.** Ocho llevan fecha impresa, entre junio
de 2025 y enero de 2026; las otras cuatro usan plantillas sin línea de fecha. Una sola nombra
criptoactivos de forma explícita, así que escribir «alertas sobre inversión en cripto» les pone
una palabra que la mayoría no usa. Y las dos que declaran video generado con IA con la cara de
autoridades son las dos de la misma plataforma: son dos alertas sobre un solo caso.

**El 24 % de alfabetización financiera es de una medición de 2014** y va siempre con su fecha,
apuntalado con el 6,3 % de 2024.

**Las cifras de la canasta básica están confirmadas por dos búsquedas coincidentes, no por
lectura del cuerpo del artículo**: el sitio que las publica devuelve 403 a lectura automatizada,
y la firma del autor quedó sin verificar.

**El modo de falla que más conviene recordar es otro, y apareció dos veces.** Un agente buscó
«73 %» en el informe de vigilancia del sistema de pagos del BCB y lo encontró, dos veces, pero
era el 73 % de las órdenes electrónicas que son pagos con QR, nada que ver con USDT. Lo mismo
pasó con «$us3.000 millones» en el informe de estabilidad financiera, que ahí son pérdidas por
bloqueos de caminos. Es peor que un PDF con el título equivocado, porque ahí el documento se caza
mirando la portada: acá el documento es auténtico, del emisor correcto, del área correcta y sobre
el tema correcto, y el número coincide. **Lo único que lo caza es leer la oración entera.**
