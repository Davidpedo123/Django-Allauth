import matplotlib.pyplot as plt
import requests

def generar_grafico():
    response = requests.get("http://127.0.0.1:8000/api/OrdersRegion")
    data = response.json()

    # Extrae las regiones y el total de órdenes
    regions = [item['ShipRegion'] for item in data]
    total_orders = [item['total_orders'] for item in data]

    # Crea una figura con un tamaño específico
    plt.figure(figsize=(10, 6))

    # Crea el gráfico de pastel
    plt.pie(total_orders, labels=regions, autopct='%1.1f%%')

    # Añade un título al gráfico
    plt.title('Total de Órdenes por Región')

    # Guarda el gráfico como una imagen
    plt.savefig('static/css/imgcss/Grafico.png')

# Llama a la función para generar el gráfico
generar_grafico()
