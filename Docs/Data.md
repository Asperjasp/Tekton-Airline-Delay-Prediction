## Estructura de carpetas de datos

Descripción breve de las carpetas principales usadas por el pipeline ETL. Cada carpeta contiene una etapa distinta del flujo de datos y tiene reglas claras sobre modificaciones y uso.


| Carpeta | Contenido (ejemplos) | Propósito en el pipeline ETL |
|---:|:---|:---|
| `01_raw/` | Datos originales sin modificar. Ej.: CSVs descargados desde la fuente (Kaggle, APIs, S3). | Fuente de verdad inmutable — punto de recuperación. Nunca modificar estos archivos en el pipeline. |
| `02_intermediate/` | Datos limpios y normalizados. Ej.: CSV o Parquet con tipos corregidos, nulos tratados, columnas irrelevantes eliminadas y joins parciales. | Primera transformación — salida de los scripts de limpieza (extract/clean). Listos para feature engineering. |
| `03_processed/` | Datos finales listos para modelado o análisis. Ej.: tablas de dimensión y hechos, features creadas, archivos Parquet o tablas en BigQuery. | Transformación final — datasets optimizados para entrenamiento, inferencia o consultas analíticas. |

### Ejemplos de nombres y particionado
- Patrón de particionado por fecha recomendado (S3/BigQuery/Parquet):

  - flights/year=2024/month=01/day=15/flights-20240115.parquet
  - weather/year=2024/month=01/weather-20240115.parquet

- Nombres de archivo sugeridos:

  - raw: `flights_2024-01-15_raw.csv`
  - intermediate: `flights_20240115_clean.parquet`
  - processed: `flights_2024_features_v1.parquet`

### Esquema de ejemplo (tabla `flights`)
| Columna | Tipo | Descripción |
|:---|:---|:---|
| flight_id | string/int | Identificador único del vuelo |
| origin | string | Código IATA del aeropuerto origen |
| destination | string | Código IATA del aeropuerto destino |
| scheduled_departure | timestamp | Hora programada de salida |
| actual_departure | timestamp | Hora real de salida (si está disponible) |
| arrival_delay | float | Retraso en minutos (target para modelado) |

### Recomendaciones
- Formato: usar Parquet para `02_intermediate` y `03_processed` cuando sea posible (mejor compresión y lectura columnar).
- Particionado: particionar por `year/month/day` para operaciones temporales y cargas incrementales.
- Versionado: incluir versión en el nombre del archivo o en el path (ej.: `v1`, `v2`) cuando cambien transformaciones o features.
- Reproducibilidad: jamás sobrescribir `01_raw/`; si se necesita cambiar una fuente, agregar una nueva carpeta con la fecha o versión.

Si quieres, añado un diagrama ASCII del flujo ETL o genero ejemplos reales desde el contenido de `Data/` si hay archivos: dime cuál prefieres.

### Extensiones de los archivos

A continuación se listan las extensiones encontradas en `Data/` con su propósito y relevancia.

| File Extension | Full Name | Purpose | Relevance to Data |
|---|---|---|---|
| `.shp` | Shape Format | Stores the primary geometric data (the shape itself) for the features, such as points (airport locations) or polygons (state borders). | Contains the actual coordinates needed for mapping. |
| `.dbf` | dBase File | Stores the attribute data (non-spatial information) for each feature. This is essentially a database table where each row corresponds to a geometric feature in the `.shp` file. | Will contain attributes like the name of the airport, IATA code, city, state, or region. |
| `.shx` | Shape Index Format | Stores a positional index of the feature geometry to allow for quick forward and backward searching. | Essential for software to efficiently read the geometric data. |


