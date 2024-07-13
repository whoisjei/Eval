import FuncionesMatriz

listaempleados = FuncionesMatriz

while True:
    print ("")
    print("---------SISTEMA DE REPORTES----------")
    print("1. Asignar sueldos aleatorios.")
    print("2. Clasificar sueldos.")
    print("3. Ver estadisticas.")
    print("4. Reporte de sueldos.")
    print("5. Salir del programa.")
    op = int (input("¿Que desea ejecutar?: "))
    print("")

    while op:
        if op == 1: #Asignarsueldos
            FuncionesMatriz.Asignarsueldos(listaempleados)
        if op == 2: #Listadeempleados
            FuncionesMatriz.MostrarInfoempleados(listaempleados)
     