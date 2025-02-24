def optimize_purchase(purchase):
    # Convierte la lista en un conjunto para eliminar duplicados
    unique_products = list(set(purchase))
    # Ordena los productos para mantener un orden consistente (opcional)
    unique_products.sort()
    return unique_products

# Ejemplo de uso
purchase = [12, 12, 34, 34, 34, 89]
optimized_purchase = optimize_purchase(purchase)
print(optimized_purchase)  # Salida: [12, 34, 89]
