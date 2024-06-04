import gui
import plots
import intropage
from tkinter import Tk
import random
from itertools import count


def on_closing(window):
    window.quit()

def get_pressure(aux_count, x_axis, y_axis):
    y_axis.append(random.uniform(4.7,6.2))
    x_axis.append(next(aux_count))

def get_frecuency(aux_count, x_axis, y_axis):
    y_axis.append(random.uniform(98,125))
    x_axis.append(next(aux_count))

def exit_fullscreen(window):
    window.attributes('-fullscreen', False)

def on_escape(event, window):
    exit_fullscreen(window)

def new_resolution(window):
    window.geometry("1280x720")

def make_fullscreen(window):
    window.attributes('-fullscreen', True)


def main_gui_test(window):

    # Datos presion
    press_y = []
    press_x = []
    press_index = count()

    # Datos frecuecia
    frec_y = []
    frec_x = [] 
    frec_index = count()

    def loop():
        get_pressure(press_index,press_x,press_y)
        get_frecuency(frec_index,frec_x,frec_y)
        window.after(1000,loop)

    loop()

    plots.frecuency_plot(frec_x,frec_y,window)
    plots.pressure_plot(press_x, press_y, window)
    plots.ef_frecuency_plot(press_y,frec_y,window)

    def testing():
        print(frec_x)
        print(frec_y)
        window.after(1000, testing)
    
    #testing()


def main():

    window = Tk()
    window.geometry("640x480")
    window.configure(bg = "#183274")

    intropage.create_intropage(window)

    # Mostrar la ventana
    window.protocol("WM_DELETE_WINDOW", lambda: on_closing(window))
    window.bind("<Escape>",lambda event: on_escape(event=event, window=window))  # Llama a la función on_escape cuando se presiona la tecla Escape

    window.resizable(False, False)
    window.mainloop()


if __name__ == "__main__":
    main()