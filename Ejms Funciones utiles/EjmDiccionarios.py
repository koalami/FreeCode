def ejemplo_diccionarios():
    # Crear un diccionario de ejemplo
    capitales = {'Francia': 'París', 'España': 'Madrid', 'Italia': 'Roma'}
    
    # Acceder a un valor por su clave
    print("Capital de España:", capitales['España'])
    
    # Agregar un nuevo par clave-valor
    capitales['Alemania'] = 'Berlín'
    print("Diccionario después de agregar Alemania:", capitales)
    
    # Eliminar un par clave-valor
    del capitales['Italia']
    print("Diccionario después de eliminar Italia:", capitales)
    
    # Obtener todas las claves del diccionario
    print("Claves del diccionario:", list(capitales.keys()))
    
    # Obtener todos los valores del diccionario
    print("Valores del diccionario:", list(capitales.values()))
    
    # Verificar si una clave existe en el diccionario
    existe = 'Francia' in capitales
    print("¿Existe 'Francia' en el diccionario?", existe)

# Ejecución del ejemplo
ejemplo_diccionarios()
