# Universo Monetario

Sistema de análisis que consolida y presenta de manera ordenada las operaciones de pago con
dólares digitales de importadores bolivianos, y estima qué crédito fiscal queda en riesgo cuando
esos pagos no cuentan con un documento de respaldo válido bajo la normativa tributaria vigente.

Proyecto Integrador del sexto semestre de Ingeniería en Ciencia de Datos, Universidad Privada del
Valle — Santa Cruz de la Sierra. El repositorio también sostiene los entregables de Business
Intelligence II, materia en la que el proyecto se desarrolla.

## Equipo

- Sabrina Adrián Zelaya
- Fiorella Michelle Sandoval Castro
- Samuel Roberto Castillo Cornejo
- Carlos Andrés Méndez Cadario

## Cómo está organizado

El repositorio sigue la misma estructura que el de Minería de Datos, que es la convención estándar
para proyectos de ciencia de datos: los datos originales separados de los procesados, el código
reutilizable aparte de los cuadernos, y las salidas en su propia carpeta.

| Ruta | Propósito |
| --- | --- |
| `data/raw/` | Datos originales tal como se descargaron; no se modifican nunca. |
| `data/processed/` | Datos generados por limpieza o transformación. |
| `notebooks/` | Cuadernos de análisis, ordenados y numerados. |
| `src/` | Código Python reutilizable. |
| `reports/` | Entregables: el mapa de impacto, el árbol de problemas y el veredicto sobre el rumbo. |
| `reports/figures/` | Figuras y resultados gráficos generados. |
| `docs/` | Documentación del proyecto: planteamiento, reproducibilidad e investigación inicial. |
| `fuentes.json` | Catálogo de fuentes con lo que aporta cada una y su estado de verificación. |
| `environment.yml` | Entorno Conda del proyecto. |

### Qué hay en cada archivo

| Archivo | Contenido |
| --- | --- |
| `docs/PROYECTO.md` | Planteamiento, problema específico, objetivos, alcance y datos previstos. |
| `docs/PLANTEAMIENTO.md` | Desarrollo extendido del planteamiento. |
| `docs/REPRODUCIBILIDAD.md` | Cómo rehacer por tu cuenta lo que afirmamos, y qué todavía no se puede rehacer. |
| `docs/investigacion-inicial/` | Evidencia del problema, marco normativo y catálogo de fuentes de datos. |
| `reports/mapa-impacto.md` | Mapa de impacto en texto: objetivo, cuatro actores, dieciséis impactos y treinta y dos entregables. |
| `reports/mapa-impacto.pdf` | El mismo mapa como diagrama, en una hoja para imprimir o proyectar. |
| `reports/mapa-impacto.html` | La versión navegable del diagrama, con filtros por rama. |
| `reports/arbol-problemas.html` | Árbol de problemas: causas, problema central y efectos. |
| `reports/veredicto-rumbo.pdf` | Veredicto sobre qué eje debe seguir el proyecto, con la evidencia que lo sostiene. |
| `src/mapa_datos.py` | Fuente única de los datos del mapa de impacto. |
| `src/verificar_fuentes.py` | Comprueba que las fuentes declaradas siguen en pie, con control negativo. |

## Comprobalo vos

```bash
git clone https://github.com/UM-Proyecto/universo-monetario.git
cd universo-monetario
python3 src/verificar_fuentes.py
```

Sin dependencias que instalar: solo la biblioteca estándar de Python 3.8 o superior. Los detalles
y los límites de esa comprobación están en `REPRODUCIBILIDAD.md`.

## Estado

En fase de investigación inicial y definición de alcance. El avance operativo se lleva en el
tablero del proyecto; este repositorio guarda los documentos y, más adelante, el código.

## Lo que hay que contestar antes de la defensa

Si el comprobante que emite un proveedor de servicios de activos virtuales autorizado por ASFI
califica como documento de pago bajo la RND 102400000021. La respuesta cambia el tamaño del
problema en presente, aunque no toca el stock acumulado entre 2023 y abril de 2026. Está
desarrollado en `docs/investigacion-inicial/01-marco-normativo.md`.

## Advertencia sobre las cifras

Los documentos de `docs/investigacion-inicial/` citan datos macroeconómicos bolivianos de 2025 y 2026 que envejecen
rápido, en particular los que dependen del tipo de cambio: el régimen cambiario cambió el 29 de
junio de 2026 y cualquier conversión a dólares hecha antes da un resultado distinto hoy. Cada
cifra va con su fecha de corte y su fuente. Antes de reutilizarlas en el documento final conviene
volver a la fuente: una parte de este material ya pasó por una ronda donde doce afirmaciones
resultaron mal citadas, y las advertencias que salieron de ahí están al final de
`docs/investigacion-inicial/00-investigacion-inicial.md`.
