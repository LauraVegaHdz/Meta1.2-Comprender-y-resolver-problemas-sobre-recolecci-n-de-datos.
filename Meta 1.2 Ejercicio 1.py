#Meta 1.2 Comprender y resolver problemas sobre recolección de datos.
#Laura Yolanda Vega Hernandez 27/08/2023


#1.Escribir un programa que genere y muestre por pantalla 
#un DataFrame con los datos de la tabla siguiente:
# Mes      Ventas  Gastos
# Enero    30500   22000
# Febrero  35600   23400
# Marzo    28300   18100
# Abril    33900   20700


import pandas as pd

datos = {
    'Mes': ['Enero', 'Febrero', 'Marzo', 'Abril'],
    'Ventas': [30500, 35600, 28300, 33900],
    'Gastos': [22000, 23400, 18100, 20700]
}

df = pd.DataFrame(datos)
print(df)


