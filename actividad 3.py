# -*- coding: utf-8 -*-
"""
Created on Tue Mar 14 18:56:53 2023

@author: luis mercado
"""
from collections import deque

# Abrimos el archivo y leemos los datos
with open('proceso.txt', 'r') as f:
    lines = f.readlines()

# Creamos la lista de procesos en el formato adecuado roundrobin
procesos = []
for line in lines:
    nombre, llegada, procesamiento, prioridad = line.strip().split(',')
    procesos.append({
        'nombre': nombre,
        'llegada': int(llegada),
        'procesamiento': int(procesamiento),
        'prioridad': int(prioridad)
    })

# Definimos el tiempo de cuánto se ejecuta cada proceso en cada ronda
lapso = 2

# Definimos la lista de procesos ordenada por tiempo de llegada
procesos = sorted(procesos, key=lambda p: p['llegada'])

# Creamos una cola de procesos
cola = deque(procesos)

# Definimos el tiempo actual
tiempo_actual = 0

# Creamos una lista para almacenar los tiempos de finalización de cada proceso
tiempos_finalizacion = []

# Simulamos el algoritmo Round Robin
while len(cola) > 0:
    proceso_actual = cola.popleft()
    tiempo_ejecucion = min(lapso, proceso_actual['procesamiento'])
    proceso_actual['procesamiento'] -= tiempo_ejecucion
    tiempo_actual += tiempo_ejecucion
    if proceso_actual['procesamiento'] > 0:
        cola.append(proceso_actual)
    else:
        tiempos_finalizacion.append(tiempo_actual)

print("\nprocesamiento por roundrobin\n")
# Imprimimos los tiempos de finalización de cada proceso
for i in range(len(procesos)):
    print(f"El proceso {procesos[i]['nombre']} terminó en el tiempo {tiempos_finalizacion[i]}.")
    
# Abrimos el archivo y leemos los datos
with open('proceso.txt', 'r') as f:
    lines = f.readlines()

# Creamos la lista de procesos en el formato adecuado fifo
procesos = []
for line in lines:
    nombre, llegada, procesamiento, prioridad = line.strip().split(',')
    procesos.append({
        'nombre': nombre,
        'llegada': int(llegada),
        'procesamiento': int(procesamiento),
        'prioridad': int(prioridad)
    })

# Definimos la lista de procesos ordenada por tiempo de llegada
procesos = sorted(procesos, key=lambda p: p['llegada'])

# Definimos el tiempo actual
tiempo_actual = 0

# Creamos una lista para almacenar los tiempos de finalización de cada proceso
tiempos_finalizacion = []

# Simulamos el algoritmo FIFO
for proceso in procesos:
    tiempo_espera = max(0, tiempo_actual - proceso['llegada'])
    tiempo_ejecucion = proceso['procesamiento']
    tiempo_actual += tiempo_espera + tiempo_ejecucion
    tiempos_finalizacion.append(tiempo_actual)

print("\nprocesamiento por pila (fifo)\n\n ")
# Imprimimos los tiempos de finalización de cada proceso
for i in range(len(procesos)):
    print(f"El proceso {procesos[i]['nombre']} terminó en el tiempo {tiempos_finalizacion[i]}.")
    
# Abrimos el archivo y leemos los datos sfj
with open('proceso.txt', 'r') as f:
    lines = f.readlines()

# Creamos la lista de procesos en el formato adecuado
procesos = []
for line in lines:
    nombre, llegada, procesamiento, prioridad = line.strip().split(',')
    procesos.append({
        'nombre': nombre,
        'llegada': int(llegada),
        'procesamiento': int(procesamiento),
        'prioridad': int(prioridad)
    })

# Definimos la lista de procesos ordenada por tiempo de llegada
procesos = sorted(procesos, key=lambda p: p['llegada'])

# Definimos el tiempo actual y una lista de procesos pendientes
tiempo_actual = 0
procesos_pendientes = procesos.copy()

# Creamos una lista para almacenar los tiempos de finalización de cada proceso
tiempos_finalizacion = []

# Simulamos el algoritmo SJF
while procesos_pendientes:
    # Buscamos el proceso con el menor tiempo de procesamiento pendiente
    proceso_actual = min(procesos_pendientes, key=lambda p: p['procesamiento'])

    # Actualizamos el tiempo actual y eliminamos el proceso de la lista de pendientes
    tiempo_espera = max(0, tiempo_actual - proceso_actual['llegada'])
    tiempo_ejecucion = proceso_actual['procesamiento']
    tiempo_actual += tiempo_espera + tiempo_ejecucion
    tiempos_finalizacion.append(tiempo_actual)
    procesos_pendientes.remove(proceso_actual)

# Imprimimos los tiempos de finalización de cada proceso prioridad
print("\nprocesamiento por sfj\n")
for i in range(len(procesos)):
    print(f"El proceso {procesos[i]['nombre']} terminó en el tiempo {tiempos_finalizacion[i]}.")

# Abrimos el archivo y leemos los datos
with open('proceso.txt', 'r') as f:
    lines = f.readlines()

# Creamos la lista de procesos en el formato adecuado
procesos = []
for line in lines:
    nombre, llegada, procesamiento, prioridad = line.strip().split(',')
    procesos.append({
        'nombre': nombre,
        'llegada': int(llegada),
        'procesamiento': int(procesamiento),
        'prioridad': int(prioridad)
    })

# Definimos la lista de procesos ordenada por tiempo de llegada
procesos = sorted(procesos, key=lambda p: p['llegada'])

# Definimos el tiempo actual y una lista de procesos pendientes
tiempo_actual = 0
procesos_pendientes = procesos.copy()

# Creamos una lista para almacenar los tiempos de finalización de cada proceso
tiempos_finalizacion = []

# Simulamos el algoritmo de planificación con prioridad
while procesos_pendientes:
    # Buscamos el proceso con la mayor prioridad
    proceso_actual = max(procesos_pendientes, key=lambda p: p['prioridad'])

    # Verificamos si el proceso ha llegado
    if proceso_actual['llegada'] <= tiempo_actual:
        # Actualizamos el tiempo actual y eliminamos el proceso de la lista de pendientes
        tiempo_espera = max(0, tiempo_actual - proceso_actual['llegada'])
        tiempo_ejecucion = proceso_actual['procesamiento']
        tiempo_actual += tiempo_espera + tiempo_ejecucion
        tiempos_finalizacion.append(tiempo_actual)
        procesos_pendientes.remove(proceso_actual)
    else:
        # Avanzamos el tiempo hasta la llegada del proceso
        tiempo_actual = proceso_actual['llegada']

print("\nprocesamiento por prioridad\n")
# Imprimimos los tiempos de finalización de cada proceso
for i in range(len(procesos)):
    print(f"El proceso {procesos[i]['nombre']} terminó en el tiempo {tiempos_finalizacion[i]}.")


