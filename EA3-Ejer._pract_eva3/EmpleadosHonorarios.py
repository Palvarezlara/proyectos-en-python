import funciones as fn
trabajadores = []
while True:
    print("""
        1.- Registrar trabajador. 
        2.- Listar trabajadores
        3.- Imprimir listado de trabajadores. 
        4.- Salir
        """)
    try:
        opcion = int(input("Ingrese opción: "))
    except:
        print('Ingrese un número válido. ')
    if opcion == 1:
        fn.registrar_trabajadores(trabajadores)
    elif opcion == 2:
        fn.listar_trabajadores(trabajadores)
    elif opcion == 3:
        fn.imprimir_plantilla(trabajadores)
    elif opcion == 4:
        print('Saliendo del programa. ')
        break
    else:
        print('Opción ingresada es no valida.')