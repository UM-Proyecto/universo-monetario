# Universo Monetario — objetivos, alcance y datos previstos

**Materia:** Business Intelligence II · **Proyecto Integrador**, sexto semestre
**Carrera:** Ingeniería en Ciencia de Datos — Universidad Privada del Valle, Santa Cruz
**Fecha de esta versión:** 10 de septiembre de 2026

---

## 1. El problema

Bolivia tiene un canal de inversión formal que en la práctica es mayorista. Al 30 de abril de
2026 las diez agencias de bolsa autorizadas sumaban 2.157 clientes en todo el país, con una
cartera de Bs 35.512 millones, lo que da un ticket promedio cercano a Bs 16,5 millones por
cliente. Contra eso, el país tiene 7.955.358 billeteras móviles emitidas y 18,9 millones de
cuentas de depósito, con cobertura en 338 de los 339 municipios. Hay aproximadamente 3.688
billeteras móviles por cada persona con cuenta en una agencia de bolsa.

La exclusión no está escrita en ninguna norma. Ni la Bolsa Boliviana de Valores ni ninguna
agencia publica un monto mínimo de apertura. Lo que sí está publicado es el tarifario: una
tarifa mínima de cincuenta dólares por operación de renta fija hace que invertir quinientos
dólares cueste un diez por ciento solo en entrar. El mínimo formal no existe; el mínimo
económico sí, y ronda los cinco mil dólares por operación. El canal que sí funciona confirma la
lectura: los fondos de inversión administrados por las SAFI tienen 124.867 participantes, con
montos de apertura publicados desde cien dólares.

Al mismo tiempo, los últimos dos años obligaron a la población a decidir sobre su patrimonio sin
formación previa. La inflación de 2025 cerró en 20,40 %, la más alta en casi cuatro décadas. El
29 de junio de 2026 entró en vigencia el régimen cambiario flexible que terminó con quince años
de tipo de cambio fijo en Bs 6,96 por dólar. Los depósitos en dólares retenidos empezaron a
devolverse por tramos de saldo a lo largo de un año. Durante ese episodio, ninguna de las dos
opciones tradicionales del ahorrista boliviano —guardar en bolivianos o guardar dólares en el
banco— protegió el valor.

La gente reaccionó. El volumen operado con activos virtuales por entidades supervisadas pasó de
46,5 millones de dólares en el primer semestre de 2024 a 294 millones en el primero de 2025, un
alza del 630 %, con unas 252.800 personas involucradas. La composición dice para qué se usa: el
73 % de las operaciones es USDT y menos del 1 % es bitcóin o éter. No es especulación, es
cobertura.

Pero la medición internacional disponible ubica a Bolivia en 24 % de adultos financieramente
alfabetizados, contra 33 % del promedio mundial, y solo el 6,3 % declara haber ahorrado para la
vejez.

### La brecha concreta

La premisa de que no existe nada para el inversionista boliviano es falsa y conviene decirlo
antes de que lo diga el tribunal. Takenos abrió oficina comercial en Bolivia en 2026 y Belo
entró el mismo año; ambos resolvieron el problema de la entrada. Lo que ninguno hace —ni ellos,
ni los bancos, ni las agencias de bolsa— es leer lo que el usuario ya tiene disperso y
mostrárselo junto: stablecoins compradas entre pares, depósitos a plazo fijo, dólares físicos,
saldo en billeteras. Cada proveedor enseña su porción porque monetiza su vertical.

El hueco es de consolidación, no de entrada. Y hay un dato lateral que lo refuerza: de once
productos financieros revisados en la región, ninguno muestra desviación estándar. Todos
sustituyen la medida de riesgo por otra cosa; ninguno la cuantifica de forma comparable entre
alternativas.

### La dimensión fiscal

A la consolidación de patrimonio se suma una exposición que hoy nadie le muestra al usuario. La
Resolución Normativa de Directorio 102400000021, «Respaldo de Transacciones con Documentos de
Pago», aprobada el 20 de septiembre de 2024 y vigente desde el 1 de enero de 2025, obliga a
respaldar toda compraventa de bienes o servicios por un monto total igual o superior a Bs 50.000
con un documento de pago emitido o reconocido por una entidad regulada por ASFI o por el Banco
Central. Su artículo 5 fija los efectos tributarios de no tenerlo, y el principal es la pérdida
del crédito fiscal IVA para el comprador.

Quien pagó en dólares digitales por fuera del canal formal no tiene ese documento. El sistema
puede responder una pregunta que hoy no responde nadie: cuánto de lo que el usuario tiene está
en instrumentos que no puede respaldar ante el fisco.

---

## 2. Objetivos

### Objetivo general

Desarrollar un sistema de análisis que consolide el patrimonio disperso de un usuario boliviano
sin formación financiera y le muestre su riesgo en una medida comparable entre clases de activo,
expresado en bolivianos, incorporando la exposición fiscal como una dimensión más de ese riesgo.

### Objetivos específicos

1. Construir una capa de datos que integre precios de al menos cuatro clases de activo con
   frecuencias de actualización distintas, resolviendo la desincronización temporal sin generar
   artefactos.
2. Expresar todo rendimiento y todo riesgo en bolivianos, con conmutación opcional a dólares,
   manejando de forma explícita el quiebre estructural de la serie cambiaria del 29 de junio
   de 2026.
3. Implementar un modelo de clasificación con horizonte principal de siete días, reportando
   además cinco y veinte días para mostrar dónde el modelo deja de funcionar.
4. Calcular valor en riesgo por instrumento y por cartera, y presentarlo con una escala visual
   acompañada de la cifra en bolivianos.
5. Estimar, para las operaciones que el usuario registre, qué porción de su patrimonio quedaría
   sin documento de pago válido bajo la RND 102400000021.
6. Validar la comprensibilidad de la interfaz con usuarios reales sin formación financiera, que
   es el criterio que sostiene el objetivo general.

---

## 3. Alcance

### Lo que el sistema hace

El sistema consolida posiciones de las clases de activo declaradas, calcula rendimiento y riesgo
en bolivianos, clasifica el comportamiento esperado a siete días, cuantifica el valor en riesgo
y marca la porción del patrimonio expuesta fiscalmente. El universo previsto es de unos veinte
instrumentos: cinco criptomonedas, ocho acciones, cuatro pares de divisas y tres series de
bonos. Es suficiente para que las correlaciones entre clases signifiquen algo y sostenible con
caché; no alcanza para hablar de diversificación amplia dentro de cada clase, y eso queda
declarado como limitación.

### Lo que el sistema no hace, y por qué

**No ejecuta órdenes ni administra fondos.** Las cinco actividades que exigen licencia de ASFI
bajo el Decreto Supremo 5384 del 7 de mayo de 2025 son todas transaccionales: intercambio entre
criptoactivos y moneda fiduciaria, intercambio entre criptoactivos, transferencia, custodia o
administración, y emisión. Analizar y mostrar información no está entre ellas.

**No da asesoría de inversión.** El artículo 19 de la Ley 1834 del Mercado de Valores reserva a
las agencias de bolsa la asesoría financiera y la administración de inversiones en portafolio, y
en Bolivia no existe la figura del asesor de inversión independiente. El alcance seguro se
modela sobre el que la norma fija para los promotores bursátiles: informar características y
advertir sobre variabilidad de precios, nunca orientar la decisión concreta sobre un activo.

**No optimiza carteras.** La optimización de Markowitz queda como trabajo futuro. DeMiguel,
Garlappi y Uppal (2009) probaron catorce modelos de optimización sobre siete conjuntos de datos
y ninguno superó consistentemente a repartir el capital en partes iguales; estimaron que harían
falta del orden de 3.000 meses de historia con 25 activos para que la optimización le gane a la
ingenua. Con series desde 2020 no hay historia suficiente para que tenga sentido estadístico.

**No usa redes recurrentes para predecir precios.** En predicción a un paso, el LSTM tiende a
aprender la martingala: predice aproximadamente el último precio con retraso. Buena parte de la
literatura optimista arrastra fuga de datos documentada (Kapoor y Narayanan, *Patterns*, 2023).
Implementar un LSTM toma tres días; implementarlo con validez metodológica consume el semestre.

**No cubre comercio global.** La quinta clase de activo queda declarada pero su implementación
entra al final, como contexto macroeconómico, si el tiempo alcanza. Las fuentes disponibles
—Comtrade y Banco Mundial— tienen un rezago de uno a dos años, y eso se declara como limitación
explícita.

**No emite dictamen tributario.** La dimensión fiscal se presenta como estimación de exposición
con supuestos escritos, no como determinación de deuda ni como asesoría contable.

### Marco teórico incorporado

El proyecto incorpora el modelo Mundell-Fleming al marco teórico, sin llevarlo a la
implementación. El trilema describe con precisión lo que le pasó al país: no se puede sostener a
la vez tipo de cambio fijo, movilidad de capitales y política monetaria autónoma, y al pasar a
flotación la política monetaria gana tracción y la fiscal la pierde. Estimarlo formalmente hoy
es imposible —hay dos meses de datos bajo el nuevo régimen y un VAR necesita del orden de veinte
a treinta observaciones—, así que se usa como lente interpretativa apoyada en casos comparables
y no como modelo estimado.

---

## 4. Datos previstos

### Precios de activos

| Clase | Instrumentos | Frecuencia | Fuente prevista |
|---|---|---|---|
| Criptomonedas | 5 | Continua, 24/7 | APIs públicas de exchanges |
| Acciones | 8 | Diaria, cinco días hábiles | Proveedor de series históricas por definir |
| Divisas | 4 pares | Diaria | Boletín del BCB y proveedor internacional |
| Bonos | 3 series | Diaria, con cupones trimestrales | Bolsa Boliviana de Valores y proveedor internacional |
| Comercio global | Declarado, implementación final | Anual, con rezago de 1 a 2 años | UN Comtrade, Banco Mundial |

### Tipo de cambio y conversión a bolivianos

El tipo de cambio oficial del Banco Central de Bolivia es la fuente primaria de conversión. El
histórico diario va de 1940 a 2026 pero vive en páginas HTML por año, así que se raspa en lugar
de descargarse. Para el paralelo, `paralelo.bo` está verificada y tiene histórico desde 2024;
`dolarbluebolivia.click` queda por evaluar. La distinción importa menos que antes, porque tras
la flotación la brecha cayó a cerca del 1 %, pero el histórico anterior a junio de 2026 sí la
necesita: en ese tramo la brecha superaba el 40 %.

**Gotcha registrado:** los enlaces del Boletín Estadístico del BCB llevan la fecha de
publicación dentro de la ruta y cambian cada trimestre. Un pipeline que los fije se rompe solo a
los tres meses; la fecha vigente hay que resolverla desde la página índice. Los enlaces del INE,
en cambio, son permanentes.

### Series macroeconómicas

Bajan como archivos Excel reales, verificado descargando y abriendo cada uno: agregados
monetarios del BCB mensuales de 2003 a 2025, reservas internacionales netas, tipo de cambio
oficial del boletín, IPC empalmado del INE y PIB anual de 1980 a 2024.

### Datos del componente fiscal

Los agregados de operaciones con activos virtuales por entidades supervisadas, publicados por
ASFI y el BCB, acotan qué porción del volumen pasa por canal formal. Es la misma serie de la que
salen los 294 millones de dólares y las 252.800 personas. Las estadísticas de importación por
partida, origen y valor de la Aduana Nacional dan el denominador del lado de las operaciones que
superan el umbral de Bs 50.000. La diferencia entre ambos no es un dato medido sino una
estimación con supuestos, y eso es defendible siempre que los supuestos estén escritos.

### Datos de validación con usuarios

La validación de comprensibilidad se hace con usuarios reales sin formación financiera, mediante
un instrumento propio. Es dato primario levantado por el equipo, no una fuente pública.

---

## 5. Limitaciones declaradas

El universo de veinte instrumentos no permite hablar de diversificación amplia dentro de cada
clase. Las series de comercio global tienen rezago de uno a dos años. Los datos anteriores al 29
de junio de 2026 describen un régimen cambiario que ya no rige, y cualquier modelo entrenado
sobre la serie completa tiene que tratar ese quiebre de forma explícita. La estimación de
exposición fiscal depende de supuestos sobre el canal de pago que el sistema no puede observar
directamente. Y hay una pregunta abierta que conviene tener contestada antes de la defensa: si
el comprobante que emite un proveedor de servicios de activos virtuales autorizado por ASFI
califica como documento de pago bajo la RND 102400000021. La Resolución ASFI 540/2025 obligó a
esos proveedores a autorizarse y el plazo venció el 30 de abril de 2026, con más de 176
proveedores y 33 plataformas en el proceso, así que desde hace meses existen proveedores
regulados. Si el comprobante califica, la dimensión fiscal se reformula como problema de
transición; si no califica, queda confirmada por norma en su punto más atacable. En cualquiera
de los dos casos el problema no desaparece hacia atrás: las operaciones pagadas en dólares
digitales entre 2023 y abril de 2026 ya ocurrieron y su crédito fiscal ya se perdió.
