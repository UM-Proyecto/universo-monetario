# Cómo reproducir lo que hay en este repositorio

El punto de este repositorio es que un lector pueda rehacer por su cuenta todo lo que
afirmamos, sin pedirnos nada y sin credenciales. Este archivo dice cómo, y dice también qué
todavía **no** se puede reproducir, porque una lista de pasos que omite sus huecos es peor que
no tener lista.

---

## Qué necesitás

Python 3.8 o superior y `git`. Nada más por ahora: el script de verificación usa solamente la
biblioteca estándar, así que no hay dependencias que instalar ni versiones que empatar.

```bash
git clone https://github.com/UM-Proyecto/universo-monetario.git
cd universo-monetario
python3 --version     # 3.8 o superior
```

---

## Verificar que las fuentes siguen en pie

Las fuentes del proyecto están declaradas en `fuentes.json`, con lo que aporta cada una y en
qué estado de verificación está. Para comprobarlas:

```bash
python3 scripts/verificar_fuentes.py
```

Salida de la corrida del 10 de septiembre de 2026:

```
8 de 8 fuentes responden.

Control negativo — rutas que deben seguir rotas:
  [OK   ] esperaba 404, obtuvo 404   .../librerias/indicadores/otras/tipocambio.php
  [OK   ] esperaba 404, obtuvo 404   .../index.php/int-fin-estadisticas.html
  [OK   ] esperaba 404, obtuvo 404   .../aduana7/content/estadisticas
```

El script sale con código 1 si alguna fuente declarada deja de responder, así que sirve tal cual
en un cron o en integración continua.

### Por qué tiene un control negativo

Un verificador que solo comprueba lo que espera encontrar pasa la prueba igual estando ciego. Si
la red estuviera caída, si el `User-Agent` fuera rechazado por todos los sitios, o si hubiera un
proxy devolviendo una página de error con código 200, un script que solo mira "¿responde?"
podría informar cualquier cosa sin que nadie lo note.

Por eso el catálogo guarda además tres rutas que **sabemos rotas** y el script exige que sigan
devolviendo 404. Si una de ellas empezara a responder, el aviso no es "mejoró": es que el
catálogo quedó desactualizado y hay que revisarlo.

### Lo que el script no prueba

Prueba que la URL responde. **No** prueba que el archivo que buscás siga ahí, ni que diga lo que
creés que dice.

La distinción no es un tecnicismo. Una página institucional puede responder 200 durante años
mientras el Excel que colgaba de ella cambió de nombre, de ruta o de contenido. Por eso el campo
`estado` de `fuentes.json` se llena **a mano**, cuando alguien baja el archivo y lo abre, y el
script nunca lo modifica.

Hoy todas las fuentes están en `portada-ok`: el sitio responde y nadie bajó todavía el archivo
concreto para dejar anotado qué contenía y con qué fecha de corte. Cerrar esa brecha es la
primera tarea pendiente del proyecto.

### El gotcha que rompe cualquier pipeline a los tres meses

Los enlaces del Boletín Estadístico del BCB llevan la fecha de publicación dentro de la ruta y
cambian cada trimestre. Un pipeline que los fije funciona hoy y falla solo en tres meses, sin
avisar: la descarga devuelve un error o una versión vieja, y el análisis corre con datos
desactualizados sin que nadie lo note.

La ruta vigente hay que resolverla desde la página índice en cada corrida. Los enlaces del INE,
en cambio, son permanentes y se pueden fijar. Las tres rutas del control negativo son ejemplos
reales de este problema: circulaban en material anterior y hoy devuelven 404.

---

## Verificar el contenido del repositorio

Todo lo que afirmamos sobre el repositorio se comprueba con la herramienta oficial de GitHub,
sin permisos especiales, porque el repositorio es público:

```bash
gh api repos/UM-Proyecto/universo-monetario/contents \
    --jq '.[] | "\(.type)\t\(.size)\t\(.name)"'

gh api repos/UM-Proyecto/universo-monetario/contents/docs_ini \
    --jq '.[] | "\(.size)\t\(.name)"'
```

O simplemente abriendo el repositorio en el navegador. Si algún dato de este archivo no coincide
con lo que devuelven esos comandos, el que está equivocado es este archivo.

---

## Cómo se produjo la investigación inicial

Los tres documentos de `docs_ini/` los redactó un agente de inteligencia artificial (Claude Code,
modelo Opus 5) a partir de la base de conocimiento del equipo, y cada uno lo declara en su
encabezado con la fecha.

Eso significa dos cosas para quien los lee. La primera es que el texto es revisable: no hay nada
en esos documentos que no pueda contrastarse contra la fuente citada. La segunda es que **hay que
contrastarlo**, y el propio material explica por qué.

---

## Las advertencias de citación, que son parte de la reproducibilidad

Una ronda de verificación cerrada el 28 de agosto de 2026 obligó a corregir doce afirmaciones del
material del equipo. Cuatro cambiaban el sentido de lo que el documento decía. La lista completa
está al final de `docs_ini/00-investigacion-inicial.md`, y quien reutilice cualquier cifra de este
repositorio debería leerla antes.

Los dos modos de falla que más conviene tener presentes:

**Una cifra correcta con el concepto equivocado al lado.** Cartera confundida con patrimonio,
participantes de un fondo puntual presentados como del total, un agregado calculado por nosotros
atribuido al INE. El número resiste la comprobación; la frase que lo rodea, no.

**Un dato encontrado en el documento correcto que contesta otra pregunta.** Un agente buscó
«73 %» en el informe de vigilancia del sistema de pagos del BCB y lo encontró dos veces, pero era
el 73 % de las órdenes electrónicas que son pagos con QR, nada que ver con las operaciones en
USDT que se estaban citando. El documento era auténtico, del emisor correcto, del área correcta y
sobre el tema correcto, y el número coincidía. Lo único que caza ese error es leer la oración
entera.

De ahí sale la regla de trabajo del proyecto: **ninguna cifra entra al documento sin su fuente,
su fecha de corte y la oración completa de donde salió.**

---

## Qué todavía no es reproducible

Con lo que hay hoy en el repositorio, un lector puede rehacer la verificación de fuentes y leer
el planteamiento con su evidencia. **No** puede rehacer el análisis, porque el análisis no está
escrito todavía.

Cuando lo esté, esta sección tiene que desaparecer y en su lugar va a haber, como mínimo:

- Un `requirements.txt` con las versiones fijadas, no rangos.
- Los scripts de ingesta, con la fecha de corte de cada descarga registrada en el propio archivo
  de salida y no solo en el nombre.
- Una semilla fija en todo lo que tenga aleatoriedad, declarada en el código y no pasada por la
  línea de comandos.
- El corte de entrenamiento y prueba definido por fecha y no por porcentaje, porque son series
  temporales y un corte aleatorio filtra el futuro en el pasado.
- El tratamiento explícito del quiebre estructural del 29 de junio de 2026 en cualquier serie que
  cruce esa fecha.

Mientras eso no exista, decir que el proyecto es reproducible sería falso. Es reproducible la
parte que está hecha, que es la verificación de fuentes y el planteamiento.
