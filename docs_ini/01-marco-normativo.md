# Marco normativo — qué puede hacer legalmente una herramienta como ésta en Bolivia

> Investigación inicial asistida por agente de IA, 10 de septiembre de 2026. Este documento
> delimita el alcance legal del sistema y sostiene la dimensión fiscal del planteamiento. No es
> asesoramiento jurídico: es el relevamiento de las normas que el equipo tiene que citar y
> respetar, con la referencia de cada una para que un tercero la verifique.

---

## Lo que exige licencia, y por qué el sistema no cae ahí

El Decreto Supremo 5384 del 7 de mayo de 2025 enumera las actividades con activos virtuales que
requieren licencia de ASFI, y **las cinco son transaccionales**: intercambio entre criptoactivos
y moneda fiduciaria, intercambio entre criptoactivos, transferencia, custodia o administración,
y emisión.

Analizar información y mostrarla no está en esa lista. Un sistema que lee posiciones, calcula
riesgo y presenta resultados no ejecuta ninguna de las cinco actividades, siempre que no toque
fondos ni custodie claves.

## El límite real está en la asesoría

Aquí es donde el proyecto tiene que ser cuidadoso con la redacción, no con la arquitectura.

El **artículo 19 de la Ley 1834 del Mercado de Valores** reserva a las agencias de bolsa la
asesoría financiera y la administración de inversiones en portafolio. En Bolivia **no existe la
figura del asesor de inversión independiente**: el asesor es un funcionario de una agencia,
inscrito en el registro correspondiente.

El alcance seguro se modela sobre el que la norma fija para los promotores bursátiles: **informar
características y advertir sobre variabilidad de precios, nunca orientar la decisión concreta
sobre un activo**. La diferencia práctica es de verbo. «Este instrumento tuvo una desviación
estándar de X en los últimos doce meses» está adentro. «Deberías comprar este instrumento» está
afuera.

## El antecedente que fija la frontera

ASFI publicó **doce alertas sobre plataformas y empresas de inversión no autorizadas**, contadas
el 1 de septiembre de 2026 abriendo las doce imágenes. Ocho llevan fecha impresa y su rango va del
25 de junio de 2025 a enero de 2026; las otras cuatro salen de plantillas gráficas sin línea de
fecha, así que para fecharlas hay que ir a la publicación original de ASFI.

Cubren **siete plataformas distintas** que ofertaban inversión o captaban dinero a cambio de
rendimientos: QUANTUM AI, MANGA MARKETS, TEAM TRADE, MONTECH SRL, TRADE AI BOLIVIA, la Plataforma
Nacional de Apoyo Socioeconómico y unas ofertas irregulares en Telegram. **Ninguna se limitaba a
informar**, que es exactamente el límite del que este proyecto tiene que diferenciarse. Dos se
hacían pasar por la Gaceta Oficial en Facebook y una usaba el logotipo de ASFI para amedrentar a
sus propios inversores.

Dos precisiones al citarlas. Una sola nombra criptoactivos de forma explícita —TEAM TRADE—; las
demás dicen inversión, trading o captación. Y las dos alertas que declaran video generado con
inteligencia artificial con la cara de autoridades corresponden a **una sola plataforma**
(QUANTUM AI, la alerta original y su reiteración).

## Contexto normativo cripto

La Resolución de Directorio 044/2014 fue abrogada por la RD 144/2020, que prohibía el uso de
criptoactivos. La **RD 082/2024, del 25 de junio de 2024**, dejó sin efecto esa prohibición. El
26 de junio es la fecha del comunicado que la anunció, no la de la resolución: eso se verificó
leyendo la resolución firmada, y la búsqueda web devuelve la fecha equivocada de forma
consistente en varias fuentes secundarias.

---

## La dimensión fiscal: la norma que la sostiene

### Qué dice la RND 102400000021

La Resolución Normativa de Directorio **102400000021, «Respaldo de Transacciones con Documentos
de Pago»**, fue aprobada el 20 de septiembre de 2024 y rige desde el 1 de enero de 2025.

Obliga a respaldar **toda compraventa de bienes o servicios por un monto total igual o superior a
Bs 50.000** —al contado, a crédito o en pagos parciales— con un documento de pago **emitido o
reconocido por una entidad regulada por ASFI o por el Banco Central de Bolivia**: cheque, orden
de transferencia electrónica de fondos, voucher de tarjeta, o carta de crédito.

Su **artículo 5** fija los efectos tributarios de no contar con ese respaldo, y el principal para
el comprador es la **pérdida del crédito fiscal IVA**.

### La corrección que importa

El enunciado que el equipo manejaba decía que sin documento de pago la compra «se presume
inexistente para el fisco». **La norma no dice eso.** Dice que hay consecuencias tributarias, y
la principal es la pérdida del crédito fiscal. Es la diferencia entre citar la norma y citar una
versión más fuerte que la norma, y un tribunal la va a encontrar.

### La pregunta abierta que decide el tamaño del problema

La **Resolución ASFI 540/2025** obligó a los Proveedores de Servicios de Activos Virtuales y a
las plataformas de pago a obtener autorización formal. El plazo venció el **30 de abril de
2026**; más de **176 PSAV y 33 plataformas** entraron al proceso, y los que no cumplieron
quedaron impedidos de operar formalmente.

O sea que desde hace meses **existen PSAV regulados por ASFI**, y la RND acepta documentos
emitidos o reconocidos por entidad regulada por ASFI. De ahí sale la pregunta que decide todo lo
demás:

> **¿El comprobante que emite un PSAV autorizado califica como documento de pago bajo la RND
> 102400000021?**

Se contesta contrastando la enumeración de documentos admitidos de la RND contra lo que un PSAV
autorizado efectivamente emite. Es medio día de trabajo y hay que hacerlo antes de la defensa.

La pregunta sirve en los tres desenlaces posibles:

- **Si no califica**, el problema queda confirmado por norma en su punto más atacable.
- **Si califica**, el enunciado se reformula como problema de transición: quien venía pagando por
  canales entre pares tiene que migrar a un canal que recién existe, y no sabe cuánto crédito
  fiscal dejó en el camino. Es un problema más interesante, no menos.
- **En cualquiera de los dos casos**, el problema no desaparece hacia atrás. Las operaciones
  pagadas en dólares digitales entre 2023 y abril de 2026 ya ocurrieron y su crédito fiscal ya se
  perdió. Es stock, no flujo, y es cuantificable. Un tribunal que diga «eso ya se resolvió» se
  contesta con la ventana temporal.

### Por qué es una dimensión y no el eje

La evaluación del equipo sobre correr el eje entero hacia el importador encontró tres huecos, y
los tres siguen valiendo como razón para tratarlo como dimensión:

**No es, por sí solo, un problema de ciencia de datos.** El crédito fiscal es jurídico-contable.
«Presentar estas operaciones de manera ordenada» no tiene modelo, ni predicción, ni una decisión
que un modelo mejore.

**No hay datos directos.** Quien paga por fuera del canal formal no deja registro público. El
denominador se estima con fuentes públicas —Aduana Nacional, agregados de ASFI y el BCB—, pero la
porción expuesta es una estimación con supuestos, no un dato medido.

**Se perdería la evidencia acumulada.** Las alertas de ASFI, los 2.157 clientes de agencias de
bolsa contra los 7,9 millones de billeteras, los 124.867 participantes de SAFI: todo eso describe
al inversionista minorista.

Tratado como dimensión del riesgo, el hallazgo suma sin costar nada de lo anterior.

---

## Cómo se traduce todo esto al producto

| Norma | Qué prohíbe o exige | Qué implica para el sistema |
|---|---|---|
| DS 5384 (7-may-2025) | Licencia ASFI para cinco actividades transaccionales | El sistema no toca fondos, no custodia, no intercambia, no transfiere |
| Ley 1834, art. 19 | Reserva la asesoría a agencias de bolsa | El sistema informa y advierte; no recomienda instrumentos |
| RND 102400000021 | Documento de pago sobre Bs 50.000, efectos en art. 5 | El sistema estima exposición fiscal; no emite dictamen tributario |
| Res. ASFI 540/2025 | Autorización obligatoria de PSAV, vencida 30-abr-2026 | Define qué canal es «formal» a efectos de la estimación |
| RD 082/2024 (25-jun-2024) | Deja sin efecto la prohibición de la RD 144/2020 | Habilita el objeto mismo del análisis |

Cada pantalla del sistema que muestre riesgo lleva la advertencia de variabilidad de precios, y
ninguna sugiere comprar o vender un instrumento concreto. Es el mismo estándar que la norma le
fija al promotor bursátil, y adoptarlo por escrito es más barato que discutirlo después.
