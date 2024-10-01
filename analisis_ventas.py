# Paso 1: Crear la lista de ventas
ventas = [
    {"fecha": "2024-01-01", "producto": "Zapatos", "cantidad": 10, "precio": 50.0},  # Venta de zapatos
    {"fecha": "2024-01-01", "producto": "Camisa", "cantidad": 5, "precio": 20.0},   # Venta de camisas
    {"fecha": "2024-01-02", "producto": "Zapatos", "cantidad": 7, "precio": 50.0},   # Más zapatos
    {"fecha": "2024-01-02", "producto": "Pantalones", "cantidad": 3, "precio": 30.0},  # Pantalones vendidos
    {"fecha": "2024-01-03", "producto": "Camisa", "cantidad": 8, "precio": 20.0},   # Otras camisas
    {"fecha": "2024-01-03", "producto": "Pantalones", "cantidad": 6, "precio": 30.0},  # Más pantalones
    {"fecha": "2024-01-04", "producto": "Zapatos", "cantidad": 2, "precio": 50.0},   # Un par de zapatos más
]

# Paso 2: Cálculo de ingresos totales
ingresos_totales = 0  # Inicializamos la variable para los ingresos totales

for venta in ventas:  # Recorremos cada venta en la lista
    ingresos = venta["cantidad"] * venta["precio"]  # Calculamos los ingresos de la venta
    ingresos_totales += ingresos  # Acumulamos los ingresos

print(f"Ingresos Totales: ${ingresos_totales:.2f}")  # Imprimimos el total de ingresos

# Paso 3: Análisis del Producto Más Vendido
ventas_por_producto = {}  # Creamos un diccionario para contar las ventas por producto

for venta in ventas:  # Recorremos cada venta
    producto = venta["producto"]  # Obtenemos el nombre del producto
    cantidad = venta["cantidad"]  # Obtenemos la cantidad vendida
    
    # Acá revisamos si el producto ya está en el diccionario
    if producto in ventas_por_producto:
        ventas_por_producto[producto] += cantidad  # Sumamos la cantidad si ya existe
    else:
        ventas_por_producto[producto] = cantidad  # Si no existe, lo creamos

# Encontrar el producto más vendido
producto_mas_vendido = max(ventas_por_producto, key=ventas_por_producto.get)  # Buscamos el producto con más ventas
cantidad_mas_vendida = ventas_por_producto[producto_mas_vendido]  # Obtenemos la cantidad vendida de ese producto

print(f"Producto más vendido: {producto_mas_vendido} (Cantidad: {cantidad_mas_vendida})")  # Mostramos el más vendido

# Paso 4: Promedio de Precio por Producto
precios_por_producto = {}  # Diccionario para calcular el precio promedio

for venta in ventas:  # Recorremos cada venta
    producto = venta["producto"]  # Obtenemos el nombre del producto
    cantidad = venta["cantidad"]  # Obtenemos la cantidad
    precio = venta["precio"]  # Obtenemos el precio
    
    # Chequeamos si ya tenemos el producto en el diccionario
    if producto in precios_por_producto:
        precios_por_producto[producto][0] += precio * cantidad  # Suma de precios
        precios_por_producto[producto][1] += cantidad  # Cantidad total
    else:
        precios_por_producto[producto] = [precio * cantidad, cantidad]  # [suma de precios, cantidad]

# Calcular precios promedio
precios_promedio = {producto: suma / cantidad for producto, (suma, cantidad) in precios_por_producto.items()}  # Sacamos el promedio

# Mostramos el precio promedio por producto
for producto, precio in precios_promedio.items():  # Recorremos el diccionario de precios promedio
    print(f"Precio promedio de {producto}: ${precio:.2f}")  # Imprimimos el promedio de cada producto

# Paso 5: Ventas por Día
ingresos_por_dia = {}  # Diccionario para ingresos diarios

for venta in ventas:  # Recorremos cada venta
    fecha = venta["fecha"]  # Obtenemos la fecha de la venta
    ingresos = venta["cantidad"] * venta["precio"]  # Calculamos los ingresos de esa venta
    
    # Revisamos si ya existe la fecha en el diccionario
    if fecha in ingresos_por_dia:
        ingresos_por_dia[fecha] += ingresos  # Sumamos ingresos si ya existe
    else:
        ingresos_por_dia[fecha] = ingresos  # Si no existe, lo creamos

# Mostramos los ingresos por día
for fecha, ingresos in ingresos_por_dia.items():  # Recorremos el diccionario de ingresos por día
    print(f"Ingresos el {fecha}: ${ingresos:.2f}")  # Imprimimos los ingresos totales por día

# Paso 6: Resumen de Ventas
resumen_ventas = {}  # Diccionario para el resumen de ventas

for venta in ventas:  # Recorremos cada venta
    producto = venta["producto"]  # Obtenemos el nombre del producto
    cantidad = venta["cantidad"]  # Obtenemos la cantidad
    ingresos = cantidad * venta["precio"]  # Calculamos los ingresos de la venta
    
    # Si el producto no está en el resumen, lo agregamos
    if producto not in resumen_ventas:
        resumen_ventas[producto] = {
            "cantidad_total": cantidad,  # Total de productos vendidos
            "ingresos_totales": ingresos,  # Ingresos generados por el producto
            "precio_promedio": precios_promedio[producto]  # Precio promedio de venta
        }
    else:
        resumen_ventas[producto]["cantidad_total"] += cantidad  # Sumamos la cantidad total
        resumen_ventas[producto]["ingresos_totales"] += ingresos  # Sumamos los ingresos totales

# Mostramos el resumen de ventas
for producto, info in resumen_ventas.items():  # Recorremos el resumen
    print(f"Resumen de {producto}:")  # Imprimimos el producto
    print(f"  Cantidad total: {info['cantidad_total']}")  # Mostramos la cantidad total
    print(f"  Ingresos totales: ${info['ingresos_totales']:.2f}")  # Mostramos los ingresos totales
    print(f"  Precio promedio: ${info['precio_promedio']:.2f}")  # Mostramos el precio promedio

# Paso 7: Exportar resultados a un archivo de texto
with open("resumen_ventas.txt", "w") as file:  # Abrimos un archivo para escribir
    file.write("Ingresos Totales: ${:.2f}\n\n".format(ingresos_totales))  # Escribimos los ingresos totales
    file.write(f"Producto más vendido: {producto_mas_vendido} (Cantidad: {cantidad_mas_vendida})\n\n")  # Escribimos el producto más vendido
    
    file.write("Precio promedio por producto:\n")  # Encabezado para precios promedio
    for producto, precio in precios_promedio.items():  # Recorremos el diccionario de precios promedio
        file.write(f"{producto}: ${precio:.2f}\n")  # Escribimos el precio de cada producto
    
    file.write("\nIngresos por día:\n")  # Encabezado para ingresos por día
    for fecha, ingresos in ingresos_por_dia.items():  # Recorremos el diccionario de ingresos por día
        file.write(f"{fecha}: ${ingresos:.2f}\n")  # Escribimos los ingresos por fecha
    
    file.write("\nResumen de ventas:\n")  # Encabezado para resumen de ventas
    for producto, info in resumen_ventas.items():  # Recorremos el resumen de ventas
        file.write(f"{producto}:\n")  # Escribimos el nombre del producto
        file.write(f"  Cantidad total: {info['cantidad_total']}\n")  # Escribimos la cantidad total
        file.write(f"  Ingresos totales: ${info['ingresos_totales']:.2f}\n")  # Escribimos los ingresos totales
        file.write(f"  Precio promedio: ${info['precio_promedio']:.2f}\n")  # Escribimos el precio promedio

# Instrucciones para ejecutar:
# 1. Abre tu editor de Python (Jupyter Notebook, PyCharm, etc.)
# 2. Copia y pega este código en un archivo nuevo.
# 3. Guarda el archivo con extensión .py (por ejemplo, analisis_ventas.py).
# 4. Ejecuta el archivo para ver los resultados en la consola y crear el archivo "resumen_ventas.txt".
