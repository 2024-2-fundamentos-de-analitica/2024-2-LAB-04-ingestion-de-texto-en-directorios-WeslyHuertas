# pylint: disable=import-outside-toplevel
# pylint: disable=line-too-long
# flake8: noqa
"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""
import pandas as pd

def pregunta_01():
    """
    La información requerida para este laboratio esta almacenada en el
    archivo "files/input.zip" ubicado en la carpeta raíz.
    Descomprima este archivo.

    Como resultado se creara la carpeta "input" en la raiz del
    repositorio, la cual contiene la siguiente estructura de archivos:


    ```
    train/
        negative/
            0000.txt
            0001.txt
            ...
        positive/
            0000.txt
            0001.txt
            ...
        neutral/
            0000.txt
            0001.txt
            ...
    test/
        negative/
            0000.txt
            0001.txt
            ...
        positive/
            0000.txt
            0001.txt
            ...
        neutral/
            0000.txt
            0001.txt
            ...
    ```

    A partir de esta informacion escriba el código que permita generar
    dos archivos llamados "train_dataset.csv" y "test_dataset.csv". Estos
    archivos deben estar ubicados en la carpeta "output" ubicada en la raiz
    del repositorio.

    Estos archivos deben tener la siguiente estructura:

    * phrase: Texto de la frase. hay una frase por cada archivo de texto.
    * sentiment: Sentimiento de la frase. Puede ser "positive", "negative"
      o "neutral". Este corresponde al nombre del directorio donde se
      encuentra ubicado el archivo.

    Cada archivo tendria una estructura similar a la siguiente:

    ```
    |    | phrase                                                                                                                                                                 | target   |
    |---:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
    |  0 | Cardona slowed her vehicle , turned around and returned to the intersection , where she called 911                                                                     | neutral  |
    |  1 | Market data and analytics are derived from primary and secondary research                                                                                              | neutral  |
    |  2 | Exel is headquartered in Mantyharju in Finland                                                                                                                         | neutral  |
    |  3 | Both operating profit and net sales for the three-month period increased , respectively from EUR16 .0 m and EUR139m , as compared to the corresponding quarter in 2006 | positive |
    |  4 | Tampere Science Parks is a Finnish company that owns , leases and builds office properties and it specialises in facilities for technology-oriented businesses         | neutral  |
    ```


    """

    with open("files/input/clusters_report.txt", "r", encoding="utf-8") as archivo:
        contenido = archivo.readlines()

    inicio_datos = 4  # Índice donde comienzan los datos
    lineas_datos = contenido[inicio_datos:]

    lista_filas = []
    fila_temp = []

    for linea in lineas_datos:
        if linea.strip():  # Si la línea no está vacía, la añadimos a la fila temporal
            fila_temp.append(linea.strip())
        else:
            if fila_temp:  # Cuando encontramos una línea vacía, consolidamos la fila y la almacenamos
                lista_filas.append(" ".join(fila_temp))
                fila_temp = []

    datos_procesados = []
    for fila in lista_filas:
        elementos = fila.split()
        id_cluster = int(elementos[0])
        total_palabras = int(elementos[1])
        porcentaje_palabras = float(elementos[2].replace(",", "."))
        palabras_clave = (
            " ".join(elementos[3:])
            .replace(" ,", ",")
            .replace(", ", ", ")
            .strip("%")
            .rstrip(".")
            .strip()
        )
        datos_procesados.append([id_cluster, total_palabras, porcentaje_palabras, palabras_clave])

    df_resultado = pd.DataFrame(datos_procesados, columns=[
        "cluster", "cantidad_de_palabras_clave", "porcentaje_de_palabras_clave", "principales_palabras_clave"
    ])

    return df_resultado
