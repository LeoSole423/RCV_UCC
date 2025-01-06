import matplotlib.pyplot as plt
import random
from itertools import count
from matplotlib.animation import FuncAnimation
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from constantes import REFRESH_RATE


def pressure_plot(press_x, press_y, window):
    # Crear figura de matplotlib
    pressure, press_ax = plt.subplots(figsize=(5.9, 2.8))  # Tamaño personalizado para que se ajuste a la ventana
    pressure.set_facecolor('#D9D9D9')
    pressure.tight_layout()
    press_ax.set_facecolor('#D9D9D9')
    
    local_x = []
    local_y = []

    def animate(i):
        nonlocal local_x, local_y

        local_x.append(press_x[-1])
        local_y.append(press_y[-1])

        #press_x.append(next(press_index))
        #press_y.append(random.uniform(4.7,6.2))
        

        # Mantener solo los últimos 10 datos
        if len(local_x) > 10:
            local_x.pop(0)
            local_y.pop(0)
      
        # Color de las barras
        colors = ['blue' if val < 5 else 'red' if val > 6 else 'green' for val in local_y]

        press_ax.cla()
        press_ax.bar(local_x,local_y, color=colors)

        # Dibujar una zona verde translúcida para indicar frecuencia correcta
        press_ax.axhspan(5, 6, color='green', alpha=0.3)

    ani = FuncAnimation(pressure, animate, interval = REFRESH_RATE, cache_frame_data=False)

    canvas = FigureCanvasTkAgg(figure=pressure, master=window)
    canvas.draw()
    canvas.get_tk_widget().place(x=20,y=455)

def frecuency_plot(frec_x, frec_y, window):
    #Crear animacion de Frecuencia
    # Crear figura de matplotlib
    frecuency, frecuency_ax = plt.subplots(figsize=(5.9, 2.8))  # Tamaño personalizado para que se ajuste a la ventana
    frecuency.set_facecolor('#D9D9D9')
    frecuency.tight_layout()
    frecuency_ax.set_facecolor('#D9D9D9')


    frec_index = count()
    local_x = []
    local_y = []

    def animate_frecuency(i):
        nonlocal local_x, local_y

        local_x.append(frec_x[-1])
        local_y.append(frec_y[-1])

        if len(local_x) > 30:
            local_x.pop(0)
            local_y.pop(0)

        # Definir los rangos para "muy alta" y "muy baja"
        muy_alta = 120
        muy_baja = 100

        # Obtener el último valor de presión
        last_frec = frec_y[-1]

        # Cambiar el color de la línea según el valor de presión
        color = 'green'  # color predeterminado
        if last_frec > muy_alta:
            color = 'red'
        elif last_frec < muy_baja:
            color = 'blue'

        
        frecuency_ax.cla()
        frecuency_ax.plot(local_x,local_y, color=color)
        # Dibujar una zona verde translúcida para indicar frecuencia correcta
        frecuency_ax.axhspan(muy_baja, muy_alta, color='green', alpha=0.3)



    frec_ani = FuncAnimation(frecuency, animate_frecuency, interval = REFRESH_RATE, cache_frame_data=False)

    frecuency_canvas = FigureCanvasTkAgg(figure=frecuency, master=window)
    frecuency_canvas.draw()
    frecuency_canvas.get_tk_widget().place(x=649,y=455)


def ef_frecuency_plot(press_y, frec_y, window):

    # Datos para el gráfico
    labels = ['Correctas', 'Incorrectas']
    sizes = [0.0, 100.0]  # Porcentajes de cada sección
    colors = ['green', 'red']  # Colores de cada sección
    explode = (0.1, 0)  # Qué tan alejado se muestra cada segmento

    # Crear el gráfico de torta
    ef_frec, ef_frec_ax = plt.subplots(figsize=(2.8, 2.8))
    ef_frec.set_facecolor('#D9D9D9')
    ef_frec.tight_layout()
    ef_frec_ax.set_facecolor('#D9D9D9')

    ef_frec_ax.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
    ef_frec_ax.axis('equal')  # Ajusta el aspecto de la gráfica para que se vea como un círculo

    def animate_ef_frecuency(i):
        nonlocal sizes
        contador = 0
        # Iterar sobre ambas listas simultáneamente
        for press, frec in zip(press_y, frec_y):
            # Verificar si se cumplen ambas condiciones
            if 5 <= press <= 6 and 100 <= frec <= 120:
                contador += 1
            
        
        # Calcular el porcentaje
        porcentaje = (contador / len(press_y)) * 100

        sizes = [porcentaje,100-porcentaje]
        #print(f"Contador: {contador}")
        #print(f"Porcentaje: {porcentaje}")
        #print(f"Sizes {sizes}")
        ef_frec_ax.cla()
        ef_frec_ax.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
        contador=0

    ef_frec_ani = FuncAnimation(ef_frec, animate_ef_frecuency, interval = REFRESH_RATE, cache_frame_data=False)

    ef_frecuency_canvas = FigureCanvasTkAgg(figure=ef_frec, master=window)
    ef_frecuency_canvas.draw()
    ef_frecuency_canvas.get_tk_widget().place(x=318,y=118) 
