
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path
import gui
import main
# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\leone\Desktop\GUI_RCV\ENV\assets\frame1")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def exit_fullscreen(window):
    window.attributes('-fullscreen', False)

def on_escape(event, window):
    exit_fullscreen(window)

def new_resolution(window):
    window.geometry("1280x768")

def make_fullscreen(window):
    window.attributes('-fullscreen', True)

# window = Tk()

# window.geometry("640x480")
# window.configure(bg = "#183274")



def create_intropage(window):
    
    canvas = Canvas(
        window,
        bg = "#183274",
        height = 480,
        width = 640,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    canvas.create_text(
        117.0,
        33.0,
        anchor="nw",
        text="Simulador de Resucitación Cardio-Vascular",
        fill="#FFFFFF",
        font=("Inter", 20 * -1)
    )

    canvas.create_rectangle(
        0.0,
        85.0,
        640.0,
        174.0,
        fill="#D9D9D9",
        outline="")

    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        320.0,
        129.0,
        image=image_image_1
    )

    canvas.create_rectangle(
        42.0,
        227.0,
        599.0,
        371.0,
        fill="#D9D9D9",
        outline="")
    
    def button_1_click(event=None):
        print("button_1 clicked")
        new_resolution(window)
        gui.create_canvas(window)
        main.main_gui_test(window)


    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=button_1_click,
        relief="flat"
    )
    button_1.place(
        x=255.0,
        y=287.0,
        width=145.0,
        height=37.0
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_2 clicked"),
        relief="flat"
    )
    button_2.place(
        x=63.0,
        y=287.0,
        width=145.0,
        height=37.0
    )

    button_image_3 = PhotoImage(
        file=relative_to_assets("button_3.png"))
    button_3 = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_3 clicked"),
        relief="flat"
    )
    button_3.place(
        x=438.0,
        y=287.0,
        width=145.0,
        height=37.0
    )

    canvas.create_text(
        53.0,
        237.0,
        anchor="nw",
        text="Resolución de Pantalla:",
        fill="#000000",
        font=("Inter", 15 * -1)
    )

    # Mantener una referencia a las imágenes
    canvas.image_image_1 = image_image_1
    canvas.button_image_1 = button_image_1
    canvas.button_image_2 = button_image_2
    canvas.button_image_3 = button_image_3


    return canvas


# window.resizable(False, False)
# window.bind("<Escape>", on_escape)  # Llama a la función on_escape cuando se presiona la tecla Escape

# window.mainloop()
