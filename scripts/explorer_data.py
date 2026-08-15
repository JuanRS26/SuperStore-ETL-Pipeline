import pandas as pd

# Se exportan los datos
df = pd.read_csv('data/raw/samplesuperstore.csv')


def exploration():
    """
    SuperStore - Data Exploration

    Objetivo:
        Explorar el conjunto de datos brutos de SuperStore y comprender su estructura,
        identificadores, relaciones y posibles problemas de calidad de datos.

    Este archivo contiene código exploratorio.
    NO forma parte del proceso ETL de producción.
    """


    # ============================================================
    # 1. DATASET OVERVIEW
    # ============================================================

    print("\n\t---------- 1. DATASET OVERVIEW ----------\n")
    ''' 
    Dudas:
    - Que hay en el dataset?

    Metodo:
    - Abrir el dataset y observar las columnas, tipos de datos y cantidad de registros.

    Resultados:
    - Miramos que contiene el dataset y que tipos de datos hay en cada columna.
    '''

    print("\n---------- 1.1 INFORMACION DEL DATASET ----------\n")
    print(df.info())

    '''
    Conclusion:
    - Hay 21 columnas, de las cuales 16 son strings, 3 son floats y 2 numericas enteras.
    - Hay un total de 10.194 registros, de los cuales 10.194 son no nulos.

    Accion:
    - No se requiere ninguna accion adicional, ya que es un proceso exploratorio.
    '''


    # ============================================================
    # 2. ROW ID ANALYSIS
    # ============================================================

    print("\n\n\t---------- 2. ROW ID ANALYSIS ----------\n")
    ''' 
    Dudas:
    - cuantos Registros unicos hay en la columna Row ID?

    Metodo:
    - Se realizara un conteo de los valores unicos para Row ID.

    Resultados:
    - Usamos el metodo nunique() para contar los valores unicos en la columna Row ID.
    '''

    print("\n---------- 2.1 VALORES UNICOS ----------\n")
    print(f"Hay {df['Row ID'].nunique()} registros unicos en la columna Row ID.")

    '''
    Conclusion:
    - Hay 10.194 registros unicos en la columna Row ID, lo que indica que cada registro tiene un identificador unico.

    Accion:
    - No se requiere ninguna accion adicional, ya que es un proceso exploratorio.
    '''


    # ============================================================
    # 3. ORDER ID ANALYSIS
    # ============================================================

    print("\n\n\t---------- 3. ORDER ID ANALYSIS ----------\n")
    ''' 
    Dudas:
    - Cuantos Registros unicos hay en la columna Order ID?
    - Cuantas veces se repite un mismo registro en la columna Order ID?

    Metodo:
    - Se realizara un conteo de los valores unicos para Order ID.
    - Se Realizara unn conteo de la cantidad de veces que se repite un mismo registro en la columna Order ID.

    Resultados:
    - Usamos el metodo nunique() para contar los valores unicos.
    - Usamos el metodo value_counts() para contar la cantidad de veces que se repite un mismo registro.
    '''

    print("\n---------- 3.1 VALORES UNICOS ----------\n")
    print(F"Hay {df['Order ID'].nunique()} registros unicos en la columna Order ID.")
    print("\n---------- 3.2 CANTIDAD DE VECES QUE APARECE UN MISMO REGISTRO ----------\n")
    print(df['Order ID'].value_counts())

    '''
    Conclusion:
    - Hay 5111 registros unicos en la columna Order ID, lo que indica que hay varios registros que se repiten 1 o mas veces
      siendo US-2026-100111 el registro con mayor veces s erepite, 14 veces.

    Accion:
    - No se requiere ninguna accion adicional, ya que es un proceso exploratorio.
    '''


    # ============================================================
    # 4. DUPLICATE RECORD ANALYSIS
    # ============================================================

    print("\n\n\t---------- 4. DUPLICATE RECORD ANALYSIS ----------\n")
    ''' 
    Dudas:
    - Cuantos resgistros totalmente duplicados hay en el dataset?

    Metodo:
    - Se compararan todos los registros para saber si hay rigistros duplicados omitiendo la columna Row ID.

    Resultados:
    - Se realizo la consulta para registros duplicados omitiendo la columna Row ID.
    '''

    print("\n---------- 4.1 REGISTROS DUPLICADOS ----------\n")
    print(df[df.duplicated(subset=df.columns.difference(['Row ID']), keep=False)])

    '''
    Conclusion:
    - Se encontraros 2 pares de registros duplicados los cuales tienen como Row ID (391, 392) y (1699, 1700).

    Accion:
    - No se requiere ninguna accion adicional, ya que es un proceso exploratorio.
    '''


    # ============================================================
    # 5. EXPLORATION CONCLUSIONS
    # ============================================================

    # Summarize the discoveries made during this exploration.
    #
    # Example:
    #
    # - Row ID appears to uniquely identify each dataset record.
    # - Order ID can appear in multiple records.
    # - Therefore, one Order ID can contain multiple records.
    # - Duplicate-looking records require further investigation
    #   before deciding whether they should be removed.