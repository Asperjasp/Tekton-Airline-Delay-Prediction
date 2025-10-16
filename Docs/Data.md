## Estructura de carpetas de datos

Descripción breve de las carpetas principales usadas por el pipeline ETL. Cada carpeta contiene una etapa distinta del flujo de datos y tiene reglas claras sobre modificaciones y uso.

| Carpeta | Contenido (ejemplos) | Propósito en el pipeline ETL |
|---:|:---|:---|
| `01_raw/` | Datos originales sin modificar. Ej.: CSVs descargados desde la fuente (Kaggle, APIs, S3). | Fuente de verdad inmutable — punto de recuperación. Nunca modificar estos archivos en el pipeline. |
| `02_intermediate/` | Datos limpios y normalizados. Ej.: CSV o Parquet con tipos corregidos, nulos tratados, columnas irrelevantes eliminadas y joins parciales. | Primera transformación — salida de los scripts de limpieza (extract/clean). Listos para feature engineering. |
| `03_processed/` | Datos finales listos para modelado o análisis. Ej.: tablas de dimensión y hechos, features creadas, archivos Parquet o tablas en BigQuery. | Transformación final — datasets optimizados para entrenamiento, inferencia o consultas analíticas. |

### Notas
- Conserva el prefijo numérico para mantener el orden (01_, 02_, 03_).
- Prefiere formatos columnar (Parquet) y compresión para `02_intermediate` y `03_processed` cuando sea posible.
- Para reproducibilidad: si necesitas rehacer transformaciones, re-deriva desde `01_raw/`.

¿Quieres que añada ejemplos de nombres de archivos, esquema de particionado o un diagrama del flujo ETL debajo de esta tabla?
| Carpeta   |            Contenido             |    Propósito ETL |
| ---       | ---                              | --- |
| 01_raw/   | Datos originales descargados. (Ej: Los archivos .csv de Kaggle tal como se descargaron con Kaggle CLI).	| Inmutable. Nunca se modifican. Si el código falla, siempre se puede volver a este punto. |

| 02_intermediate/ |	Datos Limpiados. (Ej: Archivos CSV o Parquet que ya tienen formatos corregidos, valores nulos tratados, columnas irrelevantes eliminadas o datos combinados). |	Transformación I. Es el resultado de aplicar las primeras reglas de limpieza del script extract.py. |
 
| 03_processed/	 | Datos Listos para Modelar. (Ej: Tablas de dimensión y la tabla de hechos final, quizás en formato Parquet, optimizadas para el modelo ML). | 	Transformación II. Es el resultado final de tu script SQL en BigQuery o la tabla lista para tu modelo. Estos son los datos con features creadas.|