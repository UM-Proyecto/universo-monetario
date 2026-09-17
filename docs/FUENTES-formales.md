# Fuentes formales bolivianas: ASFI, BBV y BCB

> **ESTE DOCUMENTO YA NO FIJA EL ESTADO DE LAS FUENTES.** Desde el 17 de septiembre de 2026 el
> catálogo único del proyecto es [`CATALOGO-FUENTES.md`](CATALOGO-FUENTES.md), que unifica este
> archivo con `FUENTES-formales.md` y con el `fuentes.json` del repositorio del equipo, que se
> contradecían entre sí por ser de momentos distintos.
>
> Lo que sigue valiendo de acá es el **procedimiento**: cómo se descarga cada fuente, qué endpoints
> tiene y qué notas de manejo hay que respetar. Lo que **no** vale es el estado de cada fuente.
> Ejemplo concreto medido: este documento da a `paralelo.bo` por caída, y el 17-sep-2026 está viva,
> con su histórico completo descargado.



Este catálogo cubre las tres columnas del cuadro comparativo que hasta ahora no tenían fuente
verificada: depósitos a plazo fijo, fondos de inversión SAFI y bolsa de valores. Complementa a
`docs/FUENTES.md`, que cubre las fuentes internacionales y el dólar paralelo.

**Ronda de verificación: 11 de septiembre de 2026, desde el servidor `pop-os`.** El relevamiento
de páginas y el manejo de la aplicación de fondos de ASFI se hicieron con Chromium headless sobre
Playwright 1.49; las descargas de archivos estáticos, una vez resuelta la dirección, se hicieron
con pedidos HTTP comunes. Cuándo hace falta cada cosa —y por qué la premisa del encargo sobre
esto era equivocada— está al final, en «Por qué hizo falta un navegador».

El criterio de esta ronda fue el mismo que el del catálogo anterior, y más estricto: una fuente
cuenta como verificada solamente si el archivo se descargó, se abrió, y se anotó cuántas filas
trajo, qué columnas tiene y qué rango de fechas cubre. Que la página responda no cuenta como
evidencia, y tampoco cuenta que el enlace exista.

---

## Estado resumido

| Fuente | Columna que alimenta | Formato | Periodicidad | Rango verificado | Estado |
|---|---|---|---|---|---|
| ASFI — Evolutivo de Fondos de Inversión (aplicación web) | Fondos SAFI | XLS por fondo | Diaria | 2010-01-01 a 2026-09-08 | **Descargada y abierta** |
| ASFI — Boletín Estadístico del Mercado de Valores | Fondos SAFI, DPF y bolsa | XLS/XLSX de 21 hojas | Mensual | Ene-2015 a Abr-2026 | **Descargada y abierta** |
| ASFI — Inversiones (evolutivos de cartera) | Fondos SAFI | ZIP con XLSX y ODS | Semestral, con rezago | Corte 31-12-2025 y 30-04-2026 | **Descargada y abierta** |
| ASFI — Tarifarios | Costo de entrada del banco | ZIP con XLSX y ODS | Puntual, sin serie | Corte 31-01-2026 | **Descargada y abierta** |
| BCB — Tasas de interés pasivas | DPF y caja de ahorro | XLSX | Diaria, semanal, mensual y anual | Ene-2001 a Ago-2026 | **Descargada y abierta** |
| BBV — Tasas Promedio Ponderadas (TPP) | DPF y bolsa | PDF diario direccionable por fecha | Diaria hábil | 2022-06-30 a 2026-09-11 | **Descargada y abierta** |
| BBV — Estadísticas bursátiles del sitio web | Bolsa | Tablas HTML del período corriente | Sin histórico gratuito | Período corriente únicamente | Accesible, sin serie |

Las tres columnas que faltaban quedan cubiertas. El detalle, y las limitaciones de cada una,
van abajo.

---

## 1. ASFI — Fondos de inversión SAFI

### 1.1 La aplicación de reportes dinámicos: la fuente principal

Es la mejor fuente encontrada en toda la ronda y no aparece enlazada desde la página de
estadísticas: hay que entrar por «Estadísticas → Mercado de Valores → Reportes Dinámicos», y de
ahí a dos aplicaciones ASP.NET alojadas en un dominio distinto del sitio principal.

- **Evolutivo por fondo:** `https://appweb2.asfi.gob.bo/PaginasPublicas2/vistareportevalores/EvolutivoFondosInversion.aspx`
- **Información general a una fecha:** `https://appweb2.asfi.gob.bo/PaginasPublicas2/vistareportevalores/fondosInversionGeneral.aspx`

La primera tiene un desplegable con **106 entradas de fondo**, un rango de fechas «Del … Al …» y
un botón **«Descargar datos en formato XLS»** que entrega la serie completa del rango pedido, sin
el recorte de la grilla en pantalla. No pide registro ni clave.

**Qué se descargó el 2026-09-11.** Se pidieron los 101 códigos únicos del desplegable con el
rango 2010-01-01 a 2026-09-11. Bajaron **100 archivos XLS, 107 MB en total**, en
`datos/crudo/asfi/fondos-evolutivo/` (un archivo por código, nombrado con el código del fondo).

**Qué contienen.** Convertidos a CSV y contados: **382.424 filas de datos**, con las quince
columnas siguientes, idénticas en los cien archivos:

```
Serie, Fecha, Valor Cuota, Cuota Vigente, Participantes, Tasa Último Día,
Tasa Últimos 30 Días, Tasa Últimos 90 Días, Tasa Últimos 180 Días,
Tasa Últimos 360 Días, Tasa Efectiva Anual, Total Liquidez,
Cartera Neta, Cartera Bruta, Moneda
```

La resolución es **diaria**. El rango global va del **1 de enero de 2010 al 8 de septiembre de
2026**, es decir, hasta tres días antes de la descarga. La profundidad varía mucho por fondo,
porque cada uno arranca cuando se autorizó: los más largos son MIC con 9.408 filas (2010-01-01 a
2016-06-09, ya liquidado), FPP con 8.140 (2012-09-12 a 2023-11-08) y CGF con 7.101 (2016-12-16 a
2026-09-08); los más cortos son fondos nuevos, como OAC con 41 filas desde el 30 de julio de
2026. Un mismo fondo puede tener varias series, y por eso el conteo de filas de algunos supera
la cantidad de días calendario del período.

**Un código quedó vacío.** `CFU` (Credifondo UFV, Fondo de Inversión Abierto a Mediano Plazo)
devolvió «Sin datos para mostrar» para todo el rango. Es un fondo del desplegable que no tiene
serie publicada, no un fallo de la descarga.

**Lo que se puede leer directamente de estos datos.** En la última fecha disponible
(2026-09-08), treinta fondos abiertos traen tasa efectiva anual numérica. Veinte cotizan en
bolivianos, once en dólares y tres en unidades de fomento a la vivienda. Los rendimientos en
bolivianos del último día van desde valores cercanos a cero hasta 44,15 % en el caso de Avanza
Bs. **Ese 44 % hay que tratarlo con cuidado**: la tasa efectiva anual de estos reportes es una
anualización de una ventana corta, así que en un fondo con movimientos fuertes de cartera puede
dispararse sin que nadie haya ganado esa tasa durante un año. Para la comparación contra el
índice de precios al consumidor conviene usar la tasa de los últimos 360 días, que está en la
misma tabla y no tiene ese problema.

### 1.2 El Boletín Estadístico del Mercado de Valores: la serie mensual

Entrada: `https://www.asfi.gob.bo/pb/boletines-estadisticos-mercado-valores`, que lleva a una
página por gestión, de 2015 a 2026.

**Qué se descargó.** Las doce páginas de gestión, y de ellas **135 boletines**, en
`datos/crudo/asfi/boletines-mv/` (213 MB una vez descomprimidos; los de 2025 y 2026 vienen en
ZIP, los anteriores como XLS o XLSX directo).

**Cobertura medida:** de **enero de 2015 a abril de 2026**, con un solo mes faltante en el sitio,
**julio de 2017**. La gestión 2026 llega hasta abril, o sea que el boletín publica con unos
cuatro meses de rezago.

**Qué contiene cada boletín.** Un libro de veintiuna hojas. Verificado sobre el de abril de 2026
y contrastado con los de 2015, 2019 y 2022, que traen la misma estructura con los nombres de
hoja cambiados:

| Hoja | Contenido | Tamaño en abril de 2026 |
|---|---|---|
| 1 | Reporte de depósitos a plazo fijo, por entidad emisora y moneda | 61 filas |
| 2 | Reporte de emisiones vigentes | 591 filas |
| 3 | Fondos de inversión: cartera y tasas de rendimiento a 1 y 30 días | 359 filas |
| 4 | Número de participantes por fondo | 156 filas |
| 5 a 11 | Cartera de los fondos por emisor, por instrumento y por plazo de vida | — |
| 12 | **Tasas de rendimiento de compra venta ponderadas por plazo y moneda** | 174 filas |
| 13 | Ídem, moneda extranjera | 137 filas |
| 14 | Tasas de rendimiento de reporto ponderadas por plazo y moneda | 586 filas |
| 15 a 18 | Agencias de bolsa: cartera propia, de clientes, número de clientes | — |
| 19 | Monto negociado en la Bolsa Boliviana de Valores por tipo de operación | 32 filas |

Las hojas 12, 13 y 14 son el hallazgo que cambia el panorama de la columna «bolsa», y conviene
decirlo explícitamente: **ASFI republica mensualmente las tasas de rendimiento de la Bolsa
Boliviana de Valores, por instrumento, emisor, plazo y moneda, de forma gratuita y con serie
desde 2015.** Los tramos de plazo son 1-30, 31-60, 61-90, 91-120, 121-150, 151-180, 181-360,
361-720 y más de 720 días. La hoja 19 trae además el monto negociado del mes.

**Una advertencia sobre el grosor de esos datos.** La hoja 12 de abril de 2026 tiene 174 filas de
formato pero solamente **seis filas con operación efectiva** en bolivianos: dos bonos bancarios
bursátiles y tres pagarés. El mercado secundario de compraventa boliviano es delgado y hay meses
en que casi no opera. La hoja de reporto, en cambio, trae 586 filas. Si el cuadro comparativo va
a usar un rendimiento de bolsa, tiene que decir de qué tipo de operación sale, porque compraventa
y reporto no son lo mismo y uno de los dos puede estar vacío en cualquier mes dado.

### 1.3 Inversiones: los evolutivos de cartera

Entrada: `https://www.asfi.gob.bo/la/inversiones`. Once archivos ZIP, descargados a
`datos/crudo/asfi/inversiones/`. Cada uno contiene el mismo contenido en XLSX y en ODS.

El más útil es `Fondos_de_Inv._Abiertos_(31-12-2025)_Evolutivo_-_ultimos_6_meses.zip`. Abierto:
cuatro hojas, la principal de **593 filas por 188 columnas**, con una columna por día del **1 de
julio al 31 de diciembre de 2025** y cuatro filas por fondo (cartera bruta, liquidez total, tasa
de los últimos 30 días y tasa efectiva anual). Es la misma información que entrega la aplicación
de reportes dinámicos, pero consolidada en un solo archivo.

**La limitación es el corte.** Salvo el evolutivo de duración, que corta al 30 de abril de 2026,
todos los demás están al 31 de diciembre de 2025 y se publicaron en julio de 2026. Para una serie
al día sirve la aplicación de reportes dinámicos, no esta página.

---

## 2. Tasas pasivas: caja de ahorro y depósitos a plazo fijo

### 2.1 BCB — la fuente con serie larga

Entrada: `https://www.bcb.gob.bo/?q=tasas_interes`, pestaña «Pasivas».

Hay un detalle que cuesta tiempo si no se sabe: **los filtros por año de esa página no funcionan
por cadena de consulta.** Pedir el año 2020, el 2013 o el año inexistente 1899 devuelve
exactamente el mismo listado de 362 archivos, byte por byte. El formulario de verdad vive en la
vista suelta `/?q=tasas-de-inter-s-pasivas`, donde el parámetro `field_tipo_de_tasa_pasiva_value`
sí discrimina (`pa` para plazo fijo, `ah` para caja de ahorro), y donde el listado ya viene
completo sin filtro de año.

**Qué se descargó.** Los 89 archivos XLSX únicos de las dos vistas, a
`datos/crudo/bcb/tasas-pasivas/` (26 MB). Más dos archivos sueltos de muestra en
`datos/crudo/bcb/`: la publicación semanal consolidada al 31 de agosto de 2026 y el reporte
diario del 9 de septiembre de 2026.

**Qué contienen, medido abriéndolos.**

El anual de plazo fijo (`28PAANUAL_0.xlsx`) tiene cuatro hojas, una por denominación: moneda
nacional, moneda extranjera, moneda nacional con mantenimiento de valor y unidad de fomento a la
vivienda. Cada hoja tiene 869 filas y cubre **veinticinco años, de 2001 a 2025**, con las
entidades agrupadas en bancos, cooperativas, fondos financieros y mutuales, y los plazos en
tramos de 1-30, 31-60, 61-90, 91-180, 181-360, 361-720 y 721-1080 días. Cada tramo trae tasa
nominal y tasa efectiva. El anual de caja de ahorro (`28AHANUAL_1.xlsx`) tiene una sola hoja de
870 filas con la misma cobertura y las cuatro denominaciones como columnas.

Los mensuales son la serie fina. Contando los meses efectivamente presentes en los archivos:

| Serie | Archivos | Meses presentes | Rango | Meses faltantes |
|---|---|---|---|---|
| Depósitos a plazo fijo | 26 | 302 de 308 | Ene-2001 a Ago-2026 | Abr, May, Jun, Jul y Ago de 2017; Jul de 2019 |
| Caja de ahorro | 26 | 301 de 308 | Ene-2001 a Ago-2026 | Abr a Sep de 2017; Jul de 2019 |

Los huecos de 2017 y 2019 están en los archivos mensuales del sitio, no en la descarga. Los
mismos meses deberían poder reconstruirse desde los archivos semanales, que también se bajaron,
pero eso todavía no se hizo.

Los diarios (`TD_DD MM AAAA.xlsx`) traen dos hojas, `ACT` y `PAS`. La hoja `PAS` es la relevante:
por entidad individual —no por grupo—, caja de ahorro y depósitos a plazo a 30, 60, 90, 180, 360,
720, 1080 días y «Mayor», en moneda nacional, extranjera, unidad de fomento a la vivienda y
mantenimiento de valor. Verificado sobre el del 9 de septiembre de 2026: 108 filas por 23
columnas.

**El orden de magnitud, para calibrar.** En la semana del 31 de agosto de 2026, las tasas
pasivas en moneda nacional van de alrededor de 1 % a 4 % en caja de ahorro, y de 7 % a 11 % en
depósitos a plazo largo según la entidad. Las mismas tasas en moneda extranjera están cerca de
cero, con varias entidades en 0,01 %.

### 2.2 BBV — Tasas Promedio Ponderadas, la fuente diaria alternativa

En «Estadísticas → Otras estadísticas» la Bolsa publica un reporte llamado **Tasas Promedio
Ponderadas de Mercado Primario de Series Registradas en Bolsa**, construido con los depósitos a
plazo fijo y los depósitos a plazo anotados en cuenta que registran agencias de bolsa,
administradoras de fondos y administradoras de pensiones.

El enlace del día apunta a una ruta con la fecha adentro:
`https://www.bbv.com.bo/Media/Default/InformacionBursatil/InformacionASFI/TPP-AAAA-MM-DD.PDF`.
**Esa ruta es direccionable hacia atrás**, lo que convierte un reporte del día en una serie
diaria.

**Qué se descargó y qué trae.** `datos/crudo/bbv/TPP-2026-09-11.pdf`, 45.092 bytes. Abierto: una
página, encabezada «Periodo observado: del 12JUL2026 al 10SEP2026», con las tasas cruzadas por
tres ejes: moneda (N para nacional, E para extranjera, U para unidad de fomento a la vivienda, V
para mantenimiento de valor), tipo de valor, y veintisiete tramos de plazo en columnas, con las
filas por sigla de entidad emisora (BGA, BIS, BME, BNB, BSO, BTB, CRE, FEF, FIE, BEC, BUN y
otras). Los valores en moneda nacional del reporte del 11 de septiembre de 2026 caen entre 6 % y
11 %; los de moneda extranjera, alrededor de 1 %.

**Hasta dónde llega el archivo: arranca el 30 de junio de 2022.** Se probó día hábil por día
hábil, con una pausa de tres segundos entre pedidos y un control positivo antes y después de
cada tanda. El corte es limpio y no admite otra lectura: los diez días hábiles del 16 al 29 de
junio de 2022 devuelven 404 y los dieciséis del 30 de junio al 20 de julio devuelven 200, con
cuerpos de entre 47 y 49 KB. Hacia atrás, las muestras de junio de 2018, 2019, 2020 y 2021, y
las de enero, marzo y mayo de 2022, devuelven todas 404, igual que el control negativo con fecha
1899-01-02. Hacia adelante, marzo de 2023 tiene los once días hábiles completos con respuesta
200. El control positivo —`TPP-2026-09-11.PDF`, 45.092 bytes— respondió igual al principio y al
final de cada tanda, así que ningún 404 de esta serie es un bloqueo disfrazado.

**La ventana móvil es una trampa.** Cada reporte no describe su propio día: describe los dos
meses anteriores. El del 11 de septiembre de 2026 observa desde el 12 de julio. Dos reportes de
días consecutivos comparten casi toda su ventana, así que **no se pueden apilar como si fueran
observaciones independientes.** Para una serie mensual hay que tomar un reporte por mes y tratar
su ventana como el período que describe.

### 2.3 ASFI — Tarifarios: costo, no rendimiento

`https://asfi.gob.bo/la/tarifarios` publica dieciocho ZIP, uno por producto. Se descargó y se
abrió el de caja de ahorros (`datos/crudo/asfi/tarifarios/`): cinco hojas, una por tipo de
entidad —bancos múltiples, bancos PYME, entidades financieras de vivienda, cooperativas e
instituciones financieras de desarrollo—, con las entidades en columnas y los conceptos en filas.

Lo que trae son **comisiones, no tasas**: emisión de extracto adicional, emisión y reposición de
tarjeta de débito, reimpresión de clave, seguro de protección de tarjeta. Sirve para la dimensión
«costo de entrada» de la opción bancaria y no sirve para la de rendimiento. Es además **una foto
sin serie**: el corte es al 31 de enero de 2026 y el sitio no publica versiones anteriores.

---

## 3. Bolsa y renta fija

La conclusión práctica es que el sitio de la Bolsa Boliviana de Valores **no es el camino** para
la serie histórica, y que ASFI sí lo es.

### 3.1 Qué hay gratis en el sitio de la BBV

Las tres secciones de `https://www.bbv.com.bo/estadisticas/` se cargaron y se leyeron:

- **Estadísticas económicas.** Una foto del día: tipo de cambio oficial, euro, unidad de fomento
  a la vivienda, real, sol y peso chileno; inflación y variación del producto de tres regiones;
  seis precios de materias primas. Sin serie y con fuentes de terceros declaradas —Investing y
  Global Rates para los indicadores internacionales, Business Insider para las materias primas—.
  No sirve como fuente primaria.
- **Estadísticas bursátiles.** Cuatro subsecciones: transacciones en bolsa, valores inscritos,
  valores vigentes y depósitos a plazo fijo pignorados. Las tablas están completas y son ricas.
  «Montos negociados por instrumento» trae la apertura por piso de negociación y mercado
  electrónico, por instrumento y por participación. «Valores inscritos en bolsa» trae cada
  emisión con instrumento, emisor, programa, serie, plazo, fechas de inscripción, emisión y
  vencimiento, monto inscrito, valor nominal, **tasa**, período de pago de interés, garantía y
  calificación de riesgo.
- **Otras estadísticas.** Las Tasas Promedio Ponderadas ya descritas, y dos reportes de acciones
  —valoración y hechos de emisores— también con la fecha en la ruta.

**El problema es el período, no el contenido.** Las tablas vienen con su rango fijado por el
servidor: «01AGO2026 al 31AGO2026» para los montos negociados, «01ENE2025 a 31AGO2026» para los
valores inscritos. Se revisó cómo se arman: los desplegables de la página **filtran del lado del
cliente** —no tienen atributo `name` ni `id` y no disparan ninguna petición—, y de las 67
peticiones de red que hace la página **ninguna es una llamada de datos**: todo es Google
Analytics y reCAPTCHA. Es decir, no hay punto final al que se le pueda pedir otro rango. Lo que
el servidor manda es lo único que hay.

Esto confirma lo que ya se sabía y lo precisa: el histórico detallado se vende por suscripción
(«BBV al día» y «Bases de Datos», contacto `comunicacion@bbv.com.bo`). **No se encontró ningún
índice bursátil con histórico publicado gratuitamente.**

### 3.2 Por dónde sí sale la serie de bolsa

Por el Boletín Estadístico del Mercado de Valores de ASFI, descrito en el punto 1.2. Sus hojas 12,
13 y 14 traen las tasas de rendimiento ponderadas por plazo y moneda —compraventa en moneda
nacional, compraventa en moneda extranjera y reporto— y la hoja 19 el monto negociado del mes.
Con los 135 boletines descargados, eso es una serie mensual de **enero de 2015 a abril de 2026**,
sin costo.

Para el lado de emisiones primarias, la serie diaria de Tasas Promedio Ponderadas del punto 2.2
cubre desde 2023, con la advertencia de la ventana móvil.

---

## Por qué hizo falta un navegador, y por qué no fue por lo que parecía

El encargo de esta ronda venía con una premisa: que el sitio de ASFI arma sus listados con
JavaScript, que por eso `curl` devuelve cero enlaces a archivos en páginas donde sí los hay, y
que ese cero no se distingue de «no hay nada publicado». **Esa premisa es falsa y conviene
dejarlo escrito, porque manda a resolver con un navegador cosas que no lo necesitan.**

Medido el 2026-09-11, misma máquina y mismo minuto, contando enlaces a archivo en el HTML crudo
de `curl` contra el conteo del mismo código corriendo sobre el árbol ya renderizado por
Chromium:

| Página de ASFI | `curl` | Chromium |
|---|---|---|
| Estadísticas del Mercado de Valores | 0 | 0 |
| Anuario Estadístico | 17 | 17 |
| Inversiones | 11 | 11 |
| Tarifarios | 18 | 18 |
| Boletines Estadísticos, gestión 2026 | 4 | 4 |
| Reglamentos internos de fondos de inversión | 0 | 0 |

Coinciden en las seis. El Drupal de ASFI entrega sus listados del lado del servidor; los 99
marcadores de `drupal` y `ajax` del HTML son andamiaje del tema, no evidencia de que el contenido
se arme en el cliente. Y los dos ceros son ceros de verdad, no ceguera: esas dos páginas son
índices de navegación, no repositorios, y el contraste con las otras cuatro filas de la misma
tabla lo demuestra.

**Cómo reproducirlo.** El comando es uno solo, sin navegador:

```
curl -s -L --max-time 40 -A "Mozilla/5.0 (X11; Linux x86_64) Chrome/131" "<URL>" -o pagina.html
grep -oiE 'href="[^"]+\.(pdf|zip|xlsx?|csv|docx?)"' pagina.html | wc -l
```

Las direcciones de las cuatro páginas que sí devuelven archivos son
`https://www.asfi.gob.bo/node/1006` (Anuario, 17), `https://www.asfi.gob.bo/la/inversiones` (11),
`https://asfi.gob.bo/la/tarifarios` (18, y ese dominio va sin `www`) y
`https://www.asfi.gob.bo/la/boletines-estadisticos-mercado-valores-2026` (4).

**Qué causó el cero, medido y no supuesto.** La causa fue **elegir las cinco páginas de prueba
del mismo tipo**: las cinco eran índices de navegación, así que ninguna era un caso donde el
instrumento debiera encontrar algo. Cinco ceros y ningún positivo no distinguen entre «no hay
archivos» y «el grep está ciego», y de ahí salió la conclusión equivocada.

Conviene dejar anotado que la primera hipótesis de este informe sobre esa causa **también era
falsa**. Se había escrito que el problema probable era el patrón, porque los enlaces de ASFI son
relativos y están codificados —una línea cruda del Anuario sale
`href="/sites/default/files/2026-07/Anuario_Estad%C3%ADstico%202025.zip"`— y un patrón que exija
`https://` no encontraría ninguno. Es cierto que son así, pero no era el problema: el grep de la
otra sesión no exigía esquema ni dominio y resolvía bien los enlaces relativos y codificados.
Quedó descartada al reproducir los controles.

O sea que la misma falla apareció dos veces seguidas y en las dos puntas: declarar una causa
plausible sin medirla. La primera vez costó cuatro documentos y un PDF ya entregado; la segunda,
este párrafo. **La causa de un cero se mide con un control positivo, no se deduce del código.**

**Un segundo control, que no depende del patrón de extensión.** Contar apariciones de la cadena
`sites/default/files` separa las dos clases de página sin ambigüedad: Anuario 27, Tarifarios 28,
Inversiones 21, Boletines 14; contra exactamente 10 en las tres páginas índice. Ese 10 es la
línea base del tema de Drupal —logos, hojas de estilo, íconos—, así que cualquier página con
adjuntos queda por encima. La señal se confirma por un tercer camino: las páginas con archivos
traen la tabla de adjuntos de Drupal y `grep -c '>Adjunto<'` devuelve 1 en las cuatro y 0 en las
tres restantes.

**Dónde el navegador sí fue indispensable:** en la aplicación de fondos de
`appweb2.asfi.gob.bo`, que es ASP.NET con componentes DevExpress. Ahí no hay enlace que copiar.
Hay que fijar el valor del desplegable por su interfaz de cliente, fijar las dos fechas,
disparar un `postback` que arrastra `__VIEWSTATE` y `__EVENTVALIDATION`, esperar a que la grilla
se repueble y recién entonces apretar el botón que genera el XLS. Reproducir eso con `curl`
significa reconstruir el estado de vista a mano en cada iteración. Con el navegador son cuatro
líneas. Los 107 MB de serie diaria de fondos salieron de ahí, y sin navegador no salían.

**El control del instrumento, en las dos direcciones.** Dentro de esa misma aplicación: un
código de fondo inventado (`UFP`) devolvió «Sin datos para mostrar» y el botón de descarga no
produjo archivo; el código real de ese mismo fondo (`UPA`, UFV Protección) devolvió 210 filas y
un XLS de 97.792 bytes. La herramienta distingue.

---

## Límites de esta ronda, y qué quedó sin medir

**El sitio de la BBV bloqueó a este servidor durante la medición, y fui yo quien lo provocó.**
Para acotar desde cuándo existe el archivo de Tasas Promedio Ponderadas lancé sondas concurrentes
—diez hilos, veinte peticiones por mes— sobre varios meses seguidos. En algún punto de esa
ráfaga el sitio dejó de responder: la conexión TCP se establece pero el saludo TLS se corta
(`unexpected eof while reading`), y eso vale para todo `bbv.com.bo`, no solo para los PDF.
Comprobado con el control positivo, que es lo que lo delata: `TPP-2026-09-11.PDF`, que había
respondido 200 con 45.092 bytes minutos antes, pasó a responder nada, y la portada del sitio
también. Chromium tampoco entra, así que es un bloqueo por dirección, no por huella de cliente.

Consecuencia inmediata: **toda la primera tanda de sondas por meses de 2022 y de enero de 2023
quedó inservible**, porque cayó después del bloqueo y sus 404 son indistinguibles de un sitio que
no contesta. El bloqueo se levantó solo a los veinte minutos, y la medición se rehízo entera de
forma secuencial, con tres segundos entre pedidos y control positivo antes y después de cada
tanda: de ahí sale la fecha de arranque del punto 2.2, que ya está resuelta.

La lección operativa para la próxima vez que haya que sondear un sitio ajeno: **si el control
positivo deja de responder, todo lo medido desde ahí se descarta**, y la sonda se repite en
serie. Concurrencia contra un sitio que uno no controla compra minutos y cuesta horas.

Lo que quedó pendiente:

- Reconstruir los meses faltantes de las tasas pasivas del BCB —abril a agosto de 2017 y julio de
  2019— desde los archivos semanales, que ya están descargados.
- Bajar la serie histórica completa de Tasas Promedio Ponderadas. Hoy hay un solo reporte, el del
  11 de septiembre de 2026. Son unos 1.070 días hábiles desde el 30 de junio de 2022, y hay que
  bajarlos en serie, no en paralelo.
- Consolidar los 135 boletines mensuales de ASFI en una sola tabla. Hoy son 135 libros de
  veintiuna hojas cada uno; la serie existe pero todavía no está armada.
- Averiguar el significado de los códigos de columna del reporte de Tasas Promedio Ponderadas.
  Son veintisiete números que casi con certeza son tramos de plazo. La página de códigos de la
  BBV (`https://www.bbv.com.bo/materiales/codigos/`) se abrió una vez levantado el bloqueo y
  **no los explica**: es un glosario de instrumentos, agencias de bolsa y emisores, sin ninguna
  tabla de plazos. Hay que preguntarlo o deducirlo de los datos.

---

## Dónde quedó cada cosa

Todo bajo `/home/adminodoo/universo-monetario/datos/crudo/`:

| Carpeta | Contenido | Tamaño |
|---|---|---|
| `asfi/fondos-evolutivo/` | 100 XLS, uno por fondo, serie diaria 2010-2026 | 107 MB |
| `asfi/boletines-mv/` | 135 boletines mensuales, Ene-2015 a Abr-2026 | 213 MB |
| `asfi/inversiones/` | 11 ZIP de evolutivos de cartera, corte 31-12-2025 | 16 MB |
| `asfi/tarifarios/` | Tarifario de caja de ahorros, corte 31-01-2026 | 136 KB |
| `bcb/tasas-pasivas/` | 89 XLSX de tasas pasivas, 2001-2026 | 26 MB |
| `bcb/` | Publicación semanal al 31-08-2026 y reporte diario del 09-09-2026 | 105 KB |
| `bbv/` | Reporte de Tasas Promedio Ponderadas del 11-09-2026 | 45 KB |

En total, 366 archivos y 366 MB, de los cuales 340 se descargaron en esta ronda.

**Nada de esto está versionado, y la decisión sigue abierta.** Los 3,1 MB del dólar paralelo que
ya estaban en el repositorio sí lo están; los 366 MB de esta ronda quedaron fuera de git, porque
meterlos infla el repositorio de forma permanente y esa no es una decisión que corresponda tomar
de oficio. Las opciones razonables son tres: ignorarlos y tratar el disco del servidor como el
almacén, versionar solamente las tablas consolidadas que salgan de ellos, o mover el crudo a un
respaldo aparte. Sam la tiene planteada; la recomendación de la otra sesión es la segunda, para
que un repositorio académico que el tribunal pueda querer clonar no arrastre cientos de megas.

**Lo que sí está resuelto es el respaldo.** El 11 de septiembre de 2026 quedaron dos copias, y
las dos verificadas por suma de comprobación y no por conteo de archivos:

| Copia | Dónde | Qué es | Verificación |
|---|---|---|---|
| Local | `/media/adminodoo/Disco 2TB/backups/universo-monetario/datos-crudo-2026-09-11/` | El árbol completo, navegable | Los 367 `sha256` coinciden uno a uno con el origen |
| Fuera de la máquina | `onedrive_crypt:universo-monetario/universo-crudo-2026-09-11.tar.gz` | Un `tar.gz` de 141 MB, cifrado del lado del cliente | Se volvió a descargar y su `sha256` coincide con el original |

El árbol lleva adentro `MANIFEST-sha256-2026-09-11.txt`, con la suma de los 366 archivos de
datos, así que cualquiera de las dos copias se puede auditar sola.

Las dos verificaciones se hicieron con un control negativo al lado, porque una comparación que
no puede fallar no prueba nada: al cotejo de sumas se le pasó un manifiesto alterado a propósito
y reportó la diferencia; al listado remoto se le pidió una carpeta inexistente y devolvió
`directory not found` en vez de un vacío mudo.
