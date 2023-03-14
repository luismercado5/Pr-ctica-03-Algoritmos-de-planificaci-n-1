# -*- coding: utf-8 -*-
"""
Created on Tue Mar 14 01:20:36 2023

@author: luis mercado
"""
# algoritmo de planificacion de pila


class FIFO:
    def __init__(self, name, entrada, burst_time):
        self.name = name
        self.entrada = entrada
        self.burst_time = burst_time
# pila


def first_in_first_out(proceso):
    n = len(proceso)
    tiempo_de_completacion = [0] * n
    espera = [0] * n
    tiempo_respuesta = [0] * n
    total_espera = 0
    total_respuesta = 0
    for i in range(n):
        if i == 0:
            tiempo_de_completacion[i] = proceso[i].burst_time
        else:
            tiempo_de_completacion[i] = tiempo_de_completacion[i -
                                                               1] + proceso[i].burst_time
        tiempo_respuesta[i] = tiempo_de_completacion[i] - proceso[i].entrada
        espera[i] = tiempo_respuesta[i] - proceso[i].burst_time
        total_espera += espera[i]
        total_respuesta += tiempo_respuesta[i]
    promedio_espera = total_espera / n
    promedio_respuesta = total_respuesta / n
    # impresion de datos y lectura de archivo

    print("pila")
    for i in range(n):
        print("name", proceso[i].name, "\n", "entrada", proceso[i].entrada, "\n", "burst", proceso[i].burst_time, "\n",
              "completado", tiempo_de_completacion[i], "\n", "espera", espera[i], "\n", "respuesta", tiempo_respuesta[i], "\n")
    print("tiempo promedio  de espera:", promedio_espera)
    print("tiempo promedio de llegada:", promedio_respuesta)


filename = "procesos.txt"  # abre el archivo
proceso = []
with open(filename) as f:
    for i, line in enumerate(f):
        if i == 20:
            break
        name, entrada, burst_time = line.strip().split()
        proceso.append(FIFO(name, int(entrada), int(burst_time)))

proceso.sort(key=lambda x: x.entrada)

first_in_first_out(proceso)
# prioridad
# variables


class Prioridad:
    def __init__(self, name, entrada, burst_time, prioridad):
        self.name = name
        self.entrada = entrada
        self.burst_time = burst_time
        self.prioridad = prioridad
    # proceso


def prioritario(proceso):
    n = len(proceso)
    completacion = [0] * n
    espera = [0] * n
    respuesta = [0] * n
    total_espera = 0
    total_respuesta = 0
    tiempo = 0
    while True:
        proceso_restante = [
            p for p in proceso if p.entrada <= tiempo and p.burst_time > 0]
        if len(proceso_restante) == 0:
            break
        proceso_seleccionado = min(
            proceso_restante, key=lambda x: x.prioritario)
        indice_proceso = proceso.indice(proceso_seleccionado)
        proceso[indice_proceso].burst_time -= 1
        tiempo += 1
        if proceso[indice_proceso].burst_time == 0:
            completacion[indice_proceso] = tiempo
            respuesta[indice_proceso] = completacion[indice_proceso] - \
                proceso[indice_proceso].llegada
            espera[indice_proceso] = respuesta[indice_proceso] - \
                proceso[indice_proceso].burst_time
            total_espera += espera[indice_proceso]
            total_respuesta += respuesta[indice_proceso]
    promedio_espera = total_espera / n
    promedio_respuesta = total_respuesta / n
    # datos y lectura de archivo

    for i in range(n):
        print("prioridad")
        print("name", proceso[i].name, "\n", "entrada", proceso[i].entrada, "\n", "burst", proceso[i].burst_time, "\n", "prioridad",
              proceso[i].prioridad, "\n", "completado", completacion[i], "\n", "espera", espera[i], "\n", "respuesta", respuesta[i])
    print(" promedio espera:", promedio_espera)
    print("promedio respuesta:", promedio_respuesta)


filename = "procesosprioridad.txt"  # abre el archivo
proceso = []
with open(filename) as f:
    for line in f:
        name, llegada, burst_time, prioridad = line.strip().split()
        proceso.append(Prioridad(name, int(entrada),
                       int(burst_time), int(prioridad)))

proceso.sort(key=lambda x: x.entrada)

prioritario(proceso)
# round_robin


class Rr:
    def __init__(self, name, burst_time):
        self.name = name
        self.burst_time = burst_time
        self.tiempo_promedio = burst_time
# inicio de algoritmo round robin


def round_robin(proceso, quantum):
    n = len(proceso)
    espera = [0] * n
    respuesta = [0] * n
    tiempo = 0
    cola = []
    for i in range(n):
        cola.append(proceso[i])
    while True:
        all_done = True
        for i in range(n):
            procesos = cola.pop(0)
            if procesos.tiempo_promedio > 0:
                all_done = False
                if procesos.tiempo_promedio > quantum:
                    tiempo += quantum
                    procesos.tiempo_promedio -= quantum
                    cola.append(procesos)
                else:
                    tiempo += procesos.tiempo_promedio
                    espera[i] = tiempo - procesos.burst_time
                    procesos.tiempo_faltante = 0
                    respuesta[i] = tiempo
        if all_done:
            break

    total_espera = 0
    total_respuesta = 0
    # datos lectura de archivo

    for i in range(n):
        print("name", proceso[i].name, "\n", "burst", proceso[i].burst_time,
              "\n", "espera", espera[i], "\n", "respuesta", respuesta[i], "\n")
        total_espera += espera[i]
        total_respuesta += respuesta[i]


# Apertura de archivos
filename = "procesosroundrobin.txt"
quantum = 3
# Inicializa la lista de procesos
proceso = []

with open('procesosroundrobin.txt', 'r') as f:
    for line in f:
        procesos = line.strip().split(',')
        proceso.append(procesos)

# inicializa el tiempo
max_tiempo = 10
tiempo_actual = 0

# Se iteran los procesos hasta completarlos todos
while proceso:

    procesos = proceso[0]

    print(int(procesos[0][0:1]))

    if int(procesos[0][0:1]) <= max_tiempo:

        proceso.pop(0)

        tiempo_actual += int(procesos[0][0:1])
        # impresion individual de cada proceso segun el quamtum utilizado

        print(procesos[0], "completado en", tiempo_actual)
    else:

        procesos[1] -= max_tiempo

        proceso.append(proceso)

        tiempo_actual += max_tiempo

# tiempo final al completar todos los procesos
print("Todos los procesos completados en:", tiempo_actual)

round_robin(proceso, quantum)

# sjf


class Sjf:
    def __init__(self, name, burst_time):
        self.name = name
        self.burst_time = burst_time

    # algoritmo

def shortest_job_first(proceso):
    n = len(proceso)
    tiempo_promedio = [0] * n
    for i in range(n):
        tiempo_promedio[i] = proceso[i].burst_time
    completado = 0
    tiempo = 0
    espera = 0
    while True:
        min_burst_time = float('inf')
        min_index = n
        for i in range(n):
            if tiempo_promedio[i] > 0 and tiempo_promedio[i] < min_burst_time:
                min_burst_time = tiempo_promedio[i]
                min_index = i
        if min_index == n:
            break
        procesos = proceso[min_index]
        espera += tiempo
        tiempo += procesos.burst_time
        tiempo_promedio[min_index] = 0
        completado += 1
    promedio_espera = espera / n
    print("Sjf\tBurst Time\tespera")
    for i in range(n):
        espera = tiempo - proceso[i].burst_time
        print(proceso[i].name, "\t\t", proceso[i].burst_time, "\t\t", espera)
    print("promedio espera:", promedio_espera)


filename = "procesossjf.txt"  # abre el archivo
proceso = []
with open(filename) as f:
    for line in f:
        name, burst_time = line.strip().split()
        proceso.append(Sjf(name, int(burst_time)))

proceso.sort(key=lambda x: x.burst_time)

shortest_job_first(proceso)
