import datetime as dt
from datetime import timedelta

salas = {1:("Alfa", 10), 2:("Beta", 15), 3:("Gamma", 5)} # Tres salas iniciales
clientes = {}
reservaciones = {}
hoy = dt.datetime.now()

def agregarCliente():
    while True:
        nombre = input("Ingresa el nombre: ")
        if nombre == "" or nombre.strip() == "":
            print("ⓘ El nombre no puede estar vacio.")
            continue
        break
    while True:
        apellidos = input("Ingresa los apellidos: ")
        if apellidos == "" or apellidos.strip() == "":
            print("ⓘ Los apellidos no pueden estar vacios.")
            continue
        break
    if clientes:
        siguienteClave = max(clientes.keys()) + 1
        clientes.update({siguienteClave:[nombre, apellidos]})
    else:
        clientes.update({100:[nombre, apellidos]})
    print("✓ Cliente agregado con exito.\n")

def mostrarClientes():
    print("\nClientes registrados:")
    print("*"*30)
    print("Clave\tNombre completo")
    for clave, nombreCompleto in clientes.items():
        print(f"{clave}\t{nombreCompleto[0]} {nombreCompleto[1]}")
    print("*"*30)

def reservarSala():
    if not clientes:
        print("⚠︎ No hay clientes registrados. Agrega uno ahora:")
        agregarCliente()
    while True:
        mostrarClientes()
        try:
            claveCliente = int(input("Ingresa tu clave de cliente: "))
        except:
            print("⚠︎ Clave no valida.")
            continue
        if claveCliente not in clientes.keys():
            print("⚠︎ La clave de cliente no existe.")
            opcionCancelar = input("Cancelar operacion? (Y/N)")
            if opcionCancelar.upper() == "Y":
                menu()
            elif opcionCancelar.upper() == "N":
                continue
            else:
                print("⚠︎ Opcion no reconocida.")
                continue
        else:
            clienteAgendado = claveCliente
            break
    while True:
        fecha_string = input("Ingresa la fecha a agendar (dd/mm/aaaa): ")
        try:
            fechaAgendada = dt.datetime.strptime(fecha_string, "%d/%m/%Y")
        except:
            print("⚠︎ Fecha no valida.")
            continue
        if fechaAgendada >= hoy + timedelta(days=2):
            break
        else:
            print("ⓘ La reservacion tiene que ser hecha con 2 (dos) dias de anticipacion como minimo.")
            continue
    while True:
        turno = input("Elige el turno a agendar (M - Matutino, V - Vespertino, N - Nocturno): ")
        if turno.upper() == "M":
            turnoAgendado = "M"
        elif turno.upper() == "V":
            turnoAgendado = "V"
        elif turno.upper() == "N":
            turnoAgendado = "N"
        else:
            print("⚠︎ Turno no valido.")
            continue
        break
    while True:
        print(f"\nSalas disponibles y cupo:")
        print("*"*30)
        print(f"Clave\tNombre\tCupo")
        for clave, datos in salas.items():
            print(f"{clave}\t{datos[0]}\t{datos[1]}")
        print("*"*30)
        try:
            salaAgendada = int(input("Ingresa la clave de la sala a agendar: "))
        except ValueError:
            print("⚠︎ Clave no valida.")
            continue
        if salaAgendada not in salas.keys():
            print("ⓘ La sala no existe.")
            continue
        break
    while True:
        nombreEvento = input("Ingresa el nombre del evento: ")
        if nombreEvento == "" or nombreEvento.strip() == "":
            print("ⓘ El nombre del evento no puede estar vacio.")
            continue
        break
    reservaciones.update({fechaAgendada:[{turnoAgendado:{salaAgendada:[clienteAgendado, nombreEvento]}}]})
    print("✓ La reservacion fue registrada con exito.\n")

def consultarReservaciones():
    print(reservaciones)

def registrarSala():
    while True:
        nombreSala = input("Ingresa el nombre de la sala: ")
        if nombreSala == "" or nombreSala.strip() == "":
            print("ⓘ El nombre no puede estar vacio.")
            continue
        break
    while True:
        try:
            cupoSala = int(input("Ingresa el cupo de la sala: "))
        except ValueError:
            print("ⓘ El valor ingresado no es valido. Debe ser un entero.")
            continue
        break
    if salas:
        siguienteSala = max(salas.keys()) + 1
        salas.update({siguienteSala:[nombreSala, cupoSala]})
    print("✓ La sala fue registrada con exito.\n")

def editarEvento():
    pass

def menu():
    while True:
        print("*"*30)
        print("SISTEMA DE RESERVA DE SALAS PARA COWORKING")
        print("\nSelecciona una opcion para continuar:")
        print("(a) Reservar una sala")
        print("(b) Editar el nombre de una reservacion")
        print("(c) Consultar reservaciones")
        print("(d) Registrar nuevo cliente")
        print("(e) Registrar nueva sala")
        print("(f) Salir\n")
        opcion = input()
        if opcion.lower() == "a":
            reservarSala()
            continue
        elif opcion.lower() == "b":
            editarEvento()
            continue
        elif opcion.lower() == "c":
            consultarReservaciones()
            continue
        elif opcion.lower() == "d":
            agregarCliente()
            continue
        elif opcion.lower() == "e":
            registrarSala()
            continue
        elif opcion.lower() == "f":
            print("Saliendo...")
            break
        else:
            print("⚠︎ Opcion no reconocida.")
            continue

menu()
