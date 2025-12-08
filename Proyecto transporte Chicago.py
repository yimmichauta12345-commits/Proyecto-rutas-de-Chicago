#Importar librerias
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import ttest_ind

#Leer los datos
df1 = pd.read_csv('/datasets/project_sql_result_01.csv')
df2 = pd.read_csv('/datasets/project_sql_result_04.csv')
df3 = pd.read_csv('/datasets/project_sql_result_07.csv')

#Validar superficialmete los DataFrames
df1.info()
df2.info()
df3.info()

#Validar estructura, estadisticas basicas y valores nulos df1
print('Primeras 5 filas df1')
print(df1.head())
print()
print('Datos estadisticos basicos df1')
print(df1.describe())
print()
print('Validar si hay datos nulos df1')
print(df1.isna().sum())


#Validar estructura, estadistica basica y valores nulos df2
print('Primeras 5 filas df2')
print(df2.head())
print()
print('Datos estadisticos basiicos df2')
print(df2.describe())
print()
print('Validar si hay datos nulos')
print(df2.isna().sum())


#Validar estructura, estadistica basica y valores nulos df3
print('Primeras 5 filas df3')
print(df3.head())
print()
print('Datos estadisticos basiicos df3')
print(df3.describe())
print()
print('Validar si hay datos nulos')
print(df3.isna().sum())


#Top de promedio de viajes por locación
top10_neighborhoods = df2.sort_values(by='average_trips', ascending=False).head(10)
top10_neighborhoods


#Grafica de viajes por compañia
plt.figure(figsize=(8,12))
plt.barh(df1['company_name'], df1['trips_amount'])
plt.xlabel('Número de viajes')
plt.ylabel('Compañía de taxis')
plt.title('Viajes por compañía de taxis (15 y 16 de noviembre 2017)')
plt.gca().invert_yaxis()
plt.show()

#En el grafico podemos apreciar que la compañia que mas viajes realizo fue Flash Cab con una/
#diferencia considerable frente a las demas compañias y pese a que hay muchas compañias la mayoria/
#de los viajes se centran en 9.


#Grafica de top de barrios mas visitados
plt.figure(figsize=(8,6))
plt.bar(top10_neighborhoods['dropoff_location_name'], top10_neighborhoods['average_trips'])
plt.xlabel('Barrio')
plt.ylabel('Viajes promedio')
plt.title('Top 10 barrios por finalización de viajes (noviembre 2017)')
plt.xticks(rotation=45, ha='right')
plt.show()


#Cambio de formato para una columna del df3
df3['start_ts'] = pd.to_datetime(df3['start_ts'])
df3['day_of_week'] = df3['start_ts'].dt.dayofweek 
#Generar columna para filtrar el clima
df3['rainy'] = df3['weather_conditions'].str.contains('Bad', case=False, regex=True)

saturday_rain = df3[(df3['day_of_week'] == 5) & (df3['rainy'])]
saturday_no_rain = df3[(df3['day_of_week'] == 5) & (~df3['rainy'])]

#Hipotesis:
#Hipotesis nula Ho: La duración promedio de los viajes es igual los sábados lluviosos y los sábados sin lluvia
#Hipotesis alternativa H1: La duración promedio de los viajes cambia cuando llueve los sábados.


alpha = 0.05

result = ttest_ind(
    saturday_rain['duration_seconds'],
    saturday_no_rain['duration_seconds'],
    equal_var=False   # Welch t-test
)

print(result)

if result.pvalue < alpha:
    print("Rechazamos H0: las duraciones cambian en sábados lluviosos.")
else:
    print("No rechazamos H0: no hay evidencia de un cambio en la duración.")


#Cómo planteaste las hipótesis
#H0: medias iguales.
#H1: medias diferentes.

#Qué criterio usaste para probar las hipótesis y por qué
#Se usa una prueba t de muestras independientes porque:
#Se comparan medias entre dos grupos
#las observaciones son independientes
#tamaño de muestra > 30
#Welch corrige varianzas desiguales