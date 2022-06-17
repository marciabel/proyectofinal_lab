'''
Proyecto final: "Alicia en el Pais de las Encrucijadas"
Materia: Laboratorio de Computacion I
Profesores:
            Balmaceda, Javier
            Coppo, Ricardo
Autores:
        Alvarez, Marcia Belen
        D'Annunzio, Stefano 
'''
import tkinter
from tkinter.font import BOLD
from tkinter.ttk import LabelFrame
from turtle import bgpic
from PIL import ImageTk, Image

#Creación de la ventana raiz y asignación propiedades.
window = tkinter.Tk()
window.title("Alicia en el Pais de las Encrucijadas")
window.geometry("720x565")
#window.iconbitmap() <- Agregar iconito a la ventana

#Creación pantalla Bienvenida------------------------------------------------------------------------------------------------------
welcome_screen = LabelFrame(window, width=712, height=540)
welcome_screen.place(x=0, y=0, relheight=1, relwidth=1)

welcome_screen_image = ImageTk.PhotoImage(Image.open("Images/home_screen.png"))
canvas_welcome_image = tkinter.Canvas(welcome_screen, width = 712, height=540, )
canvas_welcome_image.pack(fill="both", expand=True)
canvas_welcome_image.create_image(0,0, image=welcome_screen_image, anchor="nw")

#----------Texto de Bienvenida-------------------------------------------------------------------------------------------------------
canvas_welcome_image.create_text(356, 100, text="Alicia en el Pais de las Encrucijadas", font=("Gabriola", 40, "bold"),fill="white")

#----------Boton-------------------------------------------------------------------------------------------------------------------
start_button = tkinter.Button(welcome_screen, text = "Comenzar", font=("Gabriola",20,"bold"), padx= 150)
start_button_window = canvas_welcome_image.create_window(150,430, anchor="nw", window=start_button)

window.mainloop()
