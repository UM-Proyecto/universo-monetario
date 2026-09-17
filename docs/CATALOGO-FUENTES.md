# Catálogo de fuentes del proyecto Universo Monetario

**Fecha de corte: 17 de septiembre de 2026.** Este documento **reemplaza** a los tres catálogos
que había antes y que se contradecían entre sí, porque eran de momentos distintos:

- `fuentes.json` del repositorio del equipo (8 entradas, todas en estado `portada-ok`)
- `docs/FUENTES.md` (fuentes internacionales y dólar paralelo, verificado el 1-sep-2026)
- `docs/FUENTES-formales.md` (ASFI, BBV y BCB, verificado el 11-sep-2026)

Los dos documentos siguen en el repositorio como **detalle histórico**: traen procedimientos de
descarga y notas de manejo que no se repiten acá. Lo que ya no vale de ellos es el **estado** de
cada fuente, que ahora vive únicamente en este catálogo.

---

## La regla que ordena este catálogo

**Verificar es abrir el archivo, no comprobar que la página responda.** Que un sitio devuelva 200
sólo prueba que el sitio está en pie. Por eso cada entrada declara tres cosas distintas, y hay que
leerlas como distintas:

| Estado | Qué significa |
|---|---|
| **Descargada y abierta** | Alguien bajó el archivo, lo abrió y anotó cuántas filas trajo, qué columnas y qué rango de fechas. Es el único estado que cuenta como evidencia. |
| **Responde** | El sitio contesta y su control negativo está sano, pero nadie abrió el documento concreto. |
| **Su 200 no prueba nada** | El dominio devuelve éxito también a rutas inventadas. Aquí el código de respuesta es información nula. |
| **No publica lo que se creía** | La entrada anterior del catálogo describía algo que la fuente no tiene. |

Y hay un estado que **no** se usa nunca: «verificada» a secas.

### Cómo se mide

`scripts/verificar_fuentes.py` pide cada URL **junto a una ruta inventada del mismo dominio** y
compara los dos cuerpos, no los dos códigos. Clasifica como soft-404 tanto el caso obvio —mismo
hash— como el caso que engaña: mismo `<title>` y prácticamente el mismo tamaño, donde el hash
difiere sólo por contenido rotativo. Deja su medición en `datos/fuentes-medicion-<fecha>.json`.

---

## 1. Fuentes con archivo descargado y abierto

Éstas son las que sostienen cifras del proyecto.

### 1.1 INE — Bases de importaciones

| | |
|---|---|
| **Qué es** | Registros de importación por mes, aduana, vía, medio, país y partida NANDINA |
| **Descargada** | 16 de septiembre de 2026, de `nube.ine.gob.bo` |
| **Qué contenía** | Cuatro bases XLSX: 2023, 2024, 2025 y enero–julio 2026. **1.433.610 registros, 201 MB.** Abiertas y contadas, no sólo bajadas |
| **Período** | Enero de 2023 a julio de 2026 |
| **Control** | Ruta inventada del mismo dominio: **503**, cuerpo HTML de 8.239 bytes |

**El dato es de la Aduana pero quien lo publica es el INE.** Es fuente primaria de origen
administrativo.

**Límite que hay que declarar en cualquier uso:** cada registro es una **agregación**. No hay
identificador de importador ni operaciones individuales. Esta base **no permite** contar
operaciones sobre Bs 50.000 por empresa, que era lo que la tarjeta original del proyecto quería.

De aquí salen: la canasta de repuestos de siete partidas (USD 232,4 millones, enero–julio 2026),
Santa Cruz con 45,4 % de la canasta, China con 55,6 % del origen, y el tipo de cambio implícito de
aduana clavado en 6,96 durante 42 meses contra 561 valores distintos en julio de 2026.

### 1.2 BCB — Tasas de interés pasivas

| | |
|---|---|
| **Qué es** | Tasas por entidad y plazo, de 30 a 1.080 días, en XLSX |
| **Descargada** | 11 de septiembre de 2026 |
| **Qué contenía** | **302 de 308 meses.** Faltan abril a agosto de 2017 y julio de 2019 |
| **Período** | Enero de 2001 a agosto de 2026 |

**Trampa pagada:** la página lista **55 archivos `.xlsx`** y uno de ellos es de Reservas
Internacionales, de otra sección del sitio. Tomar «el primer Excel de la página» baja un archivo
que abre perfecto, con hojas y números plausibles, y no da ningún síntoma. **Hay que filtrar por la
ruta de la sección, no por el orden en la página.**

### 1.3 ASFI — Boletín Estadístico del Mercado de Valores

| | |
|---|---|
| **Descargada** | 11 de septiembre de 2026; el de abril de 2026 se abrió hoja por hoja el 16 |
| **Qué contenía** | **135 boletines**, XLSX de 21 hojas cada uno |
| **Período** | Enero de 2015 a abril de 2026 |

**Tres correcciones al catálogo anterior, medidas abriendo el archivo:**

- Las hojas 12, 13 y 14 **no** tienen 174, 137 y 586 filas: ésas son las dimensiones de formato de
  la hoja. Filas **con dato**: 6, 49 y 60.
- La hoja 12 **no** es «compraventa» ni la 13 «ídem moneda extranjera». Según el índice del propio
  boletín: hoja 12 = mercado **primario**, hoja 13 = mercado **secundario**, y las dos traen sus
  secciones en bolivianos y en dólares.
- La advertencia «el secundario es delgado: seis filas contra 586 de reporto» mezclaba las dos
  cosas anteriores. Lo correcto para abril de 2026: **6 operaciones en el primario, 49 en el
  secundario, 60 en reporto.** La advertencia sigue valiendo; los números eran otros.

**Ojo con el quiebre:** esta serie termina en abril de 2026 y por eso **todavía no cruza** el
29-jun-2026. El primer boletín posterior a junio la convierte en una serie que cruza y hay que
aplicarle DEC-02.

### 1.4 ASFI — Evolutivo de fondos de inversión SAFI

| | |
|---|---|
| **Descargada** | 11 de septiembre de 2026, con Chromium headless sobre Playwright |
| **Qué contenía** | **100 fondos, 382.424 filas diarias**: valor cuota, participantes, tasas a 30/90/180/360 días, liquidez y cartera |
| **Período** | 1 de enero de 2010 a 8 de septiembre de 2026 |

Hace falta navegador porque es una aplicación de reportes, no un archivo estático. Una vez
resuelta la dirección, la descarga es un pedido HTTP común.

### 1.5 ASFI — Inversiones, Tarifarios y texto consolidado

- **Inversiones** (evolutivos de cartera): ZIP con XLSX y ODS, cortes 31-12-2025 y 30-04-2026.
- **Tarifarios**: ZIP, corte 31-01-2026. Es la fuente del costo de entrada bancario.
- **Texto consolidado** `servdmzw.asfi.gob.bo/circular/Textos/L01T02.pdf`: **207 páginas**, bajado y
  abierto el 15 de septiembre de 2026. Es lo citable para activos virtuales, **no** la Resolución
  540/2025 suelta, que ya no es el texto vigente. La cadena real es 540/2025 → 1203/2025 →
  373/2026, y el plazo vigente es el **30 de junio de 2026**, textual en la Sección 8 del Capítulo
  XI. Conviene volver a bajarlo antes de imprimir: ASFI tocó ese capítulo tres veces en catorce
  meses.

### 1.6 BBV — Tasas Promedio Ponderadas

PDF diario direccionable por fecha, del 30-06-2022 al 11-09-2026, descargado y abierto el 11 de
septiembre de 2026.

**Advertencia operativa medida:** la BBV **bloquea por IP** ante pedidos concurrentes, unos veinte
minutos. Sus tablas web no exponen ningún endpoint de datos y no hay histórico gratuito. Por eso
la serie de bolsa del proyecto sale del Boletín de ASFI y no de la BBV.

### 1.7 Dólar paralelo — las dos fuentes

Decidido en `docs/decisiones/DEC-01-fuente-dolar-paralelo.md`.

| | paralelo.bo | dolarbluebolivia.click |
|---|---|---|
| **Papel** | Fuente primaria del histórico | Contraste independiente |
| **Descargado** | 17-sep-2026, `/api/v1/historical.csv` | 17-sep-2026, `/v1/chart/all.csv` |
| **Qué contenía** | **773 medianas diarias**, sin hueco | **77.358 observaciones de tick** |
| **Período** | 6-ago-2024 a 17-sep-2026 | 21-jul-2024 a 17-sep-2026 |
| **Licencia** | **CC-BY 4.0**, declarada en la cabecera del CSV | Términos prohíben «copiar contenido sin autorización» |
| **Metodología** | Publicada en `/metodologia` | No publicada |

**Corrección de estado, y es la más importante de esta unificación:** `docs/FUENTES.md` daba a
paralelo.bo por **caída** al 1 de septiembre de 2026. **Está viva.** Medida hoy: portada 200 con
control negativo 404, API `/v1/rate` respondiendo, especificación OpenAPI en `/api/openapi.json`
con ocho endpoints, y el histórico completo descargado y contado. La entrada anterior describía un
corte temporal y quedó congelada como si fuera permanente.

**Cuatro trampas de estas dos fuentes**, desarrolladas en DEC-01: la última fila del CSV de
paralelo.bo no está consolidada y hay que descartarla; «compra» y «venta» están invertidas entre
las dos; la composición de la mediana de paralelo.bo cambió en septiembre de 2026 al entrar Bitget;
y la página promete «histórico desde 2022» mientras sirve desde agosto de 2024.

### 1.8 Binance P2P — la captura propia

| | |
|---|---|
| **Qué es** | Libro completo de anuncios USDT/BOB, una fila por anuncio |
| **Endpoint** | `https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search` |
| **Período** | Libro completo desde el 11-sep-2026 14h; resumen desde el 9-sep-2026 20h |
| **Estado al 17-sep** | **44.373 filas, 136 corridas horarias, cero huecos** |

Es la única serie del proyecto que **no se puede rehacer**: el libro de hoy no existe mañana.
Mantenimiento y verificación de huecos en TASK-48 y `scripts/huecos_p2p.py`.

---

## 2. Fuentes que responden pero cuyo documento nadie abrió

Estado medido hoy, con control negativo sano en los cuatro casos (la ruta inventada devuelve 404):

| Fuente | URL | Bytes | Para qué se la quiere |
|---|---|---|---|
| BCB — portada | `bcb.gob.bo/` | 308.166 | Entrada al Boletín Estadístico vigente |
| BCB — estadísticas | `bcb.gob.bo/?q=estadisticas` | 97.867 | Agregados monetarios, reservas, tipo de cambio |
| INE — portada | `ine.gob.bo/` | 295.782 | Entrada |
| INE — económicas | `ine.gob.bo/index.php/estadisticas-economicas/` | 180.476 | IPC empalmado y PIB |
| ASFI — portada | `asfi.gob.bo/` | 164.737 | Entrada a boletines y registros |

**Nota de manejo del BCB:** los enlaces del Boletín Estadístico llevan la fecha de publicación
dentro de la ruta y **cambian cada trimestre**. No se fijan: se resuelven desde la página de
estadísticas en cada corrida. Los del INE, en cambio, son permanentes y sí se pueden fijar.

---

## 3. Fuentes cuyo 200 no prueba nada

### 3.1 `impuestos.gob.bo` — soft-404 confirmado hoy

Devuelve **la misma portada con código 200 a cualquier ruta**. Medido el 17-sep-2026:
`/normativa` y `/normativa-inventada-abc123` devuelven **exactamente 148.155 bytes las dos**, el
mismo `<title>` «Impuestos - SIN», y sus 56 líneas de diferencia son todas imágenes del carrusel
rotativo.

Es el caso que más engaña de todos los del catálogo, porque **el tamaño coincide y el hash no**:
un verificador que compare hashes lo deja pasar como «cuerpo distinto». El texto de la RND
102400000021 hay que conseguirlo por otra vía y abrirlo para confirmar que es el que se cita.

### 3.2 Gaceta Oficial — baja un PDF a cualquier identificador

`gacetaoficialdebolivia.gob.bo/normas/descargarPdf/<id>` devuelve **200 y un PDF real para
cualquier número**. El falso trae una página sin una sola letra; el verdadero, veintinueve con la
ley. Ni el código ni el `content-type` distinguen: **hay que abrir el archivo y contar páginas o
caracteres.**

### 3.3 BCB histórico de tipo de cambio — devuelve el año equivocado

`bcb.gob.bo/tiposDeCambioHistorico/pdf.php?anio=1899` devuelve **200 con `application/pdf`** y
adentro trae la tabla del **año 2000**. Es el hermano exacto del caso de la Gaceta: el archivo es
real, es un PDF, abre bien, y no es el que se pidió. **Hay que leer el año adentro del documento.**

### 3.4 `udape.gob.bo` — redirige todo a la portada

Una ruta inventada devuelve **215.729 bytes de HTML, exactamente los mismos** que la ruta buena.
Una cita bibliográfica del proyecto que venía dada por buena cayó así.

---

## 4. Correcciones a entradas del catálogo anterior

### 4.1 Aduana Nacional — no publica lo que la entrada decía

La entrada `aduana-portada` de `fuentes.json` declaraba que aporta «estadísticas de importación por
partida, origen y valor» y que «es el denominador del problema». **Es falso, y está medido.**

El sitio responde —200 con 191.787 bytes, control negativo sano— pero la palabra «estadística» no
aparece **ni una vez** en sus ochenta enlaces, y la ruta antigua `/aduana7/content/estadisticas`
devuelve un 404 real con control negativo sano en el mismo dominio.

**El dato existe y lo publica el INE** (entrada 1.1). La entrada de la Aduana se conserva como
punto de entrada normativo, no como fuente de datos.

### 4.2 El plazo de los PSAV no venció el 30 de abril de 2026

Circulaba esa fecha. El plazo original era el 31-dic-2025 y el vigente es el **30 de junio de
2026**, textual en el consolidado de ASFI. El 30-abr-2026 coincide con otra cosa: la Resolución
ASFI/373/2026 del 29-abr-2026, que modificó el reglamento.

### 4.3 `economiayfinanzas.gob.bo` sirve la cadena TLS incompleta

`curl` sin `-k` devuelve **000** y el sitio parece caído; con `-k` responde 200 y el control
negativo da un 404 legítimo. La **RM 245/2026 existe y es del 26 de junio de 2026** —el 29 es la
fecha de vigencia—. Su PDF son **tres imágenes JPEG sin capa de texto**: cualquier extractor
devuelve vacío. Control positivo corrido en el mismo minuto sobre otro PDF: 6.015 caracteres.

### 4.4 Las páginas de activos virtuales del BCB están restringidas, no ausentes

Devuelven **403**, mientras una fecha inventada devuelve **404**. La diferencia importa: existen y
están restringidas. El único PDF público que queda trae quince días de precios de USDT de 2024.

**Y un dato que el proyecto tiene que saber:** el BCB tomaba el precio USDT/BOB del **P2P de
Binance ponderado por volumen**, que es la misma fuente que nosotros capturamos. Esa serie oficial
ya no es pública.

---

## 5. Fuentes internacionales

Verificadas el 1 de septiembre de 2026, sin cambios medidos desde entonces. Alimentan los veinte
instrumentos de `datos/universo.csv`.

| Fuente | Clase | Estado |
|---|---|---|
| yfinance (Yahoo Finance) | Acciones y ETF de bonos | Viva |
| `api.binance.com` | Criptomonedas | Viva |
| `api.frankfurter.dev` | Divisas | Viva, con histórico |
| `open.er-api.com` | Divisas | Viva, **sin histórico gratis** — por eso no se usa |
| FRED (`fredgraph.csv`) | Bonos | Viva y sin clave, pero **truncada** en los índices de retorno total — por eso los bonos van por yfinance |

**Nota de manejo:** Frankfurter está detrás de Cloudflare y responde **403 «error code: 1010»** al
User-Agent por defecto de `urllib`. Con `curl` la misma URL da 200. Un pipeline que no declare esto
falla de la peor forma: parece que la serie no existe, no que la consulta fue rechazada.

**Advertencia de dependencia:** yfinance se rompe cada pocos meses cuando Yahoo cambia algo. La
demostración ante el tribunal no puede depender de que un servicio externo esté vivo ese día — ver
TASK-53, caché local.

---

## 6. Cómo se rehace todo esto

```
python3 scripts/verificar_fuentes.py   # mide cada fuente con su control negativo
python3 scripts/verificar_quiebre.py   # qué serie cruza el 29-jun-2026 y si está marcada
python3 scripts/huecos_p2p.py          # huecos de la captura propia, por hora boliviana
python3 scripts/comparar_paralelo.py   # las dos fuentes del paralelo, una contra otra
```

Ninguna cifra de este catálogo hay que creerla: las cuatro órdenes de arriba las reimprimen.
