# Definición de una función para obtener la fecha de un evento.
def get_event_date(event):
    return event.date

# Función para calcular usuarios activos en máquinas.
def current_users(events):
    events.sort(key=get_event_date)  # Ordena los eventos por fecha.
    machines = {}  # Inicializa un diccionario para mapear máquinas a usuarios activos.
    for event in events:
        if event.machine not in machines:
            machines[event.machine] = set()  # Crea un conjunto para usuarios en una máquina.
        if event.type == "login":
            machines[event.machine].add(event.user)  # Agrega un usuario al conjunto.
        elif event.type == "logout":
            machines[event.machine].remove(event.user)  # Elimina un usuario del conjunto.
    return machines

# Función para generar un informe de usuarios activos en máquinas.
def generate_report(machines):
    for machine, users in machines.items():
        if len(users) > 0:
            user_list = ", ".join(users)  # Convierte la lista de usuarios en una cadena.
            print("{}: {}".format(machine, user_list))  # Imprime el informe.

# Definición de una clase llamada Event para representar eventos.
class Event:
    def __init__(self, event_date, event_type, machine_name, user):
        self.date = event_date  # Fecha del evento.
        self.type = event_type  # Tipo de evento (login o logout).
        self.machine = machine_name  # Nombre de la máquina.
        self.user = user  # Nombre de usuario.

# Creación de una lista de eventos.
events = [
    Event('2020-01-21 12:45:56', 'login', 'myworkstation.local', 'jordan'),
    Event('2020-01-22 15:53:42', 'logout', 'webserver.local', 'jordan'),
    Event('2020-01-21 18:53:21', 'login', 'webserver.local', 'lane'),
    Event('2020-01-22 10:25:34', 'logout', 'myworkstation.local', 'jordan'),
    Event('2020-01-21 08:20:01', 'login', 'webserver.local', 'jordan'),
    Event('2020-01-23 11:24:35', 'login', 'mailserver.local', 'chris'),
]

# Calcula los usuarios activos en las máquinas.
users = current_users(events)
print(users)

# Genera y muestra un informe de usuarios activos en máquinas.
generate_report(users)
