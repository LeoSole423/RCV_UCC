import random
from itertools import count
from time import sleep

def get_pressure(aux_count, x_axis, y_axis):
    y_axis.append(random.uniform(4.7,6.2))
    x_axis.append(next(aux_count))

def get_frecuency(aux_count, x_axis, y_axis):
    y_axis.append(random.uniform(98,125))
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