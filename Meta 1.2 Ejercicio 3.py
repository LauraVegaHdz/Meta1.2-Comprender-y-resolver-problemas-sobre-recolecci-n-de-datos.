#Meta 1.2 Comprender y resolver problemas sobre recolección de datos.
#Laura Yolanda Vega Hernandez 27/08/2023
# 3.El archivo cotizacion.csv contiene las cotizaciones de las empresas del 
# IBEX35 con las siguientes columnas: nombre (nombre de la empresa), 
# Final (precio de la acción al cierre de bolsa), Máximo (precio máximo de 
# la acción durante la jornada), Mínimo (precio mínimo de la acción durante la jornada), 
# volumen (Volumen al cierre de bolsa), Efectivo (capitalización al cierre en miles de euros). 
# Construir una función que construya un DataFrame a partir del archivo con el formato 
# anterior y devuelve otro DataFrame con el mínimo, el máximo y la media de cada columna.
import pandas as pd

def procesar_cotizaciones(archivo):
    # Leer el archivo CSV en un DataFrame
    df = pd.read_csv(archivo)
    print(df)
    
    resul = {
        'Mínimo': df.min(),
        'Máximo': df.max(),
        'Media': df.mean()
    }
    
    # Crear un nuevo DataFrame con los resultados
    resumen_df = pd.DataFrame(resul)
    
    return resumen_df

# Llamar a la función con el archivo cotizacion.csv
archivo = 'cotizacion.csv'
resultado = procesar_cotizaciones(archivo)
print("\nResumen:")
print(resultado)
