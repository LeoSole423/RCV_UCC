import random
from itertools import count
from time import sleep
import serial
import re

# Configura el puerto serie (ajusta el puerto y la velocidad según tus necesidades)
ser = serial.Serial('COM3', 9600, timeout=1)  # Cambia 'COM5' y 9600 si es necesario

def get_pressure(aux_count, x_axis, y_axis):
    # Si las listas están vacías, inicializa el primer valor en 0
    if not x_axis and not y_axis:
        x_axis.append(0)
        y_axis.append(0)
        print("Inicializando el primer valor: X=0, Y=0")
        return  # Salir después de inicializar

    # Lee una línea del puerto serie
    line = ser.readline().decode('utf-8').strip()

    # Usa una expresión regular para extraer solo el valor numérico de "MAX PROFUNDIDAD"
    match = re.search(r'P(\d+)', line)
    if match:
        # Convierte el valor numérico extraído a un entero
        max_depth_value = int(match.group(1))
        max_depth_value = max_depth_value * 0.1
        y_axis.append(max_depth_value)
        x_axis.append(next(aux_count))
        print("Profundidad:")
        print(max_depth_value)
    else:
        # Si no se encuentra el formato esperado, agrega un valor por defecto
        y_axis.append(0)
        x_axis.append(next(aux_count))


        
    
# def get_pressure(aux_count, x_axis, y_axis):
#     y_axis.append(random.uniform(4.7,6.2))
#     x_axis.append(next(aux_count))

def get_frecuency(aux_count, x_axis, y_axis):
    # Si las listas están vacías, inicializa el primer valor en 0
    if not x_axis and not y_axis:
        x_axis.append(0)
        y_axis.append(0)
        print("Inicializando el primer valor: X=0, Y=0")
        return  # Salir después de inicializar

    # Lee una línea del puerto serie
    line = ser.readline().decode('utf-8').strip()

    # Usa una expresión regular para extraer solo el valor numérico de "MAX PROFUNDIDAD"
    match = re.search(r'F(\d+)', line)
    if match:
        # Convierte el valor numérico extraído a un entero
        max_depth_value = int(match.group(1))
        y_axis.append(max_depth_value)
        x_axis.append(next(aux_count))
        print("PPM:")
        print(max_depth_value)
    else:
        # Si no se encuentra el formato esperado, agrega un valor por defecto
        y_axis.append(0)
        x_axis.append(next(aux_count))

def get_handspos():
    return random.randint(0,1)

#Testing
# for i in range(30):
#     get_pressure(press_index,press_x,press_y)
#     get_frecuency(frec_index,frec_x,frec_y)
#     print(press_y)
#     print(press_x)
#     sleep(0.1)