def exploration(df):
    """
    SuperStore - Data Exploration

    Objetivo:
        Explorar el conjunto de datos brutos de SuperStore y comprender su estructura,
        identificadores, relaciones y posibles problemas de calidad de datos.

    Esta funcion contiene código exploratorio.
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
    df.info()

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
    - Hay 5111 valores unicos en la columna Order ID, lo que indica que hay varios registros que se repiten 1 o mas veces
      siendo US-2026-100111 el valor que aparece 14 veces.

    Accion:
    - No se requiere ninguna accion adicional, ya que es un proceso exploratorio.
    '''


    # ============================================================
    # 4. DUPLICATE RECORD ANALYSIS
    # ============================================================

    print("\n\n\t---------- 4. DUPLICATE RECORD ANALYSIS ----------\n")
    ''' 
    Dudas:
    - Existen registros duplicados ignorando Row ID?

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
    # 5. CUSTOMER - ORDER RELATIONSHIP ANALYSIS
    # ============================================================

    print("\n\n\t---------- 5. CUSTOMER - ORDER RELATIONSHIP ANALYSIS ----------\n")
    '''
    Pregunta:
    - ¿Un mismo Customer ID puede estar asociado a múltiples Order ID?
    - ¿Un mismo Order ID puede estar asociado a múltiples Customer ID?

    Método:
    - Se analizará la frecuencia de aparición de cada Customer ID
      para comprobar si un cliente puede realizar múltiples pedidos.
    - Posteriormente, se agruparán los registros por Order ID y se
      contará cuántos Customer ID diferentes están asociados a cada pedido.

    Resultado:
    - Se observó que varios Customer ID aparecen múltiples veces
      en el dataset.
    - Esto demuestra que un cliente puede estar asociado a múltiples
      registros y, por tanto, a múltiples pedidos.
    - También se identificaron dos Order ID asociados a más de un
      Customer ID.
    '''

    print("\n---------- 5.1 FRECUENCIA DE CUSTOMER ID ----------\n")
    print(df['Customer ID'].value_counts())

    print("\n---------- 5.2 ORDER ID ASOCIADOS A MULTIPLES CUSTOMER ID ----------\n")

    inconsistencias = (
        df.groupby("Order ID")["Customer ID"]
          .nunique()
          .loc[lambda x: x > 1]
    )

    print(inconsistencias)

    '''
    Conclusión:
    - Un Customer ID puede aparecer en múltiples registros y puede
      estar asociado a múltiples Order ID.
    - Por lo tanto, la relación entre Customer ID y Order ID es 1:N.
    - Se identificaron dos Order ID que están asociados a más de un
      Customer ID:
        * CA-2025-121465
        * CA-2026-130494
    - Ambos Order ID presentan cuatro Customer ID diferentes.
    - Al analizar los registros involucrados, se observó que los cuatro
      Customer ID corresponden al mismo Customer Name: Harry Olson.
    - Esto representa una inconsistencia en la identificación del cliente,
      ya que un mismo pedido aparece asociado a múltiples Customer ID.

    Siguiente paso:
    - Investigar si los diferentes Customer ID corresponden realmente
      a clientes distintos o si representan registros duplicados,
      errores de identificación o alguna característica particular
      del dataset.
    - No se debe modificar ni eliminar estos registros hasta comprender
      la causa de la inconsistencia.
    '''


    # ============================================================
    # 6. CUSTOMER - PRODUCT RELATIONSHIP ANALYSIS
    # ============================================================

    print("\n\n\t---------- 6. CUSTOMER - PRODUCT RELATIONSHIP ANALYSIS ----------\n")
    '''
    Pregunta:
    - ¿Qué relación existe entre Customer ID y Product ID?

    Método:
    - Se analizará la cantidad de productos asociados a los clientes
      y la cantidad de clientes asociados a los productos.

    Resultado:
    - Se observó que un cliente puede adquirir múltiples productos.
    - También se observó que un mismo producto puede estar asociado
      a múltiples clientes.
    - Por lo tanto, existe una relación N:M entre Customer ID y Product ID.
    '''

    '''
    Conclusión:
    - La relación entre Customer ID y Product ID es N:M.
    - Un cliente puede comprar múltiples productos.
    - Un producto puede ser comprado por múltiples clientes.

    Siguiente paso:
    - Esta relación deberá considerarse posteriormente al diseñar
      el modelo de datos para MySQL.
    '''


    # ============================================================
    # 7. ORDER - PRODUCT RELATIONSHIP ANALYSIS
    # ============================================================

    print("\n\n\t---------- 7. ORDER - PRODUCT RELATIONSHIP ANALYSIS ----------\n")

    '''
    Pregunta:
    - ¿Qué relación existe entre Order ID y Product ID?
    - ¿Un mismo Product ID puede aparecer en múltiples Order ID?
    - ¿Un mismo Order ID puede contener múltiples Product ID?

    Método:
    - Se analizará la frecuencia de aparición de los Product ID
      dentro de los diferentes Order ID.
    - Se comprobará si un mismo producto puede formar parte de
      múltiples pedidos y si un mismo pedido puede contener
      múltiples productos.

    Resultado:
    - Se observó que un mismo Product ID puede aparecer en múltiples
      Order ID.
    - También se observó que un mismo Order ID puede contener
      múltiples Product ID.
    - Por lo tanto, la relación entre Order ID y Product ID es N:M.
    '''

    print("\n---------- 7.1 PRODUCTOS REPETIDOS DENTRO DEL MISMO PEDIDO ----------\n")

    print(df[['Order ID', 'Product ID']].value_counts())

    '''
    Pregunta:
    - ¿Puede un mismo Product ID aparecer más de una vez dentro
      del mismo Order ID?

    Método:
    - Se analizará la frecuencia de las combinaciones Order ID +
      Product ID.
    - Se investigarán las combinaciones que aparecen más de una vez
      para determinar si se trata de registros duplicados o de
      registros diferentes pertenecientes al mismo pedido.

    Resultado:
    - Se identificaron múltiples combinaciones de Order ID + Product ID
      que aparecen más de una vez.
    - Al analizar los registros involucrados, se observó que las
      columnas Quantity, Sales y Profit pueden presentar valores
      diferentes.
    - Las demás características asociadas al pedido y al producto
      permanecen iguales.
    - No se encontraron anomalías en el precio unitario del producto.
    - Las diferencias observadas en Sales son coherentes con las
      diferentes cantidades registradas para el mismo producto.
    '''

    '''
    Conclusión:
    - Un mismo Product ID puede aparecer múltiples veces dentro de
      un mismo Order ID.
    - Estas apariciones no deben considerarse automáticamente como
      registros duplicados, ya que pueden representar diferentes
      cantidades del mismo producto.
    - La combinación Order ID + Product ID no es suficiente para
      identificar de forma única un registro del dataset.
    - El análisis de Quantity, Sales y Profit no mostró anomalías
      relacionadas con el precio unitario del producto.
    - Las diferencias observadas en Sales son coherentes con las
      cantidades registradas.
    - Esto indica que los registros representan diferentes movimientos
      o líneas asociadas al mismo producto dentro de un pedido.

    Siguiente paso:
    - Investigar qué elemento o combinación de atributos permite
      diferenciar de forma única cada registro.
    - Determinar con mayor precisión la granularidad del dataset.
    - Utilizar esta información posteriormente para diseñar el
      modelo de datos y determinar cómo representar los detalles
      de cada pedido en MySQL.
    '''


    # ============================================================
    # 7.2 RELACIÓN ENTRE ORDER ID Y PRODUCT ID
    # ============================================================

    print("\n---------- 7.2 CARDINALIDAD ORDER ID - PRODUCT ID ----------\n")

    '''
    Pregunta:
    - ¿Qué cardinalidad existe entre Order ID y Product ID?

    Método:
    - Se analizará la relación existente entre pedidos y productos
      observando cuántos productos pueden pertenecer a un pedido
      y en cuántos pedidos puede aparecer un mismo producto.

    Resultado:
    - Un Order ID puede estar asociado a múltiples Product ID.
    - Un Product ID puede estar asociado a múltiples Order ID.
    '''

    '''
    Conclusión:
    - La relación entre Order ID y Product ID es N:M.
    - Un pedido puede contener múltiples productos.
    - Un producto puede aparecer en múltiples pedidos.

    Siguiente paso:
    - La relación N:M deberá ser considerada posteriormente durante
      el diseño del modelo relacional de MySQL.
    - Será necesario determinar qué entidad intermedia representa
      los detalles de cada pedido.
    '''


    # ============================================================
    # 7.3 GRANULARIDAD DEL DATASET
    # ============================================================

    print("\n---------- 7.3 GRANULARIDAD DEL DATASET ----------\n")

    '''
    Pregunta:
    - ¿Qué representa cada registro del dataset?

    Método:
    - Se analizaron las relaciones entre Order ID, Product ID,
      Quantity, Sales, Discount y Profit.
    - También se investigó si la combinación Order ID + Product ID
      identifica de forma única cada registro.

    Resultado:
    - Un mismo Order ID puede contener múltiples registros.
    - Un mismo Order ID puede contener múltiples Product ID.
    - Un mismo Product ID puede aparecer en múltiples Order ID.
    - Un mismo Product ID puede aparecer más de una vez dentro
      del mismo Order ID.
    - Cuando esto ocurre, las cantidades pueden ser diferentes,
      mientras que el precio unitario se mantiene consistente.
    - La combinación Order ID + Product ID no identifica de forma
      única cada registro.
    '''

    '''
    Conclusión:
    - La información analizada indica que cada registro representa
      un detalle individual asociado a un pedido y a un producto.
    - Las columnas Quantity, Sales, Discount y Profit contienen
      información relacionada con el comportamiento comercial
      de dicho detalle.
    - La granularidad del dataset se encuentra a nivel de detalle
      de pedido, no a nivel de pedido completo.
    - Por lo tanto, un Order ID puede estar representado por
      múltiples registros dentro del dataset.

    Siguiente paso:
    - Investigar qué columna o combinación de columnas puede actuar
      como identificador del detalle de cada pedido.
    - Esta información será necesaria para definir correctamente
      las claves y relaciones del futuro modelo de datos en MySQL.
    '''
    

    # ============================================================
    # 8. DATA DISCOVERY FINDINGS
    # ============================================================

    '''
    Resumen de los principales descubrimientos realizados hasta ahora:

    1. Row ID
       - Presenta un valor único por cada registro del dataset.

    2. Order ID
       - Un mismo Order ID puede aparecer en múltiples registros.
       - La frecuencia máxima observada es de 14 registros para un
         mismo Order ID.

    3. Duplicate Records
       - Se identificaron dos pares de registros idénticos ignorando
         la columna Row ID.
       - Los pares corresponden a los Row ID:
         * 391 y 392
         * 1699 y 1700
       - Todavía no se ha determinado si estos registros deben ser
         eliminados, ya que primero es necesario comprender su contexto.

    4. Customer ID
       - Un mismo Customer ID puede aparecer en múltiples registros
         y estar asociado a múltiples Order ID.
       - La relación observada entre Customer ID y Order ID es 1:N.

    5. Customer ID / Order ID inconsistency
       - Se identificaron dos Order ID asociados a múltiples Customer ID:
         * CA-2025-121465
         * CA-2026-130494
       - Los cuatro Customer ID involucrados en cada pedido pertenecen
         al mismo Customer Name: Harry Olson.
       - Se considera una inconsistencia que requiere investigación
         antes de realizar cualquier transformación.

    6. Customer ID / Product ID
       - La relación observada es N:M.
       - Un cliente puede adquirir múltiples productos y un producto
         puede ser adquirido por múltiples clientes.

    7. Order ID / Product ID

       - Existe una relación N:M entre Order ID y Product ID.
       - Un pedido puede contener múltiples productos.
       - Un producto puede aparecer en múltiples pedidos.
       - Un mismo producto puede aparecer más de una vez dentro del
         mismo pedido.
       - La combinación Order ID + Product ID no es suficiente para
         identificar de forma única un registro.
       - Las repeticiones de un mismo producto dentro de un pedido
         pueden presentar diferentes cantidades.
       - Las diferencias observadas en Sales y Profit son coherentes
         con las diferentes cantidades registradas.
       - No se identificaron anomalías en el precio unitario del
         producto durante esta investigación.
       - La información analizada apunta a que la granularidad del
         dataset corresponde al detalle individual de un pedido.

    8. Granularidad
       - La investigación apunta a que un registro representa una
         unidad individual dentro de un pedido.
       - Esta hipótesis todavía debe validarse analizando la relación
         entre Order ID y Product ID.
    '''