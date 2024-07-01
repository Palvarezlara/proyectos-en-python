CARGOS = ('ceo', 'desarrollador', 'analista de datos')

def registrar_trabajadores(trabajadores):
    print('   ')
    print('------Registro de trabajadores-----\n ')
    #solicitar los datos del trabajador
    nombre = input('Ingrese el nombre y apellido del trabajador: ')
    cargo = input('Ingrese el cargo del trabajador (CEO/ Desarrollador/Analista de datos): ').lower()
    if cargo not in CARGOS:
        print('Opción ingresada no existe, ingrese nuevamente. ')
        cargo = input('Ingrese el cargo del trabajador (CEO/ Desarrollador/Analista de datos): ').lower()
    sueldo_bruto = int(input('Ingrese el sueldo bruto: '))
    
    #calcular los descuentos
    descSalud = round(sueldo_bruto * 0.07)
    descAFP = round(sueldo_bruto * 0.12)
    sueldo_liquido= sueldo_bruto - descSalud - descAFP
    
    # guardar información en una lista como diccionario
    trabajadores.append({
        'Nombre' : nombre,
        'Cargo' : cargo,
        'SueldoBruto' : sueldo_bruto,
        'DescSalud' : descSalud,
        'DescAFP' : descAFP,
        'SueldoLiquido': sueldo_liquido
    })
    print('Usuario registrado con exito')
    
def listar_trabajadores(trabajadores):
    print('Listado de trabajadores')
    #print('Nombre\t\tCargo\t\tSueldo Bruto\tDesc. Salud\tDesc. AFP\tSueldo liquido')
    for trabajador in trabajadores:
        print(trabajador['Nombre'])
        #print(f'{trabajador['Nombre']}\t\t{trabajador['Cargo']}\t{trabajador['SueldoBruto']}\t\t{trabajador['DescSalud']}\t\t{trabajador['DescAFP']}\t\t{trabajador['SueldoLiquido']}')
    
def imprimir_plantilla(trabajadores):
    cargoSeleccionado= input('Ingrese cargo para imprimir planilla o bien presione ENTER para seleccionar todos: ').lower()
    if cargoSeleccionado == "":
        trabajadores_a_imprimir = trabajadores
        nombreArchivo = 'Planilla_todos.txt'
    elif cargoSeleccionado in CARGOS:
        trabajadores_a_imprimir = []
        for trabajador in trabajadores:
            if trabajador['Cargo'] == cargoSeleccionado:
                trabajadores_a_imprimir.append(trabajador)
        nombreArchivo = f'planilla_{cargoSeleccionado}.txt'
    else:
        print('Cargo no válido')
        return
    with open(nombreArchivo, 'w') as archivo:
        for trabajador in trabajadores_a_imprimir:
            archivo.write(f'Nombre y Apellido: {trabajador['Nombre']}\n')
            archivo.write(f'Cargo: {trabajador['Cargo']}\n')
            archivo.write(f'Sueldo Bruto: ${trabajador['SueldoBruto']}\n') 
            archivo.write(f'Desc. Salud: ${trabajador['DescSalud']}\n') 
            archivo.write(f'Desc. AFP: ${trabajador['DescAFP']}\n') 
            archivo.write(f'Liquido a pagar: ${trabajador['SueldoLiquido']}\n\n')         
    