import numpy as np
import pandas as pd
import logging

from pathlib import Path # working with paths OS independantly, because in linus is / and wundows has the \ s direseparat
# Trata los strings the paths como Objetos y permite manipularlos mucho mas facilmente


# Develop the file to read the data
# That is in Data/01_raw

# Read and clean the data

# Configurar el logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    )

# Definir las rutas principales

#remember : __file__ contains the path 

# resolve() convierte la ruta absoluta (__file__) en una ruta absoluta y canónica (limpia y normalizada), sin paths relativos .. o enlaces simbolicos

# three parents : data -> src -> terken

ROOT_DIR = Path(__file__).resolve().parent.parent.parent
DATA_DIR = ROOT_DIR / "Data"
RAW_DATA_DIR = DATA_DIR / "01_raw"
INTERMEDIATE_DATA_DIR = DATA_DIR / "02_intermediate"
PROCESSED_DATA_DIR = DATA_DIR / "03_processed"


logger = logging.getLogger(__name__)

def perform_initial_cleanup(df : pd.DataFrame )  -> pd.DataFrame:
    """
    Aplica las reglas de limpieza inicial: manejo de nulos y corrección de tipos.
    (Estas reglas se definieron en el notebook de exploración).
    """
    
    logging.info("Iniciando limpieza inicial...")
    
    # Ejemplo de limpieza 1: Corrección de tipos de dato
    df['FlightDate'] = pd.to_datetime(df['FlightDate'])
    
    # Ejemplo de limpieza 2: Manejo de valores nulos clave
    # Eliminamos las filas donde no tenemos información esencial para la predicción
    df.dropna(subset=['DepDelay', 'ArrDelay', 'UniqueCarrier', 'Origin'], inplace=True)
    
    # Ejemplo de limpieza 3: Eliminación de columnas redundantes o con nulos excesivos
    # Aquí puedes eliminar la columna 'Unnamed: 0' si existe
    if 'Unnamed: 0' in df.columns:
        df.drop(columns=['Unnamed: 0'], inplace=True)
        
    logging.info(f"Limpieza completada. Filas restantes: {len(df)}")
    return df

def extract_and_clean_flights():
    """
    Función principal de extracción y carga a la capa intermedia.
    """
    try:
        logging.info(f"Leyendo datos RAW desde: {RAW_DATA_DIR}")
        # Leer el archivo CSV raw, asumiendo que el separador es la coma
        df = pd.read_csv(RAW_DATA_DIR, low_memory=False)

        # Limpiar el DataFrame
        df_clean = perform_initial_cleanup(df)

        # Crear la carpeta intermedia si no existe
        INTERMEDIATE_DATA_DIR.parent.mkdir(parents=True, exist_ok=True)
        
        # Guardar en un formato eficiente como Parquet (mejor que CSV)
        logging.info(f"Guardando datos intermedios en: {INTERMEDIATE_DATA_DIR}")
        df_clean.to_parquet(INTERMEDIATE_DATA_DIR, index=False)
        
        logging.info("✅ Extracción y limpieza inicial completadas con éxito.")
        
    except FileNotFoundError:
        logging.error(f"❌ Error: Archivo CSV no encontrado en {RAW_DATA_DIR}. Asegúrate de haber ejecutado el Kaggle CLI.")
    except Exception as e:
        logging.error(f"❌ Ocurrió un error en el ETL inicial: {e}")

if __name__ == '__main__':
    extract_and_clean_flights()

def main():
    print("Hello world")


if __name__ == "__name__":
    main()