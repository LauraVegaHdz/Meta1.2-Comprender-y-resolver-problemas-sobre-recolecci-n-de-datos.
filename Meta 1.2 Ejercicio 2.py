#Meta 1.2 Comprender y resolver problemas sobre recolección de datos.
#Laura Yolanda Vega Hernandez 27/08/2023


# 2.Escribir una función que reciba un DataFrame con el formato del 
# ejercicio anterior, una lista de meses, y devuelva el balance 
# (ventas - gastos) total en los meses indicados.ç
import pandas as pd

def calcular_balance(df, meses):
    balance_total = 0
    for mes in meses:
        balance_total += df[df['Mes'] == mes]['Ventas'].values[0] - df[df['Mes'] == mes]['Gastos'].values[0]
    return balance_total

datos = {
    'Mes': ['Enero', 'Febrero', 'Marzo', 'Abril'],
    'Ventas': [30500, 35600, 28300, 33900],
    'Gastos': [22000, 23400, 18100, 20700]
}

df = pd.DataFrame(datos)

meses = ['Enero', 'Febrero']
meses2=  ['Enero', 'Marzo', 'Abril']
meses3 = ['Enero', 'Febrero', 'Marzo']
meses4=  ['Enero', 'Febrero', 'Marzo', 'Abril']
balance = calcular_balance(df, meses)
balance2 = calcular_balance(df, meses2)
balance3 = calcular_balance(df, meses3)
balance4 = calcular_balance(df, meses4)
print(f"El balance total 1 : {balance}")
print(f"El balance total 2 : {balance2}")
print(f"El balance total 3 : {balance3}")
print(f"El balance total 4 : {balance4}")
    
  