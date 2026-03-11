# Importamos pandas, la librería estrella para análisis de datos en finanzas
import pandas as pd

# Leemos el archivo CSV que ya tienes en tu repositorio
print("Iniciando la lectura de datos de Apple...")
df_apple = pd.read_csv('AAPL.csv')

# Mostramos un resumen de las primeras 5 filas para comprobar que funciona
print("¡Datos cargados exitosamente! Aquí están las primeras filas:")
print(df_apple.head())
