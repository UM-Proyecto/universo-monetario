# Universo Monetario — el tema, el cuadro y los datos

**Materia:** Business Intelligence II · **Carrera:** Ingeniería en Ciencia de Datos, Universidad
Privada del Valle — Santa Cruz · **Fecha:** 11 de septiembre de 2026

**Equipo:** Sabrina Adrián Zelaya · Fiorella Michelle Sandoval Castro · Samuel Roberto Castillo
Cornejo · Carlos Andrés Méndez Cadario

> Este documento no reemplaza a `PROYECTO.md`, lo reencuadra. `PROYECTO.md` fijó el problema del
> importador y el crédito fiscal; acá ese problema pasa a ser una parte de algo más grande, y se
> decide **qué se mide, con qué datos y de dónde salen**.

---

## 1. El tema, en una frase

Qué opciones tiene un boliviano —persona o empresa— para defender su dinero de la inflación y del
tipo de cambio, cuánto cuesta entrar a cada una, cuánto rindió cada una en términos reales, y qué
respaldo documental deja.

## 2. De dónde salió este enunciado

Circuló en el equipo una pregunta de investigación redactada así: *¿qué herramientas financieras
permiten explicar las variaciones de la inflación y del tipo de cambio en Bolivia durante la
gestión 2026?* La intuición detrás es buena y el tema final la conserva, pero la formulación tiene
dos problemas que conviene dejar escritos, porque son los que un tribunal levanta primero.

**La relación causal está invertida.** Las herramientas financieras no explican la inflación ni el
tipo de cambio: reaccionan a ellos. Un depósito a plazo fijo, un bono, un fondo, un dólar guardado
o un USDT no explican nada. Lo que explica variaciones de inflación y tipo de cambio son variables
macroeconómicas —emisión monetaria, reservas internacionales, déficit fiscal, expectativas—, y esa
es una pregunta legítima pero distinta, que además responde con agregados monetarios y no con
productos financieros.

**La ventana temporal no tiene varianza suficiente.** El tipo de cambio oficial boliviano no se
movió un centavo durante catorce años: 6,86 y 6,96 son compra y venta del mismo valor, y en 2012,
2015, 2020 y 2025 esos dos son los únicos valores de todo el año. Si la ventana es la gestión
2026, quedan unas nueve observaciones mensuales, seis de ellas bajo el régimen constante y tres
bajo el nuevo. Una variable sin varianza no se explica, y con tres puntos no se estima nada.

**El giro que la salva es cambiar el verbo.** No qué herramientas *explican* las variaciones, sino
cuáles *protegieron* de ellas, a qué costo y con qué respaldo. Eso sí es contestable, sí es un
trabajo de ciencia de datos, y da lugar a la bolsa y a los bonos, que el planteamiento anterior
había dejado afuera.

## 3. El cuadro

Seis opciones, cuatro dimensiones. Ésa es la estructura del proyecto entero.

| Opción | Fuente de datos | Estado de la fuente |
|---|---|---|
| Efectivo en bolivianos | IPC empalmado del INE | Descargado y abierto |
| Dólar físico y paralelo | `api.dolarbluebolivia.click` | 75.804 observaciones, jul-2024 a sep-2026, sin días faltantes |
| Caja de ahorro y depósito a plazo fijo | Tasas pasivas del BCB | 302 de 308 meses, ene-2001 a ago-2026, en XLSX |
| Fondos de inversión (SAFI) | Aplicación de reportes de ASFI | 382.424 filas diarias de 100 fondos, 2010 a sep-2026 |
| Bolsa: renta fija | Boletín del Mercado de Valores de ASFI | 135 boletines mensuales, ene-2015 a abr-2026 |
| USDT por mercado entre pares | Captura propia del libro de Binance | Capturando cada hora desde el 9-sep |

Las cuatro dimensiones, iguales para las seis columnas:

1. **Costo de entrada** — monto mínimo más comisión. Es lo que decide quién puede usar cada
   opción, y es donde el canal formal se cae.
2. **Rendimiento real** — rendimiento nominal menos inflación, medido contra el IPC. Sin esta
   resta, cualquier comparación miente.
3. **Liquidez** — en cuánto tiempo se recupera el dinero y con qué penalidad.
4. **Respaldo documental** — qué comprobante deja la operación y si sirve ante la administración
   tributaria.

### Por qué la cuarta dimensión es la nuestra

Las tres primeras las compara cualquier nota de prensa financiera. La cuarta no la compara nadie,
y es la que convierte el trabajo normativo que el equipo ya hizo en un resultado.

El contraste se enuncia solo: **el que paga con dólares digitales tiene el mejor acceso y el peor
respaldo; la bolsa tiene el respaldo perfecto y un costo de entrada que la vuelve inaccesible.**
Los dos extremos están medidos. Las diez agencias de bolsa autorizadas del país sumaban 2.157
clientes al 30 de abril de 2026, con un ticket promedio de Bs 16,5 millones y una tarifa mínima de
unos cincuenta dólares por operación de renta fija: es un canal mayorista. Contra eso, los fondos
administrados por SAFI tienen 124.867 participantes con montos de apertura desde cien dólares.

Ahí es donde entra el importador. Deja de ser el sujeto único del proyecto y pasa a ser el caso
que hace visible la cuarta dimensión: paga con USDT porque es la opción a la que llega, y esa
misma opción es la que no le deja un documento de pago admitido por la RND 102400000021. Todo lo
verificado sobre la norma sigue valiendo, y ahora está sostenido por una comparación en lugar de
por una afirmación.

### Un hallazgo que vuelve original al cuadro

De once productos financieros de la región revisados, **ninguno muestra desviación estándar**.
Cada uno sustituye el riesgo por otra cosa: nombres de celebridades para los niveles, la meta del
usuario, quién custodia los fondos. Ninguno lo cuantifica de forma comparable entre alternativas.
Construir esa comparación homogénea es, literalmente, el hueco.

## 4. El dato propio: el libro P2P

Es la única columna con datos que generamos nosotros, y la más rica. Desde el 9 de septiembre corre
en el servidor una captura horaria del libro de anuncios de USDT contra bolivianos de Binance,
como servicio de systemd.

**Se corrigió un defecto grave el 11 de septiembre.** La primera versión pedía veinte anuncios de
un libro de unos ciento ochenta ordenado por precio, así que guardaba el tramo mejor cotizado y no
una muestra. Medido sobre una misma corrida: la mediana de compra da 11,405 bolivianos con veinte
anuncios y 11,665 con el libro completo. El error iba siempre en la misma dirección. Ahora pagina
hasta agotar el libro.

Cada corrida guarda el libro entero comprimido, un resumen por lado, y **una fila por anuncio**
con precio, cantidad disponible, montos mínimo y máximo, límite de tiempo de pago, métodos de pago
—bancos bolivianos con nombre— y el perfil del anunciante: tipo, categoría, órdenes del último
mes, tasa de completado y tasa de valoración. El identificador del anunciante va seudonimizado con
un hash estable, para poder seguirlo en el tiempo sin arrastrar su identificador de Binance a un
repositorio público.

Son unos 380 anuncios por corrida y 24 corridas por día: alrededor de nueve mil registros diarios
con estructura de panel. Para la defensa habrá entre ocho y nueve semanas de serie propia que no
se consigue retroactivamente.

**El puente con la norma, medido el 11 de septiembre:** 53 de 178 anuncios de compra admiten
operaciones de Bs 50.000 o más, que es exactamente el umbral de la RND. Casi un tercio del mercado
opera en el tramo que la norma obliga a respaldar con un documento que este canal no emite.

## 5. Las fuentes formales, medidas

Las tres columnas que faltaban —depósitos, fondos y bolsa— **tienen fuente gratuita, descargada y
abierta**. El cuadro de seis columnas se sostiene.

**Fondos de inversión.** Es la mejor de las tres. ASFI publica una aplicación de reportes con un
botón de descarga en XLS por fondo y rango de fechas, sin registro. Se bajaron 100 fondos con
382.424 filas diarias, del 1 de enero de 2010 al 8 de septiembre de 2026, con valor de cuota,
número de participantes, tasas a 30, 90, 180 y 360 días, tasa efectiva anual, liquidez y cartera.

**Depósitos a plazo fijo y caja de ahorro.** Es la serie más larga de todo el proyecto. El Banco
Central publica las tasas pasivas en XLSX real: 302 de 308 meses entre enero de 2001 y agosto de
2026, por entidad y por plazo de 30 a 1080 días. Faltan abril a agosto de 2017 y julio de 2019.

**Bolsa, pero no por la Bolsa.** La BBV no entrega histórico: sus tablas traen el período que fija
el servidor, los desplegables filtran del lado del cliente y ninguna de las 67 peticiones de red
de la página es una llamada de datos, así que no hay endpoint al que pedirle otro rango. Los
históricos detallados se venden por suscripción. La serie igual existe, por otro lado: el Boletín
Estadístico del Mercado de Valores de ASFI republica cada mes las tasas de rendimiento ponderadas
de la BBV por plazo y moneda, más el monto negociado. Se bajaron 135 boletines, de enero de 2015 a
abril de 2026, con un solo mes faltante.

**Una advertencia para esa columna:** el mercado secundario boliviano es delgado. La hoja de
compraventa de abril de 2026 tiene seis filas con operación efectiva contra 586 de la hoja de
reporto. Cualquier número que salga de ahí tiene que decir de qué tipo de operación sale.

### La premisa que resultó falsa, y lo que enseña

La versión anterior de este documento afirmaba que el sitio de ASFI arma sus listados con
JavaScript y que por eso una consulta con `curl` devuelve cero enlaces donde sí hay archivos. **Es
falsa.** Medido el mismo minuto sobre seis páginas, `curl` y un navegador real devuelven
exactamente el mismo conteo: 0, 17, 11, 18, 4, 0.

El error no estuvo en la herramienta sino en la muestra: las cinco páginas que se habían probado
eran todas índices de navegación, que no tienen adjuntos sino enlaces a otras páginas que sí los
tienen. Cinco ceros de páginas del mismo tipo, y ningún caso donde el instrumento tuviera que
encontrar algo. De ahí se saltó a declarar una causa —el renderizado por JavaScript— que nunca se
midió.

El navegador sí hizo falta, pero para otra cosa: la aplicación de reportes de fondos es ASP.NET
con componentes que exigen postback, y ahí no hay enlace que copiar.

**La lección va a la práctica del proyecto:** un cero sólo significa algo si, en la misma corrida,
el instrumento encontró lo que tenía que encontrar en otro caso. Y una causa se escribe cuando se
mide, no cuando se supone: una explicación plausible detiene a quien iba a buscar la verdadera.

### Dos trampas y un bloqueo, ya medidos

Los enlaces del Boletín Estadístico del BCB llevan la fecha de publicación dentro de la ruta y
cambian cada trimestre. El filtro por año de su página de tasas **no funciona por cadena de
consulta**: pedir 2020, 2013 o el año inexistente 1899 devuelve el mismo listado idéntico; el
formulario verdadero está en otra ruta y ahí el listado ya viene completo.

Y la BBV **bloquea por dirección IP** ante pedidos concurrentes: veinte minutos, para todo el
dominio, detectado porque el control positivo dejó de responder. Todo lo medido en esa tanda se
descartó y se rehizo en serie.

Importa **cómo** se presenta ese bloqueo, porque decide el diseño de la caché: no es un código de
respuesta con cabecera de reintento ni una política que se pueda leer de antemano, es el saludo
TLS cortándose en seco, sin respuesta. Una caché que trate esa firma como «el servicio está caído»
y reintente va a parecer que funciona hasta el día de la defensa, que es cuando la demostración
corre desde otra dirección y con el tribunal mirando. Por eso la serie de bolsa entra por los
boletines ya descargados, que son archivos y no consultas, y por eso el criterio de cierre de la
caché no puede ser «funciona con la red desconectada»: desconectar el cable da un fallo limpio y
distinto del que hay que probar.

## 6. Cómo entra cada materia del semestre

Seis de las siete materias aportan un entregable concreto sobre el mismo conjunto de datos, que
era la condición que buscábamos: integrar las materias sin que signifique seis proyectos paralelos.

| Materia | Qué aporta |
|---|---|
| **Business Intelligence II** | El tablero comparativo: las seis opciones en sus cuatro dimensiones, con la evolución del rendimiento real |
| **Minería de Datos** | Detección de anomalías sobre anuncios fuera de patrón; reglas de asociación entre método de pago, tramo de monto y tipo de anunciante |
| **IA y Machine Learning para Organizaciones II** | Segmentación no supervisada con K-means y PCA sobre el panel de anunciantes. Es no supervisado, que es lo que corresponde porque no hay etiquetas |
| **Optimización Empresarial III** | Simulación de eventos discretos del flujo de una compra pagada con dólares digitales, con sus ramas de documentación |
| **Dirección de Operaciones** | Lectura Lean: el crédito fiscal perdido es desperdicio; el cuello de botella aparente es el pago y el causal es la documentación |
| **Programa Emprendedor** | Modelo de negocio y propuesta de valor de la capa de análisis |

Idioma Inglés cuenta como materia del semestre pero no aporta al proyecto.

## 7. Qué es el producto, y qué no

El producto defendible es una **capa de análisis**: compara opciones, calcula rendimiento real y
dice qué respaldo deja cada una. No intercambia, no transfiere, no custodia y no emite, que son
las cinco actividades que exigen licencia de ASFI bajo el Decreto Supremo 5384.

Eso descarta el clon boliviano de Takenos, y no por falta de ganas: un producto así cae entero
dentro de las cinco actividades licenciadas, necesita una autorización que un proyecto de semestre
no obtiene, y Takenos ya opera en Bolivia desde 2026 con representante local. El límite del otro
lado lo pone la Ley 1834: el sistema informa y advierte, no orienta la decisión concreta sobre un
activo. En Bolivia no existe la figura del asesor de inversión independiente.

## 8. El riesgo del alcance, declarado

Seis columnas hechas a medias es peor que dos hechas bien, y el planteamiento anterior de este
mismo equipo ya se angostó una vez por exactamente esa razón. La forma de sostener el cuadro sin
diluirlo es usarlo como **marco** y poner la profundidad en dos columnas: el mercado entre pares,
porque ahí el dato es propio y horario, y la opción formal que resulte tener datos accesibles
después de la medición en curso. Las otras cuatro entran con lo que haya, declarado.

## 9. Lo que sigue abierto

**Si Business Intelligence II y el Proyecto Integrador son la misma entrega.** La malla curricular
tiene Proyecto Integrador I en cuarto semestre y II en séptimo; en sexto no figura ninguna materia
con ese nombre. La hipótesis que sale de leer la malla es que esto es el trabajo final de Business
Intelligence II y se lo viene llamando integrador por costumbre. Hay que confirmarlo con el
docente, no deducirlo.

**Si el comprobante de un proveedor de activos virtuales autorizado sirve como documento de pago.**
La separata oficial define documento de pago como el emitido y reconocido por una entidad
financiera regulada por ASFI, y las palabras criptoactivo, activo virtual y proveedor de servicios
de activos virtuales no aparecen ni una vez en sus treinta y cuatro páginas. La lectura provisoria
es que no califica, pero falta verificar qué emite efectivamente un proveedor autorizado.

Vale anotar que el artículo 5 de la norma tiene **tres** efectos y no uno: además de la pérdida
del crédito fiscal del IVA aun teniendo la factura original, la compra pasa a ser gasto no
deducible para el IUE y no da derecho al cómputo del RC-IVA. El costo real es mayor que el que
decía nuestro enunciado.

**Qué se hace con las tarjetas del planteamiento anterior.** El tablero arrastra tareas del eje del
inversionista minorista. Con este reencuadre, varias vuelven a servir —conversión a bolivianos,
quiebre estructural, presentación del riesgo, validación de comprensibilidad— porque el eje nuevo
se parece más a aquél que al del importador puro. Hay que marcar cada una antes de seguir
agregando.

## 10. Dónde vive cada cosa

- **`UM-Proyecto/universo-monetario` en GitHub**, copia local en el laptop: documentos, catálogo de
  fuentes, investigación inicial. Es lo que ve el equipo.
- **`~/universo-monetario` en el servidor `pop-os`**, sin remoto: la captura, los datos y el
  tablero del proyecto en el puerto 6423. El avance se anota ahí.

Los datos capturados todavía no están en el repositorio del equipo. Subir `anuncios.csv` y
`resumen.csv` con su documentación de columnas es tarea de esta semana.
