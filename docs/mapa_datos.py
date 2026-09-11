# -*- coding: utf-8 -*-
"""Mapa de impacto de Universo Monetario, en la forma que pide la consigna:
4 actores, 4 impactos por actor, 2 tareas por impacto. 32 entregables.

Los cuatro actores son los que pueden acercar o alejar el objetivo. Quedaron fuera
del mapa el tribunal y los docentes -- deciden sobre el trabajo, no sobre el problema --
y los reguladores, cuyo efecto entra por los impactos del contador y del importador."""

GOAL = ("Determinar las herramientas financieras que permiten explicar las variaciones "
        "de la inflación y del tipo de cambio en Bolivia durante la gestión 2026, con el "
        "propósito de generar información que facilite la toma de decisiones financieras.")
GOAL_METRICA = ("Objetivo de Investigación Enfocado del proyecto. Los actores, impactos y entregables de este mapa son los que lo acercan o lo alejan.")

ACTORES = [
    ("ahorrista", "Ahorrista sin formación financiera",
     "Decide entre bolivianos, dólares y banco sin herramientas para comparar.",
     ["Compara opciones en la misma vara y no por costumbre",
      "Ve cuánto le cuesta quedarse en efectivo",
      "Lee el riesgo como cifra y no como adjetivo",
      "Entiende lo que lee sin formación contable"]),
    ("importador", "Importador que paga al exterior",
     "Compra mercadería y paga con dólares digitales porque es el canal al que llega.",
     ["Elige el canal de pago sabiendo qué respaldo le deja",
      "Conoce el sobrecosto real de conseguir dólares digitales",
      "Dimensiona su exposición sobre el umbral de la norma",
      "Cuantifica el crédito fiscal que ya perdió"]),
    ("contador", "Contador de la empresa",
     "Descubre la pérdida de crédito fiscal cuando ya no se puede corregir.",
     ["Detecta antes de declarar qué compras quedan sin respaldo",
      "Entiende qué formas de pago concentran el riesgo",
      "Trabaja con los tres efectos del artículo 5, no sólo el IVA",
      "Ve dónde está el desperdicio del proceso de pago"]),
    ("fuentes", "Proveedores de datos",
     "BCB, INE, ASFI, BBV y Binance. Sin ellos no hay columna que llenar.",
     ["Sus datos entran al sistema sin intervención manual",
      "Sus cambios no rompen el sistema en silencio",
      "Se sabe qué columna del cuadro puede construirse",
      "Las series cruzan el cambio de régimen sin mentir"]),
]

# (actor, impacto, entregable, sp, materia, estado, nota)
E = [
 # ---------- ahorrista ----------
 ("ahorrista",0,"Tablero comparativo: seis opciones en cuatro dimensiones",13,"BI II","pendiente",
  "Es el entregable central de la materia y el que ve el tribunal."),
 ("ahorrista",0,"Normalizar las seis opciones a una unidad común por cada Bs 1.000",5,"BI II","pendiente",
  "Sin unidad común no hay comparación, sólo seis fichas de producto. Los fondos ya traen valor cuota diario."),
 ("ahorrista",1,"Serie de rendimiento real contra el IPC empalmado del INE",8,"BI II","pendiente",
  "Nominal menos inflación. El IPC ya está descargado y abierto."),
 ("ahorrista",1,"Línea base del efectivo en bolivianos como referencia",3,"BI II","pendiente",
  "Es el costo de no hacer nada, y la vara contra la que se miden las otras cinco."),
 ("ahorrista",2,"Volatilidad por opción, con la escala derivada de la cifra",8,"BI II","pendiente",
  "De once productos de la región, ninguno publica desviación estándar."),
 ("ahorrista",2,"Presentación del riesgo: escala visual y monto en bolivianos",5,"BI II","pendiente",
  "La escala se deriva de la cifra, nunca se calculan por separado."),
 ("ahorrista",3,"Lenguaje sin jerga en toda la interfaz",5,"BI II","pendiente",
  "TASK-21 del tablero."),
 ("ahorrista",3,"Validación de comprensibilidad con usuarios reales",8,"BI II","pendiente",
  "TASK-22. El instrumento tiene que poder devolver un resultado que desmienta."),

 # ---------- importador ----------
 ("importador",0,"Columna de respaldo documental con la cita normativa",5,"BI II","parcial",
  "La RND 102400000021 ya está leída y guardada en el repositorio."),
 ("importador",0,"Semáforo de admisibilidad del documento por canal de pago",5,"BI II","pendiente",
  "Traduce la enumeración del artículo 3 a una respuesta por canal."),
 ("importador",1,"Captura horaria del libro P2P completo, una fila por anuncio",5,"—","hecho",
  "Corregida el 11-sep: antes tomaba 20 de ~180 y sesgaba la mediana 2,3 %."),
 ("importador",1,"Brecha del precio P2P contra el tipo de cambio oficial, por hora",5,"BI II","hecho",
  "Sale de resumen.csv; la serie corre desde el 9 de septiembre."),
 ("importador",2,"Conteo de anuncios y volumen por tramo contra el umbral de Bs 50.000",3,"Minería","hecho",
  "Medido el 11-sep: 53 de 178 anuncios de compra operan sobre el umbral."),
 ("importador",2,"Estimación del volumen importado expuesto, con supuestos escritos",8,"BI II","pendiente",
  "TASK-38. Necesita las estadísticas de la Aduana Nacional."),
 ("importador",3,"Estimador de crédito fiscal en riesgo por operación y período",8,"Minería","pendiente",
  "El artículo 5 tiene tres efectos: IVA, IUE y RC-IVA."),
 ("importador",3,"Serie del stock acumulado entre 2023 y abril de 2026",5,"BI II","pendiente",
  "Es stock, no flujo: ya ocurrió y no cambia con lo que decida el regulador."),

 # ---------- contador ----------
 ("contador",0,"Detección de anomalías sobre operaciones fuera del patrón documental",13,"Minería","pendiente",
  "Aporte natural de Minería de Datos y no necesita etiquetas."),
 ("contador",0,"Alerta por operación sobre el umbral sin documento admitido",5,"Minería","pendiente",
  "Antes de la declaración, que es cuando todavía se puede corregir."),
 ("contador",1,"Reglas de asociación: método de pago × tramo × tipo de contraparte",8,"Minería","pendiente",
  "Los métodos se concentran en seis bancos, así que las reglas tienen soporte."),
 ("contador",1,"Segmentación no supervisada del panel de anunciantes: K-means y PCA",13,"IA y ML II","pendiente",
  "No supervisado, que es lo que la materia pide y lo que el dato admite."),
 ("contador",2,"Cálculo separado de IVA, IUE y RC-IVA por operación",8,"BI II","pendiente",
  "El enunciado del equipo sólo mencionaba el crédito fiscal; el costo es mayor."),
 ("contador",2,"Verificar si el comprobante de un proveedor autorizado califica",5,"—","en curso",
  "TASK-36. Decide si el problema sigue abierto en presente."),
 ("contador",3,"Simulación de eventos discretos del flujo de compra y sus ramas",13,"Optimización III","pendiente",
  "Los parámetros salen del libro: tiempos de pago, disponibilidad, montos."),
 ("contador",3,"Lectura Lean: cuello de botella aparente contra causal",5,"Dir. Operaciones","pendiente",
  "El cuello de botella parece el pago; el causal es la documentación."),

 # ---------- proveedores de datos ----------
 ("fuentes",0,"Ingesta automática de las fuentes ya verificadas",8,"BI II","pendiente",
  "Las seis columnas tienen su fuente descargada y abierta."),
 ("fuentes",0,"Catálogo de fuentes con evidencia de descarga y fecha de corte",3,"—","parcial",
  "Verificar es abrir el archivo, no comprobar que la página responda."),
 ("fuentes",1,"Caché en base de datos para operar sin red",8,"—","pendiente",
  "TASK-3. La BBV bloquea por IP ante pedidos concurrentes: la demo no puede depender de ella."),
 ("fuentes",1,"Resolver la fecha del Boletín del BCB en cada corrida",3,"—","pendiente",
  "Los enlaces llevan la fecha adentro y cambian cada trimestre, sin avisar."),
 ("fuentes",2,"Relevar qué publica cada fuente formal, y con qué profundidad",5,"—","hecho",
  "Cerrada el 11-sep: las tres columnas formales tienen fuente gratis y descargada."),
 ("fuentes",2,"Decidir en qué dos columnas va la profundidad",3,"—","pendiente",
  "Ninguna queda fuera por datos: las seis tienen fuente. Es decisión de alcance."),
 ("fuentes",3,"Manejo declarado del quiebre estructural del 29 de junio de 2026",5,"BI II","pendiente",
  "TASK-15. Los datos previos describen un régimen cambiario que ya no rige."),
 ("fuentes",3,"Conversión a bolivianos con opción de dólar y su fecha de corte",5,"BI II","pendiente",
  "TASK-16. Una cifra en dólares sin su tipo de cambio envejece en una semana."),
]
