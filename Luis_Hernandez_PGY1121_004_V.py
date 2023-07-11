import numpy as np

departamento = np.zeros((10, 4), dtype=object)

precios = {
    "A": 3800,
    "B": 3000,
    "c": 2800,
    "D": 3500,
}

compradores = {}


def mostrar_departamentos():
    print("Estado de la venta actual de  deparatmenrtos:\n")
    for piso in range(10):
        for depto in range(4):
            if departamento[piso, depto] == 0:
                print(
                    f"Piso {piso+1}, departamento {chr(65+depto)}: Disponible")
            else:
                print(f"Piso {piso+1}, Departamento {chr(65+depto)}: Vendido")


def comprar_departamento():
    print("Opcion 1: Comprar departamento\n")
    piso = int(input("Ingrese el numero del piso (1-10):"))
    tipo = input("Imgrese el tipo de departamento (A, B, C, D").upper()

    if tipo not in precios.keys():
        print("Tipo de departamento invalido")
        return
    if piso < 1 or piso > 10:
        print("Numero de piso invalido")
        return
    depto = ord(tipo) - 56

    if departamento[piso-1, depto] == 0:
        run = input("Ingrese el RUN del comprador (sin puntos ni guion): ")
        compradores[run] = tipo
        departamento[piso-1, depto] = 1
        print("\n¡Operacion realizada correctamente!")
    else:
        print("\nEl deparatmento no esta disponible")


def ver_listado_compradores():
    print("Opcion 3: ver listado de conpradores\n")
    if not compradores:
        print("Aun no se han realizado compras.")
        return
    print("Listado de compradores po RUN: ")
    for run in sorted(compradores.keys()):
        print(f"Run: {run}, Departamento: {compradores[run]} ")


def mostrar_ventas_totales():
    print("Opcion 4: Mostrar ganacias totales\n")
    if not compradores:
        print("Aun no se Han realizados ventas.")
        return
    total = sum(precios[tipo]for tipo in compradores.values())
    print(f"ganacias totales por vnetas: {total} UF")


while True:
    print("_________ Menu Principal________")
    print("1. Comprar departamento ")
    print("2. Mostrar Departamento disponible")
    print("3. Ver listado de compradores ")
    print("4. Mostrar Ganacias totaales ")
    print("5._______    SALIR______________")

    opcion = input("\nSeleccione una opcion: ")
    if opcion == '1':
        comprar_departamento()
    elif opcion == '2':
        mostrar_deparatmentos
    elif opcion == '3':
        ver_listado_compradores
    elif opcion == '4':
        mostrar_ventas_totales
    elif opcion == '5':
        print("\n Gracias por utilizr el control de ventas de Departamentontos ")
        break
    else:
        print("\nOpcion invalida. Por favor, Seleccione un Opcion valida  ")
