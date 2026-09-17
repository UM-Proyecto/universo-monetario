# DEC-01 — Qué fuente del dólar paralelo usa el proyecto

**Decidido el 17 de septiembre de 2026.** Cierra TASK-52, que venía de TASK-17 del tablero anterior.
Todas las mediciones de este documento se rehacen con `scripts/comparar_paralelo.py`.

---

## La decisión, en tres líneas

1. **Histórico (hasta el 10 de septiembre de 2026): `paralelo.bo`**, endpoint
   `https://paralelo.bo/api/v1/historical.csv`.
2. **Contraste independiente: `dolarbluebolivia.click`**, endpoint
   `https://api.dolarbluebolivia.click/v1/chart/all.csv`. Se cita y se usa para verificar; no se
   redistribuye.
3. **Del 11 de septiembre de 2026 en adelante manda nuestro propio libro**, `datos/p2p/anuncios.csv`.
   Es la única serie del proyecto que podemos auditar de punta a punta, y para ese tramo las dos
   fuentes externas pasan a ser contraste, no fuente.

---

## Por qué la elección importa, y exactamente dónde

La tarjeta lo planteaba como sospecha y quedó medido. Sobre los **773 días que las dos fuentes
tienen en común** (6-ago-2024 a 17-sep-2026), la diferencia entre sus medianas diarias es:

| Régimen | Días | Diferencia mediana | p90 | Máxima |
|---|---|---|---|---|
| Post-flotación (29-jun-2026 al 16-sep-2026) | 80 | 0,25 % | 1,60 % | 2,47 % |
| Pre-flotación (hasta el 28-jun-2026) | 692 | 1,04 % | 4,66 % | 9,74 % |

Esa tabla está calculada **descartando el día en curso**, por la razón que explica la trampa 1 más
abajo. Vale la pena decir qué pasa si uno no lo descarta, porque es el ejemplo más limpio de por
qué la regla existe: con la fila del 17-sep incluida, el máximo post-flotación salta de 2,47 % a
8,37 % y aparece un día de divergencia enorme que no ocurrió. Una sola fila sin consolidar alcanza
para triplicar el peor caso de todo un régimen.

Hoy da casi igual cuál se use, como decía la tarjeta. Pero el tramo donde no da igual no es
cualquiera: **las ocho discrepancias más grandes de toda la serie caen en mayo de 2025 y julio de
2025**, y mayo de 2025 es justamente el mes en que la brecha contra el tipo de cambio oficial
tocó su máximo: brecha mediana del **136,5 %** y máxima del **158,9 %** ese mes, medidas sobre las
filas de `dolarbluebolivia.click`, que traen el oficial y el paralelo en la misma fila.

Dicho de otro modo: las dos fuentes se parecen cuando el fenómeno es chico y se separan cuando el
fenómeno es grande. Elegir fuente "porque hoy coinciden" es elegir mirando el tramo que no informa.

Las cinco mayores:

| Día | dolarblue | paralelo.bo | Diferencia |
|---|---|---|---|
| 27-may-2025 | 16,27 | 14,68 | −9,74 % |
| 24-may-2025 | 16,50 | 14,94 | −9,48 % |
| 2-jul-2025 | 14,85 | 13,50 | −9,09 % |
| 17-may-2025 | 17,46 | 15,92 | −8,85 % |
| 18-may-2025 | 17,54 | 16,02 | −8,67 % |

---

## Qué se comparó, y qué no decidió la elección

Ninguna de las dos es más exacta que la otra, y conviene decirlo antes que nada porque es lo
primero que uno esperaría que decidiera.

Contra **nuestro propio libro P2P**, sobre los seis días cerrados que tenemos (11 al 16 de
septiembre de 2026), el error absoluto medio es de **1,61 % para dolarblue y 1,50 % para
paralelo.bo**. Con seis días no hay diferencia que sostener.

| Día (hora boliviana) | Nuestro libro (mid) | dolarblue | paralelo.bo |
|---|---|---|---|
| 11-sep | 11,35 | 11,61 (+2,25 %) | 11,45 (+0,88 %) |
| 12-sep | 11,41 | 11,56 (+1,40 %) | 11,60 (+1,71 %) |
| 13-sep | 11,52 | 11,71 (+1,65 %) | 11,76 (+2,13 %) |
| 14-sep | 11,46 | 11,60 (+1,22 %) | 11,55 (+0,83 %) |
| 15-sep | 10,96 | 11,14 (+1,69 %) | 10,93 (−0,27 %) |
| 16-sep | 10,55 | 10,70 (+1,42 %) | 10,88 (+3,15 %) |

Lo que sí se ve es que **dolarblue quedó por encima de nuestro libro los seis días**, entre
+1,22 % y +2,25 %, mientras paralelo.bo osciló en los dos sentidos. Seis signos iguales seguidos
no salen por azar más que una vez de cada treinta, así que hay indicio de sesgo sistemático hacia
arriba en dolarblue. Es un indicio, no una medición: seis días es poco, y un sesgo constante es
más fácil de corregir que un ruido, así que esto no lo descalifica.

Parte de la diferencia tiene explicación conocida y no es error de nadie: paralelo.bo **filtra**
el libro antes de calcular (descarta vendedores con menos de 98 % de operaciones completadas y
órdenes de menos de 1.000 USDT) y nuestro libro no filtra nada. No son el mismo objeto con el
mismo nombre.

---

## Lo que sí decidió la elección: se puede auditar y se puede citar

**`paralelo.bo` publica su metodología completa** en `/metodologia`, con la frase explícita de que
está ahí "para que cualquier persona pueda auditarlo o reproducirlo": nombra las tres plataformas
activas (Binance P2P, Bybit P2P, Bitget P2P), las dos que descarta y por qué (OKX por falta de
liquidez en BOB, ElDorado porque su API no lista el boliviano), la frecuencia de consulta —cada 60
segundos sobre las 20 mejores órdenes de cada lado—, los filtros, el descarte de outliers a más de
5 % de una mediana provisional, y que el número público es el punto medio entre la mediana de
compra y la de venta. Su histórico se sirve bajo **licencia CC-BY 4.0**, declarada en la cabecera
del propio CSV, y su API está versionada con especificación OpenAPI en `/api/openapi.json`.

**`dolarbluebolivia.click` no publica metodología equivalente**, y sus términos de uso —revisados
el 17-sep-2026, última actualización del 3-sep-2026— dicen dos cosas que pesan para un entregable
académico: "no garantizamos la exactitud, completitud o actualidad de los datos mostrados", y
listan como uso prohibido "copiar contenido sin autorización". Su API está declarada en beta
abierta, con el aviso de que los endpoints pueden cambiar.

Para un trabajo que tiene que ser reproducible por un tribunal y que va a redistribuir la serie
en un anexo, eso alcanza para decidir. La fuente primaria es la que se puede auditar y citar con
licencia; la otra entra como contraste.

---

## Por qué dolarblue igual se queda, y para qué

Tiene tres cosas que paralelo.bo no da, y las tres son útiles:

- **Resolución de tick.** 77.358 observaciones entre el 21-jul-2024 y el 17-sep-2026, una cada
  ocho a quince minutos, contra 773 medianas diarias. Para cualquier pregunta intradiaria es la
  única de las dos que sirve.
- **El oficial y el paralelo en la misma fila.** Cada observación trae `official_buy`,
  `official_sell`, `blue_buy` y `blue_sell`. La brecha se calcula sin unir dos archivos y sin
  arriesgar un desfase de zona horaria entre ellos, que es de donde salen los errores silenciosos.
- **Dieciséis días más de historia**: arranca el 21-jul-2024 contra el 6-ago-2024.

Y sobre todo: un contraste sirve **porque es otro instrumento**. Si el proyecto usara las dos como
si fueran intercambiables, no tendría verificación de nada.

---

## Cuatro trampas que hay que dejar anotadas

1. **La última fila del CSV de paralelo.bo no está consolidada.** El 17-sep-2026 el histórico
   publicaba 9,80 para ese mismo día mientras su propia API en vivo devolvía 10,73 y nuestro libro
   daba 10,42. Son 5,95 % de error contra nuestra medición y una contradicción de la fuente contra
   sí misma. **Regla: al cargar el CSV, descartar la fila del día en curso.**
2. **"Compra" y "venta" están al revés entre las dos fuentes.** paralelo.bo publica compra 10,86 y
   venta 10,60 —compra es lo que uno paga— y dolarblue publica `blue_buy` 10,71 y `blue_sell` 10,79
   con el orden invertido. Mezclarlas da un spread con el signo cambiado y ningún error visible.
   **Regla: comparar sólo punto medio contra punto medio.**
3. **La serie de paralelo.bo no es homogénea en el tiempo.** Su propia metodología dice que Bitget
   P2P se incorporó en septiembre de 2026, o sea que la composición de la mediana cambió dentro
   del período que el proyecto usa. Es un quiebre metodológico además del quiebre cambiario del
   29-jun-2026 que trata DEC-02, y hay que declararlo en cualquier serie que cruce septiembre 2026.
4. **La página de paralelo.bo dice "Histórico desde 2022" y el CSV que sirve empieza el
   6-ago-2024.** No hay datos de 2022 ni de 2023 en ninguna de las dos fuentes. Si el proyecto
   necesita paralelo anterior a julio de 2024, la respuesta es que no lo tiene y hay que buscar
   otra fuente, no estirar ésta.

---

## Verificación de que estos 200 valen algo

Las cuatro descargas se hicieron con control negativo del mismo dominio, porque en este proyecto ya
se pagó el caso de un sitio que devuelve 200 a cualquier ruta:

| Pedido | Resultado |
|---|---|
| `paralelo.bo/` | 200, 201.174 bytes |
| `paralelo.bo/ruta-que-no-existe-abc123` | **404**, 13.938 bytes |
| `paralelo.bo/api/v1/historical.csv` | 200, 13.025 bytes, `text/csv` |
| `paralelo.bo/api/v1/historicalXYZ.csv` | **404** |
| `dolarbluebolivia.click/` | 200, 454.186 bytes |
| `dolarbluebolivia.click/ruta-que-no-existe-abc123` | **404**, 132.676 bytes |
| `api.dolarbluebolivia.click/v1/chart/all.csv` | 200, 3.277.861 bytes, `text/csv` |
| `api.dolarbluebolivia.click/v1/chart/inventado-abc123.csv` | **404**, cuerpo `{"detail":"Not Found"}` |

Los dos dominios dan 404 real a una ruta inventada, así que sus 200 significan algo. Y los dos CSV
se abrieron y se contaron: 773 y 77.358 filas de dato respectivamente, ninguna con hueco de día
dentro de su rango.
