import datetime as dt

salas = {"Alfa":10, "Beta":15, "Gamma":5, "Delta":10, "Epsilon":15} # Cinco salas iniciales
clientes = {}
reservaciones = {}

def agregarCliente():
    while True:
        nombre = input("Ingresa el nombre: ")
        if nombre == "":
            print("El nombre no puede estar vacio.")
            continue
        break
    while True:
        apellidos = input("Ingresa los apellidos: ")
        if apellidos == "":
            print("Los apellidos no pueden estar vacios.")
            continue
        break
    if clientes:
        siguienteClave = max(clientes.keys()) + 1
        clientes.update({siguienteClave:[nombre, apellidos]})
    else:
        clientes.update({100:[nombre, apellidos]})

def reservarSala():
    print(clientes)
    while True:
        try:
            claveCliente = int(input("Ingresa tu clave de cliente: "))
        except:
            print("Clave no valida.")
            continue
        if claveCliente not in clientes.keys():
            print("La clave de cliente no existe.")
            opcionCancelar = input("Cancelar operacion? (Y/N)")
            if opcionCancelar.upper() == "Y":
                break
            elif opcionCancelar.upper() == "N":
                continue
            else:
                print("Opcion no reconocida.")
                continue
        else:
            clienteAgendado = claveCliente
            break
    while True:
        fecha_string = input("Ingresa la fecha a agendar (dd/mm/aaaa): ")
        try:
            fechaAgendada = dt.datetime.strptime(fecha_string, "%d/%m/%Y")
        except:
            print("Fecha no valida.")
            continue
        break
    while True:
        turno = input("Elige el turno a agendar (M - Matutino, V - Vespertino, N - Nocturno): ")
        if turno.upper() == "M":
            turnoAgendado = "M"
        elif turno.upper() == "V":
            turnoAgendado = "V"
        elif turno.upper() == "N":
            turnoAgendado = "N"
        else:
            print("Turno no valido.")
            continue
        break
    while True:
        print(f"\nSalas disponibles y cupo:")
        print("*"*30)
        print(f"Sala\t\t\tCupo")
        for sala, cupo in salas.items():
            print(f"{sala}\t\t\t{cupo}")
        print("*"*30)
        salaAgendada = input("Ingresa el nombre de la sala a agendar: ")
        if salaAgendada not in salas.keys() or salaAgendada == "":
            print("La sala no existe.")
            continue
        break
    while True:
        nombreEvento = input("Ingresa el nombre del evento: ")
        if nombreEvento == "":
            print("El nombre del evento no puede estar vacio.")
            continue
        break
    reservaciones.update({fecha_string:[{turnoAgendado:{salaAgendada:[clienteAgendado, nombreEvento]}}]})

def mostrarReservaciones():
    pass

agregarCliente()
reservarSala()
