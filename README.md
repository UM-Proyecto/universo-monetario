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

| Ruta | Contenido |
|---|---|
| `PROYECTO.md` | Planteamiento, problema específico, objetivos, alcance y datos previstos. Es el documento de referencia. |
| `REPRODUCIBILIDAD.md` | Cómo rehacer por tu cuenta todo lo que afirmamos, y qué todavía no se puede rehacer. |
| `fuentes.json` | Catálogo de fuentes con lo que aporta cada una y su estado de verificación. |
| `scripts/verificar_fuentes.py` | Comprueba que las fuentes declaradas siguen en pie, con control negativo. |
| `docs_ini/` | Investigación inicial asistida por agente de IA: evidencia del problema, marco normativo y catálogo de fuentes de datos. |
| `docs/mapa-impacto.md` | Mapa de impacto en texto: objetivo, cuatro actores, dieciséis impactos y treinta y dos entregables con sus puntos de historia y su estado. |
| `docs/mapa-impacto.pdf` | El mismo mapa como diagrama, en una hoja para imprimir o proyectar. |
| `docs/mapa-impacto.html` | La versión navegable del diagrama, con filtros por rama. |
| `docs/mapa_datos.py` | Fuente única de los datos del mapa. El `.md`, el `.html` y el PDF salen de acá. |
| `docs/arbol-problemas-universo-monetario.html` | Árbol de problemas: causas, problema central y efectos. |

## Comprobalo vos

```bash
git clone https://github.com/UM-Proyecto/universo-monetario.git
cd universo-monetario
python3 scripts/verificar_fuentes.py
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
desarrollado en `docs_ini/01-marco-normativo.md`.

## Advertencia sobre las cifras

Los documentos de `docs_ini/` citan datos macroeconómicos bolivianos de 2025 y 2026 que envejecen
rápido, en particular los que dependen del tipo de cambio: el régimen cambiario cambió el 29 de
junio de 2026 y cualquier conversión a dólares hecha antes da un resultado distinto hoy. Cada
cifra va con su fecha de corte y su fuente. Antes de reutilizarlas en el documento final conviene
volver a la fuente: una parte de este material ya pasó por una ronda donde doce afirmaciones
resultaron mal citadas, y las advertencias que salieron de ahí están al final de
`docs_ini/00-investigacion-inicial.md`.
