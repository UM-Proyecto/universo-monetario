# Catálogo de fuentes de datos

> **ESTE DOCUMENTO YA NO FIJA EL ESTADO DE LAS FUENTES.** Desde el 17 de septiembre de 2026 el
> catálogo único del proyecto es [`CATALOGO-FUENTES.md`](CATALOGO-FUENTES.md), que unifica este
> archivo con `FUENTES-formales.md` y con el `fuentes.json` del repositorio del equipo, que se
> contradecían entre sí por ser de momentos distintos.
>
> Lo que sigue valiendo de acá es el **procedimiento**: cómo se descarga cada fuente, qué endpoints
> tiene y qué notas de manejo hay que respetar. Lo que **no** vale es el estado de cada fuente.
> Ejemplo concreto medido: este documento da a `paralelo.bo` por caída, y el 17-sep-2026 está viva,
> con su histórico completo descargado.



Cada fila de este catálogo se verificó descargando el dato, no comprobando que la página
respondiera. La columna «verificado» lleva la fecha de la última descarga real y el resultado
concreto que devolvió, porque una fuente que estaba viva hace una semana no prueba nada hoy: la
tarjeta TASK-3 existe justamente porque yfinance se rompe cada pocos meses cuando Yahoo cambia
algo, y la demostración ante el tribunal no puede depender de que un servicio externo esté vivo
ese día.

Última ronda de verificación: **1 de septiembre de 2026**, desde el servidor `pop-os`.

## Estado resumido

| Fuente | Clase | Estado | Verificado |
|---|---|---|---|
| yfinance (Yahoo Finance) | Acciones y ETF de bonos | Viva | 2026-09-01 |
| Binance público (`api.binance.com`) | Criptomonedas | Viva | 2026-09-01 |
| api.frankfurter.dev | Divisas | Viva, con histórico | 2026-09-01 |
| open.er-api.com | Divisas | Viva, pero **sin histórico gratis** | 2026-09-01 |
| FRED (`fredgraph.csv`) | Bonos | Viva y sin clave, pero **truncada** en los índices de retorno total | 2026-09-01 |
| api.dolarbluebolivia.click | Dólar paralelo y oficial | Viva, con API documentada | 2026-09-01 |
| paralelo.bo | Dólar paralelo | **Caída** | 2026-09-01 |

Las tres filas en negrita cambian lo que decía la Tabla 3 del boceto, y ninguna de las tres se
nota leyendo el documento: los tres servicios existen y responden. Lo que falla es lo que
entregan.

---

## Acciones — yfinance

- **Endpoint:** biblioteca `yfinance`, versión 1.7.0.
- **Verificado el 2026-09-01:** `yf.download(['AAPL','MSFT'], start='2020-01-01')` devolvió 1 674
  filas, del 2 de enero de 2020 al 31 de agosto de 2026. Último cierre ajustado: AAPL 319,70 y
  MSFT 507,29.
- **Costo:** cero, sin registro ni tarjeta.
- **Riesgo conocido:** es la fuente frágil del conjunto. No tiene contrato de servicio y se rompe
  cuando Yahoo cambia el formato interno. Es la razón de ser de la caché de TASK-3.
- **Entorno usado:** entorno virtual creado con `uv`; el intérprete del sistema (Python 3.10.12)
  no trae `yfinance` ni `pandas`.

## Criptomonedas — Binance público

- **Endpoint:** `https://api.binance.com/api/v3/klines?symbol=BTCUSDT&interval=1d&limit=2`
- **Verificado el 2026-09-01:** devolvió velas diarias con apertura, máximo, mínimo, cierre y
  volumen. La última cerró en 79 100,00 USDT.
- **Costo:** cero, sin clave de API para datos de mercado públicos.
- **Nota:** el par se cotiza contra USDT, no contra dólar estadounidense. Para la conversión a
  bolivianos hay que encadenar USDT → USD → BOB, y ese primer tramo no vale exactamente uno.

## Divisas — api.frankfurter.dev, y por qué no open.er-api.com

La Tabla 3 del boceto asigna las divisas a `open.er-api.com`. Esa fuente está viva y responde,
pero **no sirve para lo que el proyecto necesita**: entrega únicamente la cotización del momento.
Se probaron dos formas del endpoint histórico (`/v6/history/USD/<fecha>` y `/v6/<fecha>/USD`) y
las dos devuelven 404. Sin serie temporal, la clase divisas no puede entrar ni a la alineación de
calendarios de TASK-4 ni al cálculo de riesgo, que es todo el punto de incluirla.

La reemplaza **Frankfurter**, que publica las tasas de referencia del Banco Central Europeo:

- **Endpoint:** `https://api.frankfurter.dev/v1/<desde>..<hasta>?base=USD&symbols=EUR,BRL`
- **Verificado el 2026-09-01:** la serie del euro devolvió 7 082 observaciones diarias, del 4 de
  enero de 1999 al 31 de agosto de 2026. Real brasileño y yuan arrancan el 13 de enero de 2000.
- **Costo:** cero, sin clave ni registro.
- **Limitación que hay que declarar:** son 30 monedas, las de referencia del BCE. **No incluye
  peso argentino, boliviano, sol peruano ni peso chileno.** Cualquier análisis regional que las
  necesite tiene que buscar otra fuente.
- **Gotcha medido:** Frankfurter está detrás de Cloudflare y **rechaza el User-Agent por defecto
  de `urllib` con HTTP 403 y el cuerpo `error code: 1010`**. La misma URL con `curl` devuelve 200.
  Es la peor forma de fallar, porque el código que no lo declara concluye que la serie no existe
  en vez de que la consulta fue rechazada. Hay que mandar un User-Agent propio.

`open.er-api.com` sigue siendo útil para una cosa: la cotización del día de 166 monedas, entre
ellas el boliviano, que Frankfurter no tiene. Ojo con esa cifra: el 1 de septiembre de 2026 daba
**BOB 11,8076** mientras el oficial publicado por dolarbluebolivia ese mismo día era **12,12**.
Son dos números para el mismo concepto y hay que elegir uno antes de que aparezcan los dos en el
documento.

## Bonos — tres ETF por yfinance, y por qué no FRED

La Tabla 3 asigna los bonos a FRED y anota «Clave: Sí, gratuita». Las dos mitades necesitan
corrección, y hay además un problema de fondo que no es de fuente sino de tipo de dato.

**La clave no hace falta.** La ruta `https://fred.stlouisfed.org/graph/fredgraph.csv?id=<serie>`
descarga sin credencial: verificado el 2026-09-01 con DGS10, que bajó como CSV con cabecera
`observation_date,DGS10` y primera observación del 2 de enero de 1962. Conviene usarla y no atar
el proyecto a una credencial que caduca.

**Pero los índices de retorno total vienen truncados.** Las series de ICE BofA —corporativo
(`BAMLCC0A0CMTRIV`), alto rendimiento (`BAMLHYH0A0HYM2TRIV`) y emergentes
(`BAMLEMCBPITRIV`)— devuelven 794 filas que arrancan el 1 de septiembre de 2023, y el parámetro
`cosd=1990-01-01` no las extiende. Tres años de historia contra los seis del resto del universo.

**Y el problema de fondo:** las series `DGS` son **rendimientos, no precios**. Calcular
rendimientos porcentuales sobre una serie que ya es un rendimiento para meterla al valor en
riesgo es un error de tipo, no un problema de cobertura. Convertirlas a retornos exige suponer
una duración, que es una decisión de modelado que nadie tomó.

Por las tres razones, el universo usa **tres ETF de bonos por yfinance**, que son precios reales,
tienen historia larga y además son instrumentos que una persona puede efectivamente tener:

| Símbolo | Qué es | Serie desde |
|---|---|---|
| AGG | Deuda agregada estadounidense de grado de inversión | 2003-09-29 |
| HYG | Bonos corporativos de alto rendimiento | 2007-04-11 |
| EMB | Deuda soberana emergente en dólares | 2007-12-19 |

FRED sigue siendo la fuente correcta para tasas y contexto macro; lo que no es, es la fuente de
la clase de activo «bonos» de este universo.

## Dólar paralelo y oficial — api.dolarbluebolivia.click

Es la fuente que TASK-17 mandaba evaluar, y resultó bastante más sólida de lo que la tarjeta
suponía. No es una página para raspar: tiene una API con especificación OpenAPI publicada en
`https://api.dolarbluebolivia.click/openapi.json`, copiada en este repositorio como
`docs/dolarbluebolivia-openapi.json`.

Los endpoints que sirven al proyecto son públicos y no piden clave:

| Endpoint | Qué entrega |
|---|---|
| `/v1/officialRate` | Cotización actual: paralelo y oficial, con marca de tiempo |
| `/v1/chart/all.csv` | Historial completo a resolución nativa (~15 minutos), en CSV |
| `/v1/chart/oficial.csv` | Historial diario del tipo de cambio oficial del gobierno |
| `/v1/chart/export?from=&to=&format=&bucket=` | Exportación por rango de fechas |
| `/v1/chart/6m` | Últimos seis meses, por hora |
| `/v1/other_countries` | Cotizaciones de USDT contra otras siete monedas |

El resto del catálogo (paneles, historial analítico, libros de órdenes P2P de Binance, Bybit,
Bitget y OKX) vive bajo `/private/` y exige `X-API-Key`. No hace falta para el alcance del
semestre, pero conviene saber que existe.

### Qué se descargó y qué contiene

`datos/crudo/paralelo/dolarblue-historico-15min.csv` — descargado el 2026-09-01.

- 75 804 observaciones, del 21 de julio de 2024 al 1 de septiembre de 2026.
- Columnas: `datetime, official_buy, official_sell, blue_buy, blue_sell`.
- 773 días distintos sobre un lapso calendario de 773 días: **cero días faltantes**.
- Calidad: una sola fila con valores en cero (2026-06-02 08:42:39, con el paralelo en 0,00) sobre
  75 804, y dos saltos mayores al 10 % entre observaciones consecutivas. Hay que descartar esa
  fila en la limpieza, no dejarla entrar al cálculo de rendimientos.

`datos/crudo/paralelo/dolarblue-oficial-diario.csv` — descargado el 2026-09-01.

- 213 días, del 1 de diciembre de 2025 al 1 de septiembre de 2026.
- Columnas: `day, compra, venta, kind`.
- La columna `kind` marca el cambio de régimen en los propios datos: las filas viejas son
  `referencial` y las nuevas `unificado`. Es un marcador que el proyecto puede usar directamente
  para el corte de TASK-15 en vez de codificar la fecha a mano.

### El quiebre estructural, medido sobre estos datos

Separando el historial por la fecha de la flotación (29 de junio de 2026) y calculando la brecha
entre el punto medio del paralelo y el punto medio del oficial:

| Período | Observaciones | Brecha media | Máxima | Mínima |
|---|---|---|---|---|
| Antes del 2026-06-29 | 69 657 | 69,5 % | 174,6 % | −100,0 % |
| Desde el 2026-06-29 | 6 147 | 0,2 % | 5,6 % | −6,7 % |

La mínima de −100 % del primer período es la fila defectuosa mencionada arriba, no un dato
económico. Descontándola, el resultado sostiene con datos propios lo que hasta ahora era una
afirmación de prensa: la brecha pasó de decenas de puntos porcentuales a oscilar alrededor de
cero, y el paralelo llegó a cotizar **por debajo** del oficial.

Conviene señalar que la brecha media de 69,5 % es más alta que el «más del 40 %» que venía
circulando en los documentos del proyecto. Las dos cifras pueden convivir —40 % puede ser el valor
de un momento puntual y 69,5 % el promedio de dos años— pero antes de escribir cualquiera de las
dos en el documento hay que decir de qué período es y cómo se calculó.

## paralelo.bo — caída

La tarjeta TASK-17 pide comparar dolarbluebolivia.click «contra paralelo.bo, que ya está
verificada y tiene histórico desde 2024». **Esa premisa ya no se sostiene.**

Verificado el 2026-09-01: `https://paralelo.bo/` devuelve **HTTP 402** con el encabezado
`x-vercel-error: DEPLOYMENT_DISABLED` y el cuerpo `Payment required`. No es una caída pasajera ni
un bloqueo por agente de usuario: es un despliegue de Vercel deshabilitado, que es lo que ocurre
cuando el proyecto deja de pagarse o el dueño lo apaga. Se probó siguiendo redirecciones y con
encabezado de navegador; el resultado no cambia.

Consecuencia práctica: la comparación que pedía la tarjeta no se puede hacer contra un servicio
que no responde, y la fuente que la tarjeta daba por respaldo es la que hay que reemplazar. El
historial que se le atribuía —«desde 2024»— lo tiene dolarbluebolivia.click, medido arriba.

---

## Qué falta relevar

- **Tipo de cambio oficial del BCB como fuente primaria.** La decisión D6 lo nombra como fuente
  primaria de conversión, y lo que hay hasta ahora es el oficial que publica dolarbluebolivia,
  que no es lo mismo que el boletín del BCB. Hay un obstáculo ya documentado: los enlaces del
  Boletín Estadístico del BCB llevan la fecha de publicación dentro de la ruta y cambian cada
  trimestre, así que la fecha vigente hay que resolverla desde la página índice en vez de fijarla
  en el código.
- **Series macro del INE** (índice de precios al consumidor empalmado, producto interno bruto).
  Los enlaces del INE sí son permanentes.
- **Comercio global** (Comtrade o Banco Mundial). Va último por la decisión D2 y entra como
  contexto, nunca como activo con rendimiento estimable.
