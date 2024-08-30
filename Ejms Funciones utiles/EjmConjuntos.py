def ejemplo_conjuntos():
    # Crear dos conjuntos de ejemplo
    conjunto1 = {1, 2, 3, 4}
    conjunto2 = {3, 4, 5, 6}
    
    # Unión de conjuntos
    union = conjunto1 | conjunto2
    print("Unión de conjunto1 y conjunto2:", union)
    
    # Intersección de conjuntos
    interseccion = conjunto1 & conjunto2
    print("Intersección de conjunto1 y conjunto2:", interseccion)
    
    # Diferencia de conjuntos
    diferencia = conjunto1 - conjunto2
    print("Diferencia de conjunto1 y conjunto2:", diferencia)
    
    # Diferencia simétrica de conjuntos
    diferencia_simetrica = conjunto1 ^ conjunto2
    print("Diferencia simétrica de conjunto1 y conjunto2:", diferencia_simetrica)
    
    # Añadir un elemento al conjunto
    conjunto1.add(7)
    print("Conjunto1 después de add(7):", conjunto1)
    
    # Eliminar un elemento del conjunto
    conjunto1.discard(2)
    print("Conjunto1 después de discard(2):", conjunto1)

# Ejecución del ejemplo
ejemplo_conjuntos()
