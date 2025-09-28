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
            print("ⓘ El nombre no puede estar vacío.")
            continue
        break
    while True:
        apellidos = input("Ingresa los apellidos: ")
        if apellidos == "" or apellidos.strip() == "":
            print("ⓘ Los apellidos no pueden estar vacíos.")
            continue
        break
    if clientes:
        siguienteClave = max(clientes.keys()) + 1
        clientes.update({siguienteClave:[nombre, apellidos]})
    else:
        clientes.update({100:[nombre, apellidos]})
    print("✓ Cliente agregado con éxito.\n")

def mostrarClientes():
    print("\nClientes registrados:")
    print("*"*30)
    print("Clave\tNombre completo")
    for clave, nombreCompleto in clientes.items():
        print(f"{clave}\t{nombreCompleto[0]} {nombreCompleto[1]}")
    print("*"*30)

def reservarSala():
    if not clientes:
        print("ⓘ No hay clientes registrados. Agrega uno ahora:")
        agregarCliente()
    while True:
        mostrarClientes()
        try:
            claveCliente = int(input("Ingresa tu clave de cliente: "))
        except ValueError:
            print("⚠︎ Clave inválida.")
            continue
        if claveCliente not in clientes.keys():
            print("⚠︎ La clave de cliente no existe.")
            opcionCancelar = input("¿Cancelar operacion? (S - sí/N - no) ")
            if opcionCancelar.upper() == "S":
                menu()
            elif opcionCancelar.upper() == "N":
                continue
            else:
                print("⚠︎ Opción no reconocida.")
                continue
        else:
            clienteAgendado = claveCliente
            break
    while True:
        fecha_string = input("Ingresa la fecha a agendar (dd/mm/aaaa): ")
        try:
            fechaAgendada = dt.datetime.strptime(fecha_string, "%d/%m/%Y")
        except ValueError:
            print("⚠︎ Fecha inválida.")
            continue
        if fechaAgendada >= (hoy + timedelta(days=2)):
            break
        else:
            print("ⓘ La reservación tiene que ser hecha con 2 (dos) días de anticipación como mínimo.")
            continue
    todosTurnos = {"M", "V", "N"}
    disponibilidad = {}
    for claveSala in salas.keys():
        disponibilidad.update({claveSala:set(todosTurnos)})

    for fecha, turno, sala, *_ in reservaciones.values():
        if fecha == fechaAgendada:
            disponibilidad[sala].discard(turno)
    while True:
        print(f"\nSALAS DISPONIBLES Y TURNOS EL {fechaAgendada.strftime("%d %b %Y")}:")
        print("*"*50)
        print("Clave\tNombre\tCupo\tTurnos disponibles")
        for clave, (nombre, cupo) in salas.items():
            turnosLibres = ", ".join(sorted(disponibilidad[clave]))
            print(f"{clave}\t{nombre}\t{cupo}\t{turnosLibres}")
        print("*"*50)
        try:
            salaAgendada = int(input("Ingresa la clave de la sala a agendar: "))
        except:
            print("⚠︎ Clave inválida.")
            continue
        if salaAgendada not in salas.keys():
            print("ⓘ La sala no existe.")
            continue
        if not disponibilidad[salaAgendada]:
            print("ⓘ Esta sala no tiene turnos disponibles en la fecha seleccionada.")
            continue
        break
    while True:
        turno = input("Elige el turno a agendar (M - matutino, V - vespertino, N - nocturno): ")
        if turno.upper() not in disponibilidad[salaAgendada]:
            print("⚠︎ Turno no disponible para esta sala.")
            continue
        turnoAgendado = turno.upper()
        break
    while True:
        nombreEvento = input("Ingresa el nombre del evento: ")
        if nombreEvento == "" or nombreEvento.strip() == "":
            print("ⓘ El nombre del evento no puede estar vacío.")
            continue
        break

    if reservaciones:
        siguienteClaveEvento = max(reservaciones.keys()) + 1
        reservaciones.update({siguienteClaveEvento:[fechaAgendada, turnoAgendado, salaAgendada, clienteAgendado, nombreEvento]})
    else:
        reservaciones.update({1000:[fechaAgendada, turnoAgendado, salaAgendada, clienteAgendado, nombreEvento]})
    print("✓ La reservación fue registrada con éxito.\n")

def consultarReservaciones():
    if not reservaciones:
        print("ⓘ No hay reservaciones. Registra una ahora:")
        reservarSala()
    print("Para consultar una reservación, ingresa la fecha (dd/mm/aaaa) bajo la que fue agendada.")
    while True:
        fechaConsultada_string = input("Fecha a consultar: ")
        try:
            fechaConsultada = dt.datetime.strptime(fechaConsultada_string, "%d/%m/%Y")
        except:
            print("⚠︎ Fecha inválida.")
            continue
        break
    consultas = {}
    for llave, valor in reservaciones.items():
        if valor[0] == fechaConsultada:
            consultas.update({llave:valor})
    print("\n")
    print("*"*70)
    print(f"REPORTE DE RESERVACIONES PARA EL DIA {fechaConsultada.strftime('%d %b %Y')}")
    print("*"*70)
    print(f"{'SALA':<10}{'CLIENTE':<20}{'EVENTO':<25}{'TURNO':<10}")
    print("-"*70)
    for claveEvento, detalles in consultas.items():
        fechaAgendada, turnoAgendado, salaAgendada, clienteAgendado, nombreEvento = detalles
        print(f"{salaAgendada:<10}{clienteAgendado:<20}{nombreEvento:<25}{turnoAgendado:<10}")
    print("*" * 70)
    print("\n")

def registrarSala():
    while True:
        nombreSala = input("Ingresa el nombre de la sala: ")
        if nombreSala == "" or nombreSala.strip() == "":
            print("ⓘ El nombre no puede estar vacío.")
            continue
        break
    while True:
        try:
            cupoSala = int(input("Ingresa el cupo de la sala: "))
        except ValueError:
            print("ⓘ El valor ingresado no es válido. Debe ser un entero.")
            continue
        break
    if salas:
        siguienteSala = max(salas.keys()) + 1
        salas.update({siguienteSala:(nombreSala, cupoSala)})
    print("✓ La sala fue registrada con éxito.\n")

def editarEvento():
    if not reservaciones:
        print("ⓘ No hay reservaciones registradas.")
        return
    print("Para editar el nombre de un evento existente, ingresa el rango de fechas (dd/mm/aaaa) en el que se encuentra agendado el evento que quieres editar.")
    while True:
        inicioRango_string = input("Del: ")
        finRango_string = input("Al: ")
        try:
            inicioRango = dt.datetime.strptime(inicioRango_string, "%d/%m/%Y")
            finRango = dt.datetime.strptime(finRango_string, "%d/%m/%Y")
        except:
            print("⚠︎ Fecha inválida.")
            continue

        rangoFiltrado = {}
        for llave, valor in reservaciones.items():
            if inicioRango <= valor[0] <= finRango:
                rangoFiltrado.update({llave:valor})
        break
    print(f"\nEVENTOS REGISTRADOS ENTRE EL {inicioRango.strftime("%d %b %Y")} Y EL {finRango.strftime("%d %b %Y")}:")
    print("*"*50)
    print(f"Clave\tFecha\t\tNombre\t\tTurno\tSala")
    for idEvento, datos in rangoFiltrado.items():
        fecha, turno, sala, cliente, nombreEvento = datos
        print(f"{idEvento}\t{fecha.strftime('%d/%m/%Y')}\t{nombreEvento}\t{turno}\t{sala} '{salas.get(sala)[0]}'")
    print("*"*50)
    while True:
        try:
            eventoEditando = int(input("\nIngresa la clave del evento que deseas renombrar: "))
        except ValueError:
            print("⚠︎ Clave inválida.")
            continue
        if eventoEditando not in rangoFiltrado.keys():
            print("ⓘ Este evento no existe en el rango de fechas.")
            continue
        break
    while True:
        nuevoNombre = input("Ingresa el nuevo nombre para el evento: ")
        if nuevoNombre == "" or nuevoNombre.strip() == "":
            print("ⓘ El nombre no puede estar vacío.")
            continue
        break
    reservaciones[eventoEditando][4] = nuevoNombre
    print(f"✓ El nombre del evento con clave {eventoEditando} fue editado a '{nuevoNombre}' exitosamente.\n")

def menu():
    while True:
        print("*"*50)
        print("SISTEMA DE RESERVA DE SALAS PARA COWORKING")
        print("\nSelecciona una opción para continuar:")
        print("(a) Reservar una sala")
        print("(b) Editar el nombre de una reservación")
        print("(c) Consultar reservaciones")
        print("(d) Registrar nuevo cliente")
        print("(e) Registrar nueva sala")
        print("(f) Salir\n")
        print("*"*50)
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
            print("⚠︎ Opción no reconocida.")
            continue

menu()
