# Autor: Tiziana Meza
# Fecha: Feb-2024
# Descripción:Análisis de ventas en una tienda online para obtener insights sobre tendencias y comportamiento del cliente.
# Versión de Python: 3.6
import pandas as pd
import matplotlib.pyplot as plt

# Cargar datos
data = pd.read_csv("datos_tienda_online.csv")

# Visualizar las primeras filas del dataframe
print(data.head())

# Estadísticas descriptivas
print(data.describe())

# Visualizar histogramas de variables numéricas
data.hist(figsize=(10, 8))
plt.tight_layout()
plt.show()

# Visualizar correlaciones entre variables numéricas
correlation_matrix = data.corr()
plt.figure(figsize=(10, 8))
plt.imshow(correlation_matrix, cmap='coolwarm', interpolation='nearest')
plt.colorbar()
plt.title('Correlación entre variables numéricas')
plt.xticks(range(len(correlation_matrix)), correlation_matrix.columns, rotation=90)
plt.yticks(range(len(correlation_matrix)), correlation_matrix.columns)
plt.tight_layout()
plt.show()

# Visualizar relaciones entre variables numéricas
# Por ejemplo, scatter plot entre 'Precio' y 'Cantidad Vendida'
plt.scatter(data['Precio'], data['Cantidad Vendida'])
plt.xlabel('Precio')
plt.ylabel('Cantidad Vendida')
plt.title('Relación entre Precio y Cantidad Vendida')
plt.show()

# Visualizar relaciones entre variables categóricas
# Por ejemplo, gráfico de barras de 'Categoría' vs 'Cantidad Vendida'
plt.figure(figsize=(10, 6))
data.groupby('Categoría')['Cantidad Vendida'].sum().plot(kind='bar')
plt.xlabel('Categoría')
plt.ylabel('Cantidad Vendida')
plt.title('Cantidad Vendida por Categoría')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
