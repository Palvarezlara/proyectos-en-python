Ejercicio de preparpación para evaluación 3

Desarrolle una aplicación en Python utilizando Visual Studio que permita resolver el siguiente caso:
Una empresa necesita desarrollar una aplicación que permita registrar los sueldos brutos de los trabajadores y calcular
el liquido a pagar. Para ello necesita que la aplicación cumpla con las siguientes funcionalidades.

1. registrar trabajadores
2. Listar todos los trabajadores
3. Imprimir planilla de sueldos
4. Salir del programa

#Registrar trabajador 
Para registrar un trabajador se requiere los siguiente: Nombre y Apellido, Cargo, Sueldo Bruto. Una vez ingresado los datos, 
se deben calcular, los valores de acuerdo con la siguiente tabla. 

trabajador      Cargo       Sueldo Bruto        Desc. Salud         Desc. AFP       Líquido a pagar

Homero
Simpson         CEO             1000000             70000             120000        810000

Debe validar que todos los datos sean ingresados. 

#Listar todos los trabajadores
Debe mostrar en la pantalla la lista de todos los trabajadores similar al ejemplo anterior de registrar un solo trabajador.

#Imprimir planilla de sueldos
Para Imprimir la planilla, el usuario puede seleccionar imprimir todos o por algún cargo en especifico. Estos cargos deben estar
previamente definidos en algún tipo de colección de Python en el código y por lo menos deben ser tres, por ejemplo: CEO, Desarrollador, Analista de datos. 

Al seleccionar uno de los cargos, se generará un archivo (.txt) con el detalle de los sueldos. Este debe tener la misma
forma del registro completo de las opcion anteriores, pero en archivo de texto. 

Cada una de estas opciones de la aplicación debe estar desarrollada en una función que debe ser llamada desde el programa principal. 

El programa debe funcionar hasta que el usuario decida finalizar el programa. 

