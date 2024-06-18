from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Label
from itertools import count
import data_sim

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH.joinpath(r"assets\frame2")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


# Variables globales para el cronómetro
running = False
milliseconds = 0
seconds = 0
minutes = 0


# window = Tk()
# window.geometry("1920x1080")
# window.configure(bg = "#9993BD")

# Datos presion
press_y = []
press_x = []
press_index = count()

# Datos frecuecia
frec_y = []
frec_x = [] 
frec_index = count()



def GUI_basic_mode(window):
    #Funciones
    def check_data():
        data_sim.get_pressure(press_index,press_x,press_y)
        data_sim.get_frecuency(frec_index,frec_x,frec_y)

        #For pressure
        if(press_y[-1] > 5 and press_y[-1] < 6):
            change_rectangle_color(pressure_rectangle, "#00FF00")  # Change the second rectangle to green
        elif(press_y[-1] < 5):
            change_rectangle_color(pressure_rectangle, "#0000FF")  # Change the second rectangle to blue
        elif(press_y[-1] > 6):
            change_rectangle_color(pressure_rectangle, "#FF0000")   # Change the second rectangle to red
        
        #For frecuency
        if(frec_y[-1] > 100 and frec_y[-1] < 120):
            change_rectangle_color(frecuency_rectangle, "#00FF00")  # Change the second rectangle to green
        elif(frec_y[-1] < 100):
            change_rectangle_color(frecuency_rectangle, "#0000FF")  # Change the second rectangle to blue
        elif(frec_y[-1] > 120):
            change_rectangle_color(frecuency_rectangle, "#FF0000")   # Change the second rectangle to red

        window.after(500,check_data)
    
    def change_rectangle_color(rectangle_id, color):
        canvas.itemconfig(rectangle_id, fill=color)
    
    def start_timer():
        global running
        if not running:
            running = True
            update_timer()

    def stop_or_reset_timer():
        global running, milliseconds, seconds, minutes
        if running:
            running = False
        else:
            # Reset timer to 0:0:0 if it's not running
            milliseconds = 0
            seconds = 0
            minutes = 0
            time_string = f"{minutes:02}:{seconds:02}:{milliseconds:02}"
            timer_label.config(text=time_string)

    def update_timer():
        global milliseconds, seconds, minutes
        if running:
            milliseconds += 1
            if milliseconds == 100:
                milliseconds = 0
                seconds += 1
            if seconds == 60:
                seconds = 0
                minutes += 1
            time_string = f"{minutes:02}:{seconds:02}:{milliseconds:02}"
            timer_label.config(text=time_string)
            window.after(10, update_timer)



    #Canvas
    canvas = Canvas(
        window,
        bg = "#9993BD",
        height = 1080,
        width = 1920,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        327.0,
        819.0,
        image=image_image_1
    )

    image_image_2 = PhotoImage(
        file=relative_to_assets("image_2.png"))
    image_2 = canvas.create_image(
        1593.0,
        819.0,
        image=image_image_2
    )

    image_image_3 = PhotoImage(
        file=relative_to_assets("image_3.png"))
    image_3 = canvas.create_image(
        960.0,
        819.0,
        image=image_image_3
    )

    frecuency_rectangle = canvas.create_rectangle(
        744.0,
        620.0,
        1175.0,
        1021.0,
        fill="#93BD99",
        outline=""
    )

    pressure_rectangle = canvas.create_rectangle(
        1377.0,
        620.0,
        1808.0,
        1021.0,
        fill="#93BD99",
        outline=""
    )

    hands_rectangle = canvas.create_rectangle(
        111.0,
        620.0,
        542.0,
        1021.0,
        fill="#93BD99",
        outline=""
    )

    image_image_4 = PhotoImage(
        file=relative_to_assets("image_4.png"))
    image_4 = canvas.create_image(
        327.0,
        841.0,
        image=image_image_4
    )

    canvas.create_text(
        159.0,
        639.0,
        anchor="nw",
        text="Posición de Manos",
        fill="#000000",
        font=("Inter Black", 36 * -1)
    )

    canvas.create_text(
        859.0,
        639.0,
        anchor="nw",
        text="Frecuencia",
        fill="#000000",
        font=("Inter Black", 36 * -1)
    )

    image_image_5 = PhotoImage(
        file=relative_to_assets("image_5.png"))
    image_5 = canvas.create_image(
        959.0,
        851.0,
        image=image_image_5
    )

    image_image_6 = PhotoImage(
        file=relative_to_assets("image_6.png"))
    image_6 = canvas.create_image(
        1593.0,
        819.0,
        image=image_image_6
    )

    canvas.create_text(
        1524.0,
        639.0,
        anchor="nw",
        text="Presión",
        fill="#000000",
        font=("Inter Black", 36 * -1)
    )

    canvas.create_rectangle(
        0.0,
        29.0,
        1920.0,
        317.0,
        fill="#D9D9D9",
        outline=""
    )

    canvas.create_text(
        72.0,
        106.0,
        anchor="nw",
        text="Simulador de Resucitación Cardio-Vascular",
        fill="#000000",
        font=("Inter Black", 48 * -1)
    )

    image_image_7 = PhotoImage(
        file=relative_to_assets("image_7.png"))
    image_7 = canvas.create_image(
        1419.0,
        165.0,
        image=image_image_7
    )

    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=start_timer,
        relief="flat"
    )
    button_1.place(
        x=122.0,
        y=358.0,
        width=410.0,
        height=88.0
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=stop_or_reset_timer,
        relief="flat"
    )
    button_2.place(
        x=122.0,
        y=466.0,
        width=410.0,
        height=88.0
    )

    image_image_8 = PhotoImage(
        file=relative_to_assets("image_8.png"))
    image_8 = canvas.create_image(
        1271.0,
        467.0,
        image=image_image_8
    )

    # Etiqueta para mostrar el cronómetro
    timer_label = Label(window, text="00:00:00", font=("Inter Black", 42), bg="#B7AEAE", fg="#000000")
    timer_label.place(x=999, y=425)  # Ajusta la posición según tu diseño

    # colors = ["#FF0000", "#00FF00", "#0000FF", "#FFFF00", "#FF00FF", "#00FFFF"]
    # color_cycle = itertools.cycle(colors)

    # def update_colors():
    #     current_color = next(color_cycle)
    #     canvas.itemconfig(frecuency_rectangle, fill=current_color)
    #     canvas.itemconfig(pressure_rectangle, fill=current_color)
    #     canvas.itemconfig(hands_rectangle, fill=current_color)
    #     window.after(1000, update_colors)  # Schedule this function to run again after 1 second

    # update_colors()  # Initial call to start the cycle

    # Example usage of change_rectangle_color function
    change_rectangle_color(frecuency_rectangle, "#FF0000")  # Change the first rectangle to red
    #change_rectangle_color(pressure_rectangle, "#00FF00")  # Change the second rectangle to green
    change_rectangle_color(hands_rectangle, "#00FF00")  # Change the third rectangle to blue

    check_data()

    # Mantener una referencia a las imágenes
    canvas.button_image_1 = button_image_1
    canvas.button_image_2 = button_image_2
    canvas.image_image_1 = image_image_1
    canvas.image_image_2 = image_image_2
    canvas.image_image_3 = image_image_3
    canvas.image_image_4 = image_image_4
    canvas.image_image_5 = image_image_5
    canvas.image_image_6 = image_image_6
    canvas.image_image_7 = image_image_7
    canvas.image_image_8 = image_image_8

    return canvas

# window.resizable(False, False)
# window.mainloop()
