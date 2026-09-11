# Investigación inicial — el problema del importador que paga en dólares digitales

> **Cómo se produjo este documento.** Lo escribió un agente de IA corriendo en la terminal del
> equipo, sobre la base de conocimiento del proyecto y de una ronda
> previa de verificación de fuentes. Fecha de redacción: 10 de septiembre de 2026. Las cifras van
> con su fecha de corte porque varias envejecen rápido, y al final hay una sección de advertencias
> de citación que registra los errores que ya se cometieron una vez con este mismo material.

---

## Punto de partida: el problema general

La inflación, el aumento del dólar y la falta de herramientas financieras dificultan que las
personas y las empresas bolivianas administren su dinero. El equipo lo trabajó primero en esa
amplitud, y la investigación inicial midió las tres afirmaciones que lo sostienen.

### Las operaciones con activos virtuales crecieron, y se sabe para qué

El volumen operado por entidades supervisadas pasó de **46,5 millones de dólares en el primer
semestre de 2024 a 294 millones en el primero de 2025**, un alza del 630 %. La composición es lo
que da la clave: alrededor del **73 % de las operaciones es USDT** y menos del 1 % es bitcóin o
éter. Quien compra un activo cuyo precio está atado al dólar no está especulando, está cubriendo
valor.

Esta es exactamente la conducta que produce el problema del importador: el que paga a su proveedor
en USDT lo hace porque le resuelve la operación, no porque esté apostando.

### La infraestructura digital es masiva y el mercado formal de valores es mínimo

Hay **7.955.358 billeteras móviles emitidas** a julio de 2026 y 18.925.898 cuentas de depósito a
junio del mismo año, con cobertura en 338 de los 339 municipios y el 86 % de las transferencias
electrónicas hechas por código QR. Contra eso, las agencias de bolsa autorizadas sumaban **2.157
clientes** en abril de 2026. Son unas 3.688 billeteras móviles por cada cliente de agencia de
bolsa.

La lectura es que **la gente ya opera digitalmente**. Lo que le falta no es la herramienta de pago:
es la información que le permita entender el riesgo y respaldar lo que hace.

### El contexto que empuja: dos años sin refugio

La inflación de 2025 cerró en **20,40 %** según el INE. El 29 de junio de 2026 entró en vigencia el
régimen cambiario flexible que terminó con el tipo de cambio fijo de Bs 6,96 vigente desde
noviembre de 2011; el oficial abrió en 9,73 y llegó a **Bs 11,54 el 25 de agosto de 2026**. Los
depósitos en dólares retenidos —unos 933 millones de dólares de personas naturales— empezaron a
devolverse por tramos de saldo desde julio de 2026.

Un matiz que conviene tener a mano porque desarma un argumento mal construido: **al 5 de septiembre
de 2026 la inflación acumulada del año va en 3 %**, contra 18 % en el mismo tramo de 2025. Un
planteamiento que diga «la inflación es el problema» en presente se cae con ese dato. El que
aguanta es el de **pérdida acumulada de poder adquisitivo**: una canasta de quince productos
básicos pasó de Bs 189 en 2021 a Bs 301 en 2026.

---

## Cómo se replanteó el problema

El equipo arrancó suponiendo que el problema era la falta de acceso a inversiones. **Esa premisa no
se sostuvo al medirla.** Takenos abrió oficina comercial en Bolivia en 2026 con representante local
y alianza con Tether; Belo entró el mismo año. Los fondos administrados por las SAFI tienen
**124.867 participantes** con montos de apertura publicados desde cien dólares en algunos casos.
Cuando la puerta está abierta y el precio está escrito, el boliviano entra.

Lo que falta es **información consolidada**: cada plataforma muestra sus propios productos y
ninguna permite ver el patrimonio, los riesgos y los rendimientos en un solo lugar. Cada proveedor
enseña su porción porque monetiza su vertical.

De ese replanteo salió el enfoque específico: **los importadores bolivianos**.

---

## El problema específico

El importador compra mercadería en otro país y paga a su proveedor con dólares digitales. Puede
tener dificultades para obtener un comprobante válido de esa transferencia, y sin respaldo
documental aceptado corre el riesgo de no poder justificar formalmente la compra ante la
administración tributaria. La consecuencia concreta es la posible **pérdida del crédito fiscal**,
que le sube el costo tributario de una operación que realmente hizo y realmente pagó.

La norma que lo rige está identificada y verificada: es la **RND 102400000021**, y su tratamiento
completo está en `01-marco-normativo.md`. Dos precisiones que salieron de esa verificación y que
cambian cómo hay que redactar el planteamiento:

**La norma no dice que la compra se presuma inexistente.** Dice que sin documento de pago válido
hay consecuencias tributarias, y la principal para el comprador es la pérdida del crédito fiscal
IVA. La versión fuerte de la afirmación no está en el texto legal, y un tribunal que abra la norma
lo va a ver.

**El problema puede haberse achicado solo, y hay que medirlo antes de defenderlo.** Desde el 30 de
abril de 2026 existen proveedores de servicios de activos virtuales autorizados por ASFI, y la
norma acepta documentos emitidos o reconocidos por entidad regulada por ASFI. Si el comprobante de
un proveedor autorizado califica, el problema en presente se reduce al que opera fuera del canal
formal. Contestarlo cuesta medio día y hay que hacerlo antes de la defensa, no después.

### Por qué el problema no desaparece con esa respuesta

Aunque el comprobante califique, **las operaciones pagadas en dólares digitales entre 2023 y abril
de 2026 ya ocurrieron y su crédito fiscal ya se perdió**. Es stock, no flujo, y es cuantificable.
Un tribunal que diga «eso ya se resolvió» se contesta con la ventana temporal.

Y si califica, el enunciado se reformula como problema de transición, que es más interesante y no
menos: el importador acostumbrado a pagar por canales entre pares tiene que migrar a un canal que
recién existe, y no sabe cuánto crédito fiscal dejó en el camino.

---

## Antecedente: lo que quedó atrás y por qué

El planteamiento anterior del equipo apuntaba a consolidar el patrimonio disperso de un ahorrista
sin formación financiera, con modelos de predicción de rendimiento. Ese eje quedó como
antecedente, y dos de sus resultados siguen valiendo porque son exclusiones fundamentadas:

**Redes LSTM para predicción de precios.** En predicción a un paso el modelo tiende a reproducir la
martingala: predice aproximadamente el último precio con retraso. En pruebas sobre el S&P 500 la
estrategia de martingala rindió el doble que el LSTM. Buena parte de la literatura optimista
arrastra fuga de datos documentada (Kapoor y Narayanan, *Patterns*, 2023).

**Optimización de cartera de Markowitz.** DeMiguel, Garlappi y Uppal (2009) probaron catorce
modelos de optimización sobre siete conjuntos de datos y ninguno superó consistentemente a repartir
el capital en partes iguales. Estimaron que harían falta unos 3.000 meses de historia con 25
activos para que la optimización le gane a la ingenua.

Importa conservarlas escritas porque el escenario de clase del que nació el tema proponía
exactamente esas dos técnicas. Que el proyecto las contradiga con literatura es un resultado del
trabajo, no un recorte de conveniencia.

---

## La lección de método que este proyecto ya pagó dos veces

**Un enunciado apoyado en una fricción regulatoria puede cerrarse solo mientras se lo piensa.**

La primera vez fue el arbitraje cambiario: el planteamiento original medía la brecha entre el
oficial y el paralelo, y la flotación del 29 de junio de 2026 la llevó de más del 40 % a cerca del
1 % en el mismo mes en que se estaba escribiendo. El problema se resolvió solo.

La segunda es la que está en curso: la Resolución ASFI 540/2025 puede haber cerrado el hueco
documental del importador antes de que el proyecto lo trabaje.

La regla que sale de las dos: **fechar el enunciado contra la norma vigente antes de trabajarlo, no
después.** Y cuando la respuesta cuesta medio día, se paga antes de escribir el capítulo.

---

## Advertencias de citación

Esta lista existe porque una ronda de verificación cerrada el 28 de agosto de 2026 obligó a
corregir **doce afirmaciones** del material del equipo. Cuatro cambiaban el sentido de lo que el
documento decía.

**El «tope de tres mil dólares por ahorrista» no existe.** La nota del Ministerio de Economía
anuncia devolución total, con tramos de saldo escalonados. Los tres mil eran el techo del primer
tramo, no un límite por persona.

**El 73 % de USDT no es una cifra del BCB.** Se abrieron y descartaron una veintena de documentos
del banco y dos de ASFI: no está en ninguno. Viene de reportes de entidades financieras difundidos
por la prensa en agosto de 2025. Citarlo como «según el BCB» es falso.

**Las «252.800 personas» que operaron con activos virtuales tampoco tienen fuente oficial con ese
dígito.** Lo publicado es «más de 252.000», y la cifra exacta circuló en prensa atribuida al GAFI.
Se cita como aproximación y con su procedencia.

**La Resolución de Directorio 082/2024 es del 25 de junio, no del 26.** El 26 es la fecha del
comunicado que la anunció. Se verificó leyendo la resolución firmada, que hubo que extraer como
imagen incrustada porque el PDF es un escaneo sin capa de texto. La búsqueda web devuelve «26 de
junio» de forma consistente en varias fuentes secundarias, incluido material jurídico. Ninguna
cantidad de fuentes secundarias coincidentes reemplaza al documento firmado.

**«La inflación más alta en 36 años» es de prensa, no del INE.** El 20,40 % sí es del INE. Al
citarlo, el superlativo va por separado y con su fuente, o no va.

**El 24 % de alfabetización financiera es de una medición de 2014** (Klapper, Lusardi y Van
Oudheusden, S&P Global FinLit Survey) y va siempre con su fecha, apuntalado con el 6,3 % que
declara haber ahorrado para la vejez, del Global Findex 2025 del Banco Mundial.

**No mezclar la cifra de Chainalysis con la del BCB.** Los 14.800 millones de dólares de valor
on-chain recibido y los 430 millones acumulados del BCB miden cosas distintas y difieren en tres
órdenes de magnitud.

**Las cifras de la canasta básica están confirmadas por dos búsquedas coincidentes, no por lectura
del cuerpo del artículo**: el sitio que las publica devuelve 403 a lectura automatizada, y la firma
del autor quedó sin verificar.

**El modo de falla que más conviene recordar es otro, y apareció dos veces.** Un agente buscó
«73 %» en el informe de vigilancia del sistema de pagos del BCB y lo encontró, dos veces, pero era
el 73 % de las órdenes electrónicas que son pagos con QR, nada que ver con USDT. Lo mismo pasó con
«$us3.000 millones» en el informe de estabilidad financiera, que ahí son pérdidas por bloqueos de
caminos. Es peor que un PDF con el título equivocado, porque ése se caza mirando la portada: acá el
documento es auténtico, del emisor correcto, del área correcta y sobre el tema correcto, y el
número coincide. **Lo único que lo caza es leer la oración entera.**
