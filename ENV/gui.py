
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH.joinpath(r"assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)



def create_canvas(window):
    canvas = Canvas(
    window,
    bg = "#9598DE",
    height = 768,
    width = 1280,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    canvas.create_rectangle(
        0.0,
        0.0,
        1280.0,
        74.0,
        fill="#4D6DDB",
        outline="")

    canvas.create_text(
        23.0,
        18.0,
        anchor="nw",
        text="Simulador de RCV",
        fill="#FFFFFF",
        font=("Sintony", 32 * -1)
    )

    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        159.0,
        246.0,
        image=image_image_1,
        state = 'hidden'
    )

    image_image_2 = PhotoImage(
        file=relative_to_assets("image_2.png"))
    image_2 = canvas.create_image(
        326.0,
        578.0,
        image=image_image_2
    )

    image_image_3 = PhotoImage(
        file=relative_to_assets("image_3.png"))
    image_3 = canvas.create_image(
        951.0,
        578.0,
        image=image_image_3
    )

    image_image_4 = PhotoImage(
        file=relative_to_assets("image_4.png"))
    image_4 = canvas.create_image(
        475.0,
        246.0,
        image=image_image_4
    )

    canvas.create_text(
        63.0,
        107.0,
        anchor="nw",
        text="Posicion de Manos",
        fill="#000000",
        font=("Inter Bold", 20 * -1)
    )

    canvas.create_text(
        55.0,
        432.0,
        anchor="nw",
        text="Profundidad",
        fill="#000000",
        font=("Inter Bold", 20 * -1)
    )

    canvas.create_text(
        664.0,
        432.0,
        anchor="nw",
        text="Frecuencia",
        fill="#000000",
        font=("Inter Bold", 20 * -1)
    )

    canvas.create_text(
        367.0,
        99.0,
        anchor="nw",
        text="Frecuencia Efectiva",
        fill="#000000",
        font=("Inter Bold", 20 * -1)
    )

    image_image_5 = PhotoImage(
        file=relative_to_assets("image_5.png"))
    image_5 = canvas.create_image(
        1185.0,
        37.0,
        image=image_image_5
    )

    image_image_6 = PhotoImage(
        file=relative_to_assets("image_6.png"))
    image_6 = canvas.create_image(
        156.0,
        272.0,
        image=image_image_6
    )

    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_1 clicked"),
        relief="flat"
    )
    button_1.place(
        x=819.0,
        y=126.0,
        width=317.0,
        height=57.0
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
        x=819.0,
        y=203.0,
        width=316.0,
        height=57.0
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
        x=820.0,
        y=280.0,
        width=316.0,
        height=57.0
    )

    canvas.create_rectangle(
        230.0,
        426.0,
        374.0,
        463.0,
        fill="#A1A1A1",
        outline="")

    canvas.create_rectangle(
        834.0,
        426.0,
        978.0,
        463.0,
        fill="#A1A1A1",
        outline="")

    # Mantener una referencia a las imágenes
    canvas.button_image_1 = button_image_1
    canvas.button_image_2 = button_image_2
    canvas.button_image_3 = button_image_3
    canvas.image_image_1 = image_image_1
    canvas.image_image_2 = image_image_2
    canvas.image_image_3 = image_image_3
    canvas.image_image_4 = image_image_4
    canvas.image_image_5 = image_image_5
    canvas.image_image_6 = image_image_6
    
    return canvas