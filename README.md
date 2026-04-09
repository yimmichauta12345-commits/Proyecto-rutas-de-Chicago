# 🚕 Chicago Taxi Demand Analysis

## 📌 Descripción del proyecto

Este proyecto tiene como objetivo analizar patrones de demanda en el servicio de taxis en Chicago, identificando tendencias por compañía y ubicación, así como evaluar el impacto de las condiciones climáticas en la duración de los viajes.

El análisis combina exploración de datos (EDA), visualización y pruebas estadísticas para generar insights relevantes para la toma de decisiones en el sector de transporte.

---

## 🎯 Objetivos

- Analizar la distribución de viajes por compañía de taxis  
- Identificar las zonas con mayor demanda de viajes  
- Visualizar tendencias clave en el comportamiento del servicio  
- Evaluar el impacto de la lluvia en la duración de los viajes  
- Validar hipótesis estadísticas mediante pruebas T  

---

## 🛠️ Tecnologías utilizadas

- Python  
- Pandas  
- Matplotlib  
- SciPy (estadística)  
- Jupyter Notebook  

---

## 🔍 Proceso de análisis

### 1. Exploración de datos
- Carga de múltiples datasets provenientes de consultas SQL  
- Validación de estructura, tipos de datos y valores nulos  
- Análisis descriptivo inicial  

### 2. Análisis exploratorio (EDA)
- Análisis de número de viajes por compañía  
- Identificación de las compañías con mayor volumen de servicios  
- Análisis de barrios con mayor número de destinos (drop-off)  

### 3. Visualización de datos
- Gráficos de barras para comparar volumen de viajes por compañía  
- Visualización de top 10 barrios con mayor demanda  
- Identificación de concentración de viajes en ciertas zonas  

### 4. Preparación para análisis estadístico
- Conversión de variables de tiempo  
- Creación de variables derivadas (día de la semana, condiciones climáticas)  
- Segmentación de datos (días lluviosos vs no lluviosos)  

### 5. Análisis estadístico
- Formulación de hipótesis:
  - H₀: No hay diferencia en la duración de los viajes en sábados lluviosos vs no lluviosos  
  - H₁: Existe diferencia en la duración de los viajes  
- Aplicación de prueba t de muestras independientes (Welch’s t-test)  
- Evaluación de resultados con nivel de significancia α = 0.05  

---

## 📊 Principales insights

- Se identificó una alta concentración de viajes en pocas compañías, destacando líderes claros en el mercado.  
- La demanda de taxis está geográficamente concentrada en ciertos barrios clave.  
- Las condiciones climáticas tienen impacto en la duración de los viajes, lo que puede afectar la planificación operativa.  
- El uso de análisis estadístico permite validar si las diferencias observadas son significativas.  

---

## 📁 Dataset

El análisis se basa en múltiples datasets que incluyen:

- Compañías de taxis y número de viajes  
- Ubicaciones de destino (barrios)  
- Información temporal de los viajes  
- Condiciones climáticas  
- Duración de los viajes  

---

## 📌 Conclusión

El análisis permitió identificar patrones relevantes en la demanda de servicios de taxi en Chicago, así como evaluar el impacto de factores externos como el clima. Estos hallazgos pueden ser útiles para optimizar operaciones, mejorar la asignación de recursos y entender el comportamiento del mercado.

---

## 🚀 Posibles mejoras

- Incorporar modelos predictivos para estimar demanda  
- Integrar datos en tiempo real  
- Desarrollar dashboards interactivos (Power BI / Tableau)  
- Analizar impacto de otras variables (hora del día, eventos, tráfico)  

---

## 🔗 Repositorio

[Ver proyecto en GitHub](https://github.com/yimmichauta12345-commits/Proyecto-rutas-de-Chicago)
