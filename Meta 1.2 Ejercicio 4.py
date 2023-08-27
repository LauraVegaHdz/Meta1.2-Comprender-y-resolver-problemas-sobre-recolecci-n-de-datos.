#Meta 1.2 Comprender y resolver problemas sobre recolección de datos.
#Laura Yolanda Vega Hernandez 27/08/2023

# 4.El archivo titanic.csv contiene información sobre los pasajeros del Titanic.
# Escribir un programa con los siguientes requisitos:
# Generar un DataFrame con los datos del archivo.
# Mostrar por pantalla las dimensiones del DataFrame.
# Mostrar el número de datos que contiene, los nombres de sus columnas.
# Mostrar las 10 primeras filas y las 10 últimas filas.
# Mostrar por pantalla el porcentaje de personas que sobrevivieron y murieron.
# Mostrar por pantalla el porcentaje de personas que sobrevivieron en cada clase.
# Cargar el archivo CSV en un DataFrame
import pandas as pd
import numpy as np

df = pd.read_csv('titanic.csv')
print(f"Dimensiones del DataFrame:\n{df.shape}")
print("\nInformación sobre los datos:\n", df.info())
print("\nLas 10 primeras filas:\n", df.head(10))
print("\nLas 10 últimas filas:",df.tail(10))

# Porcentaje de personas que sobrevivieron y murieron
sobrevivieron = np.sum(df['Survived'] == 1)
murieron = np.sum(df['Survived'] == 0)
total_pasajeros = df.shape[0]

porcentaje_sobrevivieron = (sobrevivieron / total_pasajeros) * 100
porcentaje_murieron = (murieron / total_pasajeros) * 100

print(f"\nPorcentaje de personas que sobrevivieron: {porcentaje_sobrevivieron:.2f}%")
print(f"Porcentaje de personas que murieron: {porcentaje_murieron:.2f}%")

# Porcentaje de personas que sobrevivieron por cada clase
porcentaje_sobrevivieron_clase = df.groupby('Pclass')['Survived'].mean() * 100
print("\nPorcentaje de personas que sobrevivieron en cada clase:")
print(porcentaje_sobrevivieron_clase)

